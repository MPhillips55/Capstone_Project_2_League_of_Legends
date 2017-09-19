# Capstone Project 2 Proposal - League of Legends Professional Games Dataset
# Michael Phillips

## What is League of Legends?

Leage of Legends (LoL) is an online, 5 vs. 5 competitive PC game. It happens to be one of, if not the most, popular games on any platform. In September, 2016 the worldwide player count was estimated to be over 100 million by the game's developer - Riot Games. Despite that, LoL has surprisingly had very little mainstream coverage which is most likely due to the general complexity of the game. It's hard to learn the basics of the game, let alone actually be good at it.

If you have never heard of LoL, it might be helpful to imagine pick-up basketball games down at the park or gym. 5 vs. 5 competitive matches. Different tactics required for different players on each team. The same rules (more or less) no matter where or when you play. Not that difficult to understand the goals and how to win, but mastery takes a very long time.

Another layer on top of the base game is that LoL has a professional league. The top prize for the best team is over \$5 million dollars. The average player makes a six-figure income, with one player rumored to make $3 million dollars per year. Peak concurrent viewership for the league finals in 2016 was 14.7 million people, a number that compares favorably with recent MLB World Series TV ratings.

So, now that you have some idea of what LoL is, why is it exciting to have a dataset pulled from competitive matches?

Much the same way that data informs other professional sports throughout the world, data can show trends and best-practices in LoL as well.

## 1. What is the problem you want to solve?

League of Legends is very complex. Just a cursory tour of this dataset shows a wealth of variables covering many aspects of the game.

While advanced statistics exist for traditional professional sports that quantify how and why teams win, there are no equivalent metrics for LoL. I want to find those signals in the data.

## 2. Who is your client and why do they care about this problem?

I envision my client being a team owner or coach. I'll reduce the drive to win in professional sports to one thing - money.

Riot has begun the process of franchising the professional LoL league sometime within the next six months to a year. This will function similarly to franchising in other professional sports. The teams that secure a franchise spot will be cut into the viewership revenue (the pot is roughly \$400 million dollars guaranteed over the next several years), as well as sponsorship, advertising, and merchandising deals that will bring in unquantifiable additional revenue.

The LoL league is highly attractive for branding reasons as well. Professional NBA, MLB, and soccer teams have begun buying LoL teams over the past 18 months. LoL is a global game with reach into the far corners of the globe. Being able to spread a brand worldwide to a complementary set of fans/viewers could be invaluable.

## 3. What data are you going to use?

The League of Legends competitive dataset was acquired from a public Kaggle repo, provided by user Chuck Ephron. It has complete data for 2015 up through the recent 'Mid-Season Invitational' tournament.

## 4. Outline your approach for solving this problem?

I plan to get a better sense of what the data holds using EDA methods.

I think some data wrangling will be necessary to get the data into the form I would like, which is one row per team/game. I also want to split up the 'gold values' which are currently in list form into their own columns.

Lastly, I will use machine learning to go through the wrangled data and find the signals that most strongly correlate with winning.

## 5. What are your deliverables?

I will submit an EDA of the data, with my own analysis. The most important features as detailed by the machine learning techniques I use, and (ideally) a baseline set of statistics that correlate to winning, perhaps broken down by year as LoL does evolve significantly over time.

Lastly, I will present my findings in a Tableau slidedeck.

## Dataset Link:

https://www.kaggle.com/chuckephron/leagueoflegends
