import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner
from led_tester import utils
from led_tester import regClean as rc

def test_parseFile():
    testFile = "C:\input.in"
    N, instructions = utils.parseFile(testFile)
    assert N == 10
    assert instructions == [
        'turn on 2,6 through 4,9\n', 'switch -1,0 through 15,10']

def test_regEx():
    testFile = "C:\input.in"
    N, instructions = utils.parseFile(testFile)
    for i in instructions:
        method, l1, l2, l3, l4 = rc.regexClean(i,N)
    assert method == 'switch'
    assert l1 == 0
    assert l2 == 0
    assert l3 == 9
    assert l4 == 9

def test_RegexNone():
    testFile = "C:\input.in"
    N, instructions = utils.parseFile(testFile)
    for i in instructions:
        method, l1, l2, l3, l4 = rc.regexClean(i,N)
    assert method == None
    assert l1 == None
    assert l2 == None
    assert l3 == None
    assert l4 == None
    

def test_NumbersOutofBounds():
    testFile = "C:\input.in"
    N, instructions = utils.parseFile(testFile)
    for i in instructions:
        method, l1, l2, l3, l4 = rc.regexClean(i,N)
    assert method == 'switch'
    assert l1 == 0
    assert l2 == 0
    assert l3 == 9
    assert l4 == 9
    
