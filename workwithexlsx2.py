import os, zipfile, openpyxl
zf = zipfile.ZipFile('rogaikopyta.zip', 'r')
zf.extractall('rogaikopyta')
zf.close()
print(os.listdir())
os.chdir(r'D:/MyUniversity/Python ВШЭ/rogaikopyta')
total = []
for files in os.listdir():
    exel = openpyxl.load_workbook(files)
    sheet = exel.active
    total.append([sheet['b2'].value, sheet['d2'].value])
with open(r'D:/MyUniversity/Python ВШЭ/rogaikopyta.txt', 'w', encoding='utf-8') as outfile:
    for el in sorted(total):
        print(*el, file=outfile)


# dir1 = os.getcwd()
# print(type(dir1))
# print(os.listdir())