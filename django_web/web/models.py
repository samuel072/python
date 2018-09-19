from django.db import models

# Create your models here.


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=40)
    user_name = models.CharField(max_length=120, verbose_name="用户名")
    phone = models.CharField(max_length=11, verbose_name="手机号")
    password = models.CharField(max_length=16, verbose_name="密码")
    ip = models.CharField(max_length=20, verbose_name="ip地址")
    login_error_num = models.IntegerField(default=0, verbose_name="登录错误次数")
    create_date = models.DateField(verbose_name="记录创建时间")
    last_login_date = models.DateField(verbose_name="最后一次登录时间")

    class Meta():
        db_table = "f_user"


class Role(models.Model):
    id = models.CharField(primary_key=True, max_length=40, verbose_name="ID")
    role_name = models.CharField(max_length=120, verbose_name="角色名")
    description = models.CharField(max_length=120, verbose_name="描述")

    class Meta():
        db_table = "f_role"
