def makebold(fn):
    def inner():
        return "<b>" + fn() + "</b>"
    return inner
    
def makeitalic(fn):
    def inner():
        return "<i>" + fn() + "</i>"
    return inner

@makebold
@makeitalic
def hello():
    return "Hello World"
	
print hello()