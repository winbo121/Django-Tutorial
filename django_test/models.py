from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sample'




# create table sample (
# id int auto_increment,
# book_name varchar(255),
# created_at datetime default now()
# primary key(id,book_name));

