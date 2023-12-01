from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class Conference(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    registration_start_date = models.DateField()
    registration_end_date = models.DateField()
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField()
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1)
    status = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)

class Submission(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    keywords = models.CharField(max_length=255)
    submission_date = models.DateTimeField()
    submission_status = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    external_url = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class SubmissionChanges(models.Model):
    id = models.AutoField(primary_key=True)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    modification_date = models.DateTimeField()
    modifying_author = models.ForeignKey(User, on_delete=models.CASCADE)
    modified_field = models.CharField(max_length=255)
    previous_value = models.TextField()
    new_value = models.TextField()


class SubmissionEvaluation(models.Model):
    id = models.AutoField(primary_key=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    score = models.IntegerField()
    evaluation_start_date = models.DateTimeField()
    evaluation_end_date = models.DateTimeField()
    tags = models.CharField(max_length=255)
    evaluation_status = models.CharField(max_length=255)


class EvaluationComments(models.Model):
    id = models.AutoField(primary_key=True)
    evaluation = models.ForeignKey(SubmissionEvaluation, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_date = models.DateTimeField()
    comment_text = models.TextField()


class Participant(models.Model):
    id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    registration_date = models.DateTimeField()
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    target_audience = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class ActivitySchedule(models.Model):
    id = models.AutoField(primary_key=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
