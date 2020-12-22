from solution import *

def testcase_one():
    assert binary_parser(0, 127, "FBFBBFF") == 44
    assert binary_parser(0, 7, "RLR") == 5

def testcase_two():
    assert binary_parser(0, 127, "BFFFBBF") == 70
    assert binary_parser(0, 7, "RRR") == 7

def testcase_three():
    assert binary_parser(0, 127, "FFFBBBF") == 14
    assert binary_parser(0, 7, "RRR") == 7

def testcase_four():
    assert binary_parser(0, 127, "BBFFBBF") == 102
    assert binary_parser(0, 7, "RLL") == 4



