# Stardist-BATCH
a Jython script designed to run in ImageJ which operates on raw images, and identifies fluorescent nuclei using the StarDist plugin for ImageJ.


This script is designed to run on an experiment folder with raw images of cells output from the microscope. The 'input_folder' in line 16 should be the top level folder (in 'example data' folder, this would be the PATH of the TileScan folder. 
![image](https://user-images.githubusercontent.com/75409146/151273758-7823bad3-83c1-4f28-bd0d-c0d38913e2b8.png)

Then, fill in the variable 'file_identifier' by picking an element within the filename of the images you wish to analyse, and adding it to file_identifier. e.g. if the name of the images you wish to analyse all have 'Ch00' within the name (R1_Ch00, R2_Ch00 ... and so on) then make this line in the script file_identifier = 'Ch00' and as a result it will gather all images with those letters in the name and analyse them. 

The script outputs all the results back into the same folder they came from, with the same image name + 'label' at the beginning of the name so they can be identified. If you run this with 'TileScan' or top folder as the input folder, it will run on all images 3 folders DOWN the path from TileScan, and be able to send them back to the subfolder they came from. 
