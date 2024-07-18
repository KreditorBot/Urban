my_dict = {'Google': 980907896, 'Yandex': 5678546, 'Onion': 47458754}
print('Dict:', my_dict)
print('Existing value:', my_dict['Google'])
print('Not existing value:', my_dict.get('Bing'))
my_dict.update({
    'Rambler': 56758,
    'Siri': 4756865798
})
print('Deleted value:', my_dict.pop('Siri'))
print('Modified dictionary:', my_dict)

my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 'String', False, (1, 4, 6)}
print('Set:', my_set)
my_set.update([90, 80])
my_set.discard(90)
print('Modified set:', my_set)