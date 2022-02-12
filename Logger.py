

logLevel = 0

def debug(text):
    if logLevel > 3:
        print(text)
    
def info(text):
    if logLevel > 2:
        print(text)
    
def warn(text):
    if logLevel > 1:
        print(text)
    
def error(text):
    if logLevel > 0:
        print(text)
    
def setLogLevel(level):
    global logLevel
    logLevel = level