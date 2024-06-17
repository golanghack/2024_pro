from django.db import models

class FileUpload(models.Model):
    """Create model for files 
    
    Attrs:
        name -> str - name of file
        file -> file in db
    """
    
    name = models.CharField(max_length=200, verbose_name='file name', help_text='file name')
    file = models.FileField(blank=False, verbose_name='file', help_text='file')
    
    def __str__(self) -> str:
        return self.name 