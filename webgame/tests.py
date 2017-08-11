from django.test import TestCase
from .views import index,game_engine
# Create your tests here.
from django.core.urlresolvers import reverse

class GameSetUpTests(TestCase):
    def test_index(self):
        c=self.client
        url=reverse('games:welcome')
        response=c.get(url,follow=True)
        session=c.session
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Central Corridor")
        self.assertEqual(session['name'],"Central Corridor")
        self.assertEqual(session['count'],9)
    def test_empty_form(self):
        c=self.client
        url=reverse('games:welcome')
        c.get(url)
        response=c.post(reverse('games:engine'),{'your_move':""},follow=True)
        #test redirectchain
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(response.status_code,200)
        self.assertEqual(c.session.get('name'),"Central Corridor")
        self.assertContains(response,"Central Corridor")
    def test_youdied(self):
        c=self.client
        url=reverse('games:welcome')
        c.get(url)
        response=c.post(reverse('games:engine'),{'your_move':'0132'})
        self.assertEqual(response.status_code,200)
        self.assertEqual(c.session.get('name'),None)
        self.assertContains(response,"You Died!")

class GameFlowTests(TestCase):
    def test_win_path(self):
        c=self.client
        url=reverse('games:welcome')
        c.get(url)
        response=c.post(reverse('games:engine'),{'your_move':'tell a joke'},follow=True)
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(c.session.get('name'),'Laser Weapon Armory')
        self.assertContains(response,"Laser")
        
        response=c.post(reverse('games:engine'),{'your_move':'0132'},follow=True)
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(c.session.get('name'),'The Bridge')
        self.assertContains(response,"Bridge")
        
        response=c.post(reverse('games:engine'),{'your_move':'slowly place the bomb'},follow=True)
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(c.session.get('name'),'Escape Pod')
        self.assertContains(response,"Escape")
        
        response=c.post(reverse('games:engine'),{'your_move':'2'},follow=True)
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(c.session.get('name'),None)
        self.assertContains(response,"Play Again")
        self.assertContains(response,"You Won")
    
    def test_lose_path(self):
        c=self.client
        url=reverse('games:welcome')
        c.get(url)
        response=c.post(reverse('games:engine'),{'your_move':'tell a joke'},follow=True)
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(c.session.get('name'),'Laser Weapon Armory')
        self.assertContains(response,"Laser")
        
        response=c.post(reverse('games:engine'),{'your_move':'0132'},follow=True)
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(c.session.get('name'),'The Bridge')
        self.assertContains(response,"Bridge")
        
        response=c.post(reverse('games:engine'),{'your_move':'slowly place the bomb'},follow=True)
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(c.session.get('name'),'Escape Pod')
        self.assertContains(response,"Escape")
        
        response=c.post(reverse('games:engine'),{'your_move':'5'},follow=True)
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(c.session.get('name'),None)
        self.assertContains(response,"Play Again")
        self.assertContains(response,"You Lost")
        
    def test_keypad_fail(self):
        c=self.client
        url=reverse('games:welcome')
        c.get(url)
        response=c.post(reverse('games:engine'),{'your_move':'tell a joke'},follow=True)
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(c.session.get('name'),'Laser Weapon Armory')
        self.assertContains(response,"Laser")
        
        for i in range(9):
            response=c.post(reverse('games:engine'),{'your_move':'0123'},follow=True)
            self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
            self.assertEqual(c.session.get('name'),'keypad')
            self.assertContains(response,9-i)
       
        response=c.post(reverse('games:engine'),{'your_move':'0123'},follow=True)
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(c.session.get('name'),None)
        self.assertContains(response,'Play Again')
        self.assertContains(response,'death')
        
    def test_keypad_success(self):
        c=self.client
        url=reverse('games:welcome')
        c.get(url)
        response=c.post(reverse('games:engine'),{'your_move':'tell a joke'},follow=True)
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(c.session.get('name'),'Laser Weapon Armory')
        self.assertContains(response,"Laser")
        
        for i in range(9):
            response=c.post(reverse('games:engine'),{'your_move':'0123'},follow=True)
            self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
            self.assertEqual(c.session.get('name'),'keypad')
            self.assertContains(response,9-i)
       
        response=c.post(reverse('games:engine'),{'your_move':'0132'},follow=True)
        self.assertEqual(response.redirect_chain,[(reverse('games:engine'),302)])
        self.assertEqual(c.session.get('name'),'The Bridge')
        self.assertContains(response,'The Bridge')
        
        response=c.post(reverse('games:engine'),{'your_move':'0132'},follow=True)
        self.assertEqual(c.session.get('name'),None)
        self.assertContains(response,'Play Again')
        self.assertContains(response,'You Died!')   