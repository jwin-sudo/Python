unsorted_list = [101, 49, 3, 12, 56]


def bubblesort(the_list):
    high_idx = len(the_list) - 1

    for i in range(high_idx):
        list_change = False
        for j in range(high_idx):
            item = the_list[j]
            next = the_list[j+1]

            if item > next:
                the_list[j] = next
                the_list[j+1] = item
                list_change = True

            print(the_list, i, j)
        print(list_change)
        if list_change == False:
            break


bubblesort(unsorted_list)
