import math

def rm_smallest(d):
    # Your code here!
    if (bool(dict)):
        minval = min(d.values(), default=0)
        for key in d.keys():
            if (d[key] == minval):
                del d[key]
                return d
    return d

def test():
    assert 'a' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'b' in rm_smallest({'a':1,'b':-10}).keys()
    assert not 'a' in rm_smallest({'a':1,'b':5,'c':3}).keys()
    rm_smallest({})
    print("Success!")

if __name__ == "__main__":
    test()