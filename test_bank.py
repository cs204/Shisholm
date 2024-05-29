from test_bank.bank import hello
import pytest


def test_init_1():
	a = hello('здравствуйте')
	assert a=='$0'

def test_init_2():
	a = hello('здарова')
	assert a=='$20'

def test_init_3():
	a = hello('приветик')
	assert a=='$100'
