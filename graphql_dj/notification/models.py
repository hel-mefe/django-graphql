from django.db import models
from enumfields import Enum, EnumField

class NotificationState(Enum):
    PENDING = 'PENDING'
    SEEN = 'SEEN'

class Notification(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    state = EnumField(NotificationState, default=NotificationState.PENDING)
    userId = models.ForeignKey('user.User', default=-1, on_delete=models.CASCADE, related_name='notification_user')
