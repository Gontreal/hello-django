from nose.tools import *
from libs import charactors
from sometools import readPlayerFile

man=readPlayerFile("male1.txt", 1)
women_list=readPlayerFile("female1.txt")
def test_basic():
    m=charactors.MalePlayer(*man[0])
    assert_equal(m.id(),0)
    assert_equal(m.expect_check(),True)
    assert_equal(m.is_loaded(),True)
    m.free()
    assert_equal(m.is_loaded(),False)

def test_dreamgirl():
    m=charactors.MalePlayer(*man[0])
    assert_equal(m.id(),0)

    wlist=[charactors.FemalePlayer(*w) for w in women_list]
    for w in wlist:
        m.new_girl(w)
    #TODO: figure out a way to let meet_women() take python list
   #m.meet_women(wlist)
    assert_equal(m.q_size(),12)

    woman=m.dream_girl()
    assert_equal(woman.id(),0)
    woman.chosen()

    woman=m.dream_girl()
    assert_equal(woman.id(),4)
    woman.chosen()

    woman=m.dream_girl()
    assert_equal(woman.id(),7)
    woman.chosen()
    m.restore()
    assert_equal(m.q_size(),12)
    woman=m.dream_girl()
    assert_equal(woman.id(),1)
