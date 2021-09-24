import re
import os

# Set the default input termination code
DEFAULT_INPUT_TERMINATION_CODE = '--Terminate--'

version='1.1.0'
print(f'v {version}')

# Define the default colors
Border = '#eeeeee'
Background = '#ffffff'
Foreground = '#000000'
Comment = '#DD0000'
String = '#00aa00'
Keywords = '#ff7700'
Builtins = '#900090'
Definitions = '#0000ff'


lThemes = {'Python Default':{
                'Border':'#eeeeee',
                'Background':'#ffffff',
                'Foreground':'#000000',
                'Comment':'#DD0000',
                'String':'#00aa00',
                'Keywords':'#ff7700',
                'Builtins':'#900090',
                'Definitions':'#0000ff'
                },
           'Python Default Grey':{
                'Border':'#eeeeee', 
                'Background':'#fbfcfc',
                'Foreground':'#000000',
                'Comment':'#DD0000',
                'String':'#00aa00',
                'Keywords':'#ff7700',
                'Builtins':'#900090',
                'Definitions':'#0000ff'
                },
           'Royal Blue':{
                'Border':'#eeeeee',
                'Background':'#ffffff',
                'Foreground':'#000000',
                'Comment':'#00aa00',
                'String':'#DD0000',
                'Keywords':'#0000ff',
                'Builtins':'#000099',
                'Definitions':'#493878'
                },
           'Sea':{
                'Border':'#ddddee',
                'Background':'#ffffff',
                'Foreground':'#000000',
                'Comment':'#445a71',
                'String':'#229922',
                'Keywords':'#0077aa',
                'Builtins':'#D86149',
                'Definitions':'#04B7BD'
                },
           'Red':{
                'Border':'#ffeeee',
                'Background':'#ffffff',
                'Foreground':'#000000',
                'Comment':'#445a71',
                'String':'#22863A',
                'Keywords':'#D73A49',
                'Builtins':'#6F42C1',
                'Definitions':'#AB0112'
                },
           'Grey':{
                'Border':'#cccccc',
                'Background':'#eeeeee',
                'Foreground':'#7B776F',
                'Comment':'#445a71',
                'String':'#C05726',
                'Keywords':'#3080B5',
                'Builtins':'#C05726',
                'Definitions':'#ff7700'
                }
    }
