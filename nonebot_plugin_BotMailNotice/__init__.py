from email.message import EmailMessage

from aiosmtplib import send
from nonebot import Bot, get_driver
from nonebot import logger
from nonebot.plugin import PluginMetadata
from pydantic import BaseModel, Extra


class MailUser(BaseModel):
    """
    mail配置
    """
    username: str
    """用户邮箱"""
    password: str
    """用户密码"""
    hostname: str
    """SMTP地址"""
    port: int = 587
    """SMTP发送邮件端口"""


class Config(BaseModel):
    mail_notice: MailUser

    class Config:
        extra = Extra.ignore


__plugin_meta__ = PluginMetadata(
    name="Bot上下线通知",
    description="Bot上下线发送邮件通知的插件",
    usage="",
    config=Config,
    type="application",
    homepage="https://github.com/ZM25XC/nonebot_plugin_BotMailNotice",
    supported_adapters=None,
)
Driver = get_driver()

MailConfig = Driver.config.dict()
MailStatus = MailConfig.get("mail_notice", False)


@Driver.on_bot_connect
async def bot_connect(bot: Bot):
    adapter: str = bot.adapter.get_name()
    bot_id: str = bot.self_id
    data: dict = {"adapter": adapter, "bot_id": bot_id, "status": True}
    await sendEmail(data=data)


@Driver.on_bot_disconnect
async def bot_disconnect(bot: Bot):
    adapter: str = bot.adapter.get_name()
    bot_id: str = bot.self_id
    data: dict = {"adapter": adapter, "bot_id": bot_id, "status": False}
    await sendEmail(data=data)


async def sendEmail(data: dict):
    if not MailStatus:
        return None
    mailConfig = MailConfig.get("mail_notice", {})
    message = EmailMessage()
    message["From"] = mailConfig["username"]
    message["To"] = mailConfig["username"]
    message["Subject"] = "Bot状态提醒！"
    if data["status"]:
        message.set_content(f"您的Bot上线啦!\n适配器：{data['adapter']}\nBot：{data['bot_id']}")
    else:
        message.set_content(
            f"您的Bot下线了，可能出现了问题，快去看看吧！\n适配器：{data['adapter']}\n{data['bot_id']} 下线了")
    try:
        await send(
            message,
            hostname=mailConfig["hostname"],
            port=mailConfig["port"],
            username=mailConfig["username"],
            password=mailConfig["password"]
        )
        logger.debug("邮件发送成功！")
    except Exception as e:
        logger.debug("邮件发送失败！")
        logger.error(e)
