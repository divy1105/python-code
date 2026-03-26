
#! kewword arguments

# def info(**kwargs):
#     print(kwargs)
    
# info(a=10,b=20)

#! variable length arguments

def info(*args,**kwargs):
    print(args)
    print(kwargs)
    
info(10,20,30,a=10,b=20)