from django.shortcuts import render
from .MMS.Match import Match,readPlayerFile
from django.http import HttpResponseRedirect, HttpResponse
import os
script_dir=os.path.dirname(__file__)#abs dir the script in
player_path=os.path.join(script_dir,"MMS/players.txt")
male_path=os.path.join(script_dir,"MMS/male.txt")
female_path=os.path.join(script_dir,"MMS/female.txt")

playerList=readPlayerFile(player_path)
# match=Match(male_path,female_path)
# for p in playerList:
    # match.kick_start(p)


# Create your views here.
def intro(request):
    return render(request,'MMS/main-page.html')
def match_engine(request):
    pass
