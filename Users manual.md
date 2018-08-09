The whole pipeline can be divided into four sections: Multiple sequences alignment, Generate consensus sequence and detect conserved regions, Design primers, and Filter primers.

# Multiple sequence alignment: 
This step will implement multiple sequences algnemnt with clustalw2
1. Choose the file you want to align (in fasta format). 
2. Choose the path where you want to generate the MSA file and name it. 
3. Click 'run' to genrate alignment file.
*Each time you should only upload one file.



# Generate consensus sequence and detect conserved regions: 
This step will generate consensus sequence and detect the conserved regions from the alignment files genrated from last step.
1. Choose the MSA file , then you can name your consensus sequence. 
2. Set a threshold for your consensus sequence. This is the threshold specifying how common a particular residue has to be at a position before it is added. The default is 0.7 (meaning 70%).
3. Choose where to save the consensus sequence and the conserved regions fileand name them.
4. Click 'run' to generate the two files.



# Design primers:
This step will design primers for all the sequences in the input file.
1. Choose the template sequences (input file).
2. Choose where to generate the parameter files for generating primer files (Parameter files are required by the primer3 software to design primers) and name it.
3. Choose where to generate the primer files and name it.
4. Click 'run' to generate parameters and primer files.
5. A text file and an Excel file will be generated, where users can get their primers. And userscan also visualize the primers' quality by clicking 'Show primers' quality' button on the GUI.



# THINGS TO BE NOTICED:
1. Users should only apply this pipeline to the input files one by one to avoid mistakes if they have multiple input files.
2. The 'Design primers' step in this pipeline shouldn't be executed independently, because the 'Generate consensus sequence and detect conserved regions' are conneted with the 'Design primers' step, users should always implement 'Generate consensus sequence and detect conserved regions' before using 'Design Primers'.
3. There is a para.txt file in the pipeline package, where users can change the length of conserved regions they want to adapt this pipeline to their study. The default value is 70 for thestudy of Carbapenem resistant genes' study.
