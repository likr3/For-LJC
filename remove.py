from PIL import Image
#currDir = 'C:\Users\liker\PycharmProjects\untitled'

import os
def removeFile(dir,postfix):
    if os.path.isdir(dir):
        for file in os.listdir(dir):
            removeFile(dir+'/'+file,postfix)
    else:
        if os.path.splitext(dir)[1] == postfix:
            os.remove(dir)






removeFile('./','.tmp')
removeFile('./','.jpg')