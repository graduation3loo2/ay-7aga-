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
        db_table = 'Agencies'


class Follows(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, primary_key=True)
    agency = models.ForeignKey(Agencies, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Follows'
        unique_together = (('user', 'agency'),)


class TripPhotos(models.Model):
    trip = models.ForeignKey('Trips', models.DO_NOTHING, db_column='Trip_id', primary_key=True)
    url = models.TextField(db_column='URL')

    class Meta:
        managed = False
        db_table = "Trip_photos'"


class Trips(models.Model):
    trip_id = models.AutoField(db_column='Trip_id', primary_key=True)
    agency = models.ForeignKey(Agencies, models.DO_NOTHING, db_column='Agency_id')
    name = models.CharField(db_column='Name', max_length=50)
    from_location = models.CharField(db_column='From_Location', max_length=45)
    to_location = models.CharField(db_column='To_Location', max_length=45)
    date_from = models.DateTimeField(db_column='Date_From')
    date_to = models.DateTimeField(db_column='Date_To')
    deadline = models.DateTimeField(db_column='Deadline')
    meals = models.CharField(db_column='Meals', max_length=45)
    price = models.FloatField(db_column='Price')
    description = models.TextField(db_column='Description')
    views = models.PositiveIntegerField(db_column='Views')
    rate = models.FloatField(db_column='Rate')

    class Meta:
        managed = False
        db_table = 'Trips'


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    e_mail = models.CharField(db_column='e-mail', max_length=45)
    phone = models.CharField(max_length=11, blank=True, null=True)
    city = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'Users'


class Vote(models.Model):
    vote_id = models.AutoField(db_column='Vote_id', primary_key=True)
    agency = models.ForeignKey(Agencies, models.DO_NOTHING, db_column='Agency_id')
    name = models.CharField(db_column='Name', max_length=45)
    description = models.TextField(db_column='Description')
    photo_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Vote'


class GoingTo(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_id', primary_key=True)
    trip = models.ForeignKey('Trips', models.DO_NOTHING, db_column='Trip_id')

    class Meta:
        managed = False
        db_table = 'going_to'
        unique_together = (('user', 'trip'),)