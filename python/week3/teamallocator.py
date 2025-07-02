# This program will allocate teams randomly from a list
# 1. Import the random module
# 2. Create a list of every Genius
# 3. Use the random module to randomly shuffle the list
# 4. Loop through the list and display each team's player
# 5. Using an if statement to see if the user is happy with the
# if not, it will shuffle again. if so, the program terminates

import random 

players = ["Max", "Braylen",
         "Ollie", "Xavier", "Avery",
         "Carl", "Walter", "Darren",
         "EJ", "Nahum", "Joaquin",
         "Marshawn", "Ja'Den", "Isaiah"
         "Kenlon", "Nishad", "Kauri",
         "Kriss",
         "Joseph", "Semaj", "Tay", "taqari", "jarmauri"]


def Pickteams(players):    # Create our function
    random.shuffle(players)    # Shuffle the list of players
    team1 = players[:len(players) // 2] 
    teamcaptain1 = team1[random.randrange(0,12)]

    print("TEAM 1:")
    print("Team captain: " + teamcaptain1)
    for player in team1:
        print(player)


    team1 = players[:len(players) // 2] 
    teamcaptain1 = team1[random.randrange(0,12)]
    team2 = players[len(players) // 2:] 
    teamcaptain2 = team2[random.randrange(0,12)]
   
    print("TEAM 2:")
    print("Team captain: " + teamcaptain2)
    for player in team2:
        print(player)
Pickteams(players)