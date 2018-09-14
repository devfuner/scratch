import os
import zipfile
import sys

# print(sys.argv[0])
# print(sys.argv[1])  # zip file name
# print(sys.argv[2])  # zip paht

# zip_name = 'zip_test.zip'
# zip_path = './folder1'
zip_name = sys.argv[1]
zip_path = sys.argv[2]
print(zip_name)
print(zip_path)

jungle_zip = zipfile.ZipFile(zip_name, 'w')
for folder, subfolders, files in os.walk(zip_path):

    for file in files:
        jungle_zip.write(
            os.path.join(folder, file)
            , os.path.relpath(os.path.join(folder, file), os.getcwd())
            , compress_type=zipfile.ZIP_DEFLATED)
