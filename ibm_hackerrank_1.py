# Reverse a part of an array given the start and end indices that the array should be flipped from.
# Ex. arr = [1, 3, 5, 6, 7, 9], flip = [1, 3] -> res = [1, 6, 5, 3, 7, 9]


def reverse_arr(arr, res) -> list[int]:
    l = res[0]
    r = res[1]
    left = arr[:l]
    right = arr[r + 1 :]
    rev = arr[l : r + 1][::-1]
    return left + rev + right


def main():
    test1 = ([1, 3, 5, 6, 7, 9], [1, 3])
    exp = [1, 6, 5, 3, 7, 9]
    res = reverse_arr(test1[0], test1[1])
    print(f"Expected: {exp}")
    print(f"Result: {res}")
    if res == exp:
        print("PASSED TEST 1")
    else:
        print("FAILED TEST 1")

    test2 = ([1, 3, 5, 6, 7, 9], [0, 5])
    exp = [9, 7, 6, 5, 3, 1]
    res = reverse_arr(test2[0], test2[1])
    print(f"Expected: {exp}")
    print(f"Result: {res}")
    if res == exp:
        print("PASSED TEST 2")
    else:
        print("FAILED TEST 2")

    test3 = ([1], [0, 0])
    exp = [1]
    res = reverse_arr(test3[0], test3[1])
    print(f"Expected: {exp}")
    print(f"Result: {res}")
    if res == exp:
        print("PASSED TEST 3")
    else:
        print("FAILED TEST 3")


if __name__ == "__main__":
    main()
