import json


def countWords_1(txtFile, resultFile):
    # Open file
    f = open(txtFile, "r")

    # Initialize result
    res = {}

    for x in f:
        # Split Space in Line
        line = x.split()
        for i in line:
            # Avoid string is empty
            if i != '':
                # Lower String
                s = i.lower()
                try:
                    # Increment count of word to 1
                    res[s] += 1
                # catch error when word not be exist
                except KeyError:
                    # This word has not been seen. Set their count to 1.
                    res[s] = 1

    with open(resultFile, "w") as outfile:
        json.dump(res, outfile)
    f.close()

# Call solve function 
countWords_1("sample1.txt", "sample_out_1.json")
