from django.db import models


class userregg(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    place=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    status=models.CharField(max_length=150)

class wrkregg(models.Model):
    name=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    centre=models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    labour_category=models.CharField(max_length=150)
    labour_type=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    district=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    category=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    file=models.FileField(max_length=150)

class reportss(models.Model):
    bid=models.CharField(max_length=150)
    wid=models.CharField(max_length=150)
    issue=models.CharField(max_length=150)
    uname=models.CharField(max_length=150)
    typee=models.CharField(max_length=150)
    status=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    amount=models.CharField(max_length=150)

class payment(models.Model):
    rid=models.CharField(max_length=150)
    uname=models.CharField(max_length=150)
    typee=models.CharField(max_length=150)
    wid=models.CharField(max_length=150)
    amount=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    c_num=models.CharField(max_length=150)
    e_date=models.CharField(max_length=150)
    cvv=models.CharField(max_length=150)
    

class booking(models.Model):
    uname=models.CharField(max_length=150)
    wid=models.CharField(max_length=150)
    date=models.CharField(max_length=150)
    place=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    typee=models.CharField(max_length=150)
    issue=models.CharField(max_length=150)
    no_wrkr=models.CharField(max_length=150)
    rate=models.CharField(max_length=150)
    status=models.CharField(max_length=150)

class category(models.Model):
    name=models.CharField(max_length=150)

class subcategory(models.Model):
    cname=models.CharField(max_length=150)
    sub_name=models.CharField(max_length=150)

class user_feedback(models.Model):
    uname=models.CharField(max_length=150)
    feedback=models.CharField(max_length=150)

class wrkr_feedback(models.Model):
    uname=models.CharField(max_length=150)
    feedback=models.CharField(max_length=150)

