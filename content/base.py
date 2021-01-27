import json
import logging

from linebot.models import BubbleContainer, FlexSendMessage, CarouselContainer, ButtonComponent, PostbackAction, URIAction, TextComponent, BoxComponent


class Base(object):

    def __init__(self, next_cls=None, user_id=None, state=None,
                 header_text=None, body_text=None, footer_contents=None):
        self.next_cls = next_cls
        self.user_id = user_id
        self.state = state
        self.header_text = header_text
        self.body_text = body_text
        self.footer_contents = footer_contents

    def resolve(self, state):
        if self.state == state:
            return self.as_state_action(state)
        else:
            next_cls = self.next_cls(user_id=self.user_id)
            return next_cls.resolve(state)

    def as_state_action(self, state):
        pages = len(self.header_text)
        if pages != len(self.body_text):
            logging.info("Length of header_text and body_text must be same.")
            return

        message_contents = []
        for page in range(pages):
            message_contents.append(BubbleContainer(
                direction="ltr",
                size="kilo",
                header=self._set_header(self.header_text[page]),
                body=self._set_body(self.body_text[page]),
                footer=self._set_footer(self.footer_contents[page])
            ))

        if len(message_contents) == 1:
            return FlexSendMessage(alt_text=self.header_text[0], contents=message_contents[0])
        else:
            return FlexSendMessage(alt_text=self.header_text[0], contents=CarouselContainer(contents=message_contents))

    @staticmethod
    def _set_button_component_state(label, text, state):
        return ButtonComponent(
            style="primary",
            color="#377a00",
            height="sm",
            margin="xs",
            action=PostbackAction(
                label=label,
                text=text,
                data=json.dumps({'state': state})
            )
        )

    @staticmethod
    def _set_button_component_uri(label, uri):
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

    @staticmethod
    def _set_header(header_text=None):
        header_contents = [TextComponent(text=header_text, align="center", weight="bold", color="#000000")]
        return BoxComponent(layout="vertical", contents=header_contents)

    @staticmethod
    def _set_body(body_text=None):
        body_contents = [TextComponent(text=body_text, align="start", wrap=True)]
        return BoxComponent(layout="vertical", contents=body_contents)

    @staticmethod
    def _set_footer(footer_contents=None):
        return BoxComponent(layout="horizontal", contents=footer_contents)
