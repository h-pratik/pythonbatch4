def cstodict(cs):
     a = cs.split(";")
     d = {}
     for i in a:
          k,v=i.split("=")
          d[k]=v
     return d
a= input("Enter a String : ")
b= cstodict(a)
print(b)
