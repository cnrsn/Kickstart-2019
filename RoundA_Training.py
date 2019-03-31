############### Read from Terminal ##################
#N=[]
#P=[]
#S=[]
#T = int(input())
#for i in range(T):
#    n, p = map(int, input().split())
#    P.append(p)
#    N.append(n)
#    s=input().split()
#    ss = [int(x) for x in s]
#    S.append(ss)  
######################################################



#################### Read from File ##################
filename="Input.txt"

def read_input(filename):
    lines = open(filename).readlines()
    N=[]
    P=[]
    S=[]
    for l in range(len(lines)-1):
        k=lines[l+1].split()
        k = list(map(int, k))
        if l%2==0:
            N.append(int(k[0]))
            P.append(int(k[1]))
        if l%2==1:
            S.append(k)
    return S,P,N 
(S,P,N)=read_input(filename)
del filename
#######################################################



#################### Solving Problem ##################
def training_time(Subarray):
    tt=0
    for i in Subarray:
        tt+=max(Subarray)-i       
    return tt

def training_time2(Subarray):
    tt=(max(Subarray)*len(Subarray))-sum(Subarray)     
    return tt

print(training_time2([9,3,1]))

def Calculate(S,P,N):
    Case=[]
    for i in range(len(S)):
        Array=S[i]
        p=P[i]
        n=N[i]
        Array.sort(reverse=True)
        for j in range(n-p+1):
            Subarray=Array[j:j+p]
            if j==0:
                Case.append(training_time2(Subarray))
            if training_time2(Subarray)<Case[i]:
                Case[i]=training_time2(Subarray)            
    return Case

Case=Calculate(S,P,N)

for i in range(len(Case)):
    print('Case #'+'%.f' % int(i+1) + ': ' + '%.f' % Case[i])
del i
#######################################################   

     
##################   Trash   ##########################
#Checks whether there exist enough repeating numbers 
#def check(s,p):
#    sonuc=0
#    for i in range(len(s)):
#        c=s.count(s[i])
#        if c>sonuc:
#            sonuc+=1
#    if sonuc==p:
#        return True        
#    return False
#print(check(S[0],P[0]))

#Calculates 
#def delta(s):
#    avg=sum(s)/len(s)
#    array=numpy.array(s)
#    return (array - avg)
#
#delta_S=[]
#for i in range(T):
#    delta_S.append(delta(S[i]))
#######################################################   

    

