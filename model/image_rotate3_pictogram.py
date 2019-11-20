import os
from PIL import Image, ImageOps


# change channel 3 to 1 (grayscale)
# invert white / black
# resize 255,255 -> 48,48
# test  label 56

def folder_list(file_path):

    folder = os.listdir(file_path)
    folder.sort()
    label_list=[]

    for data_folder in folder:
        print("Working on {} folder..".format(data_folder))
        data_folder_path = os.path.join(file_path,'{}'.format(data_folder))
        data_folder_list = os.listdir(data_folder_path)
        data_folder_list.sort()
        label_list.append(data_folder)
        print(folder)
        #build fix folder
        target_path = '/home/mll/Capstone/pictogram_2'
        print("{} to {} dataset...".format(target_path, data_folder))

        #case is 3 train, vaild, test
        #image total 6000
        #train 5000 vaild 500 test 500

        count = 0
        for imagefile in data_folder_list:
            image = Image.open(data_folder_path+"/"+imagefile)
            save_image = image.resize((128,128),Image.ANTIALIAS)


            '''
            #image 7000
            if(count<6000):
                save_image.save(target_path + "/train/" + data_folder + "/" + imagefile, quality=100)
            elif (count > 6000 and count <= 6500):
                save_image.save(target_path + "/test/" + data_folder + "/" + imagefile, quality=100)
            elif (count > 6500 and count <= 7000):
                save_image.save(target_path + "/valid/" + data_folder + "/" + imagefile, quality=100)
                '''
            # image 6600
            if (count < 6000):
                save_image.save(target_path+"/" + imagefile, quality=100)
            elif (count >= 6000 and count < 6500):
                save_image.save(target_path + "/test/" + data_folder + "/" + imagefile, quality=100)
            elif (count >= 6500 and count < 6600):
                save_image.save(target_path + "/valid/" + data_folder + "/" + imagefile, quality=100)

            # image 15000
            '''
            if (count < 13000):
                save_image.save(target_path + "/train/" + data_folder + "/" + imagefile, quality=100)
            elif (count >= 13000 and count < 14000):
                save_image.save(target_path + "/test/" + data_folder + "/" + imagefile, quality=100)
            elif (count >= 14000 and count < 15000):
                save_image.save(target_path + "/valid/" + data_folder + "/" + imagefile, quality=100)
            '''


            image.close()
            save_image.close()
            count = count+1
        print("{} done!".format(data_folder))



def main():

    print("Image rorate start...")

    folder_list("/home/mll/Capstone/pictogram")
    #folder_list("/home/mll/Capstone/image_data/label_100_lateset/image_set")
if __name__ == "__main__":
    main()