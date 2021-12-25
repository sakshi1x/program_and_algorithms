
def func(x):
    ctr = 0
    for y in x:
        if len(y)>1 and y[0] ==y[-1]:
            ctr += 1
    return ctr
print(func(["abc","aba","121"]))

    

        