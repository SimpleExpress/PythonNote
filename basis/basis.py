# Our first Python program
print('hello world')  # hello world


# primitives & operations
number = 123
string = 'abc'
byte = b'abc'
truth = True
compx = 1 + 2j
nop = None

# id: returns object's identity.
id(number)
id(compx)

# dir: returns a list of valid attributes
dir(string)
dir(truth)

# type
type(number)  # <class 'int'>
type(compx)  # <class 'complex'>


# list & tuple
a = [1, 2, 3, 4, 5]
b = list(range(1, 6, 1)) # [1, 2, 3, 4, 5]
c = (1, 2, 3)  # or c = tuple([1, 2, 3])

# list is a natural bidirectional queue
a = [1, 2, 3, 4, 5]
a.pop(0)  # [2, 3, 4, 5]
a.pop()  # [2, 3, 4]
a.insert(0, 7)  # [7, 2, 3, 4]
a.append(8)  # [7, 2, 3, 4, 8]

# slice operation
a = [1, 2, 3, 4, 5]
a[:]  # [1, 2, 3, 4, 5]
a[1:-1:1]  # [2, 3, 4]
a[-1::-2]  # [5, 3, 1]


# dict
d = {} # or d = dict()
d[1] = 1
d[2] = 4
d[1] # 1
d.get(3, None) # None
d.update({3: 9, 4: 16})

# method items returns the key-value pairs
for k, v in d.items(): 
	print(k, v)


# set
p = set('abc')
q = frozenset('cde')


p & q # {'c'}
p | q # {'a', 'e', 'b', 'c', 'd'}
p ^ q # {'e', 'a', 'b', 'd'}
p - q # {'a', 'b'}


# if statement
a = 1
b = int(input('enter a number:'))
if b == a: 
	print('equal')
elif b < a:
	print('lower')
else:
	print('higher')

if a < b < c: pass
if a < b and b < c: pass


# for statement
for i in range(0, 5):
	if i == 5:
		print('found the God!!!')
		break
else:
	print('not found')

# while statement
while True:
	pass
else:
	pass


# function
def func(a, b=1, *args, **kwargs):
	print(a)
	print(b)
	for arg in args: print(arg)
	for k, v in kwargs.items(): print(k, '=', v)
func('a', 'b', 1, 2, 3, c=4, d=5)


# lambda
def make_incrementor(n):
	return lambda x: x + n
f = make_incrementor(42)
f(0)  # 42
f(1)  # 43

processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)


# exception handling
while 1:
	try:
		x = int(input('please enter a number:'))
		print(10 / x)
		break
	except ValueError as e:
		print('Not a valid number')
		print(e)
	except ZeroDivisionError as e:
		print('Cannot divide by zero')
		print(e)

except (ValueError, ZeroDivisionError) as e:
	print(e)


# object oriengted programming
class Employee(object):
	def __init__(self, name, empno):
		self.name = name
		self.empno = empno
e = Employee('Tom', 101010)
e.empno  # 101010
e.name = 'Tommy'
e.mobile = '+86 021 12345678'

class Manager(Employee):
	def __init__(self, name, empno, band):
		super(Manager, self).__init__(name, empno)
		self.__band = band

	def __str__(self):
		return '%s, %d' % (self.name, self.empno)

m = Manager('Jack', 123, 9)
m.name  # Jack
m.__band  # 'Manager' object has no attribute '__band'
print(m)  # Jack, 123

class C(A, B): pass


# List Comprehensions
a = [i + 1 for i in range(10)]
a  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Multiplication Table in one line python code
print('\n'.join(['  '.join(['%d x %d = %-2d' % (i, j, i * j) for j in range(1, i + 1)]) for i in range(1, 10)]))


# slide: Decorator
def log(fn):
	def wrapper():
		print('start executing, %s' % fn.__name__)
		fn()
		print('end executing, %s' % fn.__name__)
	return wrapper

@log
def foo():
	print('I am foo')

foo()

# decorator - advanced example
from functools import wraps
def memo(fn):
	cache = {}
	miss = object()
	@wraps(fn)
	def wrapper(*args):
		result = cache.get(args, miss)
		if result is miss:
			result = fn(*args)
			cache[args] = result
		return result
	return wrapper

@memo
def fib(n):
	if n < 2: return n
	return fib(n - 1) + fib(n - 2)


# slide: Generator
def get_next_prime():
	yield 2
	yield 3

	ret = 4
	while True:
		ret += 1  # starts from 5
		for i in range(2, ret - 1):
			if ret % i == 0: break
		else: yield ret

prime_generator = get_next_prime()
next(prime_generator)  # 2
next(prime_generator)  # 3
for v in get_next_prime():
	print(v)  # endless


# coroutine
import sys
def produce(l, top):
	i = 0
	while i < top:
		l.append(i)
		yield i
		i = i + 1

def consume(l, top):
	p = produce(l, 10)
	while 1:
		try:
			next(p)
			while len(l) > 0: print(l.pop())
		except StopIteration: sys.exit(0)

consume([], 10)


# gevent
import gevent
from gevent.queue import Queue

tasks = Queue()
def worker(n):
    while not tasks.empty():
        task = tasks.get()
        print('Worker %s got task %s' % (n, task))
        gevent.sleep(0)
def boss():
    for i in xrange(1,25): tasks.put_nowait(i)

gevent.spawn(boss).join()
gevent.joinall([
    gevent.spawn(worker, 'steve'),
    gevent.spawn(worker, 'john'),
])


# Pony ORM
select(c for c in Customer if sum(c.orders.price) > 1000)

SELECT "c"."id"
FROM "Customer" "c"
  LEFT JOIN "Order" "order-1"
    ON "c"."id" = "order-1"."customer"
GROUP BY "c"."id"
HAVING coalesce(SUM("order-1"."total_price"), 0) > 1000