with open ("be_ziip_file1.txt","w+") as file:
    file.write("one file")
    file.close()

with open ("be_ziip_file2.txt","w+") as file:
    file.write("two file")
    file.close()

# on running the above code two txt files will be created

import zipfile

comp_file=zipfile.ZipFile("be_ziip_file1.zip","w")
#the above line will create a zip file

comp_file.write("be_ziip_file1.txt",compress_type=zipfile.ZIP_DEFLATED)
# now the zip file will contain the txt file created
comp_file.close()

#unzip a file
un_zip=zipfile.ZipFile("be_ziip_file1.zip","r")
un_zip.extractall("unzipfile")
#a folder unzipfile will be created which will contain one file
un_zip.close()


"""
to zip and unzip entire folder

import shutil
dir_to_zip="D://abc"
out_put_file_name= "example"
shulit.make_archieve(out_put_file_name,"zip",""dir_to_zip)
#example.zip will be created and this will contain all the files in the given path
shuilit.unpack_archieve('example.zip','unzip','zip')
#this will un zip and all the content of the zip will be extracted

"""