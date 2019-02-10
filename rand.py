import random
def rand_norepeat(_min,_max,num):
    if _max-_min+1<num:
        raise Exception("Too big num or too small number range to make sure there's in repeat in the randoms.",num)
    result=[]
    for x in range(num):
        tmp=random.randint(_min,_max)
        if random.randint(1,100)%2==1:
            tmp=-tmp;
        while result.count(tmp)!=0:
            tmp=random.randint(_min,_max)
        result.append(tmp)
    return result
def rand_by_digit(digit):
    tmp=''
    for x in range(digit):
        x=random.randint(0,9)
        tmp+=str(x)
    result=int(tmp,10)
    if random.randint(1,100)%2==1:
        result=-result;
    return tmp
