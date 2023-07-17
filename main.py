if __name__ == '__main__':
    # # створюємо масив
    # arr = ["test!", "test2", "testR"]
    #
    # # виводимо кожен елемент з нового рядка
    # for item in arr:    # item - ітератор
    #     print(item)
    # print(f"_________{arr[1]}_______\n")
    #
    # # варіант виводу за допомогою циклу while
    #
    # x = 0                   # лічильник
    # while x < len(arr):
    #      print(arr[x])
    #      x += 1
    #
    # #  варіант виводу за допомогою range
    #
    # for i in range(1, 3):
    #     print(arr[i])
    #
    # # інший варіант
    #
    # test = [x for x in arr if x == "test!"]
    # print(test)


    # СОРТУВАННЯ ТА ФІЛЬТРУВАННЯ

    # numbers = []                # створюємо корзину для зберігання е-ів
    # for i in range(1, 101, 1):  # створюємо список на сто елементів
    #     numbers.append(i)       # додаємо елемент до масиву
    # print(numbers)
    #
    # # фільтруємо масив на парні і не парні значення
    #
    #
    # even_numbers = []   # парні
    # odd_numbers = []    # не парні
    # for i in numbers:
    #     if i%2 == 0:                 # фільтруємо парні числа
    #         even_numbers.append(i)
    #     else:
    #         odd_numbers.append(i)
    # print(even_numbers)
    # print(odd_numbers)


    # СOРТУВАННЯ sort

    # arr = [4, 56, 2, 6, 3, 89]
    # arr_two = arr.copy()
    # flag = True
    # while flag:
    #     flag = False
    #     status_check = True
    #     for i in range(len(arr) - 1):
    #         if arr[i] > arr[i + 1]:
    #             # print(arr[i], " ", arr[i + 1])
    #             temp = arr[i]
    #             arr[i] = arr[i + 1]
    #             arr[i + 1] = temp
    #
    #     for item in range(len(arr) - 1):
    #         if arr[item] > arr[item + 1] and flag == False:
    #             flag = True

    # print(arr)


    # Sort methods
    # ABS
    new_val = sorted(arr_two)
    # print(arr_two)
    # print(new_val)

    arr_two.sort()
    # print(arr_two)
    # arr_two.sort()
    # DESC
    new_val_desc = sorted(arr_two, reverse=True)
    # print(new_val_desc)
    # print(arr_two)
    # print(arr_two[::-1])

    str_arr = ["MaryAnn", "MARRYANN", "Jonny", "Ann", "Ketty", "Zak"]
    #___ A-Z ___
    sort_az_arr = sorted(str_arr)
    print(sort_az_arr)
    # print(str_arr.sort())

    #___ Z-A ___
    sort_za_arr = sorted(str_arr, reverse=True)
    print(sort_za_arr)

    with open("products.json", 'r', encoding="utf-8") as file:
        products = json.load(file)

    products.sort(key=lambda product: product["price"])
    sorted_product = sorted(products, key=lambda product: product["price"], reverse=True)
    print(sorted_product)

    with open("products_az.json", "w", encoding="utf-8") as file:
        json.dump(products, file)

















































