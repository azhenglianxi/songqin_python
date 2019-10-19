file1_txt = 'file1.txt'
file2_txt = 'file2.txt'
file1_txt = file1_txt.strip()
with open(file1_txt) as file, open(file2_txt, 'w')as file2:
    filereads = file.read().splitlines()
    for i in filereads:
        if i.count(';') != 1:  # 补 未考虑到 存在多个的情况
            continue
        names, salarys = i.split(';')  # 补：未考虑到 存在多个的情况
        if names.count(':') != 1:
            continue
        if salarys.count(':') != 1:  # 补：未考虑到 存在多个的情况
            continue
        name = names.split(':')[1].strip()
        salary = int(salarys.split(':')[1].strip())

        income = int(salary * 0.9)
        tax = int(salary * 0.1)
        result = f"{{'name':{name}, 'salary':{salary},'income':{income},'tax':{tax}}}"
        print(result)

data = f"{{'name':{name}}}"
