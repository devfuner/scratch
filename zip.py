import os
import zipfile

zip_name = 'zip_test.zip'
zip_path = './folder1'

jungle_zip = zipfile.ZipFile(zip_name, 'w')  # w 쓰기, r 읽기, a 추가
for folder, subfolders, files in os.walk(zip_path):

    for file in files:
        jungle_zip.write(
            os.path.join(folder, file)
            , os.path.relpath(os.path.join(folder, file), os.getcwd())
            , compress_type=zipfile.ZIP_DEFLATED)

jungle_zip.close()


jungle_zip = zipfile.ZipFile('/Users/devfuner/PycharmProjects/scratch/zip_test.zip')
jungle_zip.extractall('/Users/devfuner')
