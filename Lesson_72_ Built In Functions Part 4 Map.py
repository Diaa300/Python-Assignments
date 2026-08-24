# --------------------------------
# --  Built In Functions => Map --
# --------------------------------
# [1] Map Take A Function + Iterator
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function Or Lambda Function
# ---------------------------------------------------------------

# Use Map With Predefined Function

def formatTexe(text) :

    return f'- {text.strip().capitalize()} -'

myTexts = ['dIaa', '  KAdRe   ', 'aHmEd  ']

# myFormatData = map(formatTexe, myTexts)

# print(myFormatData)

for name in map(formatTexe, myTexts):

    print(name)

print('=' * 50)

# Use Map With Lambda Function

    # def formatTexe(text) :

    #     return f'- {text.strip().capitalize()} -'

myTexts = ['dIaa', '  KAdRe   ', 'aHmEd  ']

for name in map(lambda text: f'- {text.strip().capitalize()} -', myTexts):

    print(name) 

