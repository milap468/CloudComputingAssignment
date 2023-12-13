from django.db import models
import uuid
from django.contrib.auth.models import User

class FileUpload(models.Model):

    fileId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to="files/")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"{self.fileId} is added by {self.user} at {self.createdAt}."

