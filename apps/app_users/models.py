from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# 继承Django内置用户类AbstractUser，并添加额外的字段
# 用户表
class UserProfile(AbstractUser):
    staff_no = models.CharField(max_length=15, verbose_name='工号', blank=True)
    department = models.CharField(max_length=15, verbose_name='部门', blank=True)
    bg_telephone = models.CharField(max_length=12, verbose_name='办公电话', blank=True)
    mobile = models.CharField(max_length=11, verbose_name='手机号码', blank=True)
    is_admin = models.CharField(max_length=10, choices=(('1', '是'), ('0', '否')),
                                verbose_name='管理员', default='0', blank=True)
    is_staff = models.CharField(max_length=10, choices=(('1', '是'), ('0', '否')),
                                verbose_name='在职', default='1', blank=True)
    modify_time = models.DateTimeField(default=datetime.now(), verbose_name='修改时间')

    class Meta:
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 用户操作日志
class UserOperateLog(models.Model):
    username = models.CharField(max_length=20, verbose_name='人员')
    scope = models.CharField(max_length=20, verbose_name='操作范围')
    type = models.CharField(max_length=20, verbose_name='操作类型')
    content = models.IntegerField(verbose_name='操作内容')
    modify_time = models.DateTimeField(default=datetime.now(), verbose_name='操作时间')

    class Meta:
        verbose_name = '用户操作日志'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username + '.' + self.type

