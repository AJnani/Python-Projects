
str1 = input("Give name1 : ") # Anagram :: strings contain same characters only order of
str2 = input("Give name2 : ") #              characters are different
                                                                       #Examples :: listen <> Silent
if len(str1) == len(str2):
    if sorted(str1) == sorted(str2):
        print("The Strings are Anagram!")
    else:
        print("OPPs! Strings are not Anagrams!")
else:
    print("OPPs! Lengths do not match!!")
    print("Check the Strings")                                 # Note : ****CASE SENSITIVE****
