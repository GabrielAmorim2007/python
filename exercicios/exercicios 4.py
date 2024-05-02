x = 1
while x > 0:
    val = input("escreva BD para bom dia \n escreva BT para boa tarde \n escreva BN para boa noite\n ou X para sair\n") 
    if val == "BD":
        print("bom dia pessoa")
        x = x-1
    elif val == "BT":
        print("boa tarde pessoa")
        x = x-1
    elif val == "BN":
        print("Boa noite pessoa")
        x = x-1
    elif val == "X":
        x = x-1
    else:
        print("valor errado".upper())
    


print("voce saiu do loop")