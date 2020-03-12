class Person(object):
    def __init__(self, name, birthday=None, teste=None):
        self.name = name
        self.birthday = birthday
        self.teste = teste
        self.last_name = name.split(' ')[-1]

    def get_last_name(self):
        return self.last_name

    def __str__(self):
        return 'Nome: ' + self.last_name + ', ' + self.name

    def __repr__(self):


marcos = Person('Marcos Manfrin', None, 1)

print(marcos)
print(marcos.last_name)
print(marcos.birthday)
print(marcos.teste)


print('.')
