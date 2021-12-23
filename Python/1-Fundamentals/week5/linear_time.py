import timeit

print(timeit.timeit("[x for x in rage(1000000)]", number=1))
print(timeit.timeit("[x for x in rage(10000000)]", number=1))
print(timeit.timeit("[x for x in rage(100000000)]", number=1))
