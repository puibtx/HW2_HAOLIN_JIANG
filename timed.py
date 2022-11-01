import time
def timeme(func):
    def decorate(*args,**kwargs):
    	start = time.time(
    	end = time.time()
    	print("Total time ",end - start)
	return func(*args,**kwargs)
    return decorate
