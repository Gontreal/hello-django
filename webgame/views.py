from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

#from django.urls import reverse
from django.core.urlresolvers import reverse
from .game import map

# Create your views here.
def index(request):
    
    request.session['name'] = map.start.name
    request.session['description'] = map.start.description
    request.session['count']=9
    return HttpResponseRedirect(reverse('games:engine'))
    
def game_engine(request):
    room=map.look_up.get(request.session['name'],None)
    if request.method=='POST':
        if room.name=='keypad':
            room.count=request.session['count']
            request.session['count']-=1
           
        action=request.POST['your_move']
        if action:
            if room.check_path(action):
                room=room.go(action)
            else:
                room =room.go('*')
        if room:
            request.session['name'] = room.name
            request.session['description'] = room.description
            return HttpResponseRedirect(reverse('games:engine'))
        else:
            request.session.flush()
            return render(request,'webgame/you_died.html')
    else:
        context={
        'name': room.name,
        'description':room.description
        }
        if room.name in ['death','You Won','You Lost']:
            context['end']=True
            request.session.flush()
        if room.name=='keypad':
            context['tries_left']=request.session['count'] 
           
        return render(request,'webgame/show_room.html',context)   
       
        
        
   
   