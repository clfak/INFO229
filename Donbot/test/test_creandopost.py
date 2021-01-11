from post import is_posted

def test_creapost():
	assert is_posted("clfak") == True


def test_creapost_2():
	assert is_posted("clsd") == False
