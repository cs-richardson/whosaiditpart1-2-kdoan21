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
    wordTotal = ""
    file = open(filename, "r")

    for i in file:
        i = i.split()
        for j in i:
            j = normalize(j)
            if j != "":
                result_dict[word]
                result_dict.append(j)
    close(filename)        
    return(result_dict)

# Get the counts for the two shortened versions
# of the texts
shakespeare_counts = get_counts("hamlet.txt")
austen_counts = get_counts("pride_and_prejudice.txt")

print(shakespeare_counts)
print(austen_counts)
# Check the contents of the dictionaries
for key in shakespeare_counts:
    print(key + ": " + str(shakespeare_counts[key]))

print("-----")

for key in austen_counts:
