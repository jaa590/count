def CountWords(s):
    wlist = s.split()
    wtot = len(wlist)
    return wtot

print("Enter the String: ", end="")
text = input()

wordLen = CountWords(text)
print("\nNumber of Word(s):", wordLen)
