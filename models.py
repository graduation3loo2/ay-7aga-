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
        db_table = 'Agencies'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Follows(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, primary_key=True)
    agency = models.ForeignKey(Agencies, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'Follows'
        unique_together = (('user', 'agency'),)


class Phones(models.Model):
    agency = models.ForeignKey(Agencies, models.DO_NOTHING, db_column='Agency_id', primary_key=True)  # Field name made lowercase.
    phone = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'Phones'
        unique_together = (('agency', 'phone'),)


class Reports(models.Model):
    report_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    agency = models.ForeignKey(Agencies, models.DO_NOTHING)
    message = models.TextField(db_column='Message', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reports'


class Response(models.Model):
    vote = models.ForeignKey('Vote', models.DO_NOTHING, db_column='Vote_id', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_id')  # Field name made lowercase.
    interested = models.IntegerField(db_column='Interested')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Response'
        unique_together = (('vote', 'user'),)


class TripPhotos(models.Model):
    trip = models.ForeignKey('Trips', models.DO_NOTHING, db_column='Trip_id', primary_key=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "Trip_photos'"


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


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    phone = models.CharField(max_length=11, blank=True, null=True)
    city = models.CharField(max_length=45)
    photo_url = models.TextField(blank=True, null=True)
    e_mail = models.CharField(db_column='e-mail', max_length=45, blank=True, null=True, unique=True )

    class Meta:
        managed = False
        db_table = 'Users'


class GoingTo(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING, db_column='User_id', primary_key=True)  # Field name made lowercase.
    trip = models.ForeignKey(Trips, models.DO_NOTHING, db_column='Trip_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'going_to'
        unique_together = (('user', 'trip'),)


class Saved(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING, db_column='User_id', primary_key=True)  # Field name made lowercase.
    trip = models.ForeignKey(Trips, models.DO_NOTHING, db_column='Trip_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'saved'
        unique_together = (('user', 'trip'),)

class Vote(models.Model):
    vote_id = models.AutoField(db_column='Vote_id', primary_key=True)  # Field name made lowercase.
    agency = models.ForeignKey(Agencies, models.DO_NOTHING, db_column='Agency_id')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    photo_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Vote'
