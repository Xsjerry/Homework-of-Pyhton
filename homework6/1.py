def isRepeated(v):
    s = set(v)
    if v == list(s):
        print('False')    
    else:
        print('True')

data = list(map(int,input().split(',')))
isRepeated(data)
       