dThemes = {'Default Dark':{
                'Border':'#aaaaaa',
                'Background':'#222222',
                'Foreground':'#dddddd',
                'Comment':'#ff3333',
                'String':'#00ff00',
                'Keywords':'#ffaa22',
                'Builtins':'#ff40c0',
                'Definitions':'#00ccff'
                },
           'Rainglow':{
                'Border':'#aaaaaa',
                'Background':'#040507',
                'Foreground':'#ffffff',
                'Comment':'#6f809f',
                'String':'#64aeb3',
                'Keywords':'#508aaa',
                'Builtins':'#6ab0a3',
                'Definitions':'#00838C'
                },
           'Dark+':{
                'Border':'#aaaaaa',
                'Background':'#1e1e1e',
                'Foreground':'#D4D4D4',
                'Comment':'#6A9955',
                'String':'#CE9178',
                'Keywords':'#569CD6',
                'Builtins':'#dcdcaa',
                'Definitions':'#9CDCFE'
                },
           'Citylights':{
                'Border':'#718CA1',
                'Background':'#1d252c',
                'Foreground':'#718CA1',
                'Comment':'#72899e',
                'String':'#68A1F0',
                'Keywords':'#508aaa',
                'Builtins':'#70E1E8',
                'Definitions':'#24A5AF'
                },
           'Panda':{
                'Border':'#676B79',
                'Background':'#292a2b',
                'Foreground':'#E6E6E6',
                'Comment':'#737787',
                'String':'#19F9D8',
                'Keywords':'#FF75B5',
                'Builtins':'#6FC1FF',
                'Definitions':'#FF9AC1'
                },
           'Rose':{
                'Border':'#F37AB0',
                'Background':'#141322',
                'Foreground':'#B4DAE9',
                'Comment':'#45898C',
                'String':'#C01B5D',
                'Keywords':'#FB4293',
                'Builtins':'#F37AB0',
                'Definitions':'#8CE1E7'
                },
           'Sea Green':{
                'Border':'#546E7A',
                'Background':'#0a1018',
                'Foreground':'#EEFFFF',
                'Comment':'#708394',
                'String':'#28735E',
                'Keywords':'#25A2A6',
                'Builtins':'#5CB4DE',
                'Definitions':'#4785bd'
                },
           'Firefly':{
                'Border':'#626a73',
                'Background':'#0a0a0a',
                'Foreground':'#a8aebd',
                'Comment':'#626a73',
                'String':'#a4bd00',
                'Keywords':'#ff0066',
                'Builtins':'#ff8533',
                'Definitions':'#827db5'
                },
           'Monikai':{
                'Border':'#5C6370',
                'Background':'#121212',
                'Foreground':'#BBBBBBFF',
                'Comment':'#5C6370',
                'String':'#E5C07B',
                'Keywords':'#56B6C2',
                'Builtins':'#E06C75',
                'Definitions':'#98C379'
                },
           'Black Ocean':{
                'Border':'#60778c',
                'Background':'#101316',
                'Foreground':'#DFDFDF',
                'Comment':'#60778c',
                'String':'#7ebea0',
                'Keywords':'#007aae',
                'Builtins':'#019d76',
                'Definitions':'#15b8ae'
                },
           'CodePen':{
                'Border':'#5C6370',
                'Background':'#1e1f27',
                'Foreground':'#D5D7DE',
                'Comment':'#88AFBF',
                'String':'#2BC7B9',
                'Keywords':'#47CF73',
                'Builtins':'#5E91F2',
                'Definitions':'#9CA0B1'
                },
           'Acme':{
                'Border':'#988e86',
                'Background':'#0f0e0d',
                'Foreground':'#EDEBE6',
                'Comment':'#988e86',
                'String':'#E0A84C',
                'Keywords':'#CF433E',
                'Builtins':'#CD122C',
                'Definitions':'#d96972'
                },
           'Arc':{
                'Border':'#aaaaaa',
                'Background':'#111111',
                'Foreground':'#EDEBE6',
                'Comment':'#757575',
                'String':'#ff1ba9',
                'Keywords':'#f28888',
                'Builtins':'#a80000',
                'Definitions':'#A5E3D0'
                }
    }


    
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


def Input(prompt=None,ml = False,Terminate=DEFAULT_INPUT_TERMINATION_CODE):
    contents = input(prompt)
    while ml:
        try:
            line = input()
            if line == Terminate:
                break
            contents+='\n'+line
        except EOFError:
            break
    #contents+='\n'+line
    return contents

    

# create a list of instances that would set off a string with single quotes
str1 = ['\'', 'f\'','u\'','b\'','r\'','\'\'\'']
# create a list of instances that would set off a string with double quotes
str2 = ['"', 'r"','f"','u"','b"','"""']

