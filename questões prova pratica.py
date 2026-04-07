#teste de maquina integrada:
print("Bem vindo á prova prática 2")

def menu():
    print("1-Questão 1:média aritmética dos números pares e a média aritmética dos números ímpares\n"
           "2-Questão 2:Calculadora de média\n",
           "3-Questão 3:programa que lê vários valores reais\n",
           "4-Questãp 4: Calculadora\n"

             )
def questao_1() :
        ct = 0
        soma = 0
        ctp = 0
        cti = 0
        somap = 0
        somai = 0
        print("Digite 0 para sair do programa")
        while True:
            num = float(input("Digite um número: "))
            if num == 0:
                break
            ct += 1
            soma += num
            if num % 2 == 0:
                ctp += 1
                somap += num
            else:
                cti += 1
                somai += num
        média_pares = somap / ctp
        média_impares = somai / cti
        print("A quatidade total de números digitados é:", ct)
        print("A soma total dos números é igual a:", soma, )
        print("A média dos pares é:", média_pares, )
        print("A média dos ímpares é:", média_impares, )




def questao_2():
        alunos = 0
        média = 0
        soma = 0
        alaprovado = 0
        alreprovado = 0
        print("Bem vindo à calculadora de médias")
        disciplina = input("Insira o nome da disciplina: ")
        print("Digite -1 para sair da sequência")

        while True:
            nota = float(input("Insira a nota: "))
            if nota == -1:
                break
            alunos += 1
            soma += nota
            if nota >= 5:
                alaprovado += 1
            else:
                alreprovado += 1

        média = soma / alunos
        print("O total de alunos é:", alunos)
        print("A média dos alunos é", média)
        print("a quantidade de alunos aprovados é:", alaprovado)
        print("a quantidade de alunos reprovados é:", alreprovado)
def questao_3():
        ct = 0
        somat = 0
        nuummaior20 = 0
        print("Digite 0 para sair da sequência")
        while True:
            num = float(input("Digite um número:"))
            if num == 0:
                break
            somat += num
            ct += 1
            if num > 20:
                nuummaior20 += 1
            ct += 1
        print("A soma dos números digitados é: ", somat)
        print("A quantidade de números digitados é: ", ct)
        print("A média dos números digitados é: ", somat / ct)
        print("A quantidade de números maiores que 20 é de:", nuummaior20)
def questao_4():
        print("Bem vindo à calculadora ")
        num1 = float(input("Digite o primeiro número: "))

        num2 = float(input("Digite o segundo número: "))

        operation = input("Digite a operação desejada( +,-,*,/): ")

        if operation == "+":
            result = num1 + num2; print("O resultado da soma é: ", result)

        elif operation == "-":
            result = num1 - num2; print("O resultado da subtração é: ", result)

        elif operation == "*":
            result = num1 * num2; print("O resultado da multiplicação é: ", result)

        elif operation == "/":
            result = num1 / num2; print("O resultado da divisão é: ", result)
while True:
     menu()
     n= int(input("Digite a opção desejada: "))
     if n ==0:
         break
     elif n == 1:
         questao_1()
     elif n == 2:
         questao_2()
     elif n == 3:
         questao_3()
     elif n == 4:
         questao_4()

     input("\nPressione Enter para voltar ao menu")
