from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime
from django.utils.translation import gettext_lazy as _
# Create your models here.
User = get_user_model()
class Post(models.Model):
    user_id = models.ForeignKey(
    User, 
    on_delete = models.CASCADE,
    verbose_name = _("Post owner"),
    )
    
    content = models.TextField(
        max_length = 3000,
        blank = False,
        null = False,
        verbose_name = _("Post content"),
        help_text = _("Required : max-3000")
    )

    post_date = models.DateField(
        auto_now_add = True,
        verbose_name = _("Post date"),
        )

    def __str__(self):
        return f'{self.content} {self.user_id.username}'

class Comment(models.Model):
    post_id = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        verbose_name = _("Post")
    )

    user_id = models.ForeignKey(
    User, 
    on_delete = models.CASCADE,
    verbose_name = _("Comment owner"),
    ) 

    content = models.TextField(
        max_length = 3000,
        blank = False,
        null = False,
        verbose_name = _("Comment content"),
        help_text = _("Required : max-3000")
    )

    comment_date = models.DateField(
        auto_now_add = True,
        verbose_name = _("Comment date"),
        )

    def __str__(self):
        return f'{self.post_id.content} {self.user_id.username}'

class Like(models.Model):
    user_id = models.ForeignKey(
    User,
    on_delete = models.CASCADE,
    verbose_name = _("Liked by")
    )

    post_id = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        verbose_name = _("Post")
    )

    def __str__(self):
        return f'{self.user_id.username} likes {self.post_id.content}'

class Photo(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        verbose_name = _("Post") 
    )

    image = models.ImageField(
        blank = True,
        null = True,
        upload_to = 'postImages'

    )


