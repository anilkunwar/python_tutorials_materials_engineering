# python 3.6.5
# nested for loop in python 3.6.5
a=-1.7
b=-1.1
i=0
n=0
while(i<11):
    f = open("output.txt", "a")
    n=n+1
    #print(n)
    print("n=",n, file=f)
    c=n*a
    d=n*b
    #print(c,d)
    print(c,d, file=f)
    f.close()
    i=1+1
    if(n>10):
       break
    
