words=["hello","world","python"] 
for word in words: 
    vowel_count=0 
    for char in word: 
        if char.lower() in ['a','e','i','o','u']: 
            vowel_count=vowel_count+1 
            print(f"word:{word},vowelcount:{vowel_count}") 
