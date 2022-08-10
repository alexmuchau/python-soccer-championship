import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

print(os.environ["DATABASE_HOST"])
print(os.environ["DATABASE_USER"])
print(os.environ["DATABASE_PASSWORD"])
print(os.environ["DATABASE_DATABASE"])

class Database:
  connection = mysql.connector.connect(
    host = os.environ["DATABASE_HOST"],
    user= os.environ["DATABASE_USER"],
    password= os.environ["DATABASE_PASSWORD"],
    database = os.environ["DATABASE_DATABASE"],
  )

  # CONECTANDO DB
  cursor = connection.cursor()

  @classmethod
  def getTeams(cls):
    connection = mysql.connector.connect(
      host = os.environ["DATABASE_HOST"],
      user= os.environ["DATABASE_USER"],
      password= os.environ["DATABASE_PASSWORD"],
      database = os.environ["DATABASE_DATABASE"],
    )
    cursor = connection.cursor()
    
    get = 'SELECT * FROM teams'
    cursor.execute(get)
    data = cursor.fetchall()
    # print(data)
    return data
  
  @classmethod
  def creatingTeams(cls, __howMany: int):
    connection = mysql.connector.connect(
      host = os.environ["DATABASE_HOST"],
      user= os.environ["DATABASE_USER"],
      password= os.environ["DATABASE_PASSWORD"],
      database = os.environ["DATABASE_DATABASE"],
    )
    
    cursor = connection.cursor()
    
    for i in range(__howMany):
      data = cls.getTeams()
      dataLength = len(data)
      teamName = str(input(f"Nome do {dataLength + 1}º time: "))
      
      teamTable = f'INSERT INTO teams (team_name) VALUES ("{teamName}")'
      cursor.execute(teamTable)
      connection.commit()

  @classmethod
  def listTeams(cls):
    data = cls.getTeams()
    dataLength = len(data)
    for team in range(dataLength):
      print(data[team][2])
    
  def updatingRoundData(_team1: list, _team2: list):
    connection = mysql.connector.connect(
      host = os.environ["DATABASE_HOST"],
      user= os.environ["DATABASE_USER"],
      password= os.environ["DATABASE_PASSWORD"],
      database = os.environ["DATABASE_DATABASE"],
    )
    
    cursor = connection.cursor()
    
    updateTeam1 = f"UPDATE teams SET team_points = {_team1[0]}, "\
      f"team_games= {_team1[2]}, "\
      f"team_wins= {_team1[3]}, "\
      f"team_draws= {_team1[4]}, "\
      f"team_defeats= {_team1[5]}, "\
      f"team_gols= {_team1[6]}, "\
      f"team_gols_against= {_team1[7]}, "\
      f"team_gols_difference= {_team1[8]} "\
      f"WHERE team_name = '{_team1[1]}'"
      
    updateTeam2 = f"UPDATE teams SET team_points = {_team2[0]}, "\
      f"team_games= {_team2[2]}, "\
      f"team_wins= {_team2[3]}, "\
      f"team_draws= {_team2[4]}, "\
      f"team_defeats= {_team2[5]}, "\
      f"team_gols= {_team2[6]}, "\
      f"team_gols_against= {_team2[7]}, "\
      f"team_gols_difference= {_team2[8]} "\
      f"WHERE team_name = '{_team2[1]}'"
      
    cursor.execute(updateTeam1)
    cursor.execute(updateTeam2)
    connection.commit()
    
    print("SUCCESSFUL UPDATE")
    print("")
    
  def deleteAllTeams():
    connection = mysql.connector.connect(
      host = os.environ["DATABASE_HOST"],
      user= os.environ["DATABASE_USER"],
      password= os.environ["DATABASE_PASSWORD"],
      database = os.environ["DATABASE_DATABASE"],
    )
    
    cursor = connection.cursor()
    
    delete = 'DELETE FROM teams WHERE id >= 0'
    cursor.execute(delete)
    connection.commit()
    
    print("SUCCESSFUL DELETE")
    
  # FECHANDO CONEXÃO DB
  cursor.close()
  connection.close()