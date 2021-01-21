import json

from linebot.models import BoxComponent, BubbleContainer, TextComponent, ButtonComponent, PostbackAction, URIAction, FlexSendMessage, ImageComponent, TextSendMessage


def bubble_container(header: BoxComponent, body: BoxComponent, footer: BoxComponent or None) -> BubbleContainer:
    return BubbleContainer(
        direction="ltr",
        size="kilo",
        header=header,
        body=body,
        footer=footer
    )


def box_component_vert(contents: list) -> BoxComponent:
    return BoxComponent(layout="vertical", contents=contents)


def box_component_hor(contents: list) -> BoxComponent:
    return BoxComponent(layout="horizontal", contents=contents)


def header_contents(text: str) -> list:
    return [TextComponent(text=text, align="center", weight="bold", color="#000000")]


def body_contents(text: str) -> list:
    return [TextComponent(text=text, align="start", wrap=True)]


def button_component_postback(label: str, text: str, data: str) -> ButtonComponent:
    return ButtonComponent(
        style="primary",
        color="#377a00",
        height="sm",
        margin="xs",
        action=PostbackAction(
            label=label,
            text=text,
            data=json.dumps({'state': data})
        )
    )


def button_component_uri(label: str, uri: str) -> ButtonComponent:
    return ButtonComponent(
        style="primary",
        color="#377a00",
        height="sm",
        margin="xs",
        action=URIAction(
            label=label,
            uri=uri
        )
    )


def send_image(url: str) -> FlexSendMessage:
    bubble = BubbleContainer(
        direction='ltr',
        size='kilo',
        hero=ImageComponent(url=url, align='center', size='full', aspect_ratio='1:1')
    )
    return FlexSendMessage(alt_text="興趣", contents=bubble)


def send_text(text: str) -> TextSendMessage:
    return TextSendMessage(text=text)
