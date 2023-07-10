from player import Player
from teams import Team
from umpire import Umpire
import random
from match import match
A = Team("A")
B = Team("B")
player1 = []
print('rqwerq')
for i in range(0,5):
  
   A.addplayer_wrt_battingorder(Player("Player1_"+str(i+1), round(random.random(),1), round(random.random(),1),round(random.random(),1), round(random.random(),1), round(random.random(),1)),0)
for i in range(5,9):
    A.addplayer_wrt_battingorder(Player("Player1_"+str(i+1), round(random.random(),1), round(random.random(),1),round(random.random(),1), round(random.random(),1), round(random.random(),1)),1)
player2 = []
for i in range(0,5):
   B.addplayer_wrt_battingorder(Player("Player1_"+str(i+1), round(random.random(),1), round(random.random(),1),round(random.random(),1), round(random.random(),1), round(random.random(),1)),0)
for i in range(5,9):
    B.addplayer_wrt_battingorder(Player("Player1_"+str(i+1), round(random.random(),1), round(random.random(),1),round(random.random(),1), round(random.random(),1), round(random.random(),1)),1)
print(1)
p = B.sending_next_player()
print(B.sending_next_player())
U = Umpire()
b = A.choose_bowler()
print(U.ball(p,b,A))
print(p.runsmade)

a = match()
a.start_match(A,B,3)