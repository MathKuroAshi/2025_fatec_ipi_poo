from calculadora import somar,subtrair,multiplicar,dividir
def menu(opcao):
    while opcao != 0:
        opcao = int(input("1 - Somar\n2 - Subtrair\n3 - Multiplicar\n0 - Sair\n"))
        if opcao == 1:
            print("Soma entre {} e {} é {}".format(x,y,somar(x,y)))
        elif opcao == 2:
            print("Subtração entre {} e {} é {}".format(x,y,subtrair(x,y)))
        elif opcao == 3:
            print("Multiplicação entre {} e {} é {}".format(x,y,multiplicar(x,y)))
    print("Obrigado por usar a calculadora")
opcao = 5
x = int(input("Digite em número: "))
y = int(input("Digite outro número: "))