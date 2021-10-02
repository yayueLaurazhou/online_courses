def insertion_sort (lst):
    count_swap = 0
    for i in range(1,len(lst)):
#Select a nunmber in the list to be compared with and store the value in current_value
        current_value = lst[i]
#Compare current_value with each of the previous number in the list, and swap them if in the wrong order
        while i > 0 and lst[i-1]>current_value:
            lst[i] = lst[i-1]
            i = i-1
            lst[i] = current_value
            count_swap = count_swap + 1
            lst_str = [str(a) for a in lst]
            print ("Swap" + str(count_swap)+": " + ",".join(lst_str))
    return lst


def calculate_mean (lst):
    sum = 0
    for i in range(0, len(lst)):
        sum = sum + lst[i]
    mean = float(sum) / len(lst)
    return mean

number = ""
while number != "exit":
    number = input("Enter a list of numbers separated by commas or type exit: ")
    l = []
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
        sorted_list = insertion_sort(l)
        sorted_list_str = [str(a) for a in sorted_list]
        print("Sorted list: " + ','.join(sorted_list_str))
        print("Mean Value:" + str(calculate_mean(sorted_list)))
