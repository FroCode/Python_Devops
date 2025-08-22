# Array if any item mtach the second array so its true
# ['a', 'b', 'c'] = ['a', 't', 'u'] => True [a] is existed in the second array
# 

def merge_sorted_arrays(arr1, arr2):
    result = []
    i, j = 0, 0
    
    # Compare elements from both arrays and add smaller one to result
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Add remaining elements from arr1, if any
    result.extend(arr1[i:])
    
    # Add remaining elements from arr2, if any
    result.extend(arr2[j:])
    
    return result

# Example usage
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

merged = merge_sorted_arrays(arr1, arr2)
print(merged)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
<<<<<<< HEAD
# this line added into the dev branch
=======
# This is an f5 feature edit
# this feature has been added from f6

# second commit f5
# second commit f99
# feature 7 added

>>>>>>> parent of b1e64c5 (F13 (#40))
