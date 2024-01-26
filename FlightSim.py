import numpy as np
import random
from math import *
from operator import attrgetter

class Team: #Creates an object to define each team
  
  def __init__(self, name, elo):
    self.name = name
    self.elo = elo #team's starting elo rating
    self.snitch = 0 #how many times in a game the team catches the snitch
    self.score = 0 #what a team's final score is
    self.winone = 0 #=1 if a team wins their first game
    self.wintwo = 0 #=1 if a team wins their second game
    self.winthree = 0 #=1 if a team wins their third game
    self.totalwin = 0
    self.breaker = 0 #If a team made the 2-0 game (first tiebreaker)
    self.rbsc = 0 #Teams' record before snitch catch (second tiebreakers)
    self.qpa = 0 #Total Quaffle Points against (third tiebreaker)
    self.qpf = 0 #Total Quaffle Points for (fourth tiebreaker)
    self.totalsnitch = 0 #Total snitch catches in flight play (fifth tiebreaker)
    self.flight = 0
    self.roundone = ""

''' This next formula is def a bs formula I made based on some
score outcomes I made for a scorigami thing that never came out
but it seems like it works. Essentially just picks a midpoint value
of a predicted winner's score at a certain score differential, adds
a little random bs to it, and outputs the score value of the winning
team. It gets really repetitive because I couldn't find a nice way
to code it for the multiple values, so if you read this paragraph 
you can just skip the next part of the code, it's pretty ugly.'''

