# SPLITIT  
A python script to **split a PDF file into its pages**.  
## Working    
SPLITIT splits the pages of a pdf file and renames the files with the following syntax  
>SerialNo_Initials.pdf  
SPLITIT will ask for the initial SerialNo and name of a text file which will contain the names of people. SPLITIT will take initials from the names given in the text file.  
The names in the text file should be like the following:```  
Raghuram Rajan  
Gunjan Roy  
Prakash Raj  
.  
.  
.  
etc.
```  
i.e. After every name there should be a new line.
Let's say the initial serial number is 1001. Then, the splitted PDFs will be named as,  
- 1001_RR.pdf
- 1002_GR.pdf
- 1003_PR.pdf
- .
- .
- etc  
## Usage   
Simply clone the repo or download the zip file. After downloading open the directory by,  
`cd splitit-master`  
Make sure you have python3 interpreter and PyPDF2 installed. If not then install PyPDF2 by,  
`pip3 install PyPDF2`  
Now, make sure the text file containing the names and the whole pdf is in the same directory.  
Then run the script by,  
`python splitit.py`  
Then type the name of the pdf,text file and the initial serial number and it would work like a charm.  
**Feel free to change the code as your need.**