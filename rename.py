import os

# Absolute path of a file
# old_name = r"sample.txt"
# new_name = r"new_sample.txt"

# Renaming the file
# os.rename(old_name, new_name)

# print(os.listdir())
value = os.listdir()
for i in value:
    print(i)

# verify file exist
print(os.path.isfile('file.txt'))