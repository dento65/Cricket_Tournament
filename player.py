class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name 
        self.bowling = bowling 
        self.batting = batting 
        self.fielding = fielding 
        self.running = running 
        self.experience = experience
        self.runsmade = 0
        self.singles = 0
        self.fours = 0
        self.sixes = 0
        self.runsgiven = 0
        self.wickets = 0
        self.noballs = 0
        self.wides = 0

    def update_runs_scored(self, runs):
        self.runs_scored += runs

    def update_wickets_taken(self, wickets):
        self.wickets_taken += wickets
    def print_scorecard(self):
        print("--------------------------------------------------------------------------------------------------")
        print(f"{self.name}\t\t{self.runsmade}\t\t{self.singles}\t\t{self.fours}\t\t{self.sixes}\t\t{self.runsgiven}\t\t{self.wickets}\t\t{self.noballs}\t\t{self.wides}")