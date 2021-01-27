import datetime
import json
import logging

import pytz
from linebot import WebhookHandler
from linebot.models import MessageEvent, TextMessage, PostbackEvent

from MyLineBot.settings import LINE_SECRET
from .messages import *

handler = WebhookHandler(LINE_SECRET)
bot = LineBotApi(LINE_ACCESS_TOKEN)
tw = pytz.timezone("Asia/Taipei")
time = datetime.datetime.now(tw)


# 處理輸入文字的event
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    bot_user_name = bot.get_profile(event.source.user_id).display_name
    text = event.message.text

    if text[0] != "/":    # 以/為開頭是Postback回傳的訊息
        contact_me_message = ContactMeMessage(None)
        message = contact_me_message.as_state_action("contact_me")
        bot.reply_message(event.reply_token, message)

        logging.info(f"[{time}] A message with {bot_user_name} text : {event.message.text}")


# 處理PostbackEvent
@handler.add(PostbackEvent)
def handle_postback_message(event):
    bot_user_id = event.source.user_id
    bot_user_name = bot.get_profile(bot_user_id).display_name

    state = json.loads(event.postback.data)["state"]

    logging.info(f"[{time}] A message with {bot_user_name} state : {state}")

    lifestyle_menu = LifestyleMenu(bot_user_id)
    message = lifestyle_menu.resolve(state)

    if message is not None:    # 若message is None，為切換選單的情況
        bot.reply_message(event.reply_token, message)
