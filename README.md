# HTML Python Syntax Highlighter


![html_Syntax](https://user-images.githubusercontent.com/47753578/135888901-0019fdca-20e2-40b6-8551-a96c06105661.png)


#### A program to generate Python syntax highlighting in HTML.

Latest version (v 2.0.0): [View](https://raw.githubusercontent.com/24-Tony/HTML_Python_Syntax_Highlighter/main/Html_Code_Formatter.py)





Previous versions:

Version | View
------- | -------
v 2.0.0 | [View](https://raw.githubusercontent.com/24-Tony/HTML_Python_Syntax_Highlighter/main/Html_Code_Formatter_v2.0.0.py)
v 1.1.0 | [View](https://raw.githubusercontent.com/24-Tony/HTML_Python_Syntax_Highlighter/main/Html_Code_Formatter_v1.1.0.py)
v 1.0.3 | [View](https://raw.githubusercontent.com/24-Tony/HTML_Python_Syntax_Highlighter/main/Html_Code_Formatter_v1.0.3.py)
v 1.0.2 | [View](https://raw.githubusercontent.com/24-Tony/HTML_Python_Syntax_Highlighter/main/Html_Code_Formatter_v1.0.2.py)



# Using the Highlighter
### Note: the program may not work for every code and I probably missed a few highlighting built-ins.

You may encounter the following question:

![Prompt](https://user-images.githubusercontent.com/47753578/135868355-1114f226-4375-4dbb-bb7b-d25e62421e27.png)

If you do not encounter it you are using an older version and it is defaulting to command line mode

### Interface (only for versions 2.0.0 and higher)

On the first run, the program will complete some initialization, this may take a few seconds.

![image](https://user-images.githubusercontent.com/47753578/135868809-c35af2e3-8c7a-4234-8ef5-e267b817ab7f.png)

It is pretty self-explanitory, but here is an example video of using it: (It may seem shaky embeded in here, to solve this press the three dots (⁝) button and click download. Then open the file and watch it there.)

[Video](https://user-images.githubusercontent.com/47753578/135867233-8948b946-d9dc-4546-b97f-966bf28b2eb7.mp4)

### Command line (themes and specific outputs may be slightly different, but these instructions should give a general idea)

1. Run the program - open the file and press the [F5] button on your keyboard.
     
2. Chose the theme:

![Theme Selector Image](https://user-images.githubusercontent.com/47753578/134692006-8336ba67-ee67-4a8a-b032-b81a911d53f3.png)

3. The program should display a warning

![Warning Image](https://user-images.githubusercontent.com/47753578/134692671-8fec5c86-5366-4c4a-a0b8-95886c74e19b.png)

4. Next type your command 

   - It should resemble: `htmlCode('''Paste Code Here''')`, `htmlCode('Paste Code Here', inline=True)`, `htmlCode('''Paste Code Here''').preview()`, `htmlCode('Paste Code Here', inline=True).preview()`, `html_NoColor('''Paste Code Here''')`, or  `html_NoColor('Paste Code Here', inline=True)`

      ![Default](https://user-images.githubusercontent.com/47753578/134693555-81df5bea-a77f-4c54-b00b-288b24ff6f8c.png)
  
       Which previews as: 
       ![Default Preview](https://user-images.githubusercontent.com/47753578/134693670-b697d323-b052-497e-9f40-148c23fab72e.png)

    - Or if you are using the command `HighlightCode()`
  
      ![HighlightCode](https://user-images.githubusercontent.com/47753578/134694295-9035c07c-0f35-4538-b1af-b1d64f62d7b4.png)

       Which previews as: 
       ![HighlightCodePreview](https://user-images.githubusercontent.com/47753578/134693670-b697d323-b052-497e-9f40-148c23fab72e.png)

5. Copy the output and paste it into the html editor
    
    To access the editor:
      - Go to your post
      - Click on the [Advanced] button next to cancel.

        ![image](https://user-images.githubusercontent.com/47753578/134343985-b3aafade-89b0-4602-b7d9-f63972bc74dc.png)

      - Then, click on the [↴] button and then [</>] button.

        ![image](https://user-images.githubusercontent.com/47753578/134344062-2323b561-8c45-4076-83e0-4acd5806ac11.png)

      - The output would then be pasted into the HTML editor.






# Themes
![Themes](https://user-images.githubusercontent.com/47753578/134695081-48a1d83f-c6e6-494b-ab3f-2fb3eed94b7f.png)

