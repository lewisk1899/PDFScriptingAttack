# ECE509 Final Project - PDF HTML Attack

This repository contains files to perform a PDF heap spray attack by exploiting the vulnerability of internet browsers.

### Pre-requisites
To perform and evaluate this attack the following requisites are required:
- Have a Windows XP virtual machine (VM) with the following software:
  - Internet Explorer 7
  - Adobe Acrobat 8.1
  - Immunity Debugger with mono.py included in the pycommands
  - Text Editor such as Sublime Text

### How to Use
- Step 1: Download and extract the repository onto the VM into the Downloads folder
- Step 2: Open the PDF

Opening the PDF will trigger the HTML file to open as well due to the application execution code in the PDF. The HTML file contains malicious javascript that will execute a simple example heap spraying attack onto the target machine.

To view the effects of this heap spray attack one can use Immunity Debugger to view the heap. Open Immunity Debugger and attach Internet Explorer 7 onto the debugger. Then type the following mona.py command in the Immunity Debugger command line to find our malicious code:

```!mona find -s "ECE509 student ATTACK"```
