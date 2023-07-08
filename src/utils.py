def get_top(list_):
    """
    Получает топ вакансий
    из списка
    :param list_: список из которого берется топ
    :return: top_list: сам топ
    """
    top_n = int(input('\nВведите количество вакансий,\n'
                      f'которое вы хотели бы видеть из '
                      f'{len(list_)}:\n'))
    top_list = list_[:top_n]
    print(f'\nТоп вакансий по вашему запросу в количестве {top_n}:\n')
    for item in top_list:
        for key, value in item.items():
            print(value)
        print('\n')
    return top_list
