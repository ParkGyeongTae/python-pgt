import timeit

def test_for():
    for i in range(100):
        i += 1

t1 = timeit.repeat(stmt='test_for()', 
                   setup='from __main__ import test_for', 
                   number=10000, 
                   repeat=3)
print(t1)
