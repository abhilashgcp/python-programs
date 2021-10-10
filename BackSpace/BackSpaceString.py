#Given two strings S and T return if they are equal #means Backspace in this string
def backSpaceString (s,t):
    i = 0
    while (i < len(s)):
        # Check whether the current character is # 
        if (s[i] == '#'):
            # If greater than 1 Merge Previous string and after strings
            if (i > 1):
                s = s[:i-1] + s[i+1:]
            else:
                # Merge the string after
                s = s[i+1:]
            if (i >= 1):
                #Reduce the i
                i -= 1
        else:
            i += 1

    i=0
    while (i < len(t)):
        if (t[i] == '#'):
            if (i > 1):
                t = t[:i-1] + t[i+1:]
            else:
                t = t[i+1:]
            if (i >= 1):
                i -= 1
        else:
            i += 1
    return s == t

# print (backSpaceString("#ab#cd", "#ad#cd" ))
# print (backSpaceString("#", "#" ))
# print (backSpaceString("#ab#cd", "#ad#ed" ))