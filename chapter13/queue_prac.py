from __future__ import annotations
from pathlib import Path
from queue import Queue
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
        lines.extend(
            l.rstrip() for l in path.read_text().splitlines()
        )


    while True:
        query_text = query_q.get()
        if query_text is None:
            break
        results = [l for l in lines if query_text in l]
        results_q.put(results)
