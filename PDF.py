# import PyPDF2
#
# # create file object variable
# # opening method will be rb
# pdffileobj = open('curriculum_vitae_data-master/pdf/1.pdf', 'rb')
#
# # create reader variable that will read the pdffileobj
# pdfreader = PyPDF2.PdfFileReader(pdffileobj)
#
# # This will store the number of pages of this pdf file
# x = pdfreader.numPages
#
# # create a variable that will select the selected number of pages
# pageobj = pdfreader.getPage(x - 1)
#
# # (x+1) because python indentation starts with 0.
# # create text variable which will store all text datafrom pdf file
# text = pageobj.extractText()

# save the extracted data from pdf to a txt file
# we will use file handling here
# dont forget to put r before you put the file path
# go to the file location copy the path by right clicking on the file
# click properties and copy the location path and paste it here.
# put "\\your_txtfilename"
#
# file1=open(r"D:\Becode\Bouman331\projects\NLP\curriculum_vitae_data-master\txt\1.txt","a", encoding="utf-8")
# file1.writelines(text)
""" Results: BAD"""

# from tika import parser
#
# raw = parser.from_file('curriculum_vitae_data-master/pdf/1.pdf')
# # print(raw['content'])
#
# # get the content out the file
# output = raw['content']
# # convert it to utf8
# output = output.encode('utf8', errors='ignore')
# #save it to a file called X.txt
# with open ("D:\\Becode\\Bouman331\\projects\\NLP\\curriculum_vitae_data-master\\txt\\1.txt", 'w') as the_file:
#     the_file.write(str(output))
""" Results: UBER GOOD """

from pdfminer.high_level import extract_text

resume_text = extract_text('curriculum_vitae_data-master/pdf/1.pdf')

with open ("D:\\Becode\\Bouman331\\projects\\NLP\\curriculum_vitae_data-master\\txt\\1_miner.txt", 'w') as the_file:
     the_file.write(str(resume_text))
"""

now all the pdf 
"""
