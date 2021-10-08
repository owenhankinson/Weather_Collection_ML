# Volleyball_Lineup
To address an issue of prominent loss of my intramural volleyball team, I took performance data from all (8) players on the team to find the most optimal rotation of individuals that would yield the highest win probability.

The league works as a game of four versus four. Each team has a minimum of four players and a max of 8. When a team wins a point and recieves the ball back to serve a rotation commences changing the entire team of 4.

Our team having eight players there were {8!} (40,320) different combinations of orders that us players could be in. So crunching through all of them, then running averages on each rotation of 4 players in that given order. An overall team value was given to that team and stored in a dictionary with the team order as the key, and the overall team value as the value. After doing this 40,320 times, I go back to the dictionary of orders and values and take the max value of the data and that is the team that has the highest precentage of victory based on the stats.


## Reflection
This was super fun to work on and to spontaneously take on. I felt alot of joy getting to see my knowledge of python come into use randomly. All of this took the span of about a day, I will most definatley come back to veiw and improve this algorithm.
