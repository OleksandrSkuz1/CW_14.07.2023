if __name__ == '__main__':
    # arr = ["test", "test2", "testR"]

    # for item in arr:
    #     print(item)

    # x = 0
    # while x < len.(arr):
    #     print(arr[x])
    #     count += 1

    # for i in range(1, 3):
    #  print(i)

    # numbers = []
    # for i in range(1, 101, 1):
    #    numbers.append(i)
    # print(numbers)
    #
    # even_numbers = []
    # odd_numbers = []
    # if i in numbers:
    #     if i% 2 == 0:
    #         even_numbers.append(i)
    #     else:
    #         odd_numbers.append(i)
    #
    #         print(even_numbers)
    #         print(odd_numbers)


    # # sort
    # arr = [4, 56, 2, 6, 3, 89]
    # flag = Truewhile flag:
    # flag = False
    # status_check = True
    # for i in range(len(arr) - 1):
    #     if arr[i] > arr[i + 1]:
    #         print(arr[i], " ", arr[i + 1])
    #         temp = arr[i]
    #         arr[i] = arr[i + 1]
    #         arr[i + 1] = temp
    #
    # print(arr)
    # for item in range(len(arr) - 1):
    #     print(arr[item], " CHECK  ", arr[item + 1])
    #     if arr[item] > arr[item + 1] and flag == False:
    #         flag = Trueprint(arr)


    # sort metod
    # ABS
    # new_val = sorted(arr)

    str_arr = ["John", "Any", "Cat", "Zak"]
    # _______A-Z
    sort_az_arr = sorted(str_arr)                   # список по алфавіту
    print(sort_az_arr)

    #________Z-A___
    sort_az_arr = sorted(str_arr, reverse=True)     #  зворотній список (reverse) 
    print(sort_az_arr)