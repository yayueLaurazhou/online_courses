
def reverse(str):
    if len(str) == 1:
        return str
    else:
        return reverse(str[1:]) + str[0]

origninal_word = ""
while origninal_word != "exit":
    original_word  = input("Enter a word that you want to reverse or type exit: ")
    if original_word == "exit":
        print("Goodbye.")
        break
    elif isinstance(original_word, str) :
        reversed_word = reverse(original_word)
        print("Original Word:",original_word)
        print("Reversed Word:",reversed_word)
