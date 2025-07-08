from pathlib import Path

def get_suffix(paths: list[Path]) -> list[tuple[Path, str, str]]:
    results: list[tuple[Path, str, str]] = []

    for path in paths:
        if path.is_file():
            results.append((path, path.name, path.suffix))
        else:
            results.append((path, None, None))

    return results