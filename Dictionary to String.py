def dicttocs(cs):
    string = ''
    for i in cs:
        string = string+(i+"="+cs[i])+";"
    return string.strip(";")
cs = input("Enter the Dictionary: ")
cs=eval(cs)
a = dicttocs(cs)
print (a)
