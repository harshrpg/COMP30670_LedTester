import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner
from led_tester import utils


def test_command_line_interface():
    testFile = "C:\input.in"
    N, instructions = utils.parseFile(testFile)
    assert N == 10
    assert instructions == [
        'turn on 2,6 through 4,9\n', 'switch 0,0 through 9,0']
