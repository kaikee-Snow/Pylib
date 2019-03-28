def func():
    x = 1
    while True:
        y = yield x
        print('y=', y)
        x += y
        print('x=', x)


geniter = func()
res = geniter.__next__()
print('......res=', res)
res = geniter.send(3)
print('......res=', res)
res = geniter.send(10)
print('......res=', res)
