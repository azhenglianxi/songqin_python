#$  git config --global user.name "azhenglianxi"
#$  git config --global user.email "azhenglianxi@163.com"
#$ git config --list


with open("2.txt","r") as fo:
    s=fo.readlines()
    print(s)
with open("2.txt","w") as  f:
    for i in range(1,100):
        f.write(str(i) + '\n')

