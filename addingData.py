from db import Database
import time

def title(__name: str):
  for i in range(10):
    print("-"*i, end='')
    time.sleep(0.2)

  print('')

  print(__name)

  for i in range(10):
    print("-" * i, end='')
    time.sleep(0.2)

  print('')
  print("\n" * 130)

def creatingRound():
  teams = Database.getTeams()
  teamsLength = len(teams)
  teamsExist = False
  
  while teamsExist == False:
    print("===========================")
    print("Deseja criar uma rodada entre quais times?")
    team1_name = str(input("Time 1: "))
    team2_name = str(input("Time 2: "))
    print("===========================")
    
    # IS EXIST?
    team = 0
    isExistT1 = 0
    while isExistT1 < 1:
      isExistT1 = teams[team][2].count(team1_name)
      
      if isExistT1 == 1:
        oldDataTeam1 = teams[team]
        break
      
      if team == teamsLength - 1:
        isExistT1 = 2
        
      team += 1
    
    team = 0
    isExistT2 = 0
    while isExistT2 < 1:
      isExistT2 = teams[team][2].count(team2_name)
      
      if isExistT2 == 1:
        oldDataTeam2 = teams[team]
        break
      
      if team == teamsLength - 1:
        isExistT2 = 2
      
      team += 1
      
    # ROUTES
    if isExistT1 == 1 and isExistT2 == 1:
      # print(f"{team1_name} e {team2_name}")
      teamsExist = True
    else:
      if isExistT1 != 1:
        print("Digite um TIME1 válido")
      if isExistT2 != 1:
        print("Digite um TIME2 válido")
          
  addingRoundData(oldDataTeam1, oldDataTeam2)
  
def addingRoundData(__old_data_team1, __old_data_team2):
  team1_name = __old_data_team1[2]
  team2_name = __old_data_team2[2]
  
  title(f"Iniciando rodada {team1_name} x {team2_name}")
  
  print("=======================")
  print(f"QUANTOS GOLS O {team1_name} FEZ NA PARTIDA?")
  team1_gols = int(input("|"+'|'))
  print("")
  print(f"QUANTOS GOLS O {team2_name} FEZ NA PARTIDA?")
  team2_gols = int(input("|"+'|'))
  print("")
  print("=======================")
  
  # WHO WIN VERIFICATION
  if team1_gols > team2_gols:
    # POINTS
    team1_points = __old_data_team1[1] + 3
    team2_points = __old_data_team1[1]
    
    # WINS, DEFEATS, DRAWS
    team1_wins = __old_data_team1[4] + 1
    team1_defeats = __old_data_team1[6]
    
    team2_wins = __old_data_team2[4]
    team2_defeats = __old_data_team2[6] + 1
    
    team1_draws = __old_data_team1[5]
    team2_draws = __old_data_team2[5]
  else:
    if team2_gols > team1_gols:
      # POINTS
      team1_points = __old_data_team1[1]
      team2_points = __old_data_team1[1] + 3
      
      # WINS, DEFEATS, DRAWS
      team2_wins = __old_data_team2[4] + 1
      team2_defeats = __old_data_team2[6]
      
      team1_wins = __old_data_team1[4]
      team1_defeats = __old_data_team1[6] + 1
      
      team1_draws = __old_data_team1[5]
      team2_draws = __old_data_team2[5]
    else:
      if team2_gols == team1_gols:
        # POINTS
        team1_points = __old_data_team1[1] + 1
        team2_points = __old_data_team1[1] + 1
        
        # WINS, DEFEATS, DRAWS
        team1_draws = __old_data_team1[5] + 1
        team2_draws = __old_data_team2[5] + 1
        
        team1_wins = __old_data_team1[4]
        team2_wins = __old_data_team2[4]
        
        team1_defeats = __old_data_team1[6]
        team2_defeats = __old_data_team2[6]
  
  # VALUE ASSIGNMENT
  team1_games = __old_data_team1[3] + 1
  team2_games = __old_data_team2[3] + 1
  
  team1_gols_against = team2_gols + __old_data_team1[8]
  team1_gols_difference = __old_data_team1[9] + (team1_gols - team2_gols)
  
  team2_gols_against = team1_gols + __old_data_team2[8]
  team2_gols_difference = __old_data_team2[9] + (team2_gols - team1_gols)
  
  team2_gols = team2_gols + __old_data_team2[7]
  team1_gols = team1_gols + __old_data_team1[7]
    
  # LIST OF ALL INFO ABOUT TEAM1 AND TEAM2
  team1AllData = [team1_points, team1_name, team1_games, team1_wins, team1_draws, 
                   team1_defeats, team1_gols, team1_gols_against, team1_gols_difference]
  
  team2AllData = [team2_points, team2_name, team2_games, team2_wins, team2_draws,
                   team2_defeats, team2_gols, team2_gols_against, team2_gols_difference]
  
  Database.updatingRoundData(team1AllData, team2AllData)
  
def teamRounds():
  teams = Database.getTeams()
  teamsLength = len(teams)
  for i in range(teamsLength):
    print(f"O time {teams[i][2]} esta na {teams[i][3] + 1}ª rodada")

def addingData():
  way = 0
  
  title("ADICIONAR DADOS")
  while way != 3:
    print("=======================")
    print(" 1 - CRIAR RODADA | 2 - LISTAR TIMES | 3 - VOLTAR")
    way = int(input("|"+'|'))
    print("=======================")
    print("")
    
    if way == 1:
      creatingRound()
      print("")
    else:
      if way == 2:
        teamRounds()
        print("")
      else:
        if way == 3:
          print("VOLTANDO")
        else:
          print("Digite um numero correto")
          print("")

    
  
      