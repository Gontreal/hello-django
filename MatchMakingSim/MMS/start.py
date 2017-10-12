from Match import Match, readPlayerFile
import os
script_dir = os.path.dirname(__file__)  # abs dir the script in
player_path = os.path.join(script_dir, "players.txt")
male_path = os.path.join(script_dir, "male.txt")
female_path = os.path.join(script_dir, "female.txt")


# This script runs sorf of as a functional test,
# for the first player, it should match F:28,
# for the last plater, it should match M:33,
# the test program in tests dir is for nose,
# and it's not working for some reason I failed to understand,
# if you want to see the full test, go to the original repo for this project
# in my github: Match Making Simulation


def main():
    playerList = readPlayerFile(player_path)
    match = Match(male_path, female_path)
    for p in playerList:
        match.kick_start(p)
    for line in match.resultLog:
        print(line)


if __name__ == '__main__':
    main()
