def ft_count_harvest_iterative():
    harvest_day = int(input("Days until harvest: "))
    for i in range(harvest_day):
        i += 1
        print(f'Day {i}')
    print('Harvest time!')
