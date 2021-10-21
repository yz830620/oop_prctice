import time
import concurrent.futures
import ast
from typing import Set, NamedTuple
from pathlib import Path

from directory_search import all_source

class ImportResult(NamedTuple):
    path: Path
    imports: Set[str]

    @property
    def focus(self) -> bool:
        return "typing" in self.imports

class ImportVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.imports: Set[str] = set()
    
    def visit_Import(self, node: ast.Import) -> None:
        for alias in node.names:
            self.imports.add(alias.name)

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.module:
            self.imports.add(node.module)

def find_imports(path: Path) -> ImportResult:
    tree = ast.parse(path.read_text())
    iv = ImportVisitor()
    iv.visit(tree)
    return ImportResult(path, iv.imports)    

def main() -> None:
    start = time.perf_counter()
    base = Path.cwd().parent
    with concurrent.futures.ThreadPoolExecutor(24) as pool:
        analyzers = [
            pool.submit(find_imports, path)
            for path in all_source(base, "*.py")
        ]
        analyzed = (
            worker.result()
            for worker in concurrent.futures.as_completed(analyzers)
        )
    for example in sorted(analyzed):
        print(
            f"{'->' if example.focus else '':2s} "
            f"{example.path.relative_to(base)} {example.imports}"
        )
        end = time.perf_counter()
        rate = 1000 * (end - start) / len(analyzers)
        print(f"Searched {len(analyzers)} files at {rate:.3f}ms/file")

if __name__ == "__main__":
    main()