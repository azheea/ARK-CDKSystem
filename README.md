
# Arknight-CDKeySystem 外置CDKey

Arknight-CDKeySystem 是一个 Arknight 外置系统, 你可以用它来轻松的兑换和分发游戏的CDKey

前端页面源自[blueyst](https://github.com/blueyst/blueyst.github.io)

原始代码来自[赵苦瓜](https://github.com/Zhaokugua/Grasscutter-CDKeySystem)，感谢他的工作！

同样使用本项目接口的QQ频道机器人，[仓库](https://github.com/azheea/ArkNightBot)

Arknight 服务端的作者为江澄，感谢他的工作！
## 💡Feature

- [x] **连接服务端.**
- [x] **CDKey兑换(角色)**  - 玩家可以兑换已经生成的CDKey.
- [x] **CDKey生成**  - 管理者可以生成CDKey的内容，支持批量生成。
- [x] **自定义背景图** - 可以自定义页面的背景图链接（比如随机图）
- [ ] **CDKey兑换(物品/物品&角色)**  - 即将支持.
- [ ] **每日签到**  - 签到系统.
- [ ] **更多**  - Comming soon...

## 🍗Setup
### 安装


#### 连接Arknight：

1. 下载[某个服务端](https://github.com/azheea/ARK-CDKSystem/blob/main/hypergryph-1.9.3.zip)
2. 启动服务器，配置文件会自动在你的服务器文件夹下生成 `config.json` 文件夹。
3. 打开并编辑 `config.json`。
4. 设置 `GMkey` 的值为你的连接秘钥，建议使用至少32字符的长随机字符串。
5. 安装Python3和依赖包：
```shell
pip install django
```
6. 下载本仓库到服务器，打开并编辑`app`文件夹里的`CONSTANTS.py`文件。
7. 设置服务器地址、服务端的GMkey和自定义密码，保存

```python
# 设置服务端的GMkey
Server_token = 'GMKey_value'

# 设置服务器地址，不带后边的/
Server_addr = 'https://127.0.0.1'

# 设置登录认证的密码
auth_pwd = 'Azhegod'
```
9. 在项目目录运行
```shell
python manage.py runserver 0.0.0.0:8000
```
即可在8000端口访问到页面。



### 使用
设置CDKey的地址：/cdk_create

进入需要验证密码，即刚刚设置的`auth_pwd`

可以设置单个CDKey的使用次数

执行的命令是角色的id，id表由[Sakura616](https://github.com/Einsam616)整理，感谢！ 多条命令用回车隔开。

多条命令快速执行可能会引发异常问题，可以在其间隔添加延时指令
```shell
sleep100
```
sleep后面跟延时的时间，单位是毫秒。

生成的个数可以填多个就可以批量生成，但是不要过多。

选择CDK的过期时间（默认为90天后，可以在app/CONSTANTS.py里面更改）

限制每个uid可以兑换的同一个CDK的个数

生成速度取决于服务器性能。


### 高级

1. 设置CDK的默认过期时间。

    创建CDK时如果不想每次都设置一个时间，可以在`CONSTANTS.py`中设置默认过期时间
   ```python
    # 设置CDK默认过期时间（默认为90天）
    CDK_expire_day = 90
    ```
    >这样就会自动计算90天之后的日期，然后自动填写在生成CDK页面的表单上。


2. 由于服务端本身的特性，故设置右上角在线人数没有意义

3. 不想使用的功能
   
   可能有些提供的功能并不想使用，可以进行如下操作，以远程执行为例：
   
   ①首先修改`templates/用户后台.html`，把里面的按钮使用` {#  #} `引起来，注释掉
   ```html
   {#  <a href="./remote_cmd" class="card-title btn btn-success button-click category-button checked">远程执行</a> #}
   ```
   保存。
   
   ②注释掉可能还不够，有写人可能会猜出地址，还要禁掉对应的路由
   
   修改'djangoProject_genshin_player_backend/urls.py'
   
   在对应的功能的路由前加上`# `注释这一行
   ```python
   # path('remote_cmd', views.remote_cmd),
   ```
   保存。
   
   这样就可以把不想要的功能去掉了。


4. 自定义网页背景图
   
   大家还是喜欢背景图是随机图的多，于是直接提供了一个修改图片地址的设置参数，这样就不用一个个到html里面修改了。
   ```python
   # 设置网页背景图链接，默认是/static/images/bg.jpg文件
   # 也可以设置一些随机图的地址 比如https://api.mtyqx.cn/tapi/random.php
   # 更多随机图地址详见我博客https://blog.jixiaob.cn/?post=93
   background_image = './usr/theme/images/bg.jpg'
   ```
   默认就是/static/images/bg.jpg这个图片文件，
   当然也可以改成一些随机图的地址，比如[https://api.mtyqx.cn/tapi/random.php](https://api.mtyqx.cn/tapi/random.php)
   
   [赵苦瓜的博客](https://blog.jixiaob.cn/?post=93) 也分享了一些其他的随机图地址以供参考=w=
