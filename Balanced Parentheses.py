def balanced(string):
    num_open = 0
    num=0
    for char in string:
        if char =='(':
            num_open += 1
            num+=1
            if num_open<0:
                return False
        elif char ==')':
            num_open -= 1
            num+=1
            if num_open<0:
                return False
    if num_open != 0:
        return False
    elif num_open==0:
        if num==0:
            return True
        else:
            return True
       

print(balanced(input()))