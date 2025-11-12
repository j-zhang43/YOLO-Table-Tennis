import os
import sys


def make_file_struct():
    os.mkdir("data")
    os.mkdir("data/train_split")
    os.mkdir("data/test_split")


def main():
    if not os.isdir("data"):
        make_file_struct()

    if len(sys.argv) != 3:
        print("Usage: python split_train_test_data.py")
    


main()


