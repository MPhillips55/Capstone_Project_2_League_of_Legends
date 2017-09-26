## Capstone Project 2 - League of Legends Professional Games Dataset
## Michael Phillips

### 1. Define the problem
League of Legends is an online multiplayer computer game, with a rapidly evolving professional scene. In the past, similar games have come and gone. Due to its immense popularity and ongoing development LoL shows no signs of slowing down. I believe that in the near future the need for more in-depth data analysis will be necessary to compete at the highest level. 

Why is this important? Why does winning matter? I'll boil it down to the most basic of reasons, but still a requirement for the ongoing success of the league - money. Winning tournaments, and even just securing a spot in the new professional league will come with significant monetary rewards - easily in the millions of dollars over the next several years. 

LoL is an extremely complex game with many factors that contribute to winning a game. This project is meant to examine the data as it currently exists through Riot's API. Additionally, feature generation and machine learning will be used to find useful metrics that are not present in the raw data.

### 2. Identify your client
The potential client for this information could be one of two entities. 

- Riot Games, developer of LoL and steward of the professional league which has spread to countries across the world. The data and analysis found within this project could be used to tune and/or balance the game in an ongoing fashion.
- Professional teams would likely be very interested in seeing what this analysis uncovers. The difference between winning and losing is often a narrow margin, any possibility to improve a team's chances should be considered.

### 3. Describe the data
The data for this project came from the Riot Games API. It contains fairly thorough data for each professional game played since mid-2014. Some of the variables available for analysis include gold totals by minute for teams and players, ban information, player names, and objective counts/times for each game.

Cleaning the data was a more involved process than I had initially guessed it would be. I would say each of the csv files was around 90% clean. That remaining 10% however was tricky to properly clean. The major issues I discovered was player names listed in the wrong column and some issues with Game ID's being duplicated throughout the data. The data cleaning notebooks in the EDA folder of this repository show the full data cleaning steps and final data formats.

### 4. List other potential datasets
The data I have is good. There is a lot of information there. 

However, the one area that is not covered that I would very much like to have is creep scores for players and teams during each game. 'Creep score', also known as 'farm', is a measure of how effective a player is at resource gathering. I'm not sure why this data was not present. I will explore whether or not it is feasible to pull this additional data from Riot's API as it would improve the overall quality of the project.

### 5. Explain your initial findings
My initial findings are available in the EDA notebook found in this repository. To summarize, there are three apparent keys to winning a LoL game: kills, objectives, and gold totals (creep score/farming). Gold allows a player to purchase items which increase their power in-game. More gold means you can buy better items. 

One aspect of this idea that I hope to explore further is how the timings for things like kills and objectives affects the expected win percentage. Should a team focus on securing objectives/farm or on denying their opponents those gold sources?

### 6. Next steps
The machine learning portion of this project will go into more depth on the data. As previously mentioned, LoL is a very complex game with dramatically different win conditions depending on which teams are playing and the strategies they employ. For example it is possible to win a game with 5 kills in 65 minutes, or in 19 minutes with 20 kills. Both are valid wins, one is not any better than the other. Sorting this out with the data is not an easy task or something a person could intuitively do. Machine learning will be employed to examine the data for each game and determine win percentages at different time periods through the game. 

