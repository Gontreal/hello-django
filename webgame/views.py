from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

#from django.urls import reverse
from django.core.urlresolvers import reverse
from .game import map

# Create your views here.
def index(request):
    
    request.session['name'] = map.start.name
    request.session['description'] = map.start.description
    request.session['count']=3
    #GameEngine(map.start)
    
    return HttpResponseRedirect(reverse('games:engine'))
    #return render(request,'webgame/show_room.html',context)
    #return GET(request,map.start.name)
 
  
def game_engine(request):
    room=map.look_up.get(request.session['name'],None)
    if request.method=='POST':
        if room.name=='keypad':
            room.count=request.session['count']
            request.session['count']-=1
           
        action=request.POST['your_move']
        #next_room=room
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
        #'name':request.session['name']
        'description':room.description,
        #'tries_left':request.session['count'] 
        }
        if room.name in ['death','You Won','You Lost']:
            context['end']=True
            request.session.flush()
        if room.name=='keypad':
            context['tries_left']=request.session['count'] 
            #context['tries_left'] = '%d' %room.count
        return render(request,'webgame/show_room.html',context)   
       
        
        
   
   