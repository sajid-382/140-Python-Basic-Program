from collections import OrderedDict
# Create an OrderedDict
ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])
print(ordered_dict)

new_item = ('a',1)

new_ordered_dict = OrderedDict([new_item])

new_ordered_dict.update(ordered_dict)

print(new_ordered_dict)