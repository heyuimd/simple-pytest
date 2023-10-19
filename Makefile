test_ch01:
	@pytest -s tests/ch01

test_ch02:
	@pytest -s tests/ch02

test_ch03:
	@pytest -s tests/ch03

test_ch04:
	@pytest -s tests/ch04

test_all: test_ch01 test_ch02 test_ch03 test_ch04