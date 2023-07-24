<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-BotMailNotice

_✨ bot断连时的Mail通知插件 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/ZM25XC/BotMailNotice.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-BotMailNotice">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-BotMailNotice.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>


## 介绍

- 可以在bot断开与nonebot2的连接时向指定邮箱发送邮件通知，用来通知是否掉线
  

##  安装及更新

<details>
<summary>第一种方式(不推荐)</summary>

- 使用`git clone https://github.com/ZM25XC/BotMailNotice.git`指令克隆本仓库或下载压缩包文件

</details>

<details>
<summary>第二种方式(二选一)</summary>

- 使用`pip install nonebot-plugin-BotMailNotice`来进行安装,使用`pip install nonebot-plugin-BotMailNotice -U`进行更新
- 使用`nb plugin install nonebot-plugin-BotMailNotice`来进行安装,使用`nb plugin install nonebot-plugin-BotMailNotice -U`进行更新

</details>


## 导入插件

<details>
<summary>使用第一种方式安装看此方法</summary>

- 将`nonebot_plugin_BotMailNotice`放在nb的`plugins`目录下，运行nb机器人即可

- 文件结构如下

    ```py
    📦 AweSome-Bot
    ├── 📂 awesome_bot
    │   └── 📂 plugins
    |       └── 📂 nonebot_plugin_BotMailNotice
    |           └── 📜 __init__.py
    ├── 📜 .env.prod
    ├── 📜 .gitignore
    ├── 📜 pyproject.toml
    └── 📜 README.md
    ```

    

</details>

<details>
<summary>使用第二种方式安装看此方法</summary>

- 在`pyproject.toml`里的`[tool.nonebot]`中添加`plugins = ["nonebot_plugin_BotMailNotice"]`

</details>



##  配置
运行插件前，需要在 nonebot2 项目的`.env.prod`文件中添加下表中配置项

|  配置项  | 必填  | 值类型 | 默认值 |            说明            |
| :------: | :---: | :----: | :----: | :------------------------: |
| username |  是   |  str   |   ""   |          邮箱账号          |
| password |  是   |  str   |   ""   |      邮箱密码或授权码      |
| hostname |  是   |  str   |   ""   |       邮箱服务器地址       |
|   port   |  是   |  int   |  465   | 邮箱端口号，ssl模式时为465 |

## 示例配置
  
```env
mail_notice='{
"username":"xxx@qq.com",
"password":"qflgxxxxxx",
"hostname":"smtp.qq.com",
"port":587
}'
```