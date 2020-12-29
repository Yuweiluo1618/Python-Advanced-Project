def makeBold(func):
    def function_in():
        return "<b>"+func()+"</b>"
    return function_in

def makeItalic(func):
    def function_in():
        return "<i>"+func()+"</i>"
    return function_in

@makeBold
@makeItalic
def test():
    return "hellpworld"


print(test())