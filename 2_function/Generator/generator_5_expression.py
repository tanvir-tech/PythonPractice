numbers = range(5)
gen_obj = (x for x in numbers)               # generator expression

print(gen_obj)

print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))

