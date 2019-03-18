class dog(object):
    def gaga(): 
        print('汪汪')


class cat:
    def gaga():
  
        print('喵喵')


def you_say(you):
    you.gaga()
    you.gaga()


you_say(dog)
print('_'*10)
you_say(cat)
