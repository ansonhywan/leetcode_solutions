# Given a list of integers nums, and an integer num. 
# Find all instances of num in nums and move them to the center of the list keeping relative order of the other elements.

class solution:
    def move_to_center(nums: list[int], num: int) -> list[int]:
        # Similar to LeetCode 283 Move Zeroes, except we need to move to center not end.
        # Thus we can run that algorithm except twice. Once starting from beginning of list and once starting at the end.

        l = 0
        for r in range(1, (len(nums) // 2)+1):
            if nums[l] == num and nums[r] != num:
                # Swap
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                l += 1
            if nums[l] != num:
                l += 1

        l = len(nums) - 1
        for r in range(l - 1, (len(nums) // 2)-1, -1):
            if nums[l] == num and nums[r] != num:
                # Swap
                temp = nums[r]
                nums[r] = nums[l]
                nums[l] = temp
                l -= 1
            if nums[l] != num:
                l -= 1
        
        return nums


def main():
    test1 = ([1,2,2,45,6,7,9,88,2], 2)
    print(test1[0])
    res_test1 = solution.move_to_center(test1[0],test1[1])
    print(res_test1)

    test2 = ([1,3,5,45,6,2,9,88,2], 2)
    print(test2[0])
    res_test2 = solution.move_to_center(test2[0],test2[1])
    print(res_test2)

    test3 = ([0], 0)
    print(test3[0])
    res_test3 = solution.move_to_center(test3[0],test3[1])
    print(res_test3)

    test4 = ([0], 1)
    print(test4[0])
    res_test4 = solution.move_to_center(test4[0],test4[1])
    print(res_test4)

    test5 = ([23, 69, 6, 7, 8], 23)
    print(test5[0])
    res_test5 = solution.move_to_center(test5[0],test5[1])
    print(res_test5)

if __name__ == "__main__":
    main()