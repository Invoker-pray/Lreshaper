import argparse
import start

def main():
    parser = argparse.ArgumentParser(description="reshape your dataset's labels.")

    parser.add_argument('--mode', required = True, help = "Choose the type of the dataset.")
    parser.add_argument('--outpath', help = "Choose the output files path you want to store at.")
    parser.add_argument('--labelname', required = False, help = "The label name you want to reshape.")
    parser.add_argument('--newname', required = False, help = "The label name you want to rename to, if none, will not change.")
    parser.add_argument('--labelnumber', required = False, help = "THe label number you want to reshape.")
    parser.add_argument('--newnumber', required = False, help = "The label number you want to change to.")
    parser.add_argument('--data', required = True, help = "The path of data description such as data.yaml in yolov11.")



    args = parser.parse_args()
    start.start(args.mode, args.data, args.outpath, args.labelname, args.labelnumber, args.newname, args.newnumber)





if __name__ == "__main__":
    main()
