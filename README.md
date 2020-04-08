## django项目
   对于python项目的管理，最好使用虚拟环境，防止不同版本的python的报错
   ### 虚拟环境的创建
   两种方法，一种是使用virtualenv，一种是pipenv，我使用pipenv
   全局安装pipenv，然后进入到文件夹，使用pipenv install
   安装后，使用pipenv shell激活，这样在这个文件夹创建的项目，就处于虚拟环境中了
   ### django项目的创建
   使用django-admin startproject projectname就可以了
   ### 应用的创建
   进入项目文件夹(就是存在manage.py的文件夹)使用python manage.py startapp appname就可以了
   ### 展示一个html的方法
   先将应用添加到项目中，在settings.py中INSTALLED_APPS添加
   在应用的views.py里面创建路由，然后添加到urls.py里面
   ### 拆分静态的(css、js、images)放入到static，html放入到templates之下
   两种方案：1. 放入到对应的app下面
             2. 放入到全局的template和static目录之下
             配置全局的static问价访问路径的配置：
             STATICFILES_DIRS = [
                os.path.join(BASE_DIR, 'static')
            ]
## django项目连接mysql创建表生成迁移的bug
   django2.1版本之后，就已经不支持mysql5.5了，所以会报错：....(6) NOT NULL...之类
   修正的方法有两个：1. 将mysql升级到5.6之后
                    2. 将django版本更改到2.0

## django项目连接mysql生成数据表名称规则：应用名称_模型名
  如果想要更改为自己命名的表名，需要在模型中使用db_table = "message"           
  然后再重新运行：
   python manage.py makemigrations
   python manage.py migrate 即可更改成功