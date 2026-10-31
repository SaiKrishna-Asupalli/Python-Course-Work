s="sai krishna reddy"
words=s.split()
rev_words=""
for i in range(len(words)-1,-1,-1):
    rev_words+=words[i] + " "

print(rev_words)