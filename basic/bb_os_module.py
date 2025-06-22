"""
pwd = current working directory


"""
import os
print(os.getcwd()) # D:\Dev\Python\PythonInDetails\basic

print(os.listdir()) # it will give all the files in that dir
print("2222222222")
print(os.listdir("D:\\dev"))
#['.idea', '12Nov-2020 Mobile', 'apache-log4j-2.17.2-bin', 'apache-maven-3.8.5', 'chromedriver_win32', 'jar', 'JavaTutorial', 'Naveen Automationlabs', 'Postman-win64-Setup.exe', 'Python', 'Selenium', 'SpringBoot', 'SpringBootUdem
# /y']

print("3333333333")

"""
to move files 
import shutil
shutil.move('text.txt','D:\\dev')


to delete files
os.unlink(path) -> single file delete
os.rmdir(path) -> remove single dir
shutil.rmtree(path) -> removes all files and folder

"""