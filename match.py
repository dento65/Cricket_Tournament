import random
from commentator import commentator
from umpire import Umpire
class match:
    def __init__(self) -> None:
        self.winner = ''
    def start_match(Team1,Team2,Overs):
        toss_win = random.choice([Team1, Team2]) 
        # team 1 is that batting team so swapping if req
        if(toss_win==Team2): 
            tempvar = Team1
            Team1 = Team2
            Team2 = tempvar
        print("Team "+toss_win.name+" won the toss and decided to bat first\n")
        print("\t\t\t The match for "+str(Overs)+" overs has started b/w "+Team1.name+" and "+Team2.name+"\n")
        #team1 batting
        bowler = Team2.choose_bowler()
        batsman1 = Team1.sending_next_player()
        batsman2 = Team1.sending_next_player()
        match_over = 0
        umpire1 = Umpire()
        for over in range(1,Overs+1):
            tempvar = batsman1
            batsman1 = batsman2
            batsman2 = tempvar
            if(batsman1 == None or batsman2==None):
                print("MATCH OVER!")
                break
            bowler = Team2.choose_bowler()
            for ball in range(1,7):
                ball_outcome = umpire1.ball(batsman1,bowler,Team1)
                commentator(over,ball,ball_outcome)
                if(ball_outcome=="Out!"):
                    if(len(Team1.batting_order) == 0):
                        match_over = 1
                        print("MATCH OVER!")
                        break
                    batsman1 = Team1.sending_next_player()
            if match_over:
                break
        print("\n \t\t Team "+Team1.name+" has set a total score of "+str(Team1.total_score)+"\n\n")

        # team 2 batting
        bowler = Team1.choose_bowler()
        batsman1 = Team2.sending_next_player()
        batsman2 = Team2.sending_next_player()
        match_over = 0
        umpire1 = Umpire()
        for over in range(1,Overs+1):
            tempvar = batsman1
            batsman1 = batsman2
            batsman2 = tempvar
            bowler = Team1.choose_bowler()
            for ball in range(0,7):
                if(Team2.total_score > Team1.total_score): # team2 has chased the score
                    match_over = 1
                    break
                ball_outcome = umpire1.ball(batsman1,bowler,Team2)
                commentator(over,ball,ball_outcome)
                if(ball_outcome=="Out!"):
                    if(len(Team2.batting_order) == 0):
                        match_over = 1
                        print("MATCH OVER!")
                        break
                    batsman1 = Team2.sending_next_player()
            if match_over:
                break
        Team1.print_scorecard_all()
        Team2.print_scorecard_all()
        print("\n \t\t Team "+Team2.name+" has made a total score of "+str(Team2.total_score)+"\n")
        if(Team2.total_score > Team1.total_score):
            print("\t\t Team "+Team2.name+" has chased the score made and won!!! the match")
            return Team2
        else:
            print("\t\t Team "+Team1.name+" has won!!! the match")
            return Team1
        