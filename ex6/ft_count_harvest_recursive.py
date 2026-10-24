def ft_count_down(days):
    if days == 0:
        return
    ft_count_down(days - 1)
    print(f'Day {days}')


def ft_count_harvest_recursive():
    harvest_day = int(input('Days until harvest: '))
    ft_count_down(harvest_day)
    print('Harvest time!')
