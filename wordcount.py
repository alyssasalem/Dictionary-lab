"""Count words in file."""

import re

def word_count(filename):
    log_file = open(filename)
    
    counted = {}

    for line in log_file:
        line = line.rstrip()
        # line = line.split(" ")
        line = re.split(';|,|\*|\n|\.| |_|!|\?',line)

        for word in line:
            counted[word.lower()] = counted.get(word.lower(), 0) + 1
            
    
    log_file.close()
    return counted

# put your code here.

print(word_count("twain.txt"))
