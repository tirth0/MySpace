n,k=[int(x) for x in input().split()]
s=input()
s1=s[ :int(n/2)]
if n%2==0:
    s2=s[int(n/2): ]
else:
    s2=s[int(n/2)+1: ]
s3=s2[::-1]
c=0
for i in range(len(s1)):
    if s1[i]!=s2[i]:
        c=c+1
if (c<=k):
    print("Possible")
else:
    print("Impossible")
   
