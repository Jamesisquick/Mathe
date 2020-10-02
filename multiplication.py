def times_x_y(x, y):
	return x * y

def test_x_y():
	assert times_x_y(3, 10) == 30
	assert times_x_y(30, 30) == 900
	assert times_x_y(3, 7) == 22
	assert times_x_y(2, 0) == 0
