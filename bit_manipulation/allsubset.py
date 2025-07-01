arr = [1, 2, 3]
n = len(arr)

def subsets(arr,n):
    for mask in range(1<<n):
        ans = []
        for i in range(n):
            if (mask>>i)&1:
                ans.append(arr[i])
        print(ans)
        
subsets(arr,n)
        
