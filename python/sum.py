def sum(lst, n):
    # Your code here!
    duplicateset = lst.copy()
    for x in lst:
        duplicateset.remove(x)
        for y in duplicateset:
            if (x + y == n):
                return True
    return False

def test():
    assert sum([-1, 1], 0)
    assert not sum([0,2,3], 4)
    assert sum([0,2,2], 4)
    print("Success!")

if __name__ == "__main__":
    test()