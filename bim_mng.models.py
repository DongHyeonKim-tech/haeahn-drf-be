# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Menu(models.Model):
    menu_cd = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS')
    is_used = models.BooleanField()
    parent_cd = models.ForeignKey('self', models.DO_NOTHING, db_column='parent_cd', blank=True, null=True)
    path = models.CharField(max_length=100, db_collation='Korean_Wansung_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MENU'
