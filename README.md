# simba
"simba" stands for "Sort IMage By Alt". 

It is a short python script that sorts the images contained in a directory according to the altitude at which they were taken. 
By reading the EXIFS data for each image, the script creates folders at different altitudes and places the images in them.

For this script, you will need to install two python libraries : 
- Pillow
- ExifRead
  
You can do this with the following pip command :
```
pip install Pillow exifread
```

To use this script, please refer to the following template :
```
python3 simba.py --image_dir=argument1 --ref_alt=argument2
```
with :
- argument1: a string corresponding of the path of the directory where the image are stored.
- argument2: a int number corresponding to the reference altitude where the image have been taken.

Example :
```
python3 simba.py --image_dir=C:\Users\ImagesDirectory --ref_alt=180
```

For more informations and explanations of how the code is working, please read the comments directly in the script.
