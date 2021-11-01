def flatten(arr):
    """
    # avoid
    # base case
    # recursive
    """
    # avoid
    assert isinstance(arr, list)
    # base case
    print('-'*20,f"\ninput {arr} initialized\n", '-'*20)
    result_item = []
    for item in arr:
        print("processing item: ", item)
        print("item type: ", type(item))
        print("result before process: ", result_item)
        if isinstance(item, list):
            print("\nstart another recursion")
            result_item.extend(flatten(item))
            print('end one recursion loop\n')
        elif isinstance(item, int):
            result_item.append(item)
        print("result after process: ", result_item)
    return result_item


if __name__ == "__main__":
    test_case_1 = [1,2,3,[4,5]]
    test_case_2 = [1,[2,[3, 4, [[5]]]]]
    test_case_3 = [[1], [2], [3]]
    test_case_4 = [[[[1], [[[2]]], [[[[[[[3]]]]]]]]]]

    test_cases = [test_case_1, test_case_2 ,test_case_3, test_case_4]
    for test_case in test_cases:
        print("-"*20, '\n', "-"*20,"\ni'm going to start a new test_case\n")
        flatten(test_case)