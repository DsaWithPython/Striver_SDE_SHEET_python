def merge(arr,temp,left,mid,right):
    inv_count = 0
    i = left
    j = mid
    k = left
    while i<=(mid-1) and j<=right:
        if arr[i]<= arr[j]:
            temp[k]=arr[i]
            k+=1
            i+=1
        else:
            temp[k] = arr[j]
            k+=1
            j+=1
            inv_count+= (mid-i)
    while i<= (mid-1):
        temp[k] = arr[i]
        k+=1
        i+=1
    while j<= right:
        temp[k] = arr[j]
        k+=1
        j+=1
    for i in range(left, right+1):
        arr[i]=temp[i]
    return inv_count

def mergeSort(arr,temp,left,right):
    mid = 0
    inv_count = 0
    
    if right>left:
        mid = (left+right)//2
        inv_count += mergeSort(arr,temp,left,mid)
        inv_count += mergeSort(arr,temp,mid+1,right)
        inv_count += merge(arr,temp,left,mid+1,right)
    return inv_count

def getInversions(arr, n) :
    temp = [0]*n
    ans = mergeSort(arr,temp,0,n-1)
    return ans

# Taking inpit using fast I/O.
from sys import stdin
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))
