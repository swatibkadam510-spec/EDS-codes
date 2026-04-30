def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i]==key:
            return i
    return -1
arr=list(map(int,input().split()))
key=int(input())
result=linear_search(arr,key)
if result!=-1:
    print(result)
else:
    print("not found")