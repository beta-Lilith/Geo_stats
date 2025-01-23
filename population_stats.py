import logging

from utils import configure_logging, read_data, write_data
from constants import DATA_PATH, DOWNLOAD_DIR


def calculate_population_stats(data):
    population_stats = dict()
    for feature in data['features']:
        continent = feature['properties']['continent']
        population = feature['properties']['pop_est']
        if continent not in population_stats:
            population_stats[continent] = {
                'min': population,
                'max': population,
                'sum': population,
            }
        else:
            population_stats[continent]['min'] = min(
                population_stats[continent]['min'],
                population,
            )
            population_stats[continent]['max'] = max(
                population_stats[continent]['max'],
                population,
            )
            population_stats[continent]['sum'] += population
    return population_stats


if __name__ == '__main__':
    configure_logging()
    file_name = 'stats.json'
    write_data(
        calculate_population_stats(read_data(DATA_PATH)),
        file_name)
    logging.info(f'Данные записаны в файле {DOWNLOAD_DIR/file_name}')
