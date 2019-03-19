from recursions import recursion
from recursions import sorting


def test_sum_array():
    """
    make sure top_n works correctly
    """

    assert sorting.sum_array([1,2,3,4])==10, 'incorrect'


###################
def test_fibonacci():
    """
    make sure top_n works correctly
    """

    assert sorting.fibonacci(5) == 8, 'incorrect'


#######
def test_factorial():
    """
    make sure top_n works correctly
    """

    assert sorting.top_factorial(3) == 6, 'incorrect'


##################
def test_reverse():
    """
    make sure top_n works correctly
    """
    assert sorting.top_reversereverse("sdfgfdgd") == 'dgdfgfds', 'incorrect'

#####################
def test_bubble_sort():
    """
    make sure top_n works correctly
    """
    assert sorting.top_bubble_sort([1,78,8,0,7,8]) == [0, 1, 7, 8, 8, 78], 'incorrect'

##########################
def test_merge_sort():
    """
    make sure top_n works correctly
    """
    assert sorting.merge_sort([0, 1, 7, 8, 8, 78]) == [0, 1, 7, 8, 8, 78], 'incorrect'

##################
def test_quick_sort():
    """
    make sure top_n works correctly
    """
    assert sorting.quick_sort([1,2,3,4,5,6,6,7,8]) == [1, 2, 3, 4, 5, 6, 6, 7, 8], 'incorrect'
