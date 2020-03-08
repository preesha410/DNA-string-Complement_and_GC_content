dna= ("attatagtatg")
a=0
t=0
g=0
c=0
for i in dna:
    if i=="a":
        a=a+c
    elif i=="t":
        t=t+g
    elif i=="c":
        c=c+a
    elif i=="g":
        g=g+t
    else:
        pass
return dna
