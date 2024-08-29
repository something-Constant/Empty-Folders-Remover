import os

pwd = os.getcwd()

# will list evey dir in the pwd
folders = [i for i in os.listdir(pwd) if os.path.isdir(os.path.join(pwd, i))]

EmptyFolder = []

for folder in folders:
    if not os.listdir(folder):
        # EmptyFolder.append(folder)
        os.rmdir(folder)
        
        
# for folder in EmptyFolder:
#     os.rmdir(folder)
