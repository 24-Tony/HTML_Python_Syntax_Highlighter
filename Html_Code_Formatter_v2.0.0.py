'''
    /‾/   /‾/‾‾‾‾‾‾‾‾/‾| /‾|  /‾/
   / /___/ /‾‾‾/ /‾‾/  |/  | / /
  / ___   /   / /  / | | / |/ /
 / /   / /   / /  / /|__/| | /____
/_/___/_/_  /_/  / /    _|_|_____/
  /  _____/‾/ /‾//‾| /‾/      /  |\  /‾/
 /  <_____\ \/ //  |/ /‾‾/ /‾/ / | \/ /
 \______  \\  // | | /  / / / /| |>  <
 ______/  // // /|  /  / / / /_| | /\ \
/________//_//_/_|_/__/_/ /_//___|/  \_\_______             _______
    /‾/   /‾/‾/ _____/‾/   /‾/ /   /‾/ _____/ /   /‾/‾‾‾‾‾‾/  ____/‾‾‾‾\
   / /___/ / / /____/ /___/ / /   / / /____/ /___/ /‾‾/ /‾/  /__ / /‾) /
  / ___   / / //_  / ___   / /   / / //_  / ___   /  / / /  ___//  ‾‾ ⁄
 / /   / / / /__/ / /   / / /___/ / /__/ / /   / /  / / /  /___/  /\  \
/_/   /_/_/______/_/   /_/_____/_/______/_/   /_/  /_/ /______/__/  \__\
'''


import re
import os
##try:
##    from pip import main as pipmain
##except:
##    from pip._internal.main import main as pipmain
import subprocess
from subprocess import *
##import requests
##import io
##import zipfile
from urllib import request
import requests
def download_extract_zip(url):
    """
    Download a ZIP file and extract its contents in memory
    yields (filename, file-like object) pairs
    """
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content)) as thezip:
        for zipinfo in thezip.infolist():
            with thezip.open(zipinfo) as thefile:
                yield zipinfo.filename, thefile

import sys

py = os.path.join(sys.exec_prefix,'python.exe')


def downloadZip(url,savePath):
    remoteZip = request.urlopen(url)
    local_file = open(savePath, 'wb')
    local_file.write(remoteZip.read())
    local_file.close()

