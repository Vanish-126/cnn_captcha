import os
import re
import time
import requests

# url = 'https://e.uc.cn/sso/auth.jpg?now=1584706203447'
# url = 'https://cas.caohua.com/cas/captcha?id=cbcbb6ee-3c3e-4420-b270-a673414ea8d5'
url = 'http://172.16.163.17:8089/cas/yanzhengma/captcha?id=cbcbb6ee-3c3e-4420-b270-a673414ea8d5'
# url = 'https://cas.baidu.com/?action=image2&appid=3'
header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
root_dir = "F:\\workspace\\python\\cnn_captcha\\images_back\\cas.caohua1.com\\"

# root_dir = "F:\\workspace\\python\\cnn_captcha\\sample\\origin\\"
count = 15000

def gen_special_img(i, folder):
    # 请求
    while True:
        try:
            response = requests.get(url=url, headers=header)
            set_cookie = response.headers['Set-Cookie']
            array = re.split('[;,]',set_cookie)
            stamp = time.time()*1000
            file_name = os.path.join(folder, '{}_{}.{}'.format(array[0].split('=')[1], int(stamp), 'jpg'))
            # print(file_name)
            if response.content:
                break
            else:
                print('retry, response.content is empty')
        except Exception as err:
            print(err)
    
    # 保存图片
    with open(file_name, 'wb') as fp:
        fp.write(response.content)
        fp.close()

def main():
    # 判断文件夹是否存在
    if not os.path.exists(root_dir):
        os.makedirs(root_dir)

    for index, i in enumerate(range(count)):
        gen_special_img(i, root_dir)
        print("Generate captcha image => {}".format(index + 1))

if __name__ == "__main__":
    main()