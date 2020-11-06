from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample'




# create table sample (
# id int primary key auto_increment,
# book_name varchar(255) primary key,
# created_at datetime default now()
# );

