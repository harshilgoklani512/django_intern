from django.db import models
from user.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30,null=False)
    description = models.CharField(max_length=500)
    technology = models.CharField(max_length=100)
    estimatedHours = models.IntegerField()
    startdate = models.DateField()
    completionDate = models.DateField()

    class Meta:
        db_table = 'Project'

class Projet_team(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'Projetc_team'

class Status(models.Model):
    statusname = models.CharField(max_length=20,null=False,unique=True)

    class Meta:
        db_table ='Status'


class Project_module(models.Model):
    
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    moduelename = models.CharField(max_length=30,null=False)
    description = models.CharField(max_length=30)
    estimatedHours = models.IntegerField()

    class Meta:
        db_table = 'Project_module'

priorityChoice =  (("High" ,"High") ,("Low" ,"Low") ,("Normal" ,"Normal"))


class Task(models.Model):
    
    module = models.IntegerField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    #choice,.... take tuple...
    priority = models.CharField(choices=priorityChoice ,max_length=30)
    description = models.CharField(max_length=500,null=False)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    totalminutes = models.IntegerField()

    class Meta:
        db_table = 'Task'

class user_task(models.Model):
    #user_task_id = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    taskid = models.ForeignKey(Task,on_delete=models.CASCADE)