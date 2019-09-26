test_list = [0, 1, 2, 3, 4, 6, 7]


def return_missing_element():
    for index_test in test_list:
        any_element = test_list[index_test]
        print("any_element " + str(any_element) + " index_test " + str(index_test))
        if any_element != index_test:
            return index_test - 1


print("return_missing_element " + str(return_missing_element()))
