


def displayInventory(inventory):
    numberOfItems = 0
    print('Inventory')
    for v in inventory.values():
        numberOfItems += v
    for k, v in inventory.items():
        print('%d %s' % (v,k))
    print('Total number of items: ' + str(numberOfItems))



def addToInventory(inventory, addedItems):
    for listItem in addedItems:
        inventory.setdefault(listItem,0)
    for k in inventory.keys():
        for listItem in addedItems:
            if k == listItem:
                inventory[k] += 1
            else:
                inventory[k] += 0


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inv, dragonLoot)
displayInventory(inv)

    
