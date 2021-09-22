import re 
version='1.0.3'
print(f'v {version}')

#Determine the theme
Theme = input('Theme Dark(D)/Light(l) - Default is light:\n')

# Define the syntax separators 
separators = [',','(','[',']',')','{','}','/','*','+','-','.','|',':',';','⋞','⋟','=']

# Create a splitting function that takes a list of separators
# Code courtesy of DelftStack: https://www.delftstack.com/howto/python/how-to-split-string-with-multiple-delimiters-in-python/#make-it-a-function - I edited it some though
def custom_split(sepr_list, str_to_split):
    # Duplicate and sort the separator list
    sepr_list2 = list(sepr_list)
    sepr_list2.sort(key=len,reverse=True)
    # create regular expression dynamically
    regular_exp = '|'.join(map(re.escape, sepr_list2))
    # Return the list of splits
    return re.split(regular_exp, str_to_split)

# create a list of instances that would set off a string with single quotes
str1 = ['\'', 'f\'','u\'','b\'','r\'','\'\'\'']
# create a list of instances that would set off a string with double quotes
str2 = ['"', 'r"','f"','u"','b"','"""']

# Define the highlight colors in Hexadecimal
if Theme.upper() != 'Dark' and Theme.upper() != 'D':
    Border = '#eeeeee'
    if input('Pure white? (y/n) (default: N)').upper() != 'Y':
        Background = '#fbfcfc'
    else:
        Background = '#ffffff'
    Foreground = '#000000'
    Red = '#ff0000'
    Green = '#00aa00'
    Orange = '#ff7700'
    Purple = '#900090'
    Blue = '#0000ff'
else:
    Border = '#aaaaaa'
    Background = '#222222'
    Foreground = '#dddddd'
    Red = '#ff3333'
    Green = '#00ff00'
    Orange = '#ffaa22'
    Purple = '##ff40c0'
    Blue = '#00ccff'


