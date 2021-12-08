# PDF as a means of executing a previously injected Malicious File
How to execute this attack:
 1) Use Didier Stevens PDF tools for the beginning of this process, those steps will be listed below.
 
     i) Download Didier Stevens PDF tools as linked here https://blog.didierstevens.com/programs/pdf-tools/, more specifically the make-pdf tool.
     
     ii) You have two options, the first being to use Didier Stevens make-pdf-embedded.py which is a different route that I went and swill require some exploration, or you can use make-pdf-javascript.py.
 3) We are only using make-pdf-javascript.py as a way to make the pdf itself, we will soon open the PDF document in a code editor and make some slight changes, to use this program you have to utilize the python 2 interpreter.
     
     i) enter this command into the CLI: py -2 make-pdf-embedded.py (outputname).pdf
 
 4) Open the pdf file that was created in the above step and open the notepad to display what is inside.

5) In the this step we will find where the javascript object is and replace it with something else, firstly refer to the OpenAction object at the top. This object is labeled as object 7 as such "/OpenAction 7 0 R", this will lead you in the direction of what is being acted upon as soon as something is opened, 
 ><<
  /Type /Action
   /S /JavaScript
   /JS (app.alert({cMsg: 'Hello from PDF JavaScript', cTitle: 'Testing PDF JavaScript', nIcon: 3});)>>
 6) Here we will replace with another type of action that can be executed by a PDF which is:
 ><<
  /Type /Action
  /S /Launch
  /Win << /F (c:\\(filepath to the executable).exe >> >>
 7) After replacing the two portions of the code, you should have a pdf that is capable of executing an executable on most pdf readers, you will have to hope that the user does not read the pop up and just willingly accepts.


Relevant Material:
1) https://github.com/filipi86/MalwareAnalysis-in-PDF
6) https://blog.didierstevens.com/programs/pdf-tools/
7) https://www.blackhat.com/presentations/bh-europe-07/Sotirov/Presentation/bh-eu-07-sotirov-apr19.pdf
