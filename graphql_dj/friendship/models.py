from django.db import models
from user.models import User as User


## Docuemntation:
#### - ModelName: FriendShip
#### - Purpose: Describes the relationship between 2 users
####          antyhing that has something to with relationships
####          is being handled in this model
####
#### - ModelDescription:
####    - id: primary key for the friendship
####    - user1: the first user entity
####    - user2: the second user entity
####    - is_user1_following_user2: True if the first user following the 2nd user, False otherwise.
####    - is_user2_following_user1: True if the second user following the 1st user, False otherwise.
####    - user1_followed_user2_at: The time which the first user followed 2nd user, otherwise -1 is default
####    - user2_followed_user1_at: The time which the second user followed first user, otherwise -1 is default
####
#### - last_edited: hel-mefe

class FriendShip(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    is_user1_following_user2 = models.BooleanField(default=False)
    is_user2_following_user1 = models.BooleanField(default=False)
    user1_followed_user2_at = models.DateTimeField(default=-1)
    user2_followed_user1_at = models.DateTimeField(default=-1)