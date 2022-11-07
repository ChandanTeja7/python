n=int(input())
z=[]
for i in range(len(n)):
   a=int(input())
   z.append(a)
print("the least number is: ",min(z))   
print("the highest number is: ",max(z))
y=sum(z)/len(z)
print("the average is: ",y)
