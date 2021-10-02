def bubble_sort (lst):
    bubble_sort.num_pass = 0
    swapped = True
    for i in range(len(lst) - 1):
        swapped = False
        for j in range(len(lst) - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if swapped == False:
            break
        bubble_sort.num_pass = bubble_sort.num_pass + 1
        lst_str = [str(a) for a in lst]
        print ("Pass " + str(bubble_sort.num_pass)+ ": ", end='')
        print(",".join(lst_str))
    return lst


l = []
number = ""
while number != "exit":
    number = input("Enter a list of numbers separated by commas or type exit: ")
    if number.lower() == "exit":
        number = number.lower()
        print("Goodbye.")
#Check if the user input is valid
    else:
        try:
            for i in number.split(","):
                n = int(i)
                l.append(n)
        except ValueError:
            print("Non-numerical values entered, please try again.")
            continue

        oringinal_list_str = [str(a) for a in l]
        print("Oringinal List: " + ",".join(oringinal_list_str))
        sorted_lst = bubble_sort(l)
        sorted_list_str = [str(a) for a in sorted_lst]

        print("\n"+"Oringinal List: " + ",".join(oringinal_list_str))
        print("Sorted list: " + ",".join(sorted_list_str))
        print("Number of Passes: " + str(bubble_sort.num_pass))
