def move_hanoi_towers(n, source, destination, auxiliary, towers):
    if n == 0:
        return

    move_hanoi_towers(n-1, source, auxiliary, destination, towers)

    print (f'Перемістити диск з {source} на {destination}: {n}')
    value = towers[source].pop()
    towers[destination].append(value)
    print(f'Проміжний стан: {towers}')

    move_hanoi_towers(n-1, auxiliary, destination, source, towers)

towers = {
    'A': [3, 2, 1],
    'B': [],
    'C': []
}
n = len(towers['A'])
print(f'Початковий стан: {towers}')
move_hanoi_towers(n, 'A', 'C', 'B', towers)
print(f'Кінцевий стан: {towers}')
