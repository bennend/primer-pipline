# primer-pipline:
A pipeline integrated with GUI that can design primers for DNA sequence family.
This is a pipeline software that can be used to design primers for the consered regions of multiple homologous DNA sequences, including the multiple sequences alignemnt of the target sequences, and the consensus sequences from the alignemnt file from the MSA of the sequences, the dtection of the conserved regions of the sequences, the primer designing for the conserved region of each variant sequences. 

## FOR Mac Users:
  To use this pipeline on Linux-compatible operating system, please:
1. Download the PrimerDesignerMac from google drive. 
2. Extract the compressed file to wherever you want.
3. Doulbe click the GUI file in the extracted PrimerDesignerMac folder.

## FOR Windows system Users:
To use this pipeline on Windows, please:
1. Download a [Virtual Machine (VM)](https://www.virtualbox.org/), and a [Ubuntu Mate ISO](https://ubuntu-mate.org/download/). Choose 64-bit and version 16.04.1 LTS(Bionic) for Ubuntu.
2. Install the VM by following the [instructions](http://www.psychocats.net/ubuntu/virtualbox).
3. After installation, check the python version in yout VM: Open terminal in your VM, type python3 and the version will be shown as 'Python 3.6.5 (default, ****)'.
4. If python is version 3.6 then download the pipeline package 3.6 from google drive through the browser in your VM.
5. Extract the folder to wherever you want, right click the empty space in the extracted folder, click 'Open in Terminal'.
6. Type: 
```
sudo apt-get install python3-tk
```
to install the essential component for GUI, otherwise you will get an error from termianl: 
```
libBLT.2.5.so.8.6: cannot open shared object file: No such file or directory
```
7. Double click the GUI file in the folder, then you can play around with the pipeline (Type ``` ./GUI ```in terminal if it doesn't work).
