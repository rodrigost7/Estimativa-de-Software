#E =  a x (ksloc^b)
#T = 2.5 x (E^c)
#P = E/T

print("---------------------------------------------------")
print("|** INFORME NÚMERO DO MODO QUE DESEJA UTILIZAR ***|\n|1 - Orgânico                                     |\n|2 - Semi-destacado                               |\n|3 - Embutido                                     |")
print("---------------------------------------------------")
modo = input("Digite o número do Modo desejado: ")

ksloc_primary= int(input("Informe a quantidade de pessoas: "))

ksloc= float(ksloc_primary)

match modo:
    case "1": #ORGANICO
        RELY = 1.15
        EAF = RELY
        E = 2.4*(ksloc**1.05)*EAF
        T = 2.5*(E**0.38)
        P = E/T
        print("\nModo ôrganico:")
        print("E = {:.2f}".format(E))
        print("T = {:.2f}".format(T))
        print("P = {:.2f}".format(P))
    
    case "2": #SEMI-DESTACADO
        RELY = 1.15
        EAF = RELY
        E = 3.0*(ksloc**1.12)*EAF
        T = 2.5*(E**0.35)
        P = E/T
        print("\nModo Semi-destacado:")
        print("E = {:.2f}".format(E))
        print("T = {:.2f}".format(T))
        print("P = {:.2f}".format(P))
    
    case "3":#EMBUTIDO
        RELY = 1.15
        EAF = RELY
        E = 3.6*(ksloc**1.20)*EAF
        T = 2.5*(E**0.32)
        P = E/T
        print("\nModo Embutido:")
        print("E = {:.2f}".format(E))
        print("T = {:.2f}".format(T))
        print("P = {:.2f}".format(P))

    case _: #caso nao seja nenhum
        print("Por favor, seleicone uma opção válida!")