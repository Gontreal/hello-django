from Match import Match,readPlayerFile

playerList=readPlayerFile("players.txt")
match=Match("male.txt","female.txt")
for p in playerList:
    match.kick_start(p)



