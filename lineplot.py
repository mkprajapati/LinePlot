from matplotlib import pyplot as pl
colr=input("Enter color :")
titl=input("Enter title :")
xlab=input("Enter horizontal attribute :")
ylab=input("Enter vertical attribute :")
noofel=int(input("Enter no.. of elements you want : "))
global i
list1=[]
print("enter list of elements for x-axis :")
i=1
while(i<=noofel):
    a=float(input())
    list1.append(a)
    i+=1
i=1
list2=[]
print("enter list of elements for y-axis :")
while(i<=noofel):
    a=float(input())
    list2.append(a)
    i+=1


pl.plot(list1,list2,color=colr,marker='o')
pl.xlabel(xlab)
pl.ylabel(ylab)
pl.title(titl)
pl.show()

