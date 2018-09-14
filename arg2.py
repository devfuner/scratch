import argparse
import os
import zipfile
import datetime

# parser = argparse.ArgumentParser()
# parser.add_argument("zip_name", help="압축파일 이름을 지정하셔야 합니다.")
# parser.add_argument("source_path", help="압축 대상파일의 경로를 지정하셔야 합니다.")
# parser.add_argument("-d", "--destination_path", help="destination path")
#
# args = parser.parse_args()

# zip_name = args.zip_name
# source_path = os.path.abspath(args.source_path)
zip_name = "압축파일.zip"
source_path = "/Users/devfuner"

# if args.destination_path:
#     zip_name = os.path.join(args.destination_path, args.zip_name)

dt = datetime.date.today()

number = 1
temp_name = zip_name
while os.path.exists(temp_name):
    file_name, ext = zip_name.split(".")
    number_str = "{:0>3}".format(number)
    temp_name = file_name + "_" + str(dt) + "_" + number_str + "." + ext
    number += 1

zip_name = temp_name

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
