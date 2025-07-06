from PIL import Image
import os
from pathlib import Path


def get_image_size(paths: list[Path]) -> list[tuple[Path, str, int]]:
    """
    指定されたPathオブジェクトのリストから、画像ファイルのファイル名とサイズを取得します。

    Args:
        paths: ファイルへのPathオブジェクトのリスト。

    Returns:
        (ファイル名, ファイルサイズ) のタプルを含むリスト。
    """
    # 対応する画像ファイルの拡張子
    suffixes: list[str] = ['.jpg', '.jpeg', '.png', '.gif', '.tiff', '.psd']
    results: list[tuple[Path, str, int]] = []

    for path in paths:
        print(path)
        if path.is_file() and path.suffix.lower() in suffixes:
            file_name: str = path.name
            file_size: int = os.path.getsize(path)
            results.append((path, file_name, file_size))
        else:
            print('error:', path)

    return results


def size_format(size: int, unit: str) -> tuple[str, float]:
    """
    与えられたサイズ(size)を指定された単位(unit)に変換します。

    Args:
        size: バイト単位のサイズ。
        unit: 変換先の単位 ('B', 'KB', 'MB', 'GB', 'TB')。

    Returns:
        (単位の文字列, 変換後のサイズ) のタプル。

    Raises:
        ValueError: サポートされていない単位が指定された場合。
    """
    units = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3,
        'TB': 1024 ** 4,
        'PT': 1024 ** 5
    }

    unit = unit.upper()

    if unit in units:
        # 割り算でサイズを変換
        converted_size = size / units[unit]
        # 結果をタプルとして返す
        return unit, round(converted_size, 5)
    else:
        # 不正な単位が指定された場合はエラーを送出する
        raise ValueError(f"'{unit}' は無効な単位です。{list(units.keys())} から指定してください。")


def get_path_list(dir_paths: tuple[Path]) -> list[Path]:
    paths: list[Path] = []

    for item in dir_paths:
        if item.is_dir():
            print(f'dir_name: {item.name}')
        else:
            print('This is not a directory.')
            print(f'file_name: {item.name}')
    return paths

def main():
    print('Run From main:')

    paths_str: list[str] = [r'C:\Users\ZEROPRO\Downloads\kitten.png', r'C:\Users\ZEROPRO\Downloads\download.png', r'./tax.png']
    paths: list[Path] = [Path(path) for path in paths_str]
    print(get_image_size(paths))

    print(size_format(55672, 'B'))


if __name__ == '__main__':
    main()