def scorigami(score): 
  if abs(score) == 10:
    winscore = round(90 + np.random.normal()*sqrt(180), -1)
    if winscore < abs(score)+30:
      winscore = 40
  elif abs(score) == 20:
    winscore = round(90 + np.random.normal()*sqrt(180), -1)
    if winscore < abs(score)+30:
      winscore = 50
  elif abs(score) == 30:
    winscore = round(100 + np.random.normal()*sqrt(200), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 40:
    winscore = round(100 + np.random.normal()*sqrt(200), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 50:
    winscore = round(110 + np.random.normal()*sqrt(220), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 60:
    winscore = round(110 + np.random.normal()*sqrt(220), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 70:
    winscore = round(120 + np.random.normal()*sqrt(240), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 80:
    winscore = round(120 + np.random.normal()*sqrt(240), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 90:
    winscore = round(130 + np.random.normal()*sqrt(260), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 100:
    winscore = round(140 + np.random.normal()*sqrt(280), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 110:
    winscore = round(150 + np.random.normal()*sqrt(300), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 120:
    winscore = round(150 + np.random.normal()*sqrt(300), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 130:
    winscore = round(160 + np.random.normal()*sqrt(320), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 140:
    winscore = round(160 + np.random.normal()*sqrt(320), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 150:
    winscore = round(160 + np.random.normal()*sqrt(320), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 160:
    winscore = round(180 + np.random.normal()*sqrt(360), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 170:
    winscore = round(190 + np.random.normal()*sqrt(380), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 180:
    winscore = round(190 + np.random.normal()*sqrt(380), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) == 190:
    winscore = round(200 + np.random.normal()*sqrt(400), -1)
    if winscore < abs(score):
      winscore = abs(score)
  elif abs(score) >= 200:
    winscore = round(210 + np.random.normal()*sqrt(420), -1)
    if winscore < abs(score):
      winscore = abs(score)
  return winscore

def game(Team1, Team2, roundnum):
  Elodiff = Team1.elo - Team2.elo #Determines difference in team Elo ratings
  PredQPD = Elodiff*0.1844 #Determines predicted outcome based on Regression Model
  Zval = np.random.normal() #Sets a random Zscore for setting prediction interval
  ActualQPD = PredQPD+Zval*44.66542 #Uses randomly generated z score and the Residual Standard Error to randomly determine score differential
  RoundDiff = round(ActualQPD, -1) #Rounds to the nearest 10 to give a "quidditch score"

  if RoundDiff > 30: #If Team1 is up out of range, they win by catch (No Catches for loss!)
    Team1.snitch += 1
  elif RoundDiff < -30: #If Team2 is up out of range, they win
    Team2.snitch += 1
  elif RoundDiff == 30: #If Team1 is up 30, Team2 must win two coinflips to win
    if random.random() >= 0.5:
      Team1.snitch +=1
    else:
      Team2.snitch +=1
      if random.random() >= 0.5:
        Team1.snitch +=1
      else:
        Team2.snitch +=1
  elif RoundDiff == -30: #If Team2 is up 30, Team1 must win two coinflips to win
    if random.random() >= 0.5:
      Team2.snitch +=1
    else:
      Team1.snitch +=1
      if random.random() >= 0.5:
        Team2.snitch +=1
      else:
        Team1.snitch +=1
  else: #If game is between -20 and 20, a coinflip decides winner (it's ugly but it's what we got)
    if random.random() >= 0.5:
      Team1.snitch +=1
    else:
      Team2.snitch +=1
  '''The next four statements adjust the RoundDiff value for snitch catches 
  and give a final score differential'''
  if Team1.snitch == 1:
    RoundDiff += 30
  elif Team1.snitch == 2:
    RoundDiff += 60
  if Team2.snitch == 1:
    RoundDiff -= 30
  elif Team2.snitch == 2:
    RoundDiff -= 60
  '''These next lines use the determined RoundDiff score to call the 
  scorigami function and give an output of the game result.
  There is one teeny tiny rare issue that will almost never happen where
  a team could theoretically pull for overtime then catch in overtime
  and yet somehow end up with a score less than 60, BUT that likelihood
  is so rare AND it doesn't affect the overall outcomes of the model at 
  all so I'm not going to worry about it.
  '''
  if RoundDiff == 0:
    print("Somehow you got a tie dude")
  elif RoundDiff > 0:
    Team1.score = scorigami(RoundDiff)
    Team2.score = Team1.score-abs(RoundDiff)
  else:
    Team2.score = scorigami(RoundDiff)
    Team1.score = Team2.score-abs(RoundDiff)
  if RoundDiff > 0: #If Team 1 wins
    if Team1.snitch == 2: #If Team 1 caught two snitches
      Team1.qpf += Team1.score - 60 #tiebreaker updates, etc. 
      Team1.qpa += Team2.score
      Team2.qpf += Team2.score
      Team2.qpa += Team1.score - 60 
      Team1.totalsnitch += 2
      print (roundnum, Team1.name, Team1.score, "*^ -", Team2.name, Team2.score)
    elif Team2.snitch == 1: #If Team 2 caught to force OT
      Team1.qpf += Team1.score - 30
      Team1.qpa += Team2.score - 30
      Team2.qpf += Team2.score - 30
      Team2.qpa += Team1.score - 30 
      Team1.totalsnitch += 0.5 #50% snitch catch given value of 0.5 for tiebreakers
      Team2.totalsnitch += 0.5
      print (roundnum, Team1.name, Team1.score, "^ -", Team2.name, Team2.score, "*")
    else: #Team 1 wins in regulation
      Team1.qpf += Team1.score - 30
      Team1.qpa += Team2.score
      Team2.qpf += Team2.score
      Team2.qpa += Team1.score - 30 
      Team1.totalsnitch += 1
      print (roundnum, Team1.name, Team1.score, "* -", Team2.name, Team2.score)
  else: #If Team 2 wins
    if Team2.snitch == 2: #If Team 2 caught two snitches
      Team2.qpf += Team2.score - 60
      Team2.qpa += Team1.score
      Team1.qpf += Team1.score
      Team1.qpa += Team2.score - 60 
      Team2.totalsnitch += 2
      print (roundnum, Team2.name, Team2.score, "*^ -", Team1.name, Team1.score)
    elif Team1.snitch == 1: #If Team 1 caught to force OT
      Team2.qpf += Team2.score - 30
      Team2.qpa += Team1.score - 30
      Team1.qpf += Team1.score - 30
      Team1.qpa += Team2.score - 30 
      Team1.totalsnitch += 0.5
      Team2.totalsnitch += 0.5
      print (roundnum, Team2.name, Team2.score, "^ -", Team1.name, Team1.score, "*")
    else: #Team 1 wins in regulation
      Team2.qpf += Team2.score - 30
      Team2.qpa += Team1.score
      Team1.qpf += Team1.score
      Team1.qpa += Team2.score - 30 
      Team2.totalsnitch += 1
      print (roundnum, Team2.name, Team2.score, "* -", Team1.name, Team1.score)
  
  '''This section is only to assign the record before snitch catch tiebreaker'''
  if RoundDiff > 30: 
    Team1.rbsc += 1
  elif RoundDiff == 30:
    Team1.rbsc += 0.5
    Team2.rbsc += 0.5
  elif RoundDiff > 0:
    Team2.rbsc += 1
  elif RoundDiff > -30:
    Team1.rbsc += 1
  elif RoundDiff == -30:
    Team1.rbsc += 0.5
    Team2.rbsc += 0.5
  else:
    Team2.rbsc += 1
  
  '''This section determines which round a team should get credit for winning'''
  if roundnum == 1:
    if RoundDiff > 0:
      Team1.winone = 1
    else:
      Team2.winone = 1
  elif roundnum == 2:
    if RoundDiff > 0:
      Team1.wintwo = 1
    else:
      Team2.wintwo = 1
  elif roundnum == 3:
    if RoundDiff > 0:
      Team1.winthree = 1
    else:
      Team2.winthree = 1


  Team1.snitch = 0 #resets snitch records so they don't carry into next game
  Team2.snitch = 0 #overall snitch record still stored in team.totalsnitch

def bgame(Team1, Team2, roundnum):
  Elodiff = Team1.elo - Team2.elo #Determines difference in team Elo ratings
  PredQPD = Elodiff*0.1844 #Determines predicted outcome based on Regression Model
  Zval = np.random.normal() #Sets a random Zscore for setting prediction interval
  ActualQPD = PredQPD+Zval*44.66542 #Uses randomly generated z score and the Residual Standard Error to randomly determine score differential
  RoundDiff = round(ActualQPD, -1) #Rounds to the nearest 10 to give a "quidditch score"

  if RoundDiff > 30: #If Team1 is up out of range, they win by catch (No Suicides!!!)
    Team1.snitch += 1
  elif RoundDiff < -30: #If Team2 is up out of range, they win
    Team2.snitch += 1
  elif RoundDiff == 30: #If Team1 is up 30, Team2 must win two coinflips to win
    if random.random() >= 0.5:
      Team1.snitch +=1
    else:
      Team2.snitch +=1
      if random.random() >= 0.5:
        Team1.snitch +=1
      else:
        Team2.snitch +=1
  elif RoundDiff == -30: #If Team2 is up 30, Team1 must win two coinflips to win
    if random.random() >= 0.5:
      Team2.snitch +=1
    else:
      Team1.snitch +=1
      if random.random() >= 0.5:
        Team2.snitch +=1
      else:
        Team1.snitch +=1
  else: #If game is between -20 and 20, a coinflip decides winner (it's ugly but it's what we got)
    if random.random() >= 0.5:
      Team1.snitch +=1
    else:
      Team2.snitch +=1
  '''The next four statements adjust the RoundDiff value for snitch catches 
  and give a final score differential'''
  if Team1.snitch == 1:
    RoundDiff += 30
  elif Team1.snitch == 2:
    RoundDiff += 60
  if Team2.snitch == 1:
    RoundDiff -= 30
  elif Team2.snitch == 2:
    RoundDiff -= 60
  '''These next lines use the determined RoundDiff score to call the 
  scorigami function and give an output of the game result.
  There is one teeny tiny rare issue that will almost never happen where
  a team could theoretically pull for overtime then catch in overtime
  and yet somehow end up with a score less than 60, BUT that likelihood
  is so rare AND it doesn't effect the overall outcomes of the model at 
  all so I'm not going to worry about it.
  '''
  if RoundDiff == 0:
    print("Somehow you got a tie dude")
  elif RoundDiff > 0:
    Team1.score = scorigami(RoundDiff)
    Team2.score = Team1.score-abs(RoundDiff)
  else:
    Team2.score = scorigami(RoundDiff)
    Team1.score = Team2.score-abs(RoundDiff)
  if RoundDiff > 0: #If Team 1 wins
    if Team1.snitch == 2: #If Team 1 caught two snitches
      print (roundnum, Team1.name, Team1.score, "*^ -", Team2.name, Team2.score)
    elif Team2.snitch == 1: #If Team 2 caught to force OT
      print (roundnum, Team1.name, Team1.score, "^ -", Team2.name, Team2.score, "*")
    else: #Team 1 wins in regulation
      print (roundnum, Team1.name, Team1.score, "* -", Team2.name, Team2.score)
  else: #If Team 2 wins
    if Team2.snitch == 2: #If Team 2 caught two snitches
      print (roundnum, Team2.name, Team2.score, "*^ -", Team1.name, Team1.score)
    elif Team1.snitch == 1: #If Team 1 caught to force OT
      print (roundnum, Team2.name, Team2.score, "^ -", Team1.name, Team1.score, "*")
    else: #Team 1 wins in regulation
      print (roundnum, Team2.name, Team2.score, "* -", Team1.name, Team1.score)
  
  Team1.snitch = 0 #resets snitch records so they don't carry into next game
  Team2.snitch = 0 #overall snitch record still stored in team.totalsnitch

  '''This section determines which team should get credit for winning'''
  if RoundDiff > 0:
    return Team1
  else:
    return Team2

def returnwins(team): #sets up a formula to be called when sorting teams by win order
  return team.winone + team.wintwo + team.winthree

def returng2(team): #sets up a formula to be called when sorting teams by win order in round 3
  return team.wintwo

'''Teams listed below'''
t1 = Team(("TXQ"), 2270)
t2 = Team(("CREIG"), 1798)
t3 = Team(("MID"), 1628)
t4 = Team(("JMU"), 1664)
t5 = Team(("ISU"), 1453)
t6 = Team(("RICH"), 1505)
t7 = Team(("MSU"), 1347)
t8 = Team(("CCC"), 1325)

t9 = Team(("HARV"), 1845)
t10 = Team(("MIZ"), 1861)
t11 = Team(("UF"), 1757)
t12 = Team(("BU"), 1565)
t13 = Team(("WVU"), 1491)
t14 = Team(("VT"), 1617)
t15 = Team(("UA"), 1090)
t16 = Team(("LSU"), 1572)

t17 = Team(("UMD"), 2059)
t18 = Team(("MUOH"), 1815)
t19 = Team(("TXST"), 1898)
t20 = Team(("RIT"), 1601)
t21 = Team(("PSU"), 1571)
t22 = Team(("UOFR"), 1613)
t23 = Team(("NCSU"), 1472)
t24 = Team(("BAY"), 1623)

t25 = Team(("MICH"), 1909)
t26 = Team(("UTSA"), 2083)
t27 = Team(("BGSU"), 1609)
t28 = Team(("BSU"), 1524)
t29 = Team(("DUKE"), 1527)
t30 = Team(("TAMU"), 1863)
t31 = Team(("MINN"), 1523)
t32 = Team(("UNC"), 1349)

t33 = Team(("NYU"), 1921)
t34 = Team(("RPI"), 1800)
t35 = Team(("UCI"), 1829)
t36 = Team(("CAL"), 1800)
t37 = Team(("PITT"), 1469)
t38 = Team(("RUTG"), 1501)
t39 = Team(("FSU"), 1512)
t40 = Team(("SIUE"), 1304)

t41 = Team(("TUF"), 1869)
t42 = Team(("UVA"), 1871)
t43 = Team(("KU"), 1719)
t44 = Team(("ILL"), 1547)
t45 = Team(("SHSU"), 1875)
t46 = Team(("UVT"), 1463)
t47 = Team(("OU"), 1526)
t48 = Team(("SCAR"), 1356)

flight1 = [t1, t2, t3, t4, t5, t6, t7, t8] #put teams in a list for iteration
flight2 = [t9, t10, t11, t12, t13, t14, t15, t16]
flight3 = [t17, t18, t19, t20, t21, t22, t23, t24]
flight4 = [t25, t26, t27, t28, t29, t30, t31, t32]
flight5 = [t33, t34, t35, t36, t37, t38, t39, t40]
flight6 = [t41, t42, t43, t44, t45, t46, t47, t48]

def roundone(flight): #creates a function to run round one
  game(flight[0], flight[7], 1)
  flight[0].roundone = flight[7].name
  flight[7].roundone = flight[0].name
  game(flight[1], flight[6], 1)
  flight[1].roundone = flight[6].name
  flight[6].roundone = flight[1].name
  game(flight[2], flight[5], 1)
  flight[2].roundone = flight[5].name
  flight[5].roundone = flight[2].name
  game(flight[3], flight[4], 1)
  flight[3].roundone = flight[4].name
  flight[4].roundone = flight[3].name

def roundtwo(flight): #creates a function to run round two
  random.shuffle(flight) #randomizes team order
  flight.sort(key=returnwins, reverse = True) #sorts teams by number of wins (so 1-0 teams are paired with 1-0 teams and vice versa)
  game(flight[0], flight[1],2)
  game(flight[2], flight[3],2)
  game(flight[4], flight[5],2)
  game(flight[6], flight[7],2)

def roundthree(flight): #creates a function to run round three
  random.shuffle(flight) #randomizes team order
  flight.sort(key=returnwins,reverse = True) #sorts teams by number of wins (so same record teams are paired again)
  game(flight[0], flight[1],3)
  flight[0].breaker += 1 #Credits team with having played in flight "final"
  flight[1].breaker += 1
  game(flight[6], flight[7],3)
  midlist = flight[2:6] #Creates a "list within a list" to ensure teams with 1-1 records are organized in the correct order
  random.shuffle(midlist) 
  midlist.sort(key=returng2,reverse = True)
  if midlist[0].roundone == midlist[3].name:
    game(midlist[0], midlist[2],3)
    game(midlist[1], midlist[3],3)
  elif midlist[0].roundone == midlist[2].name:
    game(midlist[0], midlist[3],3)
    game(midlist[1], midlist[2],3)
  elif midlist[1].roundone == midlist[2].name:
    game(midlist[0], midlist[2],3)
    game(midlist[1], midlist[3],3)
  elif midlist[1].roundone == midlist[3].name:
    game(midlist[0], midlist[3],3)
    game(midlist[1], midlist[2],3)
  else:
    game(midlist[0], midlist[2],3)
    game(midlist[1], midlist[3],3)

def results(flight, flightnum): #
  for team in flight:
    print(team.name, "Wins:", returnwins(team), "WBSC:", team.rbsc, 
    "QPA:", team.qpa, "QPF:", team.qpf, "Catch%:", team.totalsnitch,
    "FirstTiebreaker:",team.breaker)
    team.totalwin = team.winone + team.wintwo + team.winthree
    team.qpa = -team.qpa
    team.flight = flightnum

roundone(flight1)
roundtwo(flight1)
roundthree(flight1)
print("Flight 1 Results:")
results(flight1, 1)
roundone(flight2)
roundtwo(flight2)
roundthree(flight2)
print("Flight 2 Results:")
results(flight2, 2)
roundone(flight3)
roundtwo(flight3)
roundthree(flight3)
print("Flight 3 Results:")
results(flight3, 3)
roundone(flight4)
roundtwo(flight4)
roundthree(flight4)
print("Flight 4 Results:")
results(flight4, 4)
roundone(flight5)
roundtwo(flight5)
roundthree(flight5)
print("Flight 5 Results:")
results(flight5, 5)
roundone(flight6)
roundtwo(flight6)
roundthree(flight6)
print("Flight 6 Results:")
results(flight6, 6)

totallist = flight1+flight2+flight3+flight4+flight5+flight6

blist = sorted(totallist, key=attrgetter('totalwin','breaker','rbsc','qpa','qpf','totalsnitch'), reverse=True)

zerolist = (blist[42:])
onelist = (blist[24:42])

random.shuffle(zerolist)
game(zerolist[0],zerolist[1], "0-3 Consolation")
game(zerolist[2],zerolist[3], "0-3 Consolation")
game(zerolist[4],zerolist[5], "0-3 Consolation")

random.shuffle(onelist)
slist = sorted(onelist, key=attrgetter('flight'))
game(slist[0],slist[3], "1-2 Consolation")
game(slist[1],slist[6], "1-2 Consolation")
game(slist[2],slist[9], "1-2 Consolation")
game(slist[4],slist[12], "1-2 Consolation")
game(slist[5],slist[15], "1-2 Consolation")
game(slist[7],slist[10], "1-2 Consolation")
game(slist[8],slist[13], "1-2 Consolation")
game(slist[11],slist[16], "1-2 Consolation")
game(slist[14],slist[17], "1-2 Consolation")

print("Bracket Seeding\n1:", blist[0].name, "2:", blist[1].name,"3:", blist[2].name,"4:", blist[3].name,"5:", blist[4].name,"6:", blist[5].name,"\n7:", blist[6].name,"8:", blist[7].name,"9:", blist[8].name,"10:", blist[9].name,"11:", blist[10].name,"12:", blist[11].name,"\n13:", blist[12].name,"14:", blist[13].name,"15:", blist[14].name,"16:", blist[15].name,"17:", blist[16].name,"18:", blist[17].name,"\n19:", blist[18].name,"20:", blist[19].name,"21:", blist[20].name,"22:", blist[21].name,"23:", blist[22].name,"24:", blist[23].name)

bgame(bgame(bgame(bgame(blist[7],bgame(blist[8], blist[23], "Play-in"),"Rnd 16"),bgame(blist[0], bgame(blist[15], blist[16], "Play-in"), "Rnd 16"), "Quarter"),bgame(bgame(blist[4], bgame(blist[11], blist[20], "Play-in"), "Rnd 16"),bgame(blist[3], bgame(blist[12], blist[19], "Play-in"),"Rnd 16"), "Quarter"), "Semi"), bgame(bgame(bgame(blist[6], bgame(blist[9], blist[22], "Play-in"), "Rnd 16"),bgame(blist[1], bgame(blist[14], blist[17], "Play-in"),"Rnd 16"), "Quarter"),bgame(bgame(blist[5], bgame(blist[10], blist[21], "Play-in"), "Rnd 16"),bgame(blist[2], bgame(blist[13], blist[18], "Play-in"),"Rnd 16"), "Quarter"), "Semi"), "Final")