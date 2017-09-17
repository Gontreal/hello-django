from nose.tools import *
from libs import charactors

def test_base():
    joe=charactors.Person(-1,20,30,40,50,30,20)
    assert_equal(joe.id,-1)
    assert_equal(joe.appearence,20)
    assert_equal(joe.personality,30)
    assert_equal(joe.wealth,40)
    assert_equal(joe.availability,True)
    assert_equal(joe.expect_check(),True)
    joe.chosen()
    assert_equal(joe.availability,False,)
    joe.ready()
    assert_equal(joe.availability,True)

    default=charactors.Person()
    assert_equal(default.id,101)
    assert_equal(default.appearence,0)
    assert_equal(default.personality,0)
    assert_equal(default.wealth,0)
    assert_equal(default.availability,True)
    assert_equal(default.expect_check(),False)
    default.chosen()
    assert_equal(default.availability,False,)
    default.ready()
    assert_equal(default.availability,True)
