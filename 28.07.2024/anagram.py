def anagram (col1,col2): 
    col1=col1.lower() 
    col2=col2.lower() 
    len(col1)==len(col2) 
    return sorted(col1)==sorted(col2) 
col1=input(" ") 
col2=input(" ") 
print(anagram(col1,col2)) 
