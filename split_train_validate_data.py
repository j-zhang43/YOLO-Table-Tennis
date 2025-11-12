import os
import sys
import random
import time
import shutil

def make_file_struct():
    os.mkdir("data")

    os.mkdir("data/train")
    os.mkdir("data/train/images")
    os.mkdir("data/train/labels")
    
    os.mkdir("data/validation")
    os.mkdir("data/validation/images")
    os.mkdir("data/validation/labels")

def main():
    if not os.path.isdir("data"):
        make_file_struct()
    else:
        print("data already made")
        return 1

    if len(sys.argv) != 2:
        print(sys.argv)
        print("Usage: python split_train_test_data.py")
        return 1

    random.seed(time.time())

    TRAIN_SPLIT = .9
    images_names = os.listdir(f"{os.getcwd()}/{sys.argv[1]}/images")
    random.shuffle(images_names)
    images_names = [name.split(".png")[0] for name in images_names]


    for i in range(len(images_names)):
        if i < int(len(images_names)*TRAIN_SPLIT):
            shutil.copy(f"{os.getcwd()}/{sys.argv[1]}/images/{images_names[i]}.png", f"{os.getcwd()}/data/train/images")
            shutil.copy(f"{os.getcwd()}/{sys.argv[1]}/labels/{images_names[i]}.txt", f"{os.getcwd()}/data/train/labels")
        else:
            shutil.copy(f"{os.getcwd()}/{sys.argv[1]}/images/{images_names[i]}.png", f"{os.getcwd()}/data/validation/images")
            shutil.copy(f"{os.getcwd()}/{sys.argv[1]}/labels/{images_names[i]}.txt", f"{os.getcwd()}/data/validation/labels")


    print(f"Train Count: {len(os.listdir(f"{os.getcwd()}/data/train/images"))}")
    print(f"Validation Count: {len(os.listdir(f"{os.getcwd()}/data/validation/images"))}")
            
            

main()


