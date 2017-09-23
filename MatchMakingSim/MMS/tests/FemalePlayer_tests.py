from nose.tools import *
from libs import charactors
from sometools import readPlayerFile

men_list=readPlayerFile("male1.txt")
woman=readPlayerFile("female1.txt",1)
def test_basic():
    w=charactors.FemalePlayer(*woman[0])
    assert_equal(w.id(),0)
    assert_equal(w.expect_check(),True)
    assert_equal(w.check_popularity(),0)
    assert_equal(w.is_loaded(),True)
    w.free()
    assert_equal(w.is_loaded(),False)

def test_sheloves():
    #initialize
    w=charactors.FemalePlayer(*woman[0])
    assert_equal(w.id(),0)
    #test initial loved_one
    prince=w.she_loves()
    assert_equal(prince.id(),101)
    m_list=[charactors.MalePlayer(*m) for m in men_list]
    #test she_loves()
    for m in m_list:
        w.meet(m)
    prince=w.she_loves()
    assert_equal(prince.id(),0)
    #test popularity
    w.more_popular()
    w.more_popular()
    w.more_popular()
    w.more_popular()
    assert_equal(w.check_popularity(),4)
    #test reset()
    w.reset()
    assert_equal(w.check_popularity(),0)
    prince=w.she_loves()
    assert_equal(prince.id(),101)
    #test fell_love()
    w.fell_love(m_list[-1])
    prince=w.she_loves()
    assert_equal(prince.id(),11)
