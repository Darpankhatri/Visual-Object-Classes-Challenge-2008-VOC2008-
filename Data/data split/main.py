import shutil
import os


folder_path = "D:\Fast\Semester 8\DLP\project\Train data\VOC2008\JPEGImages"


# get data file name
def get_data(file_name):
    data_list = []
    type_file_name = []
    type_file_name.append(file_name)
    type_file_name.append(file_name.replace("_train","_trainval"))
    type_file_name.append(file_name.replace("_train","_val"))

    for n in type_file_name:
        my_file = open(n, "r")
        data = my_file.read()

        data_into_list = data.split("\n")
        
        i = 0
        for s in data_into_list:
            if s.find(" 1") != -1:
                car_s = data_into_list[i]
                car_s = car_s.replace(" 1",".jpg")
                if(car_s not in data_list):
                    data_list.append(car_s)
            i+=1
        my_file.close()
    return data_list
# get data file name

aero_data_list = get_data("aeroplane_train.txt")
bicycle_data_list = get_data("bicycle_train.txt")
bird_data_list = get_data("bird_train.txt")
boat_data_list = get_data("boat_train.txt")
bottle_data_list = get_data("bottle_train.txt")
bus_data_list = get_data("bus_train.txt")
car_data_list = get_data("car_train.txt")
cat_data_list = get_data("cat_train.txt")
chair_data_list = get_data("chair_train.txt")
cow_data_list = get_data("cow_train.txt")
diningtable_data_list = get_data("diningtable_train.txt")
dog_data_list = get_data("dog_train.txt")
horse_data_list = get_data("horse_train.txt")
motorbike_data_list = get_data("motorbike_train.txt")
person_data_list = get_data("person_train.txt")
pottedplant_data_list = get_data("pottedplant_train.txt")
sheep_data_list = get_data("sheep_train.txt")
sofa_data_list = get_data("sofa_train.txt")
train_data_list = get_data("train_train.txt")
tvmonitor_data_list = get_data("tvmonitor_train.txt")


jpg_files = []

for file in os.listdir(folder_path):
    if file.endswith(".jpg"):
        jpg_files.append(file)
# print(jpg_files[:10])


for file in jpg_files:
    if(file in aero_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Aeroplane/"+file)
    elif(file in bicycle_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Bicycle/"+file)
    elif(file in bird_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Bird/"+file)
    elif(file in boat_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Boat/"+file)
    elif(file in bottle_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Bottle/"+file)
    elif(file in bus_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Bus/"+file)
    elif(file in car_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Car/"+file)
    elif(file in cat_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Cat/"+file)
    elif(file in chair_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Chair/"+file)
    elif(file in cow_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Cow/"+file)
    elif(file in diningtable_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Diningtable/"+file)
    elif(file in dog_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Dog/"+file)
    elif(file in horse_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Horse/"+file)
    elif(file in motorbike_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Motorbike/"+file)
    elif(file in person_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Person/"+file)
    elif(file in pottedplant_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Pottedplant/"+file)
    elif(file in sheep_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Sheep/"+file)
    elif(file in sofa_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Sofa/"+file)
    elif(file in train_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Train/"+file)
    elif(file in tvmonitor_data_list):
        shutil.copyfile(folder_path+"\\"+file,"Tvmonitor/"+file)
    
print("Done")
