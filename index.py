#coding: utf-8
escolha=0
total=0
while escolha!=10:
    from os import system
    system('clear')
    print("MENU\n1|Sanduiches\n2|Bebidas\n3|Valor Total\n4|Finalizar pedido")
    escolha=int(input("Digite sua opção e dê enter"))
    if escolha==1:
        from time import sleep
        sleep(2)
        from os import system
        system('clear')
        print("1|X-Tudo - R$ 8,00\n2|X-Salada - R$7,00\n3|X-Vegui - R$10,00\n4|Voltar\n")
        escolha=int(input("Digite sua opção e dê enter"))
        if escolha==1:
            from time import sleep
            sleep(2)
            from os import system
            system('clear')
            total=total+8
            print("Você pediu um X-Tudo\nValor total: R$", total)
            print ("1|Retornar ao menu principal\n10|Finalizar Pedido")
            escolha=int(input("Digite sua opção e dê enter"))
            from time import sleep
            sleep(2)
            from os import system
            system('clear')
            if escolha==10:
                print("Pedido Finalizado")
        elif escolha==2:
            from time import sleep
            sleep(2)
            from os import system
            system('clear')
            total=total+7
            print("Você pediu um X-Salada\nValor total: R$", total)
            print ("1|Retornar ao menu principal\n10|Finalizar Pedido")
            escolha=int(input("Digite sua opção e dê enter"))
            from time import sleep
            sleep(2)
            from os import system
            system('clear')
            if escolha==10:
                print("Pedido Finalizado")
        elif escolha==3:
            from time import sleep
            sleep(2)
            from os import system
            system('clear')
            total=total+10
            print("Você pediu um X-Vegui\nValor total: R$", total)
            print ("1|Retornar ao menu principal\n10|Finalizar Pedido")
            escolha=int(input("Digite sua opção e dê enter"))
            from time import sleep
            sleep(2)
            from os import system
            system('clear')
            if escolha==10:
                print("Pedido Finalizado")
    elif escolha==2:
        from time import sleep
        sleep(2)
        from os import system
        system('clear')
        print("1|Refrigerante Lata - R$3,00\n2|Refrigerante 2l - R$7,00\n3|Suco - R$4,00\n4|Voltar\n")
        escolha=int(input("Digite sua opção e dê enter"))
        if escolha==1:
            from time import sleep
            sleep(2)
            from os import system
            system('clear')
            total=total+3
            print("Você pediu um refrigerante lata\nValor total: R$", total)
            print ("1|Retornar ao menu principal\n10|Finalizar Pedido")
            escolha=int(input("Digite sua opção e dê enter"))
            from time import sleep
            sleep(2)
            from os import system
            system('clear')
            if escolha==10:
                print("Pedido Finalizado")
        elif escolha==2:
            from time import sleep
            sleep(2)
            from os import system
            system('clear')
            total=total+7
            print("Você pediu um Refrigerante 2l\nValor total: R$", total)
            print ("1|Retornar ao menu principal\n10|Finalizar Pedido")
            escolha=int(input("Digite sua opção e dê enter"))
            from time import sleep
            sleep(2)
            from os import system
            system('clear')
            if escolha==10:
                print("Pedido Finalizado")
        elif escolha==3:
            from time import sleep
            sleep(2)
            from os import system
            system('clear')
            total=total+4
            print("Você pediu um Suco\nValor total: R$", total)
            print ("1|Retornar ao menu principal\n10|Finalizar Pedido")
            escolha=int(input("Digite sua opção e dê enter"))
            from time import sleep
            sleep(2)
            from os import system
            system('clear')
            if escolha==10:
                print("Pedido Finalizado")
    elif escolha == 3:
        print("O valor total é", total)
    else:
        from os import system
        system('clear')
        print("Pedido Finalizado")
        escolha=10