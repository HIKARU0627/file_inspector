from img import get_image_size, get_path_list, size_format
from pathlib import Path

def main():
    print('Run From main:')

    paths_str: list[str] = [r'C:\Users\ZEROPRO\Downloads\kitten.png', r'C:\Users\ZEROPRO\Downloads\download.png', r'./tax.png']
    paths: list[Path] = [Path(path) for path in paths_str]
    print(get_image_size(paths))

    print(size_format(55672, 'kb'))


if __name__ == '__main__':
    main()