assets = {
    'в': (3, 25), 
    'п': (2, 15), 
    'б': (2, 15), 
    'а': (2, 20),
    'и': (1, 5), 
    'н': (1, 15), 
    'т': (3, 20), 
    'о': (1, 25),
    'ф': (1, 15), 
    'д': (1, 10), 
    'к': (2, 20), 
    'р': (2, 20)
}

defualt_pont = 15
score = - sum(it for items , it in assets.values()) + defualt_pont

def InventoryList(temp, capacity):
    items = list(temp.items())
    IL = [[([], score) for items in range(capacity + 1)] for items in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        for j in range(1, capacity + 1):
            item = items[i - 1]
            a, b, c = item[0], item[1][0], item[1][1]

            if b > j:
                IL[i][j] = IL[i - 1][j]
            else:
                IL[i][j] = max(IL[i - 1][j], (IL[i - 1][j - b][0] + [a], 
                IL[i - 1][j - b][1] + c * 2), key=lambda x: x[1])
    return IL


inventoryItems = InventoryList(assets, 9)  
optimized = list(inventoryItems[-1][-1])  
 
 
index, range1, range2 = [], list(range(len(optimized[0]) // 2 + 1)), list(range(-1, -len(optimized[0]) // 2, -1))

for i in range(max(len(range1), len(range2))):
    try:
        index.append(range1[i])
    except IndexError:
        pass
    try:
        index.append(range2[i])
    except IndexError:
        pass

inventory = []
for i in index:
    item = optimized[0][i]

    if assets[item][0] == 2:
        inventory.extend([item] * 2)
    elif assets[item][0] == 1:
        inventory.extend([item])

print('total score of Tom: ', optimized[1])
if optimized[1] > 0:
    print('Tom will survive') 
elif optimized[1] < 0 or optimized[1] == 0:
    print('Tom can not survive')

print(''.join([f'[{inventory[i]}],' 
if i % 3 != 2 
else f'[{inventory[i]}]\n' 
for i in range(len(inventory))]))