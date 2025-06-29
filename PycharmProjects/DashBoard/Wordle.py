# https://www.codechef.com/practice/course/strings/STRINGS/problems/WORDLE


t=2
while t>0:
    s1 = "ABCDA"
    s2 = "EDCBA"
    s=""
    for i in range(len(s1)):
       s+= "G" if s1[i]==s2[i] else "B"
    print(s)



    t-=1
