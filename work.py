import wrong
import sys
import yaml
from pathlib import Path

def modify_files(folder_path,labelnumber,newnumber):
    folder_path=folder_path[:len(folder_path)-6]+"labels"
    #print(folder_path)
    
    folder=Path(folder_path)

    for file in folder.glob("*.txt"):
        #print(f"open the {file.name}")
        with open(file,"r") as f:
            lines=f.readlines()
        #print(lines)
        newlines=[]
        for line in lines:
            #print(line)
            if(line[0]==str(labelnumber)):
                #print("find 0.")
                line=str(newnumber)+line[1:]
                #print(f"reshape to {line}")
            #print(line)
            newlines.append(line)
        #print(newlines)    
        with open(file,"w") as f:
            f.writelines(newlines)
        
    


def reshapelabel(train_dataset_path, val_dataset_path, test_dataset_path, num_labels, label_names, outpath=None, labelname=None, labelnumber=None, newname=None, newnumber=None):
    flag_change_number=1
    flag_rename=1
    flag_train=0
    flag_val=0
    flag_test=0

    if(train_dataset_path=="" and val_dataset_path=="" and test_dataset_path==""):
        wrong.no_sources_yolov11()
        sys.exit()

    if(num_labels==0 or label_names==[]):
        wrong.no_label_yolov11()

    if(labelnumber==None):
        labelnumber=label_names.index(labelname)
        #print(labelnumber)

    if(labelname==None):
        labelname=label_names[labelname]
    


    if(newname==None):
        newname=labelname
        flag_rename=0

    if(newnumber==None):
        newnumber=labelnumber
        flag_change_number=0

    new_list=label_names
    new_list[labelnumber]=newname




    if(flag_change_number==1):        
        if(train_dataset_path!=""):
            modify_files(train_dataset_path,labelnumber,newnumber)
            flag_train=1
            print("train-set has reshaped.")
        else:
            print("train-set not found.")

        if(val_dataset_path!=""):
            modify_files(val_dataset_path,labelnumber,newnumber)
            flag_val=1
            print("val-set has reshaped.")
        else:
            print("train-set not found.")

        if(test_dataset_path!=""):
            modify_files(test_dataset_path,labelnumber,newnumber)
            flag_test=1
            print("test-set has reshaped.")
        else:
            print("train-set not found.")
    else:
        print("no need to change_number.")


        
    with open("new_data.yaml","w") as f:
        f.write(f"train: ../{train_dataset_path[:len(train_dataset_path)-6]+'images'}\n")
        f.write(f"val: ../{val_dataset_path}\n")

        f.write(f"test: ../{test_dataset_path}\n")
        f.write(f"nc: {num_labels}\n")
        f.write(f"names: {new_list}\n")
        

        if(flag_rename==1):
            f.write(f"the '{labelname}' is renamed to '{newname}'")
        if(flag_change_number==1):
            f.write(f"the number of '{labelname}' is reshape to {newnumber}")

    print("'new_data.yaml' has generated.")



    


