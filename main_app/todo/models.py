from django.db import models

class Task(models.Model):
    task=models.CharField(max_length=250)
    is_completed=models.BooleanField(default=False)                                                                     #defalut is false (uncompleted by default)
    created_at = models.DateTimeField(auto_now_add=True)                                                                #automatically created
    updated_at = models.DateTimeField(auto_now=True)                                                                    #automatically created

    def __str__(self):                                                                                                  #string representation
        return self.task