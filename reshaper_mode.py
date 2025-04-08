import work



label_names_line="names: "
num_labels_line="nc: "
train_line="train: "
val_line="val: "
test_line="test: "


def yolov11(data, outpath=None, labelname=None, labelnumber=None, newname=None, newnumber=None):
    train_dataset_path=""
    val_dataset_path=""
    test_dataset_path=""
    num_labels=0
    label_names_origin=[]
    names_origin_string=""
    label_names=[]
    with open(data, 'r') as data_description:
        data_content_list=[]
        data_content=data_description.read().splitlines()
        #print(data_content)
        for line_content in data_content: 
         
            if line_content.startswith(train_line):
                train_dataset_path=line_content[10:]
                

            if line_content.startswith(val_line):
                val_dataset_path=line_content[8:]

            if line_content.startswith(test_line):
                test_dataset_path=line_content[9:]
            
            if line_content.startswith(num_labels_line): 
                num_labels=int(line_content[4:])
                
            
            if line_content.startswith(label_names_line):
                names_origin_string=line_content[7:]
        

        names_origin_string=names_origin_string[1:-1]
        label_names_origin=names_origin_string.split(",")
        for name in label_names_origin:
            name=name[1:-1]
            if(name[0] == "'"):
                name=name[1:]
            label_names.append(name)
        #print(num_labels)
        #print(label_names)
        

    work.reshapelabel(train_dataset_path, val_dataset_path, test_dataset_path, num_labels, label_names, outpath, labelname, labelnumber, newname, newnumber)

