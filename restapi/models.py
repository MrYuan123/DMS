from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User



class Apartment(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'apartment'


class Discipline(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    student = models.ForeignKey('Student')
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dis_type = models.ForeignKey('DisciplineType')

    class Meta:
        managed = False
        db_table = 'discipline'


class DisciplineType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'discipline_type'


class Dormitory(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    apartment = models.ForeignKey(Apartment)
    capacity = models.IntegerField()
    balance = models.FloatField()
    gender = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'dormitory'


class Manage(models.Model):
    admin = models.ForeignKey(User)
    dormitory = models.ForeignKey('Dormitory')

    class Meta:
        managed = False
        db_table = 'manage'
        unique_together = (('admin', 'dormitory'),)


class MoveDormitory(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student')
    src_dorm = models.ForeignKey('Dormitory', models.DO_NOTHING, blank=True, null=True, related_name='src_dormset')
    des_dorm = models.ForeignKey('Dormitory', models.DO_NOTHING, related_name='des_dormset')
    date = models.DateField()
    admin = models.ForeignKey(User, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'move_dormitory'


class Sanitation(models.Model):
    id = models.AutoField(primary_key=True)
    dormitory = models.ForeignKey('Dormitory')
    admin = models.ForeignKey(User, models.DO_NOTHING)
    date = models.DateField()
    score = models.IntegerField()
    comment = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sanitation'


class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=10)
    paid = models.IntegerField()
    dormitory = models.ForeignKey('Dormitory')
    gender = models.CharField(max_length=6)
    reside_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'student'
