# Write a Python program to find the longest common prefix of all strings. 
# Use the Python set.

def prefix(words):

    words = list(words)

    answer = ""

    for i in range(min(len(word) for word in words)):

        if len({word[i] for word in words}) == 1:
            answer += words[0][i]
        else:
            break

    print(answer)


words = {'interview' , 'internet' , 'internal'}

prefix(words)