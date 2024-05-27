from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANG_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    # date create
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    lint = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=200, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    lang = models.CharField(choices=LANG_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    
    class Meta:
        ordering = ['created']
        
    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.lang)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.lint = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)
        
        