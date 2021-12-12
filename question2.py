import json
import math

def countWords_2(txtFile, resultFile):
    # Open file
    file = open(txtFile, "r")

    # Initialize result
    count = {}

    # words contains unique word in file
    words = []

    # Sum of words in file
    sumOfWords = 0

    for x in file:
        # Split Space in Line
        line = x.split()
        for i in line:
            # Avoid string is empty
            if i != '':
                # Lower string
                s = i.lower()

                # Add word into words
                if s not in words:
                    words.append(s)
                # Increment sum to 1
                sumOfWords += 1
                # Lower String

                try:
                    # Increment count of word to 1
                    count[s] += 1
                # catch error when word not be exist
                except KeyError:
                    # This word has not been seen. Set their count to 1.
                    count[s] = 1
    # sort by count of word
    words = sorted(words, key=lambda x: count[x], reverse=True)
    res = {}
    for word in words:
        res[word] = round(count[word] / sumOfWords * 100, 2)

    # Write json to File
    with open(resultFile, "w") as outfile:
        json.dump(res, outfile)
    file.close()


countWords_2("sample.txt", "sample_out_1.json")
