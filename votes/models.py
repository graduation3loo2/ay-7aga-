from django.db import models


class Response(models.Model):
    vote = models.ForeignKey('Vote', models.DO_NOTHING, db_column='Vote_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    interested = models.IntegerField(db_column='Interested')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Response'
        unique_together = (('vote', 'user'),)




class Agencies(models.Model):
    agency_id = models.AutoField(db_column='Agency_id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    address = models.CharField(db_column='Address', max_length=45)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E-mail', max_length=45)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    commercial_id = models.CharField(max_length=45)
    bio = models.CharField(max_length=45)
    promo_code = models.CharField(db_column='promo-code', max_length=45)  # Field renamed to remove unsuitable characters.
    rate = models.CharField(db_column='Rate', max_length=45)  # Field name made lowercase.
    photo_url = models.TextField(db_column='photo_URL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Agencies'


class Vote(models.Model):
    vote_id = models.AutoField(db_column='Vote_id', primary_key=True)  # Field name made lowercase.
    agency = models.ForeignKey(Agencies, models.DO_NOTHING, db_column='Agency_id')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    photo_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Vote'



class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=11, blank=True, null=True)
    city = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Users'

