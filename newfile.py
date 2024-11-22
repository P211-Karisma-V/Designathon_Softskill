from collections import Counter
f=open("ex.txt","r")
c=Counter(f.read().split())
print("number of words in the file:",c)