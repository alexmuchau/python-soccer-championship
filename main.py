from db import Database
from start import starting
from addingData import addingData, title

way = 0

if Database.getTeams() == []:
  starting()
else:
  title('FOGOCHAMPIONSHIP 2022')
  
  while way != 5:
    print("=========================================")
    print(" 1 - COLOCAR DADOS DA RODADA | 2 - CRIAÇÃO DE TIMES | 3 - LISTAR TIMES | 4 - DELETAR TODOS OS TIMES | 5 - SAIR")
    way = int(input("|"+'|'))
    print("=========================================")
    print("")

    if way == 1:
      addingData()
    else:
      if way == 2:
        print(" Quantos times deseja colocar no campeonato?")
        howManyTeams = int(input(""))
        Database.creatingTeams(howManyTeams)
      else:
        if way == 3:
          Database.listTeams()
        else:
          if way == 4:
            Database.deleteAllTeams()
          else:
            if way == 5:
              print("SAINDO")
            else:
              if way != 1 or way != 2 or way != 3 or way != 4 or way != 5:
                print("DIGITE UM NUMERO VALIDO, LAZA")
    
    print("")
        