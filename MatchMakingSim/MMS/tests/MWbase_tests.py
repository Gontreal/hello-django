from nose.tools import *
from libs import charactors

def test_Man():
    joe=charactors.Man(-1,20,30,40,50,30,20)
    assert_equal(joe.id,-1)
    assert_equal(joe.expect_check(),True)
    assert_equal(joe.q_size(),0)

def test_Woman():
    dany=charactors.Woman(99,89,45,76,56,76,34)
    assert_equal(dany.id,99)
    dany.chosen()
    assert_equal(dany.availability,False)
    assert_equal(dany.check_popularity(),0)
    dany.more_popular()
    dany.more_popular()
    dany.more_popular()
    assert_equal(dany.check_popularity(),3)


