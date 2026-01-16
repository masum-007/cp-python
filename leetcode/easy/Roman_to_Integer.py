class Solution:
    def romanToInt(self, s: str) -> int:
        l=len(s)
        sum =0
        i=0
        while i<l:
            if s[i]=="I":
                if i+1<l and s[i+1]=="V":
                    sum=sum+4
                    i=i+2
                elif i+1<l and s[i+1]=="X":
                    sum=sum+9
                    i=i+2
                else:
                    sum=sum+1
                    i+=1
            elif s[i]=="V":
                sum =sum+5
                i+=1
            elif s[i]=="X":
                if i+1<l and s[i+1]=="L":
                    sum=sum+40
                    i=i+2
                elif i+1<l and s[i+1]=="C":
                    sum=sum+90
                    i=i+2
                else:
                    sum=sum+10
                    i+=1
            elif s[i]=="L":
                sum =sum+50
                i+=1
            elif s[i]=="C":
                if i+1<l and s[i+1]=="D":
                    sum=sum+400
                    i=i+2
                elif i+1<l and s[i+1]=="M":
                    sum=sum+900
                    i=i+2
                else:
                    sum=sum+100
                    i+=1
            elif s[i]=="D":
                sum =sum+500
                i+=1
            elif s[i]=="M":
                sum =sum+1000
                i+=1
        return sum
        
                