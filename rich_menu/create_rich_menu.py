import os

import dotenv
from linebot import LineBotApi

from rich_menu_utils import get_rich_menu


def set_rich_menu(bot: LineBotApi, rich_menu_id: str, filename: str):
    image_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        filename
    )
    with open(image_path, 'rb') as image:
        bot.set_rich_menu_image(rich_menu_id, 'image/png', image)


def main():
    dotenv_file = dotenv.find_dotenv()
    dotenv.load_dotenv(dotenv_file)

    bot = LineBotApi(os.environ["LINE_ACCESS_TOKEN"])

    default_rich_menu = get_rich_menu("主選單", ["/生活風格", "/技能專長", "/特殊經歷"], ["lifestyle", "specialty", "experience"])
    lifestyle_rich_menu = get_rich_menu("生活風格選單", ["/自傳", "/興趣"], ["autobiography", "interest"])
    specialty_rich_menu = get_rich_menu("技能專長選單", ["/Python", "/Java", "/Javascript"], ["python", "java", "javascript"])
    experience_rich_menu = get_rich_menu("特殊經歷選單", ["/畢專", "/實習"], ["project", "intern"])

    default_rich_menu_id = bot.create_rich_menu(rich_menu=default_rich_menu)
    lifestyle_rich_menu_id = bot.create_rich_menu(rich_menu=lifestyle_rich_menu)
    specialty_rich_menu_id = bot.create_rich_menu(rich_menu=specialty_rich_menu)
    experience_rich_menu_id = bot.create_rich_menu(rich_menu=experience_rich_menu)

    set_rich_menu(bot, default_rich_menu_id, "default_rich_menu.png")
    set_rich_menu(bot, lifestyle_rich_menu_id, "lifestyle_rich_menu.png")
    set_rich_menu(bot, specialty_rich_menu_id, "specialty_rich_menu.png")
    set_rich_menu(bot, experience_rich_menu_id, "experience_rich_menu.png")

    bot.set_default_rich_menu(default_rich_menu_id)

    # 改寫.env內容
    dotenv.set_key(dotenv_file, "LINE_DEFAULT_RICH_MENU", default_rich_menu_id, "never")
    dotenv.set_key(dotenv_file, "LINE_LIFESTYLE_RICH_MENU", lifestyle_rich_menu_id, "never")
    dotenv.set_key(dotenv_file, "LINE_SPECIALTY_RICH_MENU", specialty_rich_menu_id, "never")
    dotenv.set_key(dotenv_file, "LINE_EXPERIENCE_RICH_MENU", experience_rich_menu_id, "never")


if __name__ == "__main__":
    main()
