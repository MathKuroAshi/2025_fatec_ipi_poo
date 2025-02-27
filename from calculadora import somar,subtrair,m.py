from calculadora import somar,subtrair,multiplicar,dividir
def menu(opcao):
    while opcao != 0:
        opcao = int(input("1 - Somar\n0 - Sair\n"))
        if opcao == 1:
            print("Soma entre {} e {} é {}".format(x,y,somar(x,y)))
    print("Obrigado por usar a calculadora")
opcao = 5
x = int(input("Digite em número: "))
y = int(input("Digite outro número: "))