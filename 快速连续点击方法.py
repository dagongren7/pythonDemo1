import os
import time

path = r'C:/Users/admin/Desktop/batch.bat'
for i in range(10): #循环打开dianji.bat10次，
    time.sleep(2)
    os.startfile(path)