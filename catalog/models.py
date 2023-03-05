from django.db import models


# Create your models here.


class Notes(models.Model):
    headings = models.CharField(max_length=20)
    text = models.CharField(max_length=200)

    def dict(self) -> dict:
        return {
            "id": self.id,
            'text': self.text,
            'headings': self.headings,
        }

