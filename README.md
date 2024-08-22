This is project for transliteration correction for Indian words that are written in English corpora


Darshan Jain (231110009)
Shaurya Agarwal (231110046)


Dependencies:
1. MICROSOFT LID TOOL
for installation see the README file inside the project folder. This README file belongs to original authors of Microsoft  has complete information 
about the LID tool and how to use it. It also requires MALLET sofware which doesn't need to be installed but only the dependencies need to be resolved.
For that please refer to the README file of the MALLET folder which is inside our project folder.

2. AKSHARMUKHA LIBRARY
Usage: pip aksharamukha

3. XLit ENGINE
Usage: pip install ai4bharat-transliteration
Note: if there is error in this ai4bharat working while running the model it might be because of different version of fairseq library.
so use: pip install git+https://github.com/liyaodev/fairseq.git (in windows)
or refer to https://github.com/facebookresearch/fairseq/issues/5012#issuecomment-1884159687 (link to resolve this issue) 


Our Prjoct's main  code resides in the file "project_final.ipynb". 
The complete code is well commented and can be easily understood and followed.
Just go through this file to see the code. It can be run on local machine as well.

For the database, Please look into "datasets" folder 
We manually took the section 1 as given from "Original MB vol1.txt" file. And corrected those words into corresponding transliterated words.
the file "Manual_words" has the words we found as "Indian words". And the file "Manual_corrected_words.txt" is the file that has the correctly
transliterated words of "Indian Words".
Finally "Model_corrected_words.txt" is the file that is generated from the code, it consists of a dictionary with keys as words the model classified 
as Indian and their values are there corresponding corrected transliterated words.
 

 also to run the files in cmd for longer processing you can check the folder "cmd long run" folder. move those files to parent folder and run in order 
 1. run.py
 2. transl.py
 3. update.py

 in these files please correct all the file paths as per your need.