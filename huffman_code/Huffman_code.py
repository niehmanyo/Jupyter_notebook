class node():
    def __init__(self,symbol,frequency):
        self.symbol=symbol
        self.frequency=frequency
        self.left=None
        self.right=None
        self.huff=""
def find_symbol_frequency(str):
    s=list(set(str))
    frequency=[]
    for i in range(len(s)):
        index=0
        for j in range(len(str)):
            if(s[i]==str[j]):
                index+=1
        frequency.append(index)
    return s,frequency
def change(List,i,j):
    temp=List[i]
    List[i]=List[j]
    List[j]=temp
def sort(symbol,frequency):
    for i in range(0,len(frequency)):
        min=frequency[i]
        index=i
        for j in range(i,len(frequency)):
            if(frequency[j]<min):
                min=frequency[j]
                index=j
        change(frequency,i,index)
        change(symbol,i,index)
def huffman(symbol,frequency):
    List=[]
    for i in range(len(symbol)):
        r=node(symbol[i],frequency[i])
        r.left=None
        r.right=None
        List.append(r)
    for i in range(len(symbol)-1):
        p=List.pop(0)
        q=List.pop(0)
        r=node("",q.frequency+p.frequency)
        r.left=p
        r.right=q
        index=0
        for j in range(len(List)):
            if(r.frequency>List[j].frequency):
                index=j
        List.insert(index,r)
    return List.pop(0)
def preOrder(n,index,list1,list3):
    if(n!=None):
        print(n.symbol,",",n.frequency,index)
        if(n.symbol!=""):
            n.huff=index
            for i in range(len(list1)):
                if n.symbol==list1[i]:
                    list3[i]=index
        preOrder(n.left,"0"+index,list1,list3)
        preOrder(n.right,"1"+index,list1,list3)

def printHuffman(str,list1,list3):
    for i in range(len(str)):
        for j in range(len(list1)):
            if(str[i]==list1[j]):
                print(list3[j],end="")
str1=input("Please input the string:")
list1,list2=find_symbol_frequency(str1)
list3=list1.copy()
sort(list1,list2)
print(list1)
print(list2)
node1=huffman(list1,list2)
preOrder(node1,"0",list1,list3)
printHuffman(str1,list1,list3)