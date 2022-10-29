#Exercise 1

from collections import OrderedDict

inventory = {
 'gold' : 500,
 'pouch' : ['flint', 'twine', 'gemstone'],
 'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

inventory['pocket'] = 'seashell', 'strange berry', 'lint'

inventorySorted = OrderedDict(sorted(dict.items(inventory)))

print("Sorted Inventory:", inventorySorted)

inventory['backpack'] = 'xylophone', 'bedroll','bread loaf'

print("Inventory after value 'dagger' is deleted from 'backpack' key:", inventory)

inventory['gold'] = '500', '50'

print("New inventory after '50' value is added to 'gold' key:", inventory)