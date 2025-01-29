# WAF to find in which line of the file does the word "learning"occur first.
# rint -1 if word not found.

def find_word_line(word):
    data=True
    line=1
    with open("demo.txt","r") as f:
        while data:
            data=f.readline()
            if word in data:
                return line
            line+=1
        return -1


print(find_word_line("file"))