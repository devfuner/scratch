import argparse
import os
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument("zip_name", help="zip name")
parser.add_argument("source_path", help="source path")
parser.add_argument("-d", "--destination_path", help="destination path")

args = parser.parse_args()

zip_name = args.zip_name
source_path = os.path.abspath(args.source_path)

if args.destination_path:
    zip_name = os.path.join(args.destination_path, args.zip_name)

number = 1
temp_name = zip_name
while os.path.exists(temp_name):
    print("있음")

    file_name, ext = zip_name.split(".")
    print(file_name)
    print(ext)

    temp_name = file_name + "_" + str(number) + "." + ext

    print(temp_name)
    number += 1

zip_name = temp_name


# 지정한 파일이름과 같은 이름이 있으면?
    # 같은 파일이름을 덮어쓰고 생성됨
    # 같은 파일이름이 있을 경우 번호/날짜를 붙이는 방법을 만들어보세요.


jungle_zip = zipfile.ZipFile(zip_name, 'w')
for folder, subfolders, files in os.walk(source_path):
    # print('folder >', folder)

    for file in files:
        # print("\t", file)
        # print("\t1 >", os.path.join(folder, file))
        # print("\t2 >", os.path.relpath(os.path.join(folder, file), os.getcwd()))
        jungle_zip.write(
            os.path.join(folder, file)
            , os.path.relpath(os.path.join(folder, file), os.getcwd())
            , compress_type=zipfile.ZIP_DEFLATED)

jungle_zip.close()
