from db import Database
import time


def starting():
  print("=========================================")
  print("COMEÇANDO FOGOCHAMPIONSHIP 2022")
  print("=========================================")
  time.sleep(2)
  print("\n" * 130)
  
  print("=========================================")
  howManyTeams = int(input("QUANTIDADE DE TIMES QUE DESEJA REGISTRAR: "))
  
  Database.creatingTeams(howManyTeams)