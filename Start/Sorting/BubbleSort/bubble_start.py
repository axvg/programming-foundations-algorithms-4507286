# Example file for Programming Foundations: Algorithms by Joe Marini
# Bubble sort algorithm


def bubbleSort(dataset):
    # TODO: start with the array length and decrement each time
    # for i in range(len(dataset) - 1, 0, -1):
    #     for j in range(i):
    #         if dataset[j] > dataset[j + 1]:
    #             dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]

    #     print("Current state: ", dataset)

    for numpass in range(len(dataset) -1, 0, -1):
        for i in range(numpass):
            if dataset[i] > dataset[i + 1]:
                dataset[i], dataset[i + 1] = dataset[i + 1], dataset[i]
        print("Current state: ", dataset)

    # exchanges = True
    # numpass = len(dataset) - 1

    # while exchanges and numpass > 0:
    #     exchanges = False
    #     for i in range(numpass):
    #         exchanges = True
    #         if dataset[i] > dataset[i + 1]:
    #             dataset[i], dataset[i + 1] = dataset[i + 1], dataset[i]
    #     # print("Current state: ", dataset)
    #     numpass -= 1

list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
print("Start: ", list1)
bubbleSort(list1)
print("Result: ", list1)
