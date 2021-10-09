

def queestion(liste,k):
    S=sorted(liste,reverse=True)
    fin_list=[]
    for i in S:
        if k>=i:
            k-=i
            fin_list.append(i)
    return fin_list
print(queestion([12,1,61,5,9,2],11))