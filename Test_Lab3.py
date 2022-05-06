import Lab3

print("Test_Lab3")


def test_Req01A():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 120, 110, 250]
    test_arr = [11, 12, 22, 25, 34, 64, 90, 110, 120, 250]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_Req01B():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 120, 110, 250]
    test_arr = [250, 120, 110, 90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 120, 110, 250]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_Req02():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 100, 110, 11, 12]

    result = Lab3.bubble_sort(input_arr, 1)

    assert (result == 1)
def test_Req03():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 1)

    assert (result == 2)

def test_Req04():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr, 1)

    assert (result == 0)


def test_Req05():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 'H', 'sus ඞඩ', 'E', 'A']

    result = Lab3.bubble_sort(input_arr, 0)

    assert (result == 3)