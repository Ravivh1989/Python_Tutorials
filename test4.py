import os

def get_files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file


for file in get_files(r'D:\Ravi'):
    print(file)




    


