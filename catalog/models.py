from django.db import models

# Create your models here.
class Genre(models.Model):
    '''
    classdocs: book genre
    '''
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Author(models.Model):
    #Fields
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
    def __str__(self):
        return self.name

class Book(models.Model):
    '''
    classdocs: contain attribute of Book
    '''
    #Fields
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete= models.SET_NULL, null = True)
    summary = models.TextField(max_length=1000)
    genre = models.ManyToManyField(Genre)
    image = models.ImageField(upload_to = 'images', null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reversed('book-detail', agrs = [str(self.id)])

class BookInstance(models.Model):
    id = models.CharField(primary_key= True, max_length= 5)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null= True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null= True, blank=True)

    LOAN_STATUS =(
        ('m', 'Bảo trì'),
        ('o', 'Đã cho mượn'),
        ('a', 'Có sẵn'),
        ('r', 'Chưa có'),
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text= 'Book availability')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'