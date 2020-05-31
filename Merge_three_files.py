import glob
import datetime
folderfiles = glob.glob("*.txt")
 with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
     for files in folderfiles:
        with open(files, 'r') as f:
            file.write(f.read() + "\n")
