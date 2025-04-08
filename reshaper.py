import sys
from pathlib import Path


# receive a str, present the path of folder
def modify_files_in_a_folder(folder_path, origin_number, new_number):
    cnt = 0
    folder_path = folder_path[:len(folder_path)-6]+"labels"
    folder=Path(folder_path)

    for file in folder.glob("*.txt"):
        with open(file, "r") as f:
            lines = f.readlines()

        newlines = []
        #print(lines)
        for line in lines:
            number_list = line.split(" ")
            #print(number_list)
            if(int(number_list[0]) == origin_number):
                number_list[0] = str(new_number)
            number_list=' '.join(number_list)
            newlines.append(number_list)

        
        with open(file, "w") as f:
            f.writelines(newlines)
        cnt = cnt + 1

    print(f"{cnt} files have been reshaped.")


