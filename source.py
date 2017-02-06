import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

### create deck of cards
data_dict = dict([("A", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6),
                 ("7", 7), ("8", 8), ("9", 9), ("10", 10), ("J", 10), ("Q", 10), ("K", 10)])

deck_of_cards = pd.DataFrame(data_dict, index=["spades", "hearts", "diamonds", "clubs"])

deck_of_cards

### histogram of deck of cards
deck_of_cards_stack = deck_of_cards.stack()
fig1, ax1 = plt.subplots()
deck_of_cards_stack.plot(kind="hist", ax=ax1)
ax1.set_xlabel("card_value")
ax1.set_title("Histogram")
plt.show()
fig1.savefig("histogram.png")
deck_of_cards_stack.describe()


### helper functions ###################################################
## helper function 1: draw m cards from deck of cards, compute sum.
## Repeat the process n times, and put the result into numpy array.
## with replace parameter as a boolean, could draw cards with replacement
## or without replacement
def dist_of_sample_sum(n, m=3, replace=False):
    dist = np.empty((n,), dtype=int)
    for i in range(n):
        dist[i] = deck_of_cards_stack.sample(m, replace=replace).sum()
    return dist

## helper function 2: discribe data and draw histogram
def discribe_data(data, figname):
    print stats.describe(data, bias=False, ddof=1)
    print "25%, 50%, 75% percentile", np.percentile(data, [25,50,75])
    fig, ax = plt.subplots()
    ax.set_xlabel("Sum Value")
    ax.set_ylabel("frequency")
    ax.set_title("Sum Value Histogram")
    ax.hist(data)
    plt.show()
    fig.savefig("{}.png".format(figname))
#############################################################################

## draw three cards from deck of cards without replacement, compute sum and plot distribution
exp1 = dist_of_sample_sum(1000)
discribe_data(exp1, "exp1")
