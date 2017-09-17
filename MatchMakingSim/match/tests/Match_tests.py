from MMS import Match
from nose.tools import *
from libs import charactors
from sometools import readPlayerFile

def test_initialize():
    match=Match.Match("male.txt","female.txt")
    #match.initialize("male1.txt","female1.txt")
    assert_equal(match.queen.id(),101)
    for k,v in match.men_pool.items():
        assert_equal(v.q_size(),100)
    assert_equal(len(match.men_pool),100)
    assert_equal(len(match.women_pool),100)
    for m in match.men_pool.keys():
        assert_equal(m,match.men_pool[m].id())
    for w in match.women_pool.keys():
        assert_equal(w,match.women_pool[w].id())

def test_player():
    match=Match.Match("male.txt","female.txt")
    match.add_player((1,24,45,34,30,30,40))
    assert_equal(match.MainM.is_loaded(),True)
    assert_equal(match.MainM.q_size(),100)
    assert_equal(match.MainM.id(),-1)
    assert_equal(match.MainM.appearence(),24)
    assert_equal(match.MainM.personality(),45)
    assert_equal(match.MainM.wealth(),34)

    match.add_player((0,24,45,34,30,30,40))
    assert_equal(match.MainF.is_loaded(),True)
    for k,v in match.men_pool.items():
        assert_equal(v.q_size(),101)

def test_queen():
    match=Match.Match("male1.txt","female1.txt")
    match.add_player((1,1,1,99,1,1,98))

    match.make_invitation()
    assert_equal(match.queen.id(),1)
    match.matching_n_reset()

    match.make_invitation()
    assert_equal(match.queen.id(),3)
    match.matching_n_reset()

    match.make_invitation()
    assert_equal(match.queen.id(),5)
    match.matching_n_reset()

    match.make_invitation()
    assert_equal(match.queen.id(),8)
    match.matching_n_reset()

    match.make_invitation()
    assert_equal(match.queen.id(),0)
    match.matching_n_reset()

    match.make_invitation()
    assert_equal(match.queen.id(),2)
    match.matching_n_reset()


def test_invitation():
    match=Match.Match("male1.txt","female1.txt")
    match.add_player((1,1,1,99,1,1,98))
    for i in range(0,5):
        match.make_invitation()
        assert_equal(match.matching_n_reset(),True)
    match.make_invitation()
    assert_equal(match.matching_n_reset(),False)

def test_fullrun():
    match=Match.Match("male.txt","female.txt")
    playerList=readPlayerFile("players.txt")
    match.add_player(playerList[0])
    match.make_invitation()
    while match.matching_n_reset():
        match.make_invitation()
    assert_equal(match.queen.id(),28)
    match.restore()
    for p in playerList[1:-1]:
        match.kick_start(p)

    match.add_player(playerList[-1])
    match.make_invitation()
    while match.matching_n_reset():
        match.make_invitation()
    assert_equal(match.queen.she_loves().id(),33)
    match.restore()


