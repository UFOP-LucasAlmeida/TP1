import classes

filaTarefas = classes.FilaTarefas(5)
listaMaquinas = list()
listaFuncionarios = list()
print("################# TRABALHO 1 SISTEMAS OPERACIONAIS #################")

numMaquinas = int(input("\n Digite o número de máquinas "))
for x in range(numMaquinas):
    idM = input("\n Digite o identificador da máquina %i : " %(x+1))
    listaMaquinas.append(classes.Maquina(idM))
tamanhoFila = int(input("\n Digite a capacidade da fila de tarefas: "))
numFuncionarios = int(input("\n Digite o número de funcionários: "))
for x in range(numFuncionarios):
    try:
        f= open("func%i.txt" %(x+1))
    except:
        print("Arquivo do funcionario %i nao encontrado" %(x+1))
    f.close()

    print("Arquivo do funcionario %i: func%i.txt" %(x+1,x+1))
    listaFuncionarios.append(classes.Funcionario(x+1))

filaTarefas = classes.FilaTarefas(tamanhoFila)
for maquina in listaMaquinas:
    maquina.filaTarefas = filaTarefas
    

filaTarefas.inserir([0,1])

x = 0


