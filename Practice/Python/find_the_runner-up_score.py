if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

#remove duplicates from the list
arr2 =list(set(arr))

#get the second highest value
x = sorted(arr2)[-2]
print(x)
