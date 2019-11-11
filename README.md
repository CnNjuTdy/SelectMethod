### 本地部署

优点：速度快

缺点：只能局域网访问

步骤（这里仅给出macos的步骤）
1. 打开终端，如果没有homebrew，自行百度安装
2. 如果没有python3: `brew install python3`
3. 进入app.py所在目录: `pip3 install -r piplist.txt`
4. 查询自己的内网ip，具体办法是

![image-20191111185711674](/Users/tangdaye/Library/Application Support/typora-user-images/image-20191111185711674.png)

5. 命令行输入`python3 app.py xxx.xxx.xxx.xxx`
6. 其他人可以直接访问`xxx.xxx.xxx.xxx:5000`来访问应用
7. 每个人做完以后的结果会保存在static/result.csv中，每人是一行，这个文件可以直接用excel打开

### 远端部署

优点：简单省事

缺点：不稳定

目前已经部署好了，外网地址是http://106.15.184.76:5000/

警告：这个是我的服务器，服务器不稳定，使用要谨慎

获取结果方法：http://106.15.184.76:5000/static/result.csv

使用chrome浏览器可以直接下载这个文件，也可以联系我索取