#Create a dictionary with keywords and the like
Colors = {
    #Comment : ['#','##'],
    #String : ['\'', '"','f\'','u\'','b\'','r\'','r"','f"','u"','b"'],
    'Keywords' : ['and','as','assert','break','class','continue','def','del','elif','else','except','False','finally','for','from','global','if','import','in','is','lambda','None','nonlocal',
                'not','or','pass','raise','return','True','try','while','with','yield'],
    'Builtins' : ['ValueError', 'ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError',
                'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception',
                'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError',
                'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'NotADirectoryError', 'NotImplemented',
                'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'ReferenceError', 'RecursionError', 'ResourceWarning',
                'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SystemError', 'SyntaxError', 'SyntaxWarning', 'SystemExit', 'TabError', 'TimeoutError', 'TypeError',
                'UnicodeDecodeError', 'UnboundLocalError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError',
                'ZeroDivisionError', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr',
                'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int',
                'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property','quit', 'range',
                'repr', 'reversed', 'round', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
        }

# Create a dictionary with syntax ends - blank for continuous highlighting
ends = {
    'Comment': '', 
    'String': '',
    'Keywords': '</span>',
    'Builtins': '</span>'
        }


# Create a dictionary with string to be replaced
Replacers = {'<':'⋞',
             '>':'⋟',
             '<p>':'',
             '</p>':' <br> ',
             '\n':' <br> '}




ColorToType = {
        "Border" : Border,
        "Background" : Background,
        "Foreground" : Foreground,
        "Comment" : Comment,
        "String" : String,
        "Keywords" : Keywords,
        "Builtins" : Builtins,
        "Definitions" : Definitions
    }



# Create A Theme setter
def setColorScheme(Color):
    try:
        Color = int(Color)
    except:
        pass
    try:
        if type(Color) == type(2):
            theme = Themes[list(Themes)[Color-1]]
        else:
            theme = Themes[Color]
        global Border, Background, Foreground, Comment, String, Keywords, Builtins, Definitions, Colors, ends
        Border = theme['Border']
        Background = theme['Background']
        Foreground = theme['Foreground']
        Comment = theme['Comment']
        String = theme['String']
        Keywords = theme['Keywords']
        Builtins = theme['Builtins']
        Definitions = theme['Definitions']
                
    except:
        print('Invalid Theme')

#Determine the theme
Themes = {}
def ThemePrompt():
    global Themes
    Themes = {}
    print('Light themes')
    ltNames = list(lThemes)
    ltVals = list(lThemes.values())
    dtNames = list(dThemes)
    dtVals = list(dThemes.values())
    for theme in range(len(lThemes)+len(dThemes)):
        if theme  == len(lThemes):
            print('Dark themes:')
        if theme < len(lThemes):
            print('  ', str(theme+1)+'.',ltNames[theme])
            Themes[ltNames[theme]] = ltVals[theme]
        else:
            print('  ', str(theme+1)+'.',dtNames[theme-(len(lThemes))])
            Themes[dtNames[theme-(len(lThemes))]] = dtVals[theme-(len(lThemes))]
    Color = input('\n- a display of all of the themes can be shown by the command: ThemeDisplay()\nWhich theme should we use?')
    if Color.find('ThemeDisplay') != -1:
        ThemeDisplay()
        ThemePrompt()
    else:
        setColorScheme(Color)
ThemePrompt()










# Print a warning statement
print(f'''
-----------------------------------------------------------------------------------------------
===============================================================================================
###############################################################################################

Warning! Formatting issues may arise from using a python escape character like: "\\n", (a list
of these can be found at: https://www.w3schools.com/python/gloss_python_escape_characters.asp),
to fix this please replace the backslash part with two backslashes, for instance: "\\\\n".
Another method of solving this is to use the HighlightCode() function which takes a multiline
input of your code, terminated by the termination code: {DEFAULT_INPUT_TERMINATION_CODE}
Lastly, this program may not work for syntax highlighting every program. By using this,
you take on the responsibility to ensure that the highlighting is accurate.

###############################################################################################
===============================================================================================
-----------------------------------------------------------------------------------------------''')



def Preview(code):
    import datetime
    import webbrowser
    Path = os.path.join(os.path.expanduser('~'),'Downloads','Html - CodeSnippets')
    if not os.path.exists(Path):
        os.makedirs(Path)
    Name = ('Code Snippet.html')# - '+str(datetime.datetime.now())[:-10].replace(':','.')+'.html')
    fn = os.path.join(Path,Name)
    f = open(fn, 'w+', errors='replace')
    f.write(code)
    f.close()
    webbrowser.open_new(fn)




    """
        /‾/   /‾/‾‾‾‾‾‾‾‾/‾| /‾|  /‾/
       / /___/ /‾‾‾/ /‾‾/  |/  | / /
      / ___   /   / /  / | | / |/ /
     / /   / /   / /  / /|__/| | /____
    /_/   /_/   /_/  /_/     |_|_____/
    |‾\|‾|/‾‾\   /‾‾‾‾/‾‾\|‾|  /‾‾\|‾‾‾\
    |  \ | /\ | | /‾‾| /\ | | | /\ | <> |
    | \  | \/ | | \__| \/ | |_| \/ |   <
    |_|\_|\__/   \____\__/|____\__/|_|\_\
    """

# Head the function html_NoColor
def html_NoColor(code,inline = False):
    """.|‾\|‾|/‾‾\   /‾‾‾‾/‾‾\|‾|  /‾‾\|‾‾‾\ .
       .|  \ | /\ | | /‾‾| /\ | | | /\ | <> |.
       .| \  | \/ | | \__| \/ | |_| \/ |   < .
       .|_|\_|\__/   \____\__/|____\__/|_|\_\.
    """
    
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




'''
    /‾/   /‾/‾‾‾‾‾‾‾‾/‾| /‾|  /‾/
   / /___/ /‾‾‾/ /‾‾/  |/  | / /
  / ___   /   / /  / | | / |/ /
 / /   / /   / /  / /|__/| | /____
/_/   /_/   /_/  /_/_____|_|_____/
 /‾‾‾‾‾‾/‾‾‾‾‾\|‾‾‾‾‾\ |  _____|
|  /‾‾‾|  /‾\  | |‾\  \| |___
| |    | |   | | |  |  |  ___|
|  \___|  \_/  | |_/  /| |_____
 \______\_____/|_____/ |_______|
'''


# Head the function htmlCode
def html_code(code,inline = False, Return = False, color = False):
    if color != False:
        setColorScheme(color)
    global ColorToType
    ColorToType = {
        "Border" : Border,
        "Background" : Background,
        "Foreground" : Foreground,
        "Comment" : Comment,
        "String" : String,
        "Keywords" : Keywords,
        "Builtins" : Builtins,
        "Definitions" : Definitions
    }
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
                #print('-',word,'if', word.find('\'') != -1, "and(", word.find('\\\'')!=(word.find('\'')-1), "or", word.find('\\\'') ==-1,')')
                #print()
                if word.find('\'') != -1 and (word.find('\\\'')!=(word.find('\'')-1) or word.find('\\\'') ==-1):
                    # End the string
                    appendWord = word.replace('\'','\'</span>')
                    # Terminate the single quote string section
                    InStringType1 = False

            # Otherwise, if we are in a triple single quote string
            elif InStringType1_3:
                # If there is a triple single quote within our refined syntax
                if word.find('\'\'\'') != -1 and (word.find('\\\'\'\'')!=(word.find('\'\'\'')-1) or word.find('\\\'\'\'') ==-1):
                    # End the string
                    appendWord = word.replace('\'\'\'','\'\'\'</span>')
                    # Terminate the triple single quote string section
                    InStringType1_3 = False

            # Otherwise, if we are in a double quote string
            elif InStringType2:
                # If there is a double quote within our refined syntax
                if word.find('"') != -1 and (word.find('\\"')!=(word.find('"')-1) or word.find('\\"') ==-1):
                    # End the string
                    appendWord = word.replace('"','"</span>')
                    # Terminate the double quote string section
                    InStringType2 = False

            # Otherwise, if we are in a triple double quote string
            elif InStringType2_3:
                # If there is a triple double quote within our refined syntax
                if word.find('"""') != -1 and ( word.find('\\"""')!=(word.find('"""')-1) or word.find('\\"""') ==-1):
                    # End the string
                    appendWord = word.replace('"""','"""</span>')
                    # Terminate the triple double quote string section
                    InStringType2_3 = False

            # Lastly, if we are in the heading of a function or a class
            elif InDef_Class:
                # Make the word blue
                appendWord = f'<span style=“color:{Definitions}”>'+word+'</span>'
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
                            clr = ColorToType[color]
                            appendWord = (f'<span style=“color:{clr}”>'+word+ends[color])
                    # Set the first letter of the word
                    primary = word[0]
                    # get the first two and three letters of the word if it is multiple letters long
                    try:
                        secondary = word[:2]
                        secEnd = word[-2:]
                
                    except:
                        secondary = primary
                        secEnd = word[-1:]

                    try: tertiary = word[:3]
                    except: tertiary = secondary

                    # If the first three letters are triple single quote string beginings
                    if tertiary == '\'\'\'':
                        appendWord = (f'<span style=“color:{String}”>'+word)
                        InStringType1_3 = True

                    # Otherwise, if the first one or two letters are single quote string beginings
                    elif primary == '\'' or secondary in str1:
                        # if the word sets off a string or end with a string begining or the ending is not a string ending                        
                        if len(word) == 1 or secondary in str1 or (word[-1] !='\'' or secEnd =='\\\''):
                            # Start the string section
                            InStringType1 = True
                            # Color the word an indefinite green
                            appendWord = (f'<span style=“color:{String}”>'+word)
                        # Otherwise
                        else:
                            #Start and end the string on the word
                            appendWord = (f'<span style=“color:{String}”>'+word+'</span>')

                    # Otherwise, if the first three letters are triple double quote string beginings
                    elif tertiary == '"""':
                        appendWord = (f'<span style=“color:{String}”>'+word)
                        InStringType2_3 = True

                    # Otherwise, if the first one or two letters are single quote string beginings
                    elif primary == '"' or secondary in str2:
                        # if the word sets off a string or end with a string begining or the ending is not a string ending
                        if len(word) == 1 or secondary in str2 or word[-1] !='"' or secEnd =='\\"' :
                            # Start the string section
                            InStringType2 = True
                            # Color the word an indefinite green
                            appendWord = (f'<span style=“color:{String}”>'+word)
                        # Otherwise
                        else:
                            #Start and end the string on the word
                            appendWord = (f'<span style=“color:{String}”>'+word+'</span>')

                    # Otherwise, if the word sets off a commetn
                    elif primary == '#':
                        # Color the word an indefinite red
                        appendWord = (f'<span style=“color:{Comment}”>'+word)
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
        h1 = heal_code[0]
        heal_code = list(filter(None, heal_code))
        heal_code.append('')
        while len(Broken_Code)< len(heal_code):
            Broken_Code.append('')
        
        # Loop through the items in the heal_code list
        for i in range(len(heal_code)):
            try:
                # Reinfuse the subtracted characters
                if h1 == '':
                    MYWORD +=Broken_Code[i]+heal_code[i]
                else:
                    MYWORD +=heal_code[i]+Broken_Code[i]
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
    HighlightedCode = HighlightedCode.replace('“','"').replace('”','"').replace('⋞','&#60;').replace('⋟','&#62;').replace('\t','&nbsp;'*3).replace('  ','&nbsp;'*2).replace('  ','&nbsp;'*2)
    # remove the last six characters
    HighlightedCode=HighlightedCode[:-17]#6
    # Complete the formatting
    if inline == True:
        code = f'<tt style="font-size:90%; border: 2px solid {Border}; padding: 3px; background-color:{Background}; color:{Foreground};">{HighlightedCode}</tt>&nbsp;'
    else:
        code = f'<p> </p><p style="font-size:90%; border: 2px solid {Border}; padding: 10px; background-color:{Background}; color:{Foreground};"><tt>{HighlightedCode}</tt></p><p>&nbsp;</p>'
    # Print the code
    
    print(code)
    if Return == True:
        return code
        


#htmlCode(input('Code Here:'))

print('\n\nInitiate using the "htmlCode" function\n>>> htmlCode(\'\'\'CODE GOES HERE\'\'\') or >>> htmlCode(\'\'\'CODE GOES HERE\'\'\', inline = True)\nPlease use triple quotes for multiline code\n'+'-'*30+'\nThe htmlCode(\'\'\'CODE GOES HERE\'\'\') function returns an object that can be previewed using the OBJECT.preview() command.\n An immediate preview can be achieved by using the command htmlCode(\'\'\'CODE GOES HERE\'\'\').preview()\n')


class htmlCode():
    """ ../‾‾‾‾‾‾/‾‾‾‾‾\|‾‾‾‾‾\ |  _____|.
        .|  /‾‾‾|  /‾\  | |‾\  \| |___....
        .| |    | |   | | |  |  |  ___|...
        .|  \___|  \_/  | |_/  /| |_____..
        ..\______\_____/|_____/ |_______|.
        """
    def __init__(self, code, inline=False, color = False):
        print('⩋'*40+'\n')
        if type(code)==tuple or type(code)==list:
            self.code = ''
            for section in code:
                if type(color)==tuple or type(color)==list:
                    clr = color[code.index(section)]
                else:
                    clr = color
                self.code += html_code(section,inline = inline, Return = True,color=clr)[:-(6+7*(inline==False))]
        else:
            self.code = html_code(code,inline = inline, Return = True)
        print('\n'+'⩊'*40)
        
    def preview(self):
        Preview(self.code)


def HighlightCode():   
    try:
        inline = False
        code = Input(f'Code (end code with "{DEFAULT_INPUT_TERMINATION_CODE}" on an empty line after the code):',ml=True)
        if code.find('\n') ==-1: inline = bool(input('Inline? (True/False)'))
        preview = bool(input('Preview? (True/False)'))
    except ValueError:
        print('Please make sure your input for the "Inline?" and "Preview?" prompts were booleans')
        return
    print()
    code = html_code(code,inline = inline, Return = True)
    if preview:Preview(code)

def ThemeDisplay():
    code = []
    colors = []
    for Theme in Themes:
        colors.append(Theme)
        code.append( f'''# {Theme} Theme Test
def Function():
    print('Hello')''')
    htmlCode(code,color = colors).preview()
    
