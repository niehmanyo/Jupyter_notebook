# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def DFS_Backtracking(n,max_profit,now_profit,max_weight,now_weight,p_list,w_list,t_list):
    if(n>=len(p_list)):
        if(max_profit[0]==0):
            max_profit[0]=now_profit[0]
        else:
            if(now_profit[0]>max_profit[0]):
                max_profit[0]=now_profit[0]
                print(t_list)
            else:
                return
    for i in range(n,p_list.__len__()):
        now_weight[0] += w_list[i]
        if(now_weight[0]<=max_weight): ## 这里我先用中文说明写，如果可以装，那就装进来，考虑下一个装不装进行递推
            now_profit[0]+=p_list[i]
            t_list[i]=1

            DFS_Backtracking(i+1,max_profit,now_profit,max_weight,now_weight,p_list,w_list,t_list)

            now_weight[0] -= w_list[i]
            now_profit[0]-=p_list[i]#如果这里面不行，把这个价值从背包中拿出，说明i放进去，后面有些东西不可以放4
            t_list[i]=0

        else: ## 如果这个装不进去，那么就不装这个，装一个看看
            now_weight[0] -= w_list[i]
            DFS_Backtracking(i+1,max_profit,now_profit,max_weight,now_weight,p_list,w_list,t_list)
        ## 如果执行到这一步骤，说明以上的if和else都不可以，那么就是这个i有问题，所以要把这个i的重量给拿出去

class node():
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight
        self.left=None
        self.right=None
def Buildtree(p_list,w_list):
    tree_list=[]
    root=node(0,0)
    for i in range(pow(2,len(p_list)+1)-1):#从0开始，所以要物品表价值长度+1，这就是height，然后2的次方是算有多少个节点，-1是因为从0开始
        tree_list.append(0)
    tree_list[0]=root
    for i in range(len(p_list)): ##指向第i个物品
        for j in range(pow(2,i+1)-1,pow(2,i+2)-1):
            if(j%2==1):
                father=j//2
                son=node(tree_list[father].value+p_list[i],tree_list[father].weight+w_list[i])
                tree_list[j]=son
            else:
                son = node(tree_list[father].value , tree_list[father].weight)
                tree_list[j]=son
                father=(j-1)//2
    for father in range(tree_list.__len__()):
        lson=father*2+1
        rson=father*2+2
        if(lson<tree_list.__len__() and rson<tree_list.__len__()):
            tree_list[father].left=tree_list[lson]
            tree_list[father].right=tree_list[rson]
    return tree_list

def breadth_first_branch_and_bound(root,max_weight):
    Queue=[]
    Queue.append(root.left)
    Queue.append(root.right)
    max_profit=0
    while(Queue.__len__()):
        p=Queue.pop(0)
        if(p.value>max_profit and p.weight<=max_weight):
            max_profit=p.value
        if(p.left!=None):
            Queue.append(p.left)
        if(p.right!=None):
            Queue.append(p.right)
    return max_profit

max_profit=[0]
now_profit=[0]
max_weight=13
now_weight=[0]
p_list=[20,30,35,12,3]
w_list=[2,5,7,3,1]
t_list=[0,0,0,0,0]
DFS_Backtracking(0,max_profit,now_profit,max_weight,now_weight,p_list,w_list,t_list)
print(max_profit[0])
tree_list=Buildtree(p_list,w_list)

value=breadth_first_branch_and_bound(tree_list[0],13)
print(value)
