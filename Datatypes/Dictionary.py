
dict1 = {
    1 : 'Kunal' 'Rajendra' 'Patil',
    2 : 'Samarjeet',
    3 : 'Soham',
    4 : 'Alfaj',
    5 : 'Piyush'
}

#get()
print(dict1.get(1))

#items()
print(dict1.items())

#keys()
print(dict1.keys())

#values()
print(dict1.values())

#update()
dict2 = {
    6:'Atharv',
    7:'Varad'
}
dict1.update(dict2)
print(dict1)

#pop()
dict1.pop(6)
print("6 is poped :\n",dict1)

#delete 
del dict1[7]
print(dict1)
