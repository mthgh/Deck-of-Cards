## Instructions
This is the final project for [Intro to Descriptive Statistics](https://docs.google.com/document/d/1059JMJ9C5dn7vKUrmfWYle57Ai3Uk9PzxPQBGj5drjE/pub?embedded=true). This experiment will require the use of a standard deck of playing cards. This is a deck of fifty-two cards divided into four suits (spades (♠), hearts (♥), diamonds (♦), and clubs (♣)), each suit containing thirteen cards (Ace, numbers 2-10, and face cards Jack, Queen, and King). You can use either a physical deck of cards for this experiment or you may use a virtual deck of cards such as that found on random.org (http://www.random.org/playing-cards/). For the purposes of this task, assign each card a value: The Ace takes a value of 1, numbered cards take the value printed on the card, and the Jack, Queen, and King each take a value of 10.

## 1. Create Deck of Cards
![data frame](https://github.com/mthgh/Deck-of-Cards/blob/master/Capture.PNG)

## 2. Deck of Cards Value Distribution
![Deck of Cards Value Distribution](https://github.com/mthgh/Deck-of-Cards/blob/master/histogram.png)    
Description:  
count    52.000000    
mean      6.538462    
std       3.183669    
min       1.000000    
25%       4.000000    
50%       7.000000    
75%      10.000000    
max      10.000000    

## 3. Random Select Three Card(without replacement), Compute Sum, and Sum Distribution
Now, we will get samples for a new distribution. To obtain a single sample, shuffle your deck of cards and draw three cards from it. (You will be sampling from the deck without replacement.) Record the cards that you have drawn and the sum of the three cards’ values. Repeat this sampling procedure a total of at least thirty times.Let’s take a look at the distribution of the card sums. Report descriptive statistics for the samples you have drawn. Include at least two measures of central tendency and two measures of variability.
![Deck of Cards Value Distribution](https://github.com/mthgh/Deck-of-Cards/blob/master/exp1.png)
DescribeResult(nobs=1000L, minmax=(4, 30), mean=19.597000000000001, variance=28.042633633633635, skewness=-0.21009642649536145, kurtosis=-0.39057915448229785)
25%, 50%, 75% percentile [ 16.  20.  23.]

The central limit theorem states that if you have a population with mean μ and standard deviation σ and take sufficiently large random samples from the population with replacementtext annotation indicator, then the distribution of the sample means will be approximately normally distributed. This will hold true regardless of whether the source population is normal or skewed, provided the sample size is sufficiently large (usually n > 30). The resulting sum distribution is normal distribution, becuase the sample sum was taken for more than 30 times and with replacement.

## 4. Estimates
Make some estimates about values you will get on future draws. Within what range will you expect approximately 90% of your draw values to fall? What is the approximate probability that you will get a draw value of at least 20? Make sure you justify how you obtained your values.

From central limit theorem, for three card sum, 
sample_sum_mean = orgin_mean X 3=19.62  
sample_sum_std = orgin_std/sqrt(3) X 3=5.51  
z_critical(0.05) = -1.645  
margin of error = 5.51*1.645= 9.06  
90% CI = (19.62-9.06, 19.62+9.06) = (10.56, 28.68)  
for a value of 20:
z = (20-19.60)/5.51 = 0.072
p = 0.47
