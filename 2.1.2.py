std={1:"ashu",2:"neha",3:"sumit",4:"sonu"}
print("original dictionary:",std)
newkey=int(input())
newvalue=input()
std[newkey]=newvalue
print("after insertion:",std)
updatekey=int(input())
updatevalue=input()
if updatekey in std:
    std[updatekey]=updatevalue
    print("after update:",std)
deletekey=int(input())
if deletekey in std:
    del std[deletekey]
    print("aft6er deletion:",std)
print("traversing dictionary:")
for key,value in std.items():
    print(key," : ",value)