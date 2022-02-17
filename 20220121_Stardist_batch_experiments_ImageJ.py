
#@ DatasetIOService io
#@ CommandService command
""" This example runs stardist on all tif files in a folder
Full list of Parameters:
res = command.run(StarDist2D, False,
             "input", imp, "modelChoice", "Versatile (fluorescent nuclei)",
             "modelFile","/path/to/TF_SavedModel.zip",
             "normalizeInput",True, "percentileBottom",1, "percentileTop",99.8,
             "probThresh",0.5, "nmsThresh", 0.3, "outputType","Label Image",
             "nTiles",1, "excludeBoundary",2, "verbose",1, "showCsbdeepProgress",1, "showProbAndDist",0).get();
"""
from de.csbdresden.stardist import StarDist2D
import os
from glob import glob
#define input_folder as the top level folder with all the UNPROCESSED images in it make sure this has a forward slash on the end (if it can't find the directory of the images, it's likely because this this missing)
input_folder = os.path.expanduser('C:\Users\lmcalary\Desktop\CELL PROFILER\Inputs\Image Sets\Code Test\Plate 1')
input_folder = input_folder + '/'
print(input_folder)
#fill in the file identifier with whatever part of the filename that every image you want the script to pick up contains. i.e. it must be an identifier of ONLY the ones you wish to analyse, unique to these images.
file_identifier = 'ch00'

#this gathers the file PATH (the full directory in this case) for ALL of the .tif files in the input folder and puts them in a list we can loop over with the actual StarDist module(this is why it's important for you to make sure the input folder is correct and that it has only the images you don't want to analyse in each level underneath that top level)
image_paths = [[os.path.join('%s/%s' % (root, filename)) for filename in files if file_identifier in filename] for root, dirs, files in os.walk(input_folder)]
image_paths = [item for sublist in image_paths for item in sublist]


#just a checkpoint to make sure that the paths it's picking up are actually the ones you want to analyse :)
print(image_paths)


#below is a longer way of doing exactly what I've done in line 35! If the above line confuses you this unpacked version might help to see each step (if troubleshooting)
#def list_files(input_folder):
#    image_paths = []
#    for root, dirs, files in os.walk(input_folder):
#        for name in files:
#            image_paths.append(os.path.join(root, name))
#    return image_paths
#image_paths = list_files(input_folder)
#image_paths=[filename for filename in image_paths if ' ' in filename]


#this loop does the hard work! For every FILE PATH in the 'image_paths' directory, it grabs the folder it came from and the image name, reads it and does the prediction, then creates a new folder in your exports folder where the output can be saved
for img in image_paths:
	img = img.replace('\\', '/')
	path_data = img.split('/')[-2]
	print(path_data)
	name=img.split('/')[-1]
	print(name)
	output_folder = '%s%s/'% (input_folder, path_data)
	print(output_folder)
	img = io.open(img)
	res = command.run(StarDist2D, False,
            "input", img,
            "modelChoice", "Versatile (fluorescent nuclei)",
            ).get()
	label = res.getOutput("label")
	io.save(label, os.path.join(output_folder,"label_%s" %(name)))
