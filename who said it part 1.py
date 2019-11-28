# normalize
# -----
# This function takes a word and returns the same word
# with:
#   - All non-letters removed
#   - All letters converted to lowercase
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()

# get_counts
# -----
# This function takes a filename and generates a dictionary
# whose keys are the unique words in the file and whose
# values are the counts for those words.
def get_counts(filename):
    result_dict = {}
    wordTotal = 0
    file = open(filename, "r")

    for i in file:
        i = i.split()
        for j in i:
            j = normalize(j)
            if j != "":
                if j in result_dict:
                    result_dict[j] = result_dict[j] + 1
                    wordTotal = wordTotal + 1
                else:
                    result_dict[j] = 1
                    wordTotal = wordTotal + 1
        result_dict["_total"] = wordTotal
    file.close()       
    return(result_dict)

# Get the counts for the two shortened versions
# of the texts
shakespeare_counts = get_counts("hamlet.txt")
austen_counts = get_counts("pride-and-prejudice.txt")

print(shakespeare_counts)
print(austen_counts)
# Check the contents of the dictionaries

print("-----")

