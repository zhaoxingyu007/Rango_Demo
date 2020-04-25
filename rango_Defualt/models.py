from django.db import models

# Create your models here.
class Blog(models.Model) :
    name=models.CharField( max_length=64,)
    address = models.CharField( )
    houseid = models.Interfield()


    def __str__(self):
        return self.name

class User (models.Model):
    name = models.CharField()
    age = models.Intergerfield()
    sex = models.BooleanField()

    def __str__(self):
        return self.name


class Blog(models.Model) :
    name=models.CharField( max_length=64,)
    address = models.CharField( )
    houseid = models.Interfield()


    def __str__(self):
        return self.name

class Post (models.Model):
    name = models.CharField()
    address = models.CharField()
    houseid = models.Interfield()

    def __str__(self):
        return self.name

class Blog(models.Model) :
    name=models.CharField( max_length=64,)
    address = models.CharField( )
    houseid = models.Interfield()


    def __str__(self):
        return self.name

class User (models.Model):
    name = models.CharField()
    age = models.Intergerfield()
    sex = models.BooleanField()

    def __str__(self):
        return self.name


class Blog(models.Model) :
    name=models.CharField( max_length=64,)
    address = models.CharField( )
    houseid = models.Interfield()


    def __str__(self):
        return self.name

class User (models.Model):
    name = models.CharField()
    age = models.Intergerfield()
    sex = models.BooleanField()

    def __str__(self):
        return self.name


class Blog(models.Model) :
    name=models.CharField( max_length=64,)
    address = models.CharField( )
    houseid = models.Interfield()


    def __str__(self):
        return self.name

class Comment (models.Model):
    name = models.CharField()


    def __str__(self):
        return self.name