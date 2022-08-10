from db import Database

def rankingTeams():
  rankedTeams = []
  rankedTeamsLength = 1
  
  teams = Database.getTeams()
  teamsLength = len(teams)
  
  for team in range(teamsLength):
    if team == 0:
      rankedTeams.append(teams[team])
    else:
      for rankedTeam in range(rankedTeamsLength):
        if teams[team][1] > rankedTeams[rankedTeam][1]:
          rankedTeams.insert(rankedTeams.index(rankedTeams[rankedTeam]), teams[team])
          break
        else:
          if rankedTeam == rankedTeamsLength - 1:
            rankedTeams.append(teams[team])
          if teams[team][1] == rankedTeams[rankedTeam][1]:
            rankedTeams.append(teams[team])
            break
        
        rankedTeamsLength = len(rankedTeams)
        
  
  print(rankedTeams)
  
rankingTeams()