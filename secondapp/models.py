from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id', verbose_name='用户Id')
    user_account = models.CharField(max_length=50, db_column='user_account', verbose_name='用户账户')
    user_password = models.CharField(max_length=50, db_column='user_password', verbose_name='用户密码')
    is_finance = models.IntegerField(db_column='is_finance', verbose_name='是否财务')
    remark = models.CharField(max_length=255, db_column='remark', verbose_name='备注')
    def __str__(self):
        return self.id+self.user_account+self.is_finance
    class Meta:
        db_table = 'hc_user'
        verbose_name = '用户'
        verbose_name_plural = '用户信息'

# class Person(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.IntegerField
#     def __str__(self):
#         return self.name