def install(package):
    if type(package) == list:
        for p in package:
            print(f"Installing {p}")
            #call(['py', '-m', 'pip', 'install',package])
            proc = subprocess.Popen([py, '-m', 'pip', 'install',p],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            proc.wait()
            (stdout, stderr) = proc.communicate()
            #print(type(stderr))
            if proc.returncode != 0:
                print(str(stderr))
            else:
                print("success")
            #pipmain(['install', package])
    else:
        #call(['py', '-m', 'pip', 'install',package])
        print(f"Installing {package}")
        proc = subprocess.Popen([py, '-m', 'pip', 'install',package],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        proc.wait()
        
        (stdout, stderr) = proc.communicate()
        #print(type(stderr))
        if proc.returncode != 0:
            print(str(stderr))
        else:
            print("success")
        #pipmain(['install', package])

from tkinter import *


##import requests
##import io
##import zipfile
##def download_extract_zip(url):
##    """
##    Download a ZIP file and extract its contents in memory
##    yields (filename, file-like object) pairs
##    """
##    response = requests.get(url)
##    with zipfile.ZipFile(io.BytesIO(response.content)) as thezip:
##        for zipinfo in thezip.infolist():
##            with thezip.open(zipinfo) as thefile:
##                yield zipinfo.filename, thefile
try:
    from tkhtmlview import HTMLLabel,HTMLScrolledText
    import pyperclip as pc
except ModuleNotFoundError:
    print('Running some initialization...')
    pack = ['tkhtmlview','pyperclip']#['requests','Pillow','tkhtmlview',]
    install(pack)
    #py -m pip install requests
    #py -m pip install Pillow
    #pip install tkhtmlview
    #py -m pip install tkhtmlview
    from tkhtmlview import HTMLLabel,HTMLScrolledText
    import pyperclip as pc
##THEMEpath = os.path.join(os.path.expanduser('~'),'Downloads','tcl-awthemes.zip')
##if not os.path.exists(THEMEpath):
##    print('Retreving data...')
##    #download_extract_zip('https://sourceforge.net/projects/tcl-awthemes/files/latest/download')
##    downloadZip('https://sourceforge.net/projects/tcl-awthemes/files/latest/download',THEMEpath)

##try:
##    from tkinterhtml import HTMLLabel
##except:
##    print('Running some initialization...')
##    print('   installing tkhtmlview...')
##    #pipmain(['install','--upgrade','--force-reinstall','pip'])
##    #install('Pillow')
##    #install('tk_html_widgets')
##    
##    path = os.path.join(os.path.expanduser('~'),'Downloads','tkhtmlview-master.zip')
##    #f = open(path,'w+')
##    #call(["curl", "-O",  "https://github.com/pozzolana93/tkhtmlview/archive/refs/heads/master.zip"], stdout=f)
##    #call(["curl -O https://github.com/pozzolana93/tkhtmlview/archive/refs/heads/master.zip > tkhtmlview-master.zip"], shell=True)
##    downloadZip("https://github.com/pozzolana93/tkhtmlview/archive/refs/heads/master.zip",path)
##    #f.close()
##    try:
##        a = open(path)
##        a.close()
##        print('Created file at:',path)
##    except:
##        print('installation failure')
##    install(os.path.join(os.path.expanduser('~'),'Downloads','tkhtmlview-master.zip'))
##    #print('Installed')
##    #print('   installing tkinter...')
##    #install('tkinter')
##    #print( help('modules'))
##    from tkinterhtml import HTMLLabel
##    
    
# Set the default input termination code
DEFAULT_INPUT_TERMINATION_CODE = '--Terminate--'

version='2.0.0'
print(f'v {version}')

Bold = ';font-weight: 900'

# Define the default colors
Border = '#eeeeee'
Background = '#ffffff'
Foreground = '#000000'
Comment = '#DD0000'
String = '#00aa00'
Keywords = '#ff7700'
Builtins = '#900090'
Definitions = '#0000ff'
Numbers = '#0000ff'
Errors = '#ff0000'
Output = '#0000ff'

lThemes = {'Python Default':{
                'Border':'#555555',
                'Background':'#ffffff',
                'Foreground':'#000000',
                'Comment':'#DD0000',
                'String':'#00aa00',
                'Keywords':'#ff7700',
                'Builtins':'#900090',
                'Definitions':'#0000ff',
                'Numbers':'#000000',
                'Errors':'#ff0000'
                },
           'Python Bolded':{
                'Border':'#555555', 
                'Background':'#ffffff',
                'Foreground':'#000000',
                'Comment':'#DD0000',
                'String':'#00aa00',
                'Keywords':'#ff7700'+Bold,
                'Builtins':'#900090',
                'Definitions':'#0000ff'+Bold,
                'Numbers':'#0000ff'+Bold,
                'Errors':'#ff0000'
                },
           'Royal Blue':{
                'Border':'#555566',
                'Background':'#ffffff',
                'Foreground':'#000000',
                'Comment':'#00aa00',
                'String':'#DD0000',
                'Keywords':'#0000ff'+Bold,
                'Builtins':'#000099',
                'Definitions':'#000099'+Bold,
                'Numbers':'#000099'+Bold,
                'Errors':'#ff0000'
                },
           'Sea':{
                'Border':'#445566',
                'Background':'#ffffff',
                'Foreground':'#000000',
                'Comment':'#445a71',
                'String':'#229922',
                'Keywords':'#0077aa'+Bold,
                'Builtins':'#D86149',
                'Definitions':'#04B7BD'+Bold,
                'Numbers':'#0077aa'+Bold,
                'Errors':'#ff0000'
                },
           'Red':{
                'Border':'#665555',
                'Background':'#ffffff',
                'Foreground':'#000000',
                'Comment':'#445a71',
                'String':'#22863A',
                'Keywords':'#D73A49'+Bold,
                'Builtins':'#6F42C1',
                'Definitions':'#AB0112'+Bold,
                'Numbers':'#AB0112'+Bold,
                'Errors':'#ff0000'
                },
           'Grey':{
                'Border':'#555555',
                'Background':'#eeeeee',
                'Foreground':'#7B776F',
                'Comment':'#445a71',
                'String':'#C05726',
                'Keywords':'#3080B5'+Bold,
                'Builtins':'#C05726',
                'Definitions':'#ff7700'+Bold,
                'Numbers':'#000077'+Bold,
                'Errors':'#ff0000'
                },
           'Glisten':{
                'Border':'#808080',
                'Background':'#ffffff',
                'Foreground':'#333333',
                'Comment':'#445a71',
                'String':'#DD4422',
                'Keywords':'#008800'+Bold,
                'Builtins':'#008800',
                'Definitions':'#0066BB'+Bold,
                'Numbers':'#0000dd'+Bold,
                'Errors':'#ff0000'
                }
    }
dThemes = {'Default Dark':{
                'Border':'#555555',
                'Background':'#222222',
                'Foreground':'#dddddd',
                'Comment':'#ff3333',
                'String':'#00ff00',
                'Keywords':'#ffaa22'+Bold,
                'Builtins':'#ff40c0',
                'Definitions':'#00ccff'+Bold,
                'Numbers':'#55aaff'+Bold,
                'Errors':'#ff0000'
                },
           'Rainglow':{
                'Border':'#5298c4',
                'Background':'#040507',
                'Foreground':'#ffffff',
                'Comment':'#6f809f',
                'String':'#64aeb3',
                'Keywords':'#508aaa'+Bold,
                'Builtins':'#6ab0a3',
                'Definitions':'#00838C'+Bold,
                'Numbers':'#529CA8'+Bold,
                'Errors':'#ff0000'
                },
           'Bold':{
                'Border':'#3d8e91',
                'Background':'#0f0d0d',
                'Foreground':'#ffffff',
                'Comment':'#6f809f',
                'String':'#F7A21B',
                'Keywords':'#F0624B'+Bold,
                'Builtins':'#3D8E91',
                'Definitions':'#B4B7AD'+Bold,
                'Numbers':'#F7A21B'+Bold,
                'Errors':'#ff0000'
                },
           'Dark+':{
                'Border':'#555555',
                'Background':'#1e1e1e',
                'Foreground':'#D4D4D4',
                'Comment':'#6A9955',
                'String':'#CE9178',
                'Keywords':'#569CD6'+Bold,
                'Builtins':'#dcdcaa',
                'Definitions':'#9CDCFE'+Bold,
                'Numbers':'#B5CEA8'+Bold,
                'Errors':'#ff0000'
                },
           'Citylights':{
                'Border':'#171d23',
                'Background':'#1d252c',
                'Foreground':'#718CA1',
                'Comment':'#72899e',
                'String':'#68A1F0',
                'Keywords':'#508aaa'+Bold,
                'Builtins':'#70E1E8',
                'Definitions':'#24A5AF'+Bold,
                'Numbers':'#E27E8D'+Bold,
                'Errors':'#ff0000'
                },
           'Panda':{
                'Border':'#676B79',
                'Background':'#292a2b',
                'Foreground':'#E6E6E6',
                'Comment':'#737787',
                'String':'#19F9D8',
                'Keywords':'#FFB86C'+Bold,
                'Builtins':'#FF75B5',
                'Definitions':'#6FC1FF'+Bold,
                'Numbers':'#FFB86C'+Bold,
                'Errors':'#ff0000'
                },
           'Rose':{
                'Border':'#f52277',
                'Background':'#141322',
                'Foreground':'#B4DAE9',
                'Comment':'#45898C',
                'String':'#C01B5D',
                'Keywords':'#FB4293'+Bold,
                'Builtins':'#F37AB0',
                'Definitions':'#8CE1E7'+Bold,
                'Numbers':'#E5FCA6'+Bold,
                'Errors':'#ff0000'
                },
           'Sea Green':{
                'Border':'#242b38',
                'Background':'#0a1018',
                'Foreground':'#EEFFFF',
                'Comment':'#708394',
                'String':'#28735E',
                'Keywords':'#25A2A6'+Bold,
                'Builtins':'#5CB4DE',
                'Definitions':'#4785bd'+Bold,
                'Numbers':'#28735E'+Bold,
                'Errors':'#ff0000'
                },
           'Firefly':{
                'Border':'#333333',
                'Background':'#0a0a0a',
                'Foreground':'#a8aebd',
                'Comment':'#626a73',
                'String':'#a4bd00',
                'Keywords':'#ff0066'+Bold,
                'Builtins':'#ff8533',
                'Definitions':'#827db5'+Bold,
                'Numbers':'#E6E600'+Bold,
                'Errors':'#ff0000'
                },
           'Monikai':{
                'Border':'#333333',
                'Background':'#121212',
                'Foreground':'#bbbbbb',
                'Comment':'#5C6370',
                'String':'#E5C07B',
                'Keywords':'#56B6C2'+Bold,
                'Builtins':'#E06C75',
                'Definitions':'#98C379'+Bold,
                'Numbers':'#C678DD'+Bold,
                'Errors':'#ff0000'
                },
           'Black Ocean':{
                'Border':'#0c5271',
                'Background':'#101316',
                'Foreground':'#DFDFDF',
                'Comment':'#60778c',
                'String':'#7ebea0',
                'Keywords':'#007aae'+Bold,
                'Builtins':'#019d76',
                'Definitions':'#15b8ae'+Bold,
                'Numbers':'#15b8ae'+Bold,
                'Errors':'#ff0000'
                },
           'CodePen':{
                'Border':'#9CA0B1',
                'Background':'#1e1f27',
                'Foreground':'#D5D7DE',
                'Comment':'#88AFBF',
                'String':'#2BC7B9',
                'Keywords':'#47CF73'+Bold,
                'Builtins':'#5E91F2',
                'Definitions':'#9CA0B1'+Bold,
                'Numbers':'#2BC7B9'+Bold,
                'Errors':'#ff0000'
                },
           'Acme':{
                'Border':'#a2a797',
                'Background':'#0f0e0d',
                'Foreground':'#EDEBE6',
                'Comment':'#988e86',
                'String':'#E0A84C',
                'Keywords':'#CF433E'+Bold,
                'Builtins':'#CD122C',
                'Definitions':'#d96972'+Bold,
                'Numbers':'#a5e3d0'+Bold,
                'Errors':'#ff0000'
                },
           'Arc':{
                'Border':'#3c3c3c',
                'Background':'#111111',
                'Foreground':'#EDEBE6',
                'Comment':'#888888',
                'String':'#ff1ba9',
                'Keywords':'#f28888'+Bold,
                'Builtins':'#a80000',
                'Definitions':'#A5E3D0'+Bold,                
                'Numbers':'#a5e3d0'+Bold,
                'Errors':'#ff0000'
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
str1 = ['\'', 'f\'','u\'','b\'','r\'','\'\'\'','f\'\'\'','u\'\'\'','b\'\'\'','r\'\'\'']
# create a list of instances that would set off a string with double quotes
str2 = ['"', 'r"','f"','u"','b"','"""','f"""','u"""','b"""','r"""']

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
                'repr', 'reversed', 'round', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'],
    'Numbers' : [],
    'Error'   : [],
    'Output'  : []
    }

# Create a dictionary with syntax ends - blank for continuous highlighting
ends = {
    'Comment': '', 
    'String': '',
    'Keywords': '</span>',
    'Builtins': '</span>',
    'Numbers': '</span>'
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
        "Definitions" : Definitions,
        "Numbers" : Numbers,
        "Error" : Errors,
        "Output" : Output
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
        global Border, Background, Foreground, Comment, String, Keywords, Builtins, Definitions, Colors, Numbers, Errors, Output
        Border = theme['Border']
        Background = theme['Background']
        Foreground = theme['Foreground']
        Comment = theme['Comment']
        String = theme['String']
        Keywords = theme['Keywords']
        Builtins = theme['Builtins']
        Definitions = theme['Definitions']
        Numbers = theme['Numbers']
        Errors = theme['Errors']
        Output = theme['Definitons']
    except:
        print('Invalid Theme')



#OLD
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
#NEW

def Compute(Code,color,inline):
    print(color)
    if color=='':
        color = list(Themes)[0]
    color = list(Themes).index(color)+1
    print(color)
    inline = bool(inline)
    Raw = htmlCode(Code,color=color,inline=inline)
    global root,clicked,drop,text_box,OutText_box,OUTPUT
    OutText_box.config(state='normal')
    OutText_box.delete(1.0, 'end')
    OutText_box.insert(1.0, Raw.code)
    OutText_box.config(state='disabled')
    if inline:
        a = Raw.code
        bg = Raw.code[106:113]
    else:
        a = Raw.code[8:]
        bg = Raw.code[184:191]
    OUTPUT['bg'] = bg
    OUTPUT.set_html(a)
    print(bg)
    
import random
from tkinter import scrolledtext,ttk
from functools import partial
import win32gui
#from io import BytesIO
import base64, PIL, urllib
from PIL import ImageTk
import urllib.request
class Interface():
    def __init__(self):
        
        global root,clicked,drop,text_box,OutText_box,OUTPUT,ISINLINE
        root = Tk()
        win32gui.SetForegroundWindow(root.winfo_id())
        root.title(f'HTML Syntax Highlighter v{version}')
##        root.tk.call('lappend', 'auto_path', os.path.join(THEMEpath,'awthemes-10.4.0','pkgIndex.tcl'))
##        root.tk.call('package', 'require', 'awdark')
        
##        root.style(style='Fun.root')
        fg='#ff3333'#'#3D8E91'
        bg='#0f0d0d'
        bg2='#1f1d1d'
        root.config(bg=bg)
        #try:
        url = 'https://user-images.githubusercontent.com/47753578/135677892-c14221dc-e055-4e64-8150-9629b5ef5286.png'
        raw_data = urllib.request.urlopen(url).read()
        import warnings
        warnings.filterwarnings("ignore")
        b64_data = base64.encodestring(raw_data);
        warnings.filterwarnings("always")
        image = PhotoImage(data=b64_data)
        root.tk.call('wm', 'iconphoto', root._w, image)
        #except:
        #    pass
        root.resizable(width=0, height=1)
        root.geometry("1080x800")
        Title = Label(root,text=f'HTML Syntax Highlighter v{version}',font=("Consolas", 25),pady=20,bg=bg,fg=fg).place(relx = 0.5,
                       rely =0,
                        anchor ='n')
        
        options = list(Themes)
        
        clicked = StringVar()
        
        
        label = Label( root , text = "Pick a Theme (Themes are light until 'Default Dark')" ,bg=bg,fg=fg).place(relx = 0.5,
                       rely =0.075,
                        anchor ='n')
        errout = Label( root , text = 'Use: `err` to start and end an error and `out` to start and end an output \n   to get the simply have the string of `err` or `out` put a "\\" before it.' ,bg=bg,fg=fg).place(relx = 1,
                       rely =0.075,
                        anchor ='ne')
        COLOR = StringVar()
        combostyle = ttk.Style()

        combostyle.theme_create('combostyle', parent='alt',
                                 settings = {'TCombobox':
                                             {'configure':
                                              {'selectbackground': bg,
                                               'fieldbackground': bg,
                                               'background': bg2,
                                               
                                               }}}
                                 )
                
        combostyle.theme_use('combostyle') 
        drop = ttk.Combobox( root ,textvariabl=COLOR )
        drop['values'] = options
        drop['state'] = 'readonly'
        
        #drop.config(bg = bg,fg=fg)
        #drop['menu'].config(bg=bg2,fg=fg)
        drop.place(relx = 0.5,
                       rely =0.105,
                        anchor ='n')
        #ISINLINE = BoolVar()
        ISINLINE = IntVar()
        Checkbutton(root, text='inline',bg=bg,fg=fg, variable=ISINLINE).place(relx = 0.6,
                                                                              rely =0.105,
                                                                              anchor ='n')

        message ='''Please put your code here...'''

        text_box = scrolledtext.ScrolledText(
            root,
            height=10,
            width=130,bg=bg2,fg=fg
        )
        text_box.place(relx = 0.5,
                       rely =0.15,
                        anchor ='n')#(expand=True)
        text_box.insert('end', message)
        text_box.config(state='normal')

        button = Button( root , text = "Highlight",command = lambda:Compute(text_box.get("1.0",'end-1c'),
                                                                            COLOR.get(),
                                                                            ISINLINE.get()),bg=bg,fg=fg).place(relx = 0.5,
                       rely =0.36,
                        anchor ='n')
        
        button = Button( root , text = "Copy",command = lambda:pc.copy(OutText_box.get("1.0",'end-1c')),bg=bg,fg=fg).place(relx = 0.009,rely = 0.61,
                        anchor ='nw')
        
        OutText_box = scrolledtext.ScrolledText(
            root,
            height=10,
            width=130,bg=bg2,fg=fg
        )
        OutText_box.place(relx = 0.5,
                       rely =0.4,
                        anchor ='n')#(expand=True)
        OutText_box.insert('end', 'HTML Output...')
        OutText_box.config(state='disabled')
        label2 = Label( root , text = "Output HTML code (What you want to copy) ↑ | ↓ Preview (Indentation, Bolding, and other attributes will exist in actual implementation, but may not display here)" ,bg=bg,fg=fg).place(relx = 0.5,
                       rely =0.615,
                        anchor ='n')
        OUTPUT = HTMLScrolledText(root,height=15,width=130,html='')
        OUTPUT.place(relx = 0.5,
                       rely =0.65,
                        anchor ='n')
    ##    label.pack()
        
        #button = Button( root , text = "click Me" , command = print(clicked.get())).pack()    
        
##        root.attributes("-topmost", True)
##        root.attributes("-topmost", False)
        root.mainloop()



    
def fillTemplate(HighlightedCode,inline):
    global Border, Background, Foreground, Comment, String, Keywords, Builtins, Definitions, Colors, Numbers
    if inline == True:
        return f'<tt style="font-size:80%; border-radius: 5px;  border: .1em solid {Border}; padding: 3px; background-color:{Background}; color:{Foreground};">{HighlightedCode}</tt>&nbsp;'
    else:
        return f'<p> </p><p style="font-family: Consolas; font-size:80%;line-height:1.25em; border: solid {Border}; border-radius: 5px; border-width:.1em .1em .1em .8em; padding: 10px; background-color:{Background}; color:{Foreground};">{HighlightedCode}</p><p>&nbsp;</p>'

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
    code = fillTemplate(rawcode,inline)
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
        "Definitions" : Definitions,
        "Numbers" : Numbers,
        "Error" : Errors,
        "Output" : Output
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
    InErr = False
    InOut = False
    
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

            # Otherwise, if we are in the heading of a function or a class
            elif InDef_Class:
                # Make the word blue
                appendWord = f'<span style=“color:{Definitions}”>'+word+'</span>'
                # Terminate the function or a class heading section
                InDef_Class = False
            # Otherwise, if we are in an error
            elif InErr:
                # If an error is ending and 
                if word.find('`err`') != -1 and ( word.find('\\`err`')!=(word.find('`err`')-1) or word.find('\\`err`') ==-1):
                    # End the string
                    appendWord = word.replace('`err`','</span>')
                    # Terminate the triple double quote string section
                    InErr = False
                appendWord = appendWord.replace('\`err`','`err`')
                
            # Otherwise, if we are in an output
            elif InOut:
                # If an error is ending and 
                if word.find('`out`') != -1 and ( word.find('\\`out`')!=(word.find('`out`')-1) or word.find('\\`out`') ==-1):
                    # End the string
                    appendWord = word.replace('`out`','</span>')
                    # Terminate the triple double quote string section
                    InOut = False
                appendWord = appendWord.replace('\`out`','`out`')
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
                        elif color == "Numbers":
                            if word.isnumeric():
                                clr = ColorToType[color]
                                appendWord = (f'<span style=“color:{clr}”>'+word+ends[color])
                        elif color == 'Error':
                            if word.find('`err`') != -1 and ( word.find('\\`err`')!=(word.find('`err`')-1) or word.find('\\`err`') ==-1):
                                clr = ColorToType[color]
                                appendWord = word.replace('`err`',f'<span style=“color:{clr}”>',1)
                                InErr = True
                                if len(word)>len(' `err`') and (word[-5:]=='`err`'):
                                    appendWord  = appendWord.replace('`err`','</span>')
                                    InErr = False
                            appendWord = appendWord.replace('\`err`','`err`')
                        elif color == 'Output':
                            if word.find('`out`') != -1 and ( word.find('\\`out`')!=(word.find('`out`')-1) or word.find('\\`out`') ==-1):
                                clr = ColorToType[color]
                                appendWord = word.replace('`out`',f'<span style=“color:{clr}”>',1)
                                InOut = True
                                if len(word)>len(' `out`') and (word[-5:]=='`out`'):
                                    appendWord  = appendWord.replace('`out`','</span>')
                                    InOut = False
                            appendWord = appendWord.replace('\`out`','`out`')
                        
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
                    try: qry = word[:4]
                    except: qry = tertiary
                    # If the first three letters are triple single quote string beginings
                    if tertiary == '\'\'\'' or (len(qry) == 4 and qry in str1):
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
                    elif tertiary == '"""' or (len(qry) == 4 and qry in str2):
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
    HighlightedCode=HighlightedCode[:-16]#6
    # Complete the formatting
    code = fillTemplate(HighlightedCode,inline)
   
    # Print the code
    
    print(code)
    if Return == True:
        return code
        


#htmlCode(input('Code Here:'))




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
            self.code = html_code(code,inline = inline, Return = True,color=color)
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
    """This Function is a test"""
    return str(1101.2021)''')
    htmlCode(code,color = colors).preview()
    


#Determine the theme
Themes = {}
ltNames = list(lThemes)
ltVals = list(lThemes.values())
dtNames = list(dThemes)
dtVals = list(dThemes.values())
for theme in range(len(lThemes)+len(dThemes)):
    if theme < len(lThemes):
        Themes[ltNames[theme]] = ltVals[theme]
    else:
        Themes[dtNames[theme-(len(lThemes))]] = dtVals[theme-(len(lThemes))]
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

if input('Use Interface? (y/n):').upper() == 'N':

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

    # Print a guide
    print('\n\nInitiate using the "htmlCode" function\n>>> htmlCode(\'\'\'CODE GOES HERE\'\'\') or >>> htmlCode(\'\'\'CODE GOES HERE\'\'\', inline = True)\nPlease use triple quotes for multiline code\n'+'-'*30+'\nThe htmlCode(\'\'\'CODE GOES HERE\'\'\') function returns an object that can be previewed using the OBJECT.preview() command.\n An immediate preview can be achieved by using the command htmlCode(\'\'\'CODE GOES HERE\'\'\').preview()\n')
    print('Use: `err` to start and end an error and `out` to start and end an output - to get the simply have the string of `err` or `out` put a "\\" before it.')
else:
    try:
        Interface()
    except:
        Interface()
