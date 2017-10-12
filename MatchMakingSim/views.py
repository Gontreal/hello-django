from django.shortcuts import render
from django.http import JsonResponse
from .MMS.Match import Match, readPlayerFile
# from django.http import HttpResponseRedirect, HttpResponse
import os
script_dir = os.path.dirname(__file__)  # abs dir the script in
player_path = os.path.join(script_dir, "MMS/players.txt")
male_path = os.path.join(script_dir, "MMS/male.txt")
female_path = os.path.join(script_dir, "MMS/female.txt")

# playerList = readPlayerFile(player_path)
# match=Match(male_path,female_path)
# for p in playerList:
    # match.kick_start(p)


# Create your views here.
def intro(request):
    return render(request, 'MMS/main-page.html')


def match_engine(request):
    ret = {
        "Error": False,
        "ErrMsg": '',
        "result": []
    }

    if request.method == 'POST':
        if not request.POST:
            ret['Error'] = True
            ret['ErrMsg'] = "Empty Input."
            return JsonResponse(ret)
        gen = 1 if request.POST['gender'] == "Man" else 0

        appearence = request.POST['appearence']
        personality = request.POST['personality']
        wealth = request.POST['wealth']
        exAppear = request.POST['exAppear']
        exPerson = request.POST['exPerson']
        exWealth = request.POST['exWealth']

        if(int(exAppear)+int(exPerson)+int(exWealth) == 100):
            playerTuple = (gen, int(appearence), int(personality), int(wealth),
                           int(exAppear), int(exPerson), int(exWealth))
            match = Match(male_path, female_path)
            match.kick_start(playerTuple)
            if(len(match.resultLog) == 0):
                ret["Error"] = True
                ret["ErrMsg"] = "Empty log"
                return JsonResponse(ret)
            ret["result"] = match.resultLog
            return JsonResponse(ret)
        else:
            ret["Error"] = True
            ret["ErrMsg"] = "Invalid Input."
            return JsonResponse(ret)
