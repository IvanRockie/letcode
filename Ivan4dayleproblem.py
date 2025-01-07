 result = set()
        for i, word1 in enumerate(words,start = 1):
            for word2 in words[i:]:
                if word1 in word2:
                    result.add(word1)
                elif word2 in word1:
                    result.add(word2)    
        return list(result)
