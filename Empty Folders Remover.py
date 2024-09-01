import os, shutil


pwd = os.getcwd()

# will list evey dir in the pwd
folders = [i for i in os.listdir(pwd) if os.path.isdir(os.path.join(pwd, i))]


for folder in folders:
    if os.listdir(folder):
        for file in os.listdir(folder):
            shutil.move(os.path.join(pwd, folder, file), pwd)
  

for folder in folders:
    if not os.listdir(folder):
        os.rmdir(folder)

types = []

for file in os.listdir(pwd):
    # print(file)
    if not os.path.splitext(file)[1] in types and (os.path.splitext(file)[1] != ''):
        types.append(os.path.splitext(file)[1])
        # print(types)
        
        
for file in os.listdir(pwd):
        print(file)
        print(os.path.splitext(file))
        print(os.path.splitext(file)[1] != '')
        break
        
        
for folder in types:
    os.mkdir(folder)

image = []

# types.remove(".py")
# types.remove(".python")

for item in [".py", ".python"]:
    types.remove(item)
            
for Type in types:
    for file in os.listdir(pwd):
        if os.path.splitext(file)[1] == Type and (os.path.splitext(file)[1] != ''):
            shutil.move(os.path.join(pwd, file),
                        os.path.join(pwd, Type))
  

        