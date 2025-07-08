from img import get_image_length, get_path_list, size_format, get_image_size
from type import get_suffix
from pathlib import Path

def main():
    print('Run From main:')

    paths_str: list[str] = [r'C:\Users\ZEROPRO\Downloads\kitten.png', r'C:\Users\ZEROPRO\Downloads\download.png', r'./tax.png']
    paths: list[Path] = [Path(path) for path in paths_str]
    # print(get_image_length(paths))

    # print(size_format(55672, 'kb'))

    # print(get_image_size(paths))

    print(get_suffix(paths))
if __name__ == '__main__':
    main()