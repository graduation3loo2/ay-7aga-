from django.db import models

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
        db_table = 'agencies'



class Phones(models.Model):
    agency = models.ForeignKey(Agencies, models.DO_NOTHING, db_column='Agency_id', primary_key=True)  # Field name made lowercase.
    phone = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'phones'
        unique_together = (('agency', 'phone'),)

