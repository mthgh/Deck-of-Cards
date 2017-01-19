## Instructions
This is the final project for [Intro to Descriptive Statistics](https://docs.google.com/document/d/1059JMJ9C5dn7vKUrmfWYle57Ai3Uk9PzxPQBGj5drjE/pub?embedded=true). This experiment will require the use of a standard deck of playing cards. This is a deck of fifty-two cards divided into four suits (spades (♠), hearts (♥), diamonds (♦), and clubs (♣)), each suit containing thirteen cards (Ace, numbers 2-10, and face cards Jack, Queen, and King). You can use either a physical deck of cards for this experiment or you may use a virtual deck of cards such as that found on random.org (http://www.random.org/playing-cards/). For the purposes of this task, assign each card a value: The Ace takes a value of 1, numbered cards take the value printed on the card, and the Jack, Queen, and King each take a value of 10.

## 1. Create Deck of Cards
<pre>data_dict = dict([("A", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), ("6", 6),
                 ("7", 7), ("8", 8), ("9", 9), ("10", 10), ("J", 10), ("Q", 10), ("K", 10)])

deck_of_cards = pd.DataFrame(data_dict, index=["spades", "hearts", "diamonds", "clubs"])
deck_of_cards</pre>
![data frame](https://github.com/mthgh/Deck-of-Cards/blob/master/figure_3.png)
