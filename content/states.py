from linebot import LineBotApi
from linebot.models import PostbackEvent

from MyLineBot.settings import LINE_ACCESS_TOKEN, LINE_LIFESTYLE_RICH_MENU, LINE_SPECIALTY_RICH_MENU, LINE_EXPERIENCE_RICH_MENU, LINE_DEFAULT_RICH_MENU
from content.messages import *


def state_judge(state: str, bot_user: str):
    bot = LineBotApi(LINE_ACCESS_TOKEN)

    if state == "lifestyle":    # 切換至生活風格選單
        bot.link_rich_menu_to_user(bot_user, LINE_LIFESTYLE_RICH_MENU)
    elif state == "autobiography":    # 顯示自傳內容
        return autobiography()
    elif state == "interest":    # 顯示興趣內容
        return interest()
    elif state == "interest_image":    # 顯示興趣內容的圖片
        return send_image("https://github.com/viridis959/MyLineBot/blob/master/rich_menu/interest_image.jpg?raw=true")

    elif state == "specialty":    # 切換至專長技能選單
        bot.link_rich_menu_to_user(bot_user, LINE_SPECIALTY_RICH_MENU)
    elif state == "python":    # 顯示Python內容
        return python()
    elif state == "java":    # 顯示Java內容
        return java()
    elif state == "javascript":    # 顯示Javascript內容
        return javascript()

    elif state == "experience":    # 切換至特殊經歷選單
        bot.link_rich_menu_to_user(bot_user, LINE_EXPERIENCE_RICH_MENU)
    elif state == "project":    # 顯示畢專內容
        return project()
    elif state == "intern":    # 顯示實習內容
        return intern()
    elif state == "intern_web":    # 顯示實習內容的Web影片
        return send_text("https://www.youtube.com/watch?v=o_HXemQV3T4")
    elif state == "intern_line_bot":    # 顯示實習內容的LineBot影片
        return send_text("https://www.youtube.com/watch?v=jg4wHEqxytU")

    elif state == "default":    # 切換至主選單
        bot.link_rich_menu_to_user(bot_user, LINE_DEFAULT_RICH_MENU)
    elif state == "contact_me":    # 顯示問題諮詢內容
        return contact_me()
