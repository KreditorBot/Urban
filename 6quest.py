immutable_var = 1, 2, True, 'String'
print(immutable_var)
#immutable_var[0]=2
#кортежи это неизменяемые множества, они нужны для сохранения своей константности (защита от изменений)
mutable_list = [1, 2, True, 'String']
mutable_list[2]=False
print(mutable_list)