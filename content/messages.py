from linebot import LineBotApi
from linebot.models import *

from MyLineBot.settings import LINE_ACCESS_TOKEN, LINE_LIFESTYLE_RICH_MENU, LINE_EXPERIENCE_RICH_MENU, LINE_DEFAULT_RICH_MENU, LINE_SPECIALTY_RICH_MENU
from .messages_text import *
from .base import Base


class LifestyleMenu(Base):
    def __init__(self, user_id):
        super(LifestyleMenu, self).__init__()

        self.next_cls = AutobiographyMessage
        self.user_id = user_id
        self.state = "lifestyle"

    def as_state_action(self, state):
        bot = LineBotApi(LINE_ACCESS_TOKEN)
        bot.link_rich_menu_to_user(self.user_id, LINE_LIFESTYLE_RICH_MENU)


class AutobiographyMessage(Base):

    def __init__(self, user_id):
        super(AutobiographyMessage, self).__init__()

        self.next_cls = InterestMessage
        self.user_id = user_id
        self.state = "autobiography"
        self.header_text = ["自傳", "自傳"]
        self.body_text = [autobiography_text1, autobiography_text2]
        self.footer_contents = [None, None]


class InterestMessage(Base):

    def __init__(self, user_id):
        super(InterestMessage, self).__init__()

        self.next_cls = InterestImageMessage
        self.user_id = user_id
        self.state = "interest"
        self.header_text = ["興趣"]
        self.body_text = [interest_text]
        self.footer_contents = [[self._set_button_component_state("查看相片", "/查看相片", "interest_image")]]


class InterestImageMessage(Base):
    def __init__(self, user_id):
        super(InterestImageMessage, self).__init__()

        self.next_cls = SpecialtyMenu
        self.user_id = user_id
        self.state = "interest_image"

    def as_state_action(self, state):
        bubble = BubbleContainer(
            direction='ltr',
            size='kilo',
            hero=ImageComponent(url="https://github.com/viridis959/MyLineBot/blob/master/rich_menu/interest_image.jpg?raw=true",
                                align='center', size='full', aspect_ratio='1:1')
        )
        return FlexSendMessage(alt_text="興趣", contents=bubble)


class SpecialtyMenu(Base):
    def __init__(self, user_id):
        super(SpecialtyMenu, self).__init__()

        self.next_cls = PythonMessage
        self.user_id = user_id
        self.state = "specialty"

    def as_state_action(self, state):
        bot = LineBotApi(LINE_ACCESS_TOKEN)
        bot.link_rich_menu_to_user(self.user_id, LINE_SPECIALTY_RICH_MENU)


class PythonMessage(Base):

    def __init__(self, user_id):
        super(PythonMessage, self).__init__()

        self.next_cls = JavaMessage
        self.user_id = user_id
        self.state = "python"
        self.header_text = ["Python", "Python"]
        self.body_text = [python_text1, python_text2]
        contents = [self._set_button_component_uri("爬蟲", "https://liff.line.me/1655584156-5MKLa48d"),
                    self._set_button_component_uri("Pytorch", "https://liff.line.me/1655584156-wka7VGdM")]
        self.footer_contents = [[BoxComponent(layout="horizontal", contents=contents)], None]


class JavaMessage(Base):

    def __init__(self, user_id):
        super(JavaMessage, self).__init__()

        self.next_cls = JavascriptMessage
        self.user_id = user_id
        self.state = "java"
        self.header_text = ["Java"]
        self.body_text = [java_text]
        self.footer_contents = [None]


class JavascriptMessage(Base):

    def __init__(self, user_id):
        super(JavascriptMessage, self).__init__()

        self.next_cls = ExperienceMenu
        self.user_id = user_id
        self.state = "javascript"
        self.header_text = ["Javascript"]
        self.body_text = [javascript_text]
        self.footer_contents = [[self._set_button_component_uri("Github", "https://liff.line.me/1655584156-RwKNLwB1")]]


class ExperienceMenu(Base):
    def __init__(self, user_id):
        super(ExperienceMenu, self).__init__()

        self.next_cls = ProjectMessage
        self.user_id = user_id
        self.state = "experience"

    def as_state_action(self, state):
        bot = LineBotApi(LINE_ACCESS_TOKEN)
        bot.link_rich_menu_to_user(self.user_id, LINE_EXPERIENCE_RICH_MENU)


class ProjectMessage(Base):
    def __init__(self, user_id):
        super(ProjectMessage, self).__init__()

        self.next_cls = InternMessage
        self.user_id = user_id
        self.state = "project"
        self.header_text = ["畢專"]
        self.body_text = [project_text]
        contents = [self._set_button_component_uri("Github", "https://liff.line.me/1655584156-LKywQEZb"),
                    self._set_button_component_uri("影片", "https://liff.line.me/1655584156-2aDQWEGP")]
        self.footer_contents = [[BoxComponent(layout="horizontal", contents=contents)]]


class InternMessage(Base):
    def __init__(self, user_id):
        super(InternMessage, self).__init__()

        self.next_cls = InternWebMessage
        self.user_id = user_id
        self.state = "intern"
        self.header_text = ["實習"]
        self.body_text = [project_text]
        contents = [self._set_button_component_state("Web", "/Web", "intern_web"),
                    self._set_button_component_state("LineBot", "/LineBot", "intern_line_bot")]
        self.footer_contents = [[BoxComponent(layout="horizontal", contents=contents)]]


class InternWebMessage(Base):
    def __init__(self, user_id):
        super(InternWebMessage, self).__init__()

        self.next_cls = InternLineBotMessage
        self.user_id = user_id
        self.state = "intern_web"

    def as_state_action(self, state):
        return TextSendMessage(text="https://www.youtube.com/watch?v=o_HXemQV3T4")


class InternLineBotMessage(Base):
    def __init__(self, user_id):
        super(InternLineBotMessage, self).__init__()

        self.next_cls = DefaultMenu
        self.user_id = user_id
        self.state = "intern_line_bot"

    def as_state_action(self, state):
        return TextSendMessage(text="https://www.youtube.com/watch?v=jg4wHEqxytU")


class DefaultMenu(Base):
    def __init__(self, user_id):
        super(DefaultMenu, self).__init__()

        self.next_cls = ContactMeMessage
        self.user_id = user_id
        self.state = "default"

    def as_state_action(self, state):
        bot = LineBotApi(LINE_ACCESS_TOKEN)
        bot.link_rich_menu_to_user(self.user_id, LINE_DEFAULT_RICH_MENU)


class ContactMeMessage(Base):
    def __init__(self, user_id):
        super(ContactMeMessage, self).__init__()

        self.next_cls = None
        self.user_id = user_id
        self.state = "contact_me"
        self.header_text = ["諮詢小幫手"]
        self.body_text = [contact_me_text]
        button_component_comb = BoxComponent(layout="horizontal",
                                             contents=[self._set_button_component_uri("Github", "https://liff.line.me/1655584156-LKywQEZb"),
                                                       self._set_button_component_uri("影片", "https://liff.line.me/1655584156-2aDQWEGP")])
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
        self.footer_contents = [[BoxComponent(layout="vertical",
                                              contents=[SeparatorComponent(), line_button, email_button, button_component_comb])]]
