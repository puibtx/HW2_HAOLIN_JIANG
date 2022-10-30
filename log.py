import time

def timestamp(func):
    def decorate(*args, **kwargs):
        print (time.ctime())
        return func(*args, **kwargs)
    return decorate
