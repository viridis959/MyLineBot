from linebot.models import SeparatorComponent, MessageAction, FlexSendMessage, CarouselContainer

from .messages_text import *
from .messages_utils import *


def autobiography() -> FlexSendMessage:
    _header_contents = header_contents("自傳")
    header = box_component_vert(_header_contents)

    _body_contents1 = body_contents(autobiography_text1)
    body1 = box_component_vert(_body_contents1)

    _body_contents2 = body_contents(autobiography_text2)
    body2 = box_component_vert(_body_contents2)

    bubble = bubble_container(header, body1, None)
    bubble2 = bubble_container(header, body2, None)
    carousel = CarouselContainer(contents=[bubble, bubble2])

    return FlexSendMessage(alt_text="自傳", contents=carousel)


def interest() -> FlexSendMessage:
    _header_contents = header_contents("興趣")
    header = box_component_vert(_header_contents)

    _body_contents = body_contents(interest_text)
    body = box_component_vert(_body_contents)

    button_component = button_component_postback("查看相片", "/查看相片", "interest_image")
    footer = box_component_hor([button_component])

    bubble = bubble_container(header, body, footer)

    return FlexSendMessage(alt_text="興趣", contents=bubble)


def python() -> FlexSendMessage:
    _header_contents = header_contents("Python")
    header = box_component_vert(_header_contents)

    _body_contents = body_contents(python_text)
    body = box_component_vert(_body_contents)

    button_component_l = button_component_uri("爬蟲", "https://liff.line.me/1655584156-5MKLa48d")
    button_component_r = button_component_uri("Pytorch", "https://liff.line.me/1655584156-wka7VGdM")
    footer = box_component_hor([button_component_l, button_component_r])

    bubble = bubble_container(header, body, footer)

    return FlexSendMessage(alt_text="Python", contents=bubble)


def java() -> FlexSendMessage:
    _header_contents = header_contents("Java")
    header = box_component_vert(_header_contents)

    _body_contents = body_contents(java_text)
    body = box_component_vert(_body_contents)

    bubble = bubble_container(header, body, None)

    return FlexSendMessage(alt_text="Java", contents=bubble)


def javascript() -> FlexSendMessage:
    _header_contents = header_contents("Javascript")
    header = box_component_vert(_header_contents)

    _body_contents = body_contents(javascript_text)
    body = box_component_vert(_body_contents)

    button_component = button_component_uri("Github", "https://liff.line.me/1655584156-RwKNLwB1")
    footer = box_component_hor([button_component])

    bubble = bubble_container(header, body, footer)

    return FlexSendMessage(alt_text="Python", contents=bubble)


def project() -> FlexSendMessage:
    _header_contents = header_contents("畢專")
    header = box_component_vert(_header_contents)

    _body_contents = body_contents(project_text)
    body = box_component_vert(_body_contents)

    button_component_l = button_component_uri("Github", "https://liff.line.me/1655584156-LKywQEZb")
    button_component_r = button_component_uri("影片", "https://liff.line.me/1655584156-2aDQWEGP")
    footer = box_component_hor([button_component_l, button_component_r])

    bubble = bubble_container(header, body, footer)

    return FlexSendMessage(alt_text="Python", contents=bubble)


def intern() -> FlexSendMessage:
    _header_contents = header_contents("實習")
    header = box_component_vert(_header_contents)

    _body_contents = body_contents(project_text)
    body = box_component_vert(_body_contents)

    button_component_l = button_component_postback("Web", "/Web", "intern_web")
    button_component_r = button_component_postback("LineBot", "/LineBot", "intern_line_bot")
    footer = box_component_hor([button_component_l, button_component_r])

    bubble = bubble_container(header, body, footer)
    print(bubble)

    return FlexSendMessage(alt_text="實習", contents=bubble)


def contact_me() -> FlexSendMessage:
    _header_contents = header_contents("諮詢小幫手")
    header = box_component_vert(_header_contents)

    _body_contents = body_contents(contact_me_text)
    body = box_component_vert(_body_contents)

    button_component_l = button_component_uri("Resume", "https://liff.line.me/1655584156-2Qxyk8zD")
    button_component_r = button_component_uri("LinkedIn", "https://liff.line.me/1655584156-67gWAZ0Y")
    button_component_bot_comb = box_component_hor([button_component_l, button_component_r])
    line_button = ButtonComponent(
        action=URIAction(
            label="傳Line給En-Li",
            uri="https://line.me/ti/p/-rT8KIvvlV"
        ),
        height="sm"
    )
    email_button = ButtonComponent(
        action=MessageAction(
            label="寄Email給En-Li",
            text="請點擊以下email\nviridis959@gmail.com"
        ),
        height="sm"
    )
    footer = box_component_vert([SeparatorComponent(), line_button, email_button, button_component_bot_comb])

    bubble = bubble_container(header, body, footer)

    return FlexSendMessage(alt_text="問題諮詢", contents=bubble)
