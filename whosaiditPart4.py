"""
Tung Hoang - 11/28/19

This program prompts user to enter a text, which the program will take in and
analyze in order to determine id the text is written by Jane Austen or
William Shakespeare

"""
import math


# This function takes a word and a dictionary of word counts, and it generates
# a score that approximates the relevance of the word in the document from
# which the word counts were generated. The higher the score, the more
# relevant the word.
def get_score(word, counts):
    denominator = float(1 + counts["_total"])
    if word in counts:
        return math.log((1 + counts[word]) / denominator)
    else:
        return math.log(1 / denominator)

# This function takes a word and returns the same word with:
#   - All non-letters removed
#   - All letters converted to lowercase
def normalize(word):
    return "".join(letter for letter in word if letter.isalpha()).lower()


# This function takes a filename and generates a dictionary whose keys are
# the unique words in the file and whose values are the counts for those words.
def get_counts(filename):
    result_dict = {}
    total = 0

    file = open(filename)
    for line in file:
        line = line.strip()
        for word in line.split():
            word = normalize(word)
            if word in result_dict:
                if word == '':
                    continue
                result_dict [word] += 1
                total += 1
            else:
                result_dict[word] = 1
                total += 1

    result_dict["_total"] = total
    return result_dict

# This function takes in the  uset text sample and deconstruct it into words
# Each words is going to get compare with the dictionaries to predict who it
# is written by
def predict(user_text, shakespeare_counts, austen_counts):
    shakespeare_scores = 0
    austen_scores = 0
    
    user_text = user_text.strip()
    for word in user_text.split():
        word = normalize(word)
        if word == '':
            continue
        shakespeare_scores += get_score(word,shakespeare_counts)
        austen_scores += get_score(word,austen_counts)


    if shakespeare_scores > austen_scores:
        print ("I think that was written by William Shakespeare")
    else:
        print ("I think that was written by Jane Austen")


    
# Get the counts for both of the texts
shakespeare_counts = get_counts("hamlet.txt")
austen_counts = get_counts("pride-and-prejudice.txt")

# Get the user sample text and predict whether it is written by Jane Austen
# or William Shakespeare
user_text = input("Text sample: ")
predict(user_text, shakespeare_counts, austen_counts)
 
