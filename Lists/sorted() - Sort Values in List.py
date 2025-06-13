### sort(), sorted() - Sort Values in List ####

## sort() - Sorts values from least to greatest
nums = [12, 43, 21, 1]
nums.sort()
print("Sorted list using sort():", nums)
# Print largest value in list
print("Largest value in the list:", nums[-1])  # Output: 43
# Print smallest value in list
print("Smallest value in the list:", nums[0])  # Output: 1


## sorted() - Returns a new sorted list
# Original unsorted list
nums2 = [12, 43, 21, 1]
# Create new sorted list without modifying the original
sorted_nums = sorted(nums2)
print("Original list remains unchanged:", nums2)
print("Sorted list using sorted():", sorted_nums)
# Print largest value in sorted list
print("Largest value in the sorted list:", sorted_nums[-1])  # Output: 43
# Print smallest value in sorted list
print("Smallest value in the sorted list:", sorted_nums[0])  # Output: 1
