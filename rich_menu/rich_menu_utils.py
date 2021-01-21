import json

from linebot.models import RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds, PostbackAction, URIAction


def get_rich_menu(name: str, item_text: list, item_state: list) -> RichMenu:
    items = len(item_text)
    area_list = []

    if name != "主選單":
        area_back = split_area(0, 0, 1830, 223, "/回主選單", "default")
        area_list.append(area_back)

    for i in range(items):
        area = split_area(2500 / items * i, 223, 2500 / items, 620, item_text[i], item_state[i])
        area_list.append(area)

    area_contact = split_area(1830, 0, 335, 223, "/問題諮詢", "contact_me")
    area_list.append(area_contact)

    area_github = RichMenuArea(
        bounds=RichMenuBounds(x=2165, y=0, width=335, height=223),
        action=URIAction(
            label='按鈕-github',
            uri='https://liff.line.me/1655584156-PJdR45rD'
        )
    )
    area_list.append(area_github)

    return RichMenu(
        size=RichMenuSize(width=2500, height=843),
        selected=True,
        name=name,
        chat_bar_text=name,
        areas=area_list
    )


def split_area(x: float, y: int, width: float, height: int, item_text: str, item_state: str) -> RichMenuArea:
    return RichMenuArea(
                bounds=RichMenuBounds(x=x, y=y, width=width, height=height),
                action=PostbackAction(
                    label=f"按鈕-{item_text[1:]}",
                    text=item_text,
                    data=json.dumps({
                        "state": item_state
                    })
                ),
            )


if __name__ == "__main__":
    get_rich_menu("test", ["test", "test"], ["test", "test"])
