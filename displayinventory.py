


def displayInventory(inventory):
    numberOfItems = 0
    print('Inventory')
    for v in inventory.values():
        numberOfItems += v
    for k, v in inventory.items():
        print('%d %s' % (v,k))
    print('Total number of items: ' + str(numberOfItems))



dict1 = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(dict1)
        
