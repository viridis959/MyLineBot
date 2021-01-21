from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from linebot.exceptions import InvalidSignatureError

from MyLineBot.settings import LINE_SECRET
from .handlers import handler

import datetime
import pytz
import logging


@require_POST
@csrf_exempt
def webhook(request):
    signature = request.META.get("HTTP_X_LINE_SIGNATURE")   # 分辨LINE server request Django要使用META
    body = request.body.decode("utf-8")    # 用文字的型態拿到http body

    tw = pytz.timezone("Asia/Taipei")
    time = datetime.datetime.now(tw)

    try:
        logging.info("[%s] Request body: %s", time, body)
        handler.handle(body, signature)    # 判斷非法簽章

    except InvalidSignatureError as ee:
        return HttpResponseBadRequest()

    return HttpResponse("OK")
