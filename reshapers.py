from tqdm import tqdm
import wrong
import sys
import reshaper_mode

def detect_mode(mode, data, outpath=None, labelname=None, labelnumber=None, newname=None, newnumber=None):
    if(mode == "yolov11"):
        reshaper_mode.yolov11(data, outpath, labelname, labelnumber, newname, newnumber)
    else:
        print(f"command wrong. mode type wrong or we don't support the mode of '{mode}' now.")



def reshaper(mode, data, outpath=None, labelname=None, labelnumber=None, newname=None, newnumber=None):
    
    if(labelname == None and labelnumber == None):
        wrong.both_lack1()
        sys.exit()
    #if(newname ==None and newnumber == None):
     #   wrong.both_lack2()
    detect_mode(mode, data, outpath, labelname, labelnumber, newname, newnumber)

    

    







