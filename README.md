# AutoBackup

This tool can help you to auto back up the documents from flash disk to server and local disk.

It will running in the background with silent mode.

1. Change the configure in autobacksftp.py

   ```python
   host = ""  #Your server IP
   user = "" # Your ssh user/name
   pwd = "" #Your password
   target_dir = ''  # Your local target dir
   ```

   ​


1. Install Paramiko module

   ```bash
   pip install paramiko
   ```

2. Install win32file module

   Download file which match your python version in [http://starship.python.net/~skippy/win32/Downloads.html](http://starship.python.net/~skippy/win32/Downloads.html)

3. Package your python script to exe

   ```bash
   pip install pyinstaller
   pyinstaller autobacksftp.py -F -w
   ```

4. The autobacksftp.exe will generate in dist dir

