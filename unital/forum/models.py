from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Question(models.Model):
    question = models.TextField(_("Question"))
    for_department = models.ForeignKey("main_app.Department", verbose_name=_("Question For Department"), on_delete=models.CASCADE, null=True)
    for_college = models.ForeignKey("main_app.College", verbose_name=_("Question For College"), on_delete=models.CASCADE, null=True)
    posted_by = models.ForeignKey("main_app.User", verbose_name=_("Posted By"), on_delete=models.CASCADE)
    posted_on = models.DateTimeField(_("Posted On"), auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = '1. Questions'
    

class Reply(models.Model):
    question = models.ForeignKey("Question", verbose_name=_("Question"), on_delete=models.CASCADE)
    reply = models.TextField(_("Reply"))
    posted_by = models.ForeignKey("main_app.User", verbose_name=_("Posted By"), on_delete=models.CASCADE)
    posted_on = models.DateTimeField(_("Posted On"), auto_now_add=True)

    def __str__(self):
        return self.reply
    
    class Meta:
        verbose_name_plural = '2. Replies'
    
