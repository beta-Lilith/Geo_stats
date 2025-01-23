import os


def find_files_with_extension(directory, extension):
    if not extension.startswith('.'):
        extension = '.' + extension
    file_paths = list()
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(extension):
                file_paths.append(os.path.join(dirpath, filename))
    return file_paths


if __name__ == '__main__':
    directory = input('Введите путь к директории: ')
    extension = input('Введите расширение файлов: ')
    file_paths = find_files_with_extension(directory, extension)
    if file_paths:
        print(
            'Найденные файлы:',
            *file_paths,
            sep='\n'
        )
    else:
        print(
            f'Не найдено ни одного файла с расширением {extension} '
            f'в дирректории {directory} и ее поддиректориях.'
        )
