#this is reallyy bad, but it works. Only works on your own private computers. Mobile devices not so much. 

#USE COLLABORATORY TO SEND DATA FROM CODE TO GOOGLE DRIVE



#https://cloud.google.com/storage/docs/gsutil/commands/web?authuser=1 
#https://replit.com/talk/ask/Can-I-use-localhost/32252

#pip install pydrive

from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


gauth = GoogleAuth()
app = gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)



a = drive.CreateFile({'title: name.file'})
a.SetContentString('Hello World! \n I eat booty Cheeks')
x = input('which file?')

x.upload()

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))