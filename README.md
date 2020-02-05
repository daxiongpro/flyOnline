# Fly online in NBU

**声明**
* 本项目仅用于学习用途，请不要扩散
* 本项目基于师兄的程序二次开发，以学习语言特性为目的

**使用方法**
* 新建一个文件，每行格式：`password,id`
* `python detect.py --file your_pw_id_file`

**TODO**
* `TimeoutException: Message: Timeout loading page after 300000ms`,解决思路：进行错误捕捉，如果不能加载则重新登录网址
