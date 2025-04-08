

label_names_line = "names: "
num_labels_line = "nc: "
train_line = "train: "
val_line = "val: "
test_line = "test: "


def read_description_yolov11(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    

    content_train = ""
    content_val = ""
    content_test = ""
    labels_amount = 0
    labels_list = []
    for line in lines:
        if line.startswith(train_line):
            content_train = line.split(" ")[1]

        if line.startswith(val_line):
            content_val = line.split(" ")[1]

        if line.startswith(test_line):
            content_test = line.split(" ")[1]

        if line.startswith(num_labels_line):
            labels_amount = int(line.split(" ")[1])

        if line.startswith(label_names_line):
            labels_list = line.split(" ")[1:]
            labels_list = ''.join(labels_list)[1:-2].split(",")
            temp = []
            for label in labels_list:
                label = label[1:-1]
                temp.append(label)
            labels_list = temp
            #labels_list = line.split(" ")[1][1:-1].split(",")
            #for label in labels_list:
             #   label=label[1:-1]

    '''
    print(content_train)
    print(content_val)
    print(content_test)
    print(labels_amount)
    print(labels_list)
    '''
    return content_train, content_val, content_test, labels_amount, labels_list


