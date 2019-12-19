def multi_plus(array):
    """
        sums even-indexes elements and multiply at the last
    """
    if len(array) == 0:
        return False
    s = 0
    for i in range(len(array)):
      if i % 2 == 0:
        s = s + array[i]
    return s * array[-1]





if __name__ == '__main__':
    print('Example:')
    print(multi_plus([0, 1, 2, 3, 4, 5]))
    assert multi_plus([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert multi_plus([1, 3, 5]) == 30, "(1+5)*5=30"
    assert multi_plus([6]) == 36, "(6)*6=36"
    assert multi_plus([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
