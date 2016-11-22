from nose.tools import *
from ex49.parser import ParserError


def test_subject():
    assert_equal(parser.scan("north"), [('direction', 'north')])
    result = parser.scan("north south east")
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verb():
    assert_equal(parser.scan("go"), [('verb', 'go')])
    result = parser.scan("go kill eat")
    assert_equal(result, [('verb', 'go'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])

def test_object():
    assert_equal(parser.scan("the"), [('stop', 'the')])
    result = parser.scan("the in of")
    assert_equal(result, [('stop', 'the'),
                          ('stop', 'in'),
                          ('stop', 'of')])
