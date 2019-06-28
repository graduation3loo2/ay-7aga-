from django.db import models


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    e_mail = models.CharField(db_column='e-mail', max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    city = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Users'


class Agencies(models.Model):
    agency_id = models.AutoField(db_column='Agency_id', primary_key=True)
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



class Trips(models.Model):
    trip_id = models.AutoField(db_column='Trip_id', primary_key=True)  # Field name made lowercase.
    agency = models.ForeignKey(Agencies, models.DO_NOTHING, db_column='Agency_id')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    from_location = models.CharField(db_column='From_Location', max_length=45)  # Field name made lowercase.
    to_location = models.CharField(db_column='To_Location', max_length=45)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='Date_From')  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='Date_To')  # Field name made lowercase.
    deadline = models.DateTimeField(db_column='Deadline')  # Field name made lowercase.
    meals = models.CharField(db_column='Meals', max_length=45)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    views = models.PositiveIntegerField(db_column='Views')  # Field name made lowercase.
    rate = models.FloatField(db_column='Rate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Trips'

class TripPhotos(models.Model):
    trip = models.ForeignKey('Trips', models.DO_NOTHING, db_column='Trip_id', primary_key=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "trip_photos'"


class GoingTo(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_id', primary_key=True)
    trip = models.ForeignKey('Trips', models.DO_NOTHING, db_column='Trip_id')

    class Meta:
        managed = False
        db_table = 'going_to'
        unique_together = (('user', 'trip'),)

class Follows(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, primary_key=True)
    agency = models.ForeignKey(Agencies, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Follows'
        unique_together = (('user', 'agency'),)


