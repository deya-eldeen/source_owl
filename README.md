# Source Owl

<p align="center">
    <img src="pdf_owl_logo.png">
</p>

Source Owl is a (source code backup solution), it generates a PDF document out of your source code, it scans for specific file extensions you specify, and generates  
a comprehensive document that contains the source code, along with simple statistics like number of lines & files.

Setup:  
install python3 and pip

     pip3 install -r requirements.txt 

Usage:  

you can pass the parameters like this   

    python3 source_owl.py include_types outputfile target_directory  
example  

    python3 generate.py "['swift','xcconfig']" "report.txt" "/Users/deya/Projects/iOSProject"

or you can enter the values in the config.json file

    python3 generate.py  

Known Issues (under working)  
1- pdf line length.
2- can't scan binary files like images...

To Do List  
1- ability to add a cover page.  

Temporary Notes:
  1) if you want the file as a pdf file, you can print the file as a pdf on mac, just print the txt file, choose save as pdf.  
  2) if you want syntax highlighting, open the file with your IDE, and print as PDF from the IDE itself.  

Contributions are welcome.
