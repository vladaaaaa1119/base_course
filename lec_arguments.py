def my_func(a, b):
   x = 3 * a - b
   return x


#tmp = my_func()


def my_func(a=1, b=0):
  x = 3 * a - b
  return x


print(my_func())
print(my_func(3, 4))
print(my_func(3))
print(my_func(b = 3))
print(my_func(b = 3, a = 9))


def my_func(a, b = 0):
   x = 3 * a - b
   return x


def my_func(*args):
   x = 3 * (args[0] - args[1])
   return x


print(my_func(3, 4))
print(my_func(3, 4, 8, 5))

def my_func(**kwrgs):
   x = 3 * kwrgs["obj_1"] - kwrgs["obj_2"]
   return x 


print(my_func(obj_1=3, obj_2=4))


def final_func(a: float, b: int=1, c=4, *arg, **kw):
   print(f"Hello world {a} + {b} + - {arg}/ {kw}")


def my_func(a, b):
   x1 = 3 * a - 2 * b
   x2 = 5 *b - 4 * a
   return x1, x2


tmp = my_func(3, 2)