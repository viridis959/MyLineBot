from django.db import models


class State(models.Model):
    STATE_LIFESTYLE = "lifestyle"  # 生活風格
    STATE_CONTACT_ME = "contact_me"  # 問題諮詢

    STATE_CHOICES = (
        (STATE_LIFESTYLE, "生活風格"),
        (STATE_CONTACT_ME, "問題諮詢"),
    )

    state = models.CharField(max_length=255, choices=STATE_CHOICES)

    def __str__(self):
        return f"{self.state}"