#Create a dictionary with keywords and the like
Colors = {
    #Red : ['#','##'],
    #Green : ['\'', '"','f\'','u\'','b\'','r\'','r"','f"','u"','b"'],
    Orange : ['import', 'from', 'as','class', 'def','return','else','if','elif','for','in','and','True','False','or','not','is','while','try', 'except', 'raise','None','del'],
    Purple : ['ValueError', 'ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError',
                'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception',
                'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError',
                'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', ' LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'NotADirectoryError', 'NotImplemented',
                'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'ReferenceError', 'RecursionError', 'ResourceWarning',
                'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SystemError', 'SyntaxError', 'SyntaxWarning', 'SystemExit', 'TabError', 'TimeoutError', 'TypeError',
                'UnicodeDecodeError', 'UnboundLocalError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError',
                'ZeroDivisionError', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr',
                'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int',
                'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'range',
                'repr', 'reversed', 'round', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
        }

# Create a dictionary with syntax ends - blank for continuous highlighting
ends = {
    Red: '',
    Green: '',
    Orange: '</span>',
    Purple: '</span>'
        }


# Create a dictionary with string to be replaced
Replacers = {
##             '\n\'':'\\n\'',
##             '\'\n':'\'\\n',
##             '\n"':'\\n"',
##             '"\n':'"\\n',
             '<':'&#60;',
             '>':'&#62;',
             '<p>':'',
             '</p>':' <br> ',
             '\n':' <br> '}




# Print a warning statement
print('''
-----------------------------------------------------------------------------------------------
===============================================================================================
###############################################################################################

Warning! Formatting issues may arise from using a python escape character like: "\\n", (a list
of these can be found at: https://www.w3schools.com/python/gloss_python_escape_characters.asp),
to fix this please replace the backslash part with two backslashes, for instance: "\\\\n".
Aditionally, this program may not work for syntax highlighting every program. By using this,
you take on the responsibility to ensure that the highlighting is accurate.

###############################################################################################
===============================================================================================
-----------------------------------------------------------------------------------------------''')
def html_NoColor(code,inline = False):
    # Create a copy of code
    rawcode = code
    if rawcode[-6:]!=' <br> ':
        rawcode+=' <br> '
    # Loop through the replacements
    for item in Replacers:
        # and replace
        rawcode = rawcode.replace(item,Replacers[item])
    ###### Finish Format ######
    # Replace the quotation and less/greater than string subsitution and tabs
    rawcode = rawcode.replace('“','"').replace('”','"').replace('⋞','&#60;').replace('⋟','&#62;').replace('\t','&nbsp;'*3).replace('    ','&nbsp;'*4)
    # remove the last six characters
    rawcode=rawcode[:-14]
    # Complete the formatting
    if inline == True:
        code = f'<tt style="font-size:90%; border: 2px solid {Border}; padding: 3px; background-color:{Background}; color:{Foreground};">{rawcode}</tt> &nbsp;'
    else:
        code = f'<p> </p><p style="font-size:90%; border: 2px solid {Border}; padding: 10px; background-color:{Background}; color:{Foreground};"><tt>{rawcode}</tt></p><p> &nbsp;</p>'
    # Print the code
    print(code)

# Head the function htmlCode
def htmlCode(code,inline = False):
    # Create a copy of code
    rawcode = code
    # Loop through the replacements
    for item in Replacers:
        # and replace
        rawcode = rawcode.replace(item,Replacers[item])
    # Create an empty highlighted code string
    HighlightedCode = ''

    # If the code does not end in a new line, make it    
    if rawcode[-6:]!=' <br> ':
        rawcode+=' <br> '

    # Split the code with spaces to get a rough syntax separation
    words = rawcode.split(' ')

    # Set continuous highlighting booleans
    InComment = False
    InStringType1 = False
    InStringType1_3 = False
    InStringType2 = False
    InStringType2_3 = False
    InDef_Class = False

    #access the global separators variable
    global separators

    # loop through the rough words
    for WORD in words:
        # Create an empty word
        MYWORD = ''
        # Split the word more completely
        code_words = custom_split(separators,WORD)
        # Filter out empty string
        code_words = list(filter(None, code_words))
        # Create a reinfusement map
        heal_code = custom_split(list(filter(None, code_words)),WORD)
        # Create a list for the code
        Broken_Code = []

        # Loop through the refined syntax
        for word in code_words:
            # create an appendWord variable with a default of word
            appendWord = word

            # If we are in a comment
            if InComment:
                # If we are at the end of the line
                if word == '<br>':
                    # End the comment
                    appendWord = '</span>'+word
                    # Terminate the comment section
                    InComment = False
                    
            # Otherwise, if we are in a single quote string
            elif InStringType1:
                # If there is a single quote within our refined syntax
                if word.find('\'') != -1:
                    # End the string
                    appendWord = word.replace('\'','\'</span>')
                    # Terminate the single quote string section
                    InStringType1 = False

            # Otherwise, if we are in a triple single quote string        
            elif InStringType1_3:
                # If there is a triple single quote within our refined syntax
                if word.find('\'\'\'') != -1:
                    # End the string
                    appendWord = word.replace('\'\'\'','\'\'\'</span>')
                    # Terminate the triple single quote string section
                    InStringType1_3 = False
                    
            # Otherwise, if we are in a double quote string       
            elif InStringType2:
                # If there is a double quote within our refined syntax
                if word.find('"') != -1:
                    # End the string
                    appendWord = word.replace('"','"</span>')
                    # Terminate the double quote string section
                    InStringType2 = False
                    
            # Otherwise, if we are in a triple double quote string       
            elif InStringType2_3:
                # If there is a triple double quote within our refined syntax
                if word.find('"""') != -1:
                    # End the string
                    appendWord = word.replace('"""','"""</span>')
                    # Terminate the triple double quote string section
                    InStringType2_3 = False
                    
            # Lastly, if we are in the heading of a function or a class
            elif InDef_Class:
                # Make the word blue
                appendWord = f'<span style=“color:{Blue}”>'+word+'</span>'
                # Terminate the function or a class heading section
                InDef_Class = False

            #Otherwise
            else:
                # If the word is not blank
                if word != '':
                    # loop through the colors
                    for color in Colors:
                        # if the word is in the color
                        if word in Colors[color]:
                            # Make the word the color it should be
                            appendWord = (f'<span style=“color:{color}”>'+word+ends[color]
                                          )
                    # Set the first letter of the word
                    primary = word[0]
                    # get the first two and three letters of the word if it is multiple letters long
                    try: secondary = word[:2]
                    except: secondary = primary
                    
                    try: tertiary = word[:3]
                    except: tertiary = secondary
                    
                    # If the first three letters are triple single quote string beginings        
                    if tertiary == '\'\'\'':
                        appendWord = (f'<span style=“color:{Green}”>'+word)
                        InStringType1_3 = True
                        
                    # Otherwise, if the first one or two letters are single quote string beginings 
                    elif primary == '\'' or secondary in str1:
                        # if the word sets off a string or end with a string begining or the ending is not a string ending
                        if len(word) == 1 or secondary in str1 or word[-1] !='\'':
                            # Start the string section
                            InStringType1 = True
                            # Color the word an indefinite green
                            appendWord = (f'<span style=“color:{Green}”>'+word)
                        # Otherwise
                        else:
                            #Start and end the string on the word
                            appendWord = (f'<span style=“color:{Green}”>'+word+'</span>')
                            
                    # Otherwise, if the first three letters are triple double quote string beginings        
                    elif tertiary == '"""':
                        appendWord = (f'<span style=“color:{Green}”>'+word)
                        InStringType2_3 = True
                        
                    # Otherwise, if the first one or two letters are single quote string beginings
                    elif primary == '"' or secondary in str2:
                        # if the word sets off a string or end with a string begining or the ending is not a string ending
                        if len(word) <= 1 or word[-1] !='"' or secondary in str2:
                            # Start the string section
                            InStringType2 = True
                            # Color the word an indefinite green
                            appendWord = (f'<span style=“color:{Green}”>'+word)
                        # Otherwise
                        else:
                            #Start and end the string on the word
                            appendWord = (f'<span style=“color:{Green}”>'+word+'</span>')
                    
                    # Otherwise, if the word sets off a commetn                    
                    elif primary == '#':
                        # Color the word an indefinite red
                        appendWord = (f'<span style=“color:{Red}”>'+word)
                        # Start off the comment section
                        InComment = True
                        
                    # Otherwise, if the word was def or class
                    elif word == 'def' or word == 'class' :
                        # Start the def/class head section
                        InDef_Class = True
                        
            # Append the higlighted syntax
            Broken_Code.append(appendWord)
            
        ############ reinfuse the subtracted string ##############
        # prepare the heal_code list and the broken_code list
        heal_code = list(filter(None, heal_code))
        heal_code.append('')
        while len(Broken_Code)< len(heal_code):
            Broken_Code.append('')
            
        # Loop through the items in the heal_code list
        for i in range(len(heal_code)):
            try:
                # Reinfuse the subtracted characters
                MYWORD +=Broken_Code[i]+heal_code[i]
            # if it rasies an error
            except:
                # Help the debugging
                print('An ERROR is being raised!')
                print(WORD)
                print(heal_code, f'len: {len(heal_code)}')
                print(Broken_Code, f'len: {len(Broken_Code)}')
                # raise the error
                MYWORD +=Broken_Code[i]+heal_code[i]
                
        # Append the word to the highlighted code
        HighlightedCode += MYWORD+' '

    ###### Finish Format ######
    # Replace the quotation and less/greater than string subsitution and tabs
    HighlightedCode = HighlightedCode.replace('“','"').replace('”','"').replace('⋞','&#60;').replace('⋟','&#62;').replace('\t','&nbsp;'*3).replace('    ','&nbsp;'*4)
    # remove the last six characters
    HighlightedCode=HighlightedCode[:-6]
    # Complete the formatting
    if inline == True:
        code = f'<tt style="font-size:90%; border: 2px solid {Border}; padding: 3px; background-color:{Background}; color:{Foreground};">{HighlightedCode}</tt> &nbsp;'
    else:
        code = f'<p> </p><p style="font-size:90%; border: 2px solid {Border}; padding: 10px; background-color:{Background}; color:{Foreground};"><tt>{HighlightedCode}</tt></p><p> &nbsp;</p>'
    # Print the code
    print(code)


#htmlCode(input('Code Here:'))

print('\n\nInitiate using the "htmlCode" function\n>>> htmlCode(\'\'\'CODE GOES HERE\'\'\') or >>> htmlCode(\'\'\'CODE GOES HERE\'\'\', inline = True)\nPlease use triple quotes for multiline code\n'+'-'*30+'\n')

