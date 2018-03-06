import GameModelClasses as Model


#Time steps isn't relevant here. That's like number of games.

ODDS_HEADS = 0.5
NUM_GAMES=1000
ALPHA = 0.05            # significance level


myCohort = Model.AllGames(odds_heads=ODDS_HEADS, num_games=NUM_GAMES)
cohortOutcome = myCohort.simulate()

#PROBLEM ONE
print('95% CI of Winnings', cohortOutcome.get_CI_winnings(ALPHA))
print('95% CI of Loss Probability', cohortOutcome.get_CI_loss(ALPHA))

#My confidence interval for the amount of winnings is
#My confidence interval for the probability of losing money is

#PROBLEM 2:
#If we ran this simulation 10,000 times, 9,500 of those times, the mean should fall within the
#range indicated by the confidence interval.

#PROBLEM 3:
#
