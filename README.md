# Player_Ranking_In_Sports

## Install python libraries:
- run make command `make install`

## Run program:
- run make command `make run`

# Technical Report

## Methodology:
- For this project I wanted to extract the data from 2022 MLB player stats from a .csv file. With this data I First cleaned the data and with this cleaned data I would then score the players based on features in the data set. After ranking the players I than analyze the data by creating a heat map to show what makes a player rank higher than others based on feature values.

## Data Collection:
- For data collection I first extracted the data from a .csv file using pandas. After this I proceed to clean the data. I filter only the features I will use for ranking players and removed data point with duplicate or missing features from the data set.

## Ranking System Development:
- For ranking players I would assign a weight to each feature(EX: home runs, batting average, etc.). With these weights I would then calculate a score for each player with these weights.
-  code for ranking players:
![image](https://github.com/themnsavage/Player_Ranking_In_Sports/assets/60998598/91c175cb-663a-4a89-9d07-0b4520afadf6)

## Data Analysis and Visualization:
- For analyzing I created a heat map using the python libraries matplotlib and seaborn. I decided to use a heat map, due to being able to visual the features I used to rank the players. This help me understand why certain players are rank higher than others.
- Heat map:
![image](https://github.com/themnsavage/Player_Ranking_In_Sports/assets/60998598/85304c71-7159-4c36-aa5f-a350e6150719)

## Results & Discussion:
-  From this project I was able to see that based on my ranking model. That the feature that makes a player a top ranking player is the home run score. This is shown by the heat map that the top players have very similar rankings for all the other features except for their home run scores.

## Limitations and Potential Improvements:
-  The features to score players are features that are only batting stats. So a potential improvement would be adding features that include stats about how the player play on defense. This would help find overall best player, not just best player at batting.

## Conclusion:
- In this project, I used data from 2022 MLB player stats to rank players. I cleaned the data and then scored players based on things like home runs and batting average. I used a heat map to show which features make a player rank higher. The results showed that home runs are the most important for a high ranking. However, the system only looked at batting and ignored defense. In the future, adding defense stats could make the rankings better by considering a player's overall skills, not just batting.

