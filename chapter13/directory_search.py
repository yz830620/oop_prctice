from __future__ import annotations
import os
import time
from pathlib import Path
from multiprocessing import Process, cpu_count, Queue
from fnmatch import fnmatch 
from typing import List, Iterator, Optional, Union, TYPE_CHECKING

if TYPE_CHECKING:
    Query_Q = Queue[Union[str, None]]
    Result_Q = Queue[List[str]]

def search(
    paths: list[Path],
    query_q: Query_Q,
    results_q: Result_Q
) -> None:
    print(f"PID: {os.getpid()}, paths {len(paths)}")
    lines: List[str] = []
    for path in paths:
        # !! pathlib Path load file error try to change the default value
        # encoding -> "utf-8", and errors -> "ignore"
        lines.extend(
            l.rstrip() for l in path.read_text(encoding="utf-8", errors='ignore').splitlines())

    while True:
        query_text = query_q.get()
        if query_text is None:
            break
        results = [l for l in lines if query_text in l]
        results_q.put(results)

class DirectorySearch:
    def __init__(self) -> None:
        self.query_queues: List[Query_Q]
        self.result_queue: Result_Q
        self.search_workers: List[Process]
    
    def setup_search(self, paths: List[Path], cpus: Optional[int] = None) -> None:
        if cpus is None:
            cpus = cpu_count()
        worker_paths = [paths[i::cpus] for i in range(cpus)]
        self.query_queues = [Queue() for p in range(cpus)]
        self.result_queue = Queue()

        self.search_workers = [
            Process(
                target=search, args=(paths, q, self.result_queue))
            for paths, q in zip(worker_paths, self.query_queues)
        ]
        for proc in self.search_workers:
            proc.start()

    def teardown_search(self) -> None:
        # Signal process termination
        for q in self.query_queues:
            q.put(None)
        for proc in self.search_workers:
            proc.join()

    def search(self, target: str) -> Iterator:
        for q in self.query_queues:
            q.put(target)
        
        for i in range(len(self.query_queues)):
            for match in self.result_queue.get():
                yield match

def all_source(path: Path, pattern: str) -> Iterator[Path]:
    for root, dirs, files in os.walk(path):
        for skip in {".tox", ".mypy_cache", "__pycache__", ".idea"}:
            if skip in dirs:
                dirs.remove(skip)
        yield from (Path(root) / f for f in files if fnmatch(f,pattern))


if __name__ == "__main__":
    ds = DirectorySearch()
    base = Path.cwd().parent
    all_paths = list(all_source(base, "*.py"))
    ds.setup_search(all_paths)
    for target in ("apple", "test", "try", 'if', 'except Exception'):
        start = time.perf_counter()
        count = 0
        for line in ds.search(target):
            # print(line)
            count += 1
        milliseconds = 1000*(time.perf_counter()-start)
        print(
            f"Found {count} {target!r} in {len(all_paths)} files "
            f"in {milliseconds:.3f}ms"
        )
    ds.teardown_search()



