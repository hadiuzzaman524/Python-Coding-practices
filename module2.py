def maximum(x):
    global y
    y=x[0]
    for i in x:
        if i>y:
            y=x[i]
    return y


