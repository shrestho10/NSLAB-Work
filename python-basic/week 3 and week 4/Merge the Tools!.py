def merge_the_tools(string, k):
    # your code goes here
    a=int(len(string)/k)
    s=''
    l=[]
    count=0
    for i in range(0,len(string)):
        s+=string[i]
        count+=1
        if count==k:
            l.append(s)
            s=''
            count=0
    newlist=[]
    for i in l:
        nl=''
        for j in i:
            if j not in nl:
                nl+=j
        newlist.append(nl)

    for i in newlist:
        print(i)




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)