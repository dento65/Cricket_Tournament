import random
from player import Player
from teams import Team
from match import match


class tournament:
    def generate_matches(self, teams):
        # Generate random match pairs from the list of teams
        matches = []
        while len(teams) >= 2:
            team1 = random.choice(teams)
            teams.remove(team1)
            team2 = random.choice(teams)
            teams.remove(team2)
            matches.append((team1, team2))
        return matches

    def run_tournament(self):
        # Ask user for teams and overs
        team_names = input(
            "Enter the even no of team names separated by comma: ").split(",")
        overs = int(input("Enter the number of overs for the matches: "))
        Teams_list = []
        for team in team_names:
            Teams_list.append(self.Team_init(team))
        # Generate match pairs
        matches = self.generate_matches(Teams_list)

        # Run matches until a winner is decided
        winner = None
        while len(matches) > 0:
            print("---------- Matches ----------")
            print(matches)
            print("-----------------------------")

            # Play each match
            winners = []
            for singlematch in matches:
                team1, team2 = singlematch
                team1 = self.Team_init(team1.name)
                team2 = self.Team_init(team2.name)
                print("Playing match: {} vs {}".format(team1.name, team2.name))
                winner = match.start_match(team1, team2, overs)
                winners.append(winner)
                print("{} won the match!\n".format(winner.name))

            # Generate new match pairs with the winners
            matches = self.generate_matches(winners)

        # Print the final winner
        print("---------- TOURNAMENT Winner ----------")
        print(winner.name)
        print("-----------------------------")

    def Team_init(self, Team_name):
        TeamA = Team(Team_name)
        for i in range(0, 5):
            TeamA.addplayer_wrt_battingorder(Player(TeamA.name+":"+"Player"+str(i+1), round(random.random(), 1), round(
                random.random(), 1), round(random.random(), 1), round(random.random(), 1), round(random.random(), 1)), 0)
        for i in range(5, 9):
            TeamA.addplayer_wrt_battingorder(Player(TeamA.name+":"+"Player"+str(i+1), round(random.random(), 1), round(
                random.random(), 1), round(random.random(), 1), round(random.random(), 1), round(random.random(), 1)), 1)
        return TeamA


t = tournament()
t.run_tournament()
