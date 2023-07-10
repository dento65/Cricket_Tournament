from player import Player
import random
class Team:
    def __init__(self, name):
        self.name = name 
        self.players = []
        self.captain = None 
        self.batting_order = []
        self.bowlers = []
        self.total_score = 0
        self.wickets = 0
    def addplayer_wrt_battingorder(self,Player,bowler_bool):
        if len(self.players) <= 11:
            self.players.append(Player)
            self.batting_order.append(Player)
        if bowler_bool:
            self.bowlers.append(Player)
        if len(self.players) > 11:
            print(f"you have exceeded 11 players for team {self.name}")

    def sending_next_player(self):
        if len(self.batting_order)>0:
            return self.batting_order.pop(0)
        return None 
    
    def choose_bowler(self):
        return random.choice(self.bowlers)
    def select_captain(self, captain):
        self.captain = captain
    def print_scorecard_all(self):
        print("\n\n Scorecard: of Team "+self.name)
        print("Player\t\tRuns Made\tSingles\t\tFours\t\tSixes\t\tRuns Given\tWickets\t\tNo Balls\tWides")
        for player in self.players:
            player.print_scorecard()
        print("\n\n")
