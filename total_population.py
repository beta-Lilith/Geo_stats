from collections import defaultdict

from constants import DATA_PATH
from utils import read_data


EXPECTED_RESULT = {
    'Oceania': 36782844,
    'Africa': 1219176238,
    'North America': 573042112,
    'Asia': 4389144868,
    'South America': 418540749,
    'Europe': 746398461,
    'Seven seas (open ocean)': 140,
    'Antarctica': 4050,
}


def population_by_continent(data):
    population_by_continent = defaultdict(int)
    for feature in data['features']:
        continent = feature['properties']['continent']
        population = feature['properties']['pop_est']
        population_by_continent[continent] += population
    return population_by_continent


if __name__ == '__main__':
    data = read_data(DATA_PATH)
    result = population_by_continent(data)
    assert result == EXPECTED_RESULT, (
        f'Ожидаемые данные: {EXPECTED_RESULT} Вывод: {result}'
    )
    print(result)
