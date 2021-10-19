def outer():
    def inner():
        s = 'Hello world!'
        return s            
    return inner()    
print(outer())