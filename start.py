import read_description
import reshaper
import wrong

def start(mode, data, outpath=None, labelname=None, labelnumber=None, newname=None,newnumber=None):
    if(mode == "yolov11"):
        flag_rename = 0
        flag_change_number = 0
        content_train, content_val, content_test, labels_amount, labels_list = read_description.read_description_yolov11(data)
        
        if(labelname == None and labelnumber == None):
            wrong.both_lack1()
            sys.exit()

        if(labelname == None):
            labelname = labels_list[labelnumber]

        if(labelnumber == None):
            labelnumber = labels_list.index(labelname)

        new_list = labels_list

        if(newname != None):
            new_list[labelnumber] = newname
            flag_rename = 1
        else:
            newname = labelname

        if(newnumber != None):
            dict={}
            for i in range(0,len(new_list)):
                dict[new_list[i]] = i 
                
            dict[newname] = newnumber
            flag_change_number = 1
            
            if(content_train != ""):
                train_folder = content_train[3:len(content_train)-7] + "labels"
                print(train_folder)
                reshaper.modify_files_in_a_folder(train_folder, labelnumber, newnumber)
                print("train-set labels have been reshape.")
            else:
                print("train-set not found.")

            if(content_val != ""):
                val_folder = content_val[3:len(content_val)-7] + "labels"
                reshaper.modify_files_in_a_folder(val_folder, labelnumber, newnumber)
                print("val-set labels have been reshape.")
            else:
                print("val-set not found.")

            if(content_test != ""):
                test_folder = content_test[3:len(content_test)-7] + "labels"
                reshaper.modify_files_in_a_folder(test_folder, labelnumber, newnumber)
                print("test-set labels have been reshape.")
            else:
                print("test-set not found.")
            with open("new_data.yaml","w") as f:
                f.write(f"train: {content_train}\n")
                f.write(f"val: {content_val}\n")

                f.write(f"test: {content_test}\n")
                f.write(f"nc: {labels_amount}\n")
                f.write(f"names: {new_list}\n")
        

                if(flag_rename==1):
                    f.write(f"the '{labelname}' is renamed to '{newname}'")
                if(flag_change_number==1):
                    f.write(f"the number of '{labelname}' is reshape to {newnumber}")

                f.write(str(dict))

        else:
            print(f"command wrong. mode type wrong or we don't support the mode of '{mode}' now.") 

