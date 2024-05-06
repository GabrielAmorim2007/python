name = input("nome ")

while len(name) != 3:           
    print("tem que ter no minimo 3 caractere")
    name = input("nome ")
print("nome validao, " + name)