# Fly online in NBU

循环检测内网下是否有网，如果没网就登录NBU账号，保持在线。

**声明**

* 本项目仅供学习使用，请勿用于非法用途
* 本项目基于师兄的程序二次开发，以学习语言特性为目的对项目进行了重构

**安装**

* 1.git clone https://github.com/QiangZiBro/flyOnline
* 2.pip install -r requirements.txt
* 3.下载geckodriver并将其放在系统环境中。
  * `need`已有linx/windows的geckodriver安装包，解压之
  * Linux/Mac下  `export PATH=$PATH:your_geckodriver_path`
  * Windows下 将geckodriver放进系统变量里 
* 4.安装火狐浏览器
* 5.新建一个文件`zm.txt`，每行格式：`password,id`

**使用**

* `python main.py --file zm.txt`

