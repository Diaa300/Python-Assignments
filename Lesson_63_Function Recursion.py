# ----------------------------------------------------------------
# -- Function Recursion --
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------

# Test Word [WWWWWWoooorrrlllddd] 

def cleanword(word):

    if len(word) == 1:

        return word

    if word[0] == word[1]:

        print(f'Print Before Condition {word}')

        return cleanword(word[1:]) 

    print(f'Print Before Return {word}')

    return word[0] + cleanword(word[1:])

    # Stash [  ]


print(cleanword("WWWWWWoooorrrlllddd"))