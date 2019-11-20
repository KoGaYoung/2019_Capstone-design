import os
from PIL import Image, ImageOps






def main():

    f = open("/home/mll/Capstone/2019_Capstone-design/model/save_model/label_dict.txt", 'r')

    while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()
    #for
    #result_file.write("{}'s vector mean\n".format(app_folder_name))
    print("asd")

if __name__ == "__main__":
    main()