
def get_stations(stations: dict[str:set[str]], need_regions: set[str]) -> set[str]:
    need_stations = set()

    while need_regions:
        best_station = str()
        covered_regions = set()

        for station, regions in stations.items():
            intersection_regions = need_regions & regions

            if len(intersection_regions) > len(covered_regions):
                best_station = station
                covered_regions = intersection_regions

        need_regions -= covered_regions
        need_stations.add(best_station)

    return need_stations


if __name__ == '__main__':
    centre_stations = {
        'Европа Плюс': {'Москва', 'Тверь', 'Великий Новгород', 'Санкт-петербург'},
        'Питер FM': {'Великий Новгород', 'Санкт-петербург', 'Петрозаводск', 'Псков'},
        'Радио Экстрим': {'Москва', 'Тверь', 'Великий Новгород', 'Санкт-петербург'},
        'Юмор FM': {'Москва', 'Владимир', 'Иваново', 'Рязань', 'Нижний Новгород'},
        'BEST DEEP FM': {'Мурманск', 'Архангельск'},
        'Comedy Radio': {'Ярославль', 'Вологда', 'Кострома', 'Киров'},
        'DNB FM': {'Тула', 'Калуга', 'Орёл', 'Брянск'},
        'Energy': {'Рязань', 'Тула', 'Москва', 'Нижний Новгород'},
        'Hard Rock FM': {'Москва', 'Ярославль', 'Тверь'},
    }

    need_regions_1 = {'Москва', 'Архангельск', 'Кострома', 'Ярославль'}
    need_regions_2 = {'Тверь', 'Псков', 'Тула'}
    need_regions_3 = {'Москва', 'Ярославль', 'Тверь'}

    print(get_stations(centre_stations, need_regions_1))
    print(get_stations(centre_stations, need_regions_2))
    print(get_stations(centre_stations, need_regions_3))
