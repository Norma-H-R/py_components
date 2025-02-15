from django.db import models
import requests
import uuid
import base64
import datetime
import os
# Create your models here.
# gitee 参数
access_token = 'a3fe5f8274af2f9dc48e26f2b982be2c'
owner = 'dkiss_home'
repo = 'picture-bed'
message = '上传'
local_file_path = r'C:\test\upload_file\qq.png'
# 文件名
file_name = ''
# 原始文件名
origin_file_name = ''
# 文件id
file_id = ''
# 上传用户
up_user = ''
# 上传用户id
up_id = ''
# 文件大小
file_size = ''
# 文件类型
file_extension = ''
# 上传日期
up_date = ''
# 上传ip
up_ip = ''

class UserUploadModel(models.Model):
    file = models.FileField(upload_to='userfiles/')

    file_extension = local_file_path.split('.')[-1]
    file_name = f"{uuid.uuid4().hex}.{file_extension}"
    origin_file_name = os.path.split(local_file_path)[-1]
    file_id = uuid.uuid4().hex[:7] 
    up_user = 'Anjou'
    up_id = '1'
    file_size = os.path.getsize(local_file_path)
    up_date = datetime.datetime.now()
    up_ip = requests.get('http://myip.ipip.net', timeout=5).text

    print('文件名:', file_name)
    print('原始文件名:', origin_file_name)
    print('文件id:', file_id)
    print('上传用户:', up_user)
    print('上传用户id:', up_id)
    print('文件大小:', file_size)
    print('上传日期:', up_date)
    print('上传ip:', up_ip)
    print('文件类型:', file_extension)
    print('文件位置:', local_file_path)
    def __str__(self):
        return self.name
    
    
        
    

    