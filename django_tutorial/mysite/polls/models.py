import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Question(models.Model):
    """
    設問を書いて、投稿時間を設定する
    """
    question_text = models.CharField(max_length=20) # string型変数
    pub_date = models.DateTimeField('date published') # date型変数

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        """
        投稿が最近のものか判定する
        Returns
        --------
        True : 1日以内, False: 1日以上前
        """
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    
    # choiseクラスをQuestionクラスに関連付け。1：1
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=20)
    votes = models.IntegerField(default=0) # 整数型変数

    def __str__(self):
        return self.choice_text