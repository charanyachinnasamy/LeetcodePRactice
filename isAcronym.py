def isAcronym(words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        acronym = ""
        for word in words:
            acronym = acronym + word[0]
        if acronym == s:
            return True
        return False

print(isAcronym(["alice","bob","charlie"],"ab"))
