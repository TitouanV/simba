"""
"simba" is for "Sort IMage By Alt"
Software that allows to sort images according to their altitude contained in the EXIF data.

Usage:
======
    python3 simba.py --image_dir=argument1 --ref_alt=argument2

    argument1: a string corresponding of the path of the directory where the image are stored.
    argument2: a int number corresponding to the reference altitude where the image have been taken.
"""

__authors__ = ("Titouan VERDU")
__contact__ = ("titouan.verdu@isen-ouest.yncrea.fr")
__copyright__ = "GNU GPL-3.0"
__date__ = "2025-07-02"
__version__ = "1.0.0"

from PIL import Image
import exifread
import os
import shutil
import argparse

# Define the parser
parser = argparse.ArgumentParser(description='Parse image directory and reference altitude')

# Declare an argument (`--image_dir`) and (`--ref_alt`), saying that the 
# corresponding value should be stored in the `image_dir` and `ref_alt` 
# fields, and using a default value if the argument isn't given
parser.add_argument('--image_dir', action="store", dest='image_dir', default=r"C:\Users")
parser.add_argument('--ref_alt' , action="store", dest='ref_alt', default=0)

# Now, parse the command line arguments and store the 
# values in the `args` variable
args = parser.parse_args()

def sort_image_by_altitude(image_directory_path, reference_altitude):
    """This function will search in a directory filled with images the GPS Altitude information
    of each images in the EXIF and will create repertory and move the image according to the
    relative altitude calculated
    
    Parameters
    ----------
    image_directory_path : str
        The path of the directory where the image are stored.
    reference_altitude : int
        The reference altitude where the image have been taken.

    Returns
    -------
    
    None

    """

    #Init previous altitude
    previous_altitude = 0

    #Pass through all the image of a directory
    for image_name in os.listdir(image_directory_path):

        print("____________________________________________________________________________")
        
        #Join the image name with the directory path
        image_path = os.path.join(image_directory_path, image_name)

        #Open the file in read mode
        with open(image_path, 'rb') as image_file:
            #Read the EXIF of the image
            #avoid details, avoid thumbnail extraction, 
            #return dictionnary with values in built-in Python types
            #stop processing file after tag "GPS GPSAltitude"
            tags = exifread.process_file(image_file, details=False, extract_thumbnail=False
                , builtin_types=True, stop_tag="GPS GPSAltitude")
            if tags:
                #Get the value link to the "GPS GPSAltitude" Key
                altitude = tags["GPS GPSAltitude"]
                #Process the relative altitude according to the reference
                #altitude given in argument
                relative_altitude = int(altitude)-reference_altitude

                print(f"Image : {image_name} | Real Altitude : {relative_altitude}m")

            else:
                print("No EXIF data found.")


        #if the relative altitude processed is ±1 the previous altitude do nothing
        if ((relative_altitude - previous_altitude <= 1) and 
            (relative_altitude - previous_altitude >= -1)):
            print(f"Save image in the previous directory : Altitude_{str(previous_altitude)}")

        #if the relative altitude is different of the previous altitude
        #create new directory with the name of this new relative altitude
        #give the value of the new realtive altitude to the previous_altitude variable
        else :
            print(f"Create new directory and save image in : Altitude_{str(relative_altitude)}")
            new_dir_path=os.path.join(image_directory_path,
                ("Altitude_" + str(relative_altitude)))
            if not os.path.exists(new_dir_path):
                os.makedirs(new_dir_path)

            previous_altitude = relative_altitude

        #create the new path of the image and change it
        #according to the relative altitude of the image
        new_image_path=os.path.join(new_dir_path,image_name)
        shutil.move(image_path,new_image_path)

        print("____________________________________________________________________________")

if __name__ == "__main__":
    print("############################################################################")
    print("Function call with the argument :")
    print(f"- directory path : {args.image_dir}")
    print(f"- reference altitude : {args.ref_alt}m")
    print("############################################################################")


    sort_image_by_altitude(args.image_dir, int(args.ref_alt))
