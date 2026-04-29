
import os
os.chdir(r"C:\Users\DIVY\OneDrive\Desktop\Qspider\A19(py)")

# with open("file_handling.txt") as f:
#     print(f.read())

# with open("file_handling.txt",'a') as f:
#     f.writelines("\najhgafha sagusygja  vaygsfjh agdjhb \n")

#~changing the file type txt -> csv 
#~ then change file name 
# with open("file.csv", 'x') as f:
#     f.write("ajbjsah ahsjhja habjbsaj ")
 
#~ reading the file
# with open("file.csv", 'r') as f:
#     print(f.read())

#~ file using reader()
# import csv
# with open("file.csv", 'r') as f:
#     reader = csv.reader(f)
#     for i in reader:
#         print(i)


#~ file using dictreader() in the form of tabular format so it will give us key: value format
import csv
with open("file.csv", 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['hello'],row[''])
