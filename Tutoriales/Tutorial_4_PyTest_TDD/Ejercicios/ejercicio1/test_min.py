import min

def test_get_min():
	values=[1,5,10,2]
	assert min.get_min(values) == 1

def test_get_min2():
	values=[3,30,5,6,8]
	assert min.get_min(values) == 3
