def ft_harvest_total():
    num_days = 3
    total_weight = 0
    for i in range(num_days):
        weight = int(input(f'Day {i + 1} harvest: '))
        total_weight += weight
    print('Total harvest weight: ' + str(total_weight))
