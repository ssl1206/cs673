arr1 = ["a","b","c","d"]
arr2 = [1,2,3,1,6,4]
arr = []

def combine_list(arr1, arr2):
    if len(arr1) >= len(arr2):
        for i in range(len(arr2)):
            arr.append(arr1[i])
            arr.append(arr2[i])
        for i in range(len(arr2),len(arr1)):
            arr.append(arr1[i])
    else:
        for i in range(len(arr1)):
            arr.append(arr1[i])
            arr.append(arr2[i])
        for i in range(len(arr1),len(arr2)):
            arr.append(arr2[i])
    return arr

print(combine_list(arr1,arr2))