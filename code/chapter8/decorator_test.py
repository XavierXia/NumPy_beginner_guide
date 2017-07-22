# -*- coding: utf-8 -*-

from numpy.testing.decorators import setastest
from numpy.testing.decorators import skipif
from numpy.testing.decorators import knownfailureif
from numpy.testing import decorate_methods

### nosetests -v decorator_setastest.py

@setastest(False)
def test_false():
    pass

@setastest(True)
def test_true():
    pass

#跳过测试
@skipif(True)
def test_skip():
    pass

#该测试总是不通过
@knownfailureif(True)
def test_alwaysfail():
    pass

class TestClass():
    def test_true2(self):
        pass

class TestClass2():
    def test_false2(self):
        pass

decorate_methods(TestClass2, setastest(False), 'test_false2')