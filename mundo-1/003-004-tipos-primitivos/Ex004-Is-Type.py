x = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(x))
print(x.isalnum(),'-> Para alfabético e numérico')
print(x.isalpha(),'-> Para alfabético')
print(x.isnumeric(),'-> Para numérico')
print(x.isdecimal(),'-> Para decimal')
print(x.isupper(),'-> Para tudo maiúsculo')
print(x.islower(),'-> Para tudo minúsculo')
print(x.isascii(),'-> Para tudo ser espaço')