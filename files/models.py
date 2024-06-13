from django.db import models


class File(models.Model):
    uploaded_at = models.DateTimeField()
    file = models.FileField(upload_to="media/")


# TODO(tikinang): Comments.
