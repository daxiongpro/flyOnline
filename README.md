# Fly online in NBU

**声明**
* 本项目仅用于学习用途，请不要扩散
* 本项目基于师兄的程序二次开发，以学习语言特性为目的

**使用方法**
* pip install -r requirements.txt
* geckodriver在`need`内选择对应系统的安装包，安装方法[win](https://blog.csdn.net/hy_696/article/details/80114065),linux(https://www.jianshu.com/p/cf5cec282956)
* 需要安装火狐浏览器
* 新建一个文件，每行格式：`password,id`
* 运行：`python detect.py --file your_pw_id_file`

**TODO**
* `TimeoutException: Message: Timeout loading page after 300000ms`,解决思路：进行错误捕捉，如果不能加载则重新登录网址
