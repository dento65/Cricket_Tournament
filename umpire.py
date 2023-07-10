import random

class Umpire:
    def __init__(self):
        self.probabilities = {
            "run": 0.5,
            "wicket": 0.1,
            "dot_ball": 0.15,
            "four": 0.1,
            "six": 0.05,
            "no_ball":0.05,
            "wide_ball":0.05
        }
    def event(self):
        probabilities = self.probabilities.items()
        event = random.choices(
            population=[event for event, prob in probabilities],
            weights=[prob for event, prob in probabilities]
        )[0]
        return event
    def ball(self,batsman,bowler,team):
        outcome =  self.event()
        commentary = ""
        if outcome == "run":
            runs = random.randint(0, 3)
            team.total_score += runs
            batsman.runsmade += runs
            batsman.singles += runs
            bowler.runsgiven += runs
            commentary = f"{batsman.name} scores {runs} run(s)!"
        elif outcome == "wicket":
            team.wickets += 1
            bowler.wickets += 1
            commentary = f"Out!"
        elif outcome == "four":
            team.total_score += 4
            batsman.runsmade += 4
            batsman.fours += 4
            bowler.runsgiven += 4
            commentary = f"That's a cracking four by {batsman.name}!"
        elif outcome == "six":
            team.total_score += 6
            batsman.runsmade += 6
            batsman.sixes += 6
            bowler.runsgiven += 6
            commentary = f"It's gone all the way for a six by {batsman.name}!"
        elif outcome == "no_ball":
            team.total_score += 1
            bowler.noballs += 1
            bowler.runsgiven += 1
            commentary = f"No ball! {batsman.name} gets an extra run!"
        elif outcome == "wide_ball":
            team.total_score += 1
            bowler.wides += 1
            bowler.runsgiven += 1
            commentary = f"Wide ball! {batsman.name} gets an extra run!"
        else:
            commentary = f"A dot ball"
        return commentary
        