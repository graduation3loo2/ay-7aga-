from django.db import models


class Agencies(models.Model):
    agency_id = models.AutoField(db_column='Agency_id', primary_key=True)
    name = models.CharField(max_length=45)
    address = models.CharField(db_column='Address', max_length=45)
    e_mail = models.CharField(db_column='E-mail', max_length=45)
    commercial_id = models.CharField(max_length=45)
    bio = models.CharField(max_length=45)
    promo_code = models.CharField(db_column='promo-code', max_length=45)
    rate = models.CharField(db_column='Rate', max_length=45)
    photo_url = models.TextField(db_column='photo_URL')

    class Meta:
        managed = False
        db_table = 'agencies'


class Phones(models.Model):
    agency = models.ForeignKey(Agencies, models.DO_NOTHING, db_column='Agency_id')
    phone = models.CharField(max_length=13, primary_key=True)

    class Meta:
        managed = False
        db_table = 'phones'
        unique_together = (('agency', 'phone'),)


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    e_mail = models.CharField(db_column='e-mail', max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    city = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'users'


class Follows(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, primary_key=True)
    agency = models.ForeignKey(Agencies, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'follows'
        unique_together = (('user', 'agency'),)
