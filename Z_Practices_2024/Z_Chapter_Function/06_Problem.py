def sum_dif_pro(a,b):
    sum = a+b
    dif = a-b
    pro = a*b
    div = a/b
    return sum,dif,pro,div
s,t,u,v = sum_dif_pro(10,5)
print("Sum,difference and product are:",s,t,u,v)
