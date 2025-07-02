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
