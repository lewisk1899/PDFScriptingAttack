##################################################
SET UP YOUR SYSTEM THIS PROJECT
##################################################

HOW TO USE GITHUB
1. Install Git Bash, this is a Linux command prompt
that can be used on Windows machines. 

2. Create a directory where you want the project 
to be located. (File explorer or command prompt i.e > mkdir ECE509Project)

3. Then right click in the directory, if you have Git Bash
installed properly, you should see 'Open Git Bash here'. 

4. In the Git Bash cmd prompt, type:
> git clone https://github.com/lewisk1899/PDFScriptingAttack.git
It should start downloading the repo. 

5. Now you need to create a 'branch', 
this is where all your work will be placed, it is practically
a workstation that you can make changes and everyone can see
and it will not affect anyone elses work. 
Type in Git Bash:
> git branch [name]/version_0
> git checkout [name]/version_0

git checkout, just moves you to that branch or version of
the 'main' repo. 

6. For everyone to see your work, you will need
to push your branch to the main repo. 
> git push -u remote/origin/main [name]/version_0

-----------------------------------------------------------
Anytime you make a change to the directory... 
add files, remove files, edit code, etc. When you 
are happy with your changes then you will need to push. 
> git add .
(This queues your changes so that it can be pushed)
> git commit -m "[add comment about what u did, be brief]"
> git push 
(This is 'push' your changes up to your branch, so that
others may see your changes)

To make sure that everything is good to go, use
> git status
To what git sees...if green you are good, if red..then not good lol


##################################################
TOOLS THAT ARE GOING TO BE USED...
##################################################
Python 
PyPDF2
Node.js
https://kjkpub.nyc3.digitaloceanspaces.com/software/sumatrapdf/rel/SumatraPDF-0.2-install.exe
https://blog.didierstevens.com/programs/pdf-tools/pdf-parser_V0_7_5.zip
##################################################
INSTALLING CERTAIN TOOLS
##################################################
1. In a Windows command prompt (if python is added to your path)
> pip install PyPDF2 
(PyPDF2 this tool can create PDFs)

2. https://kjkpub.nyc3.digitaloceanspaces.com/software/sumatrapdf/rel/SumatraPDF-0.2-install.exe
This is the PDF reader we need, not Adobe (too sophisticated). 

3. https://nodejs.org/en/ choose the 'Recommended for most users'

4. PDF parsing tool = https://blog.didierstevens.com/programs/pdf-tools/pdf-parser_V0_7_5.zip
(This tool help look into a PDF, on the same page there is a zip that can allow your to
embed a Javascript file into a PDF...mess around with it, looks at the  this resource: https://github.com/filipi86/MalwareAnalysis-in-PDF
to gain more understanding of the tool).