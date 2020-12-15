from os import listdir

data = listdir('./valemid')
new_data = map(lambda x: x.removesuffix('.json'), data)
print(list(new_data))
