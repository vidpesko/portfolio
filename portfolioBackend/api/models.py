from django.db import models


ICON_CHOICES = {
    "github": "GitHub",
    "web": "Web"
}


class Tag(models.Model):
    name = models.CharField(max_length=20)
    bg_color = models.CharField(max_length=10, default="#66fcf1")

    def __str__(self):
        return self.name


class ProjectLink(models.Model):
    url = models.URLField()
    icon = models.CharField(max_length=20, choices=ICON_CHOICES)

    def __str__(self):
        return self.url


class ProjectStat(models.Model):
    header = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
    label = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        if self.label:
            return f"{self.header}: {self.value}, ({self.label})"
        return f"{self.header}: {self.value}"


class Project(models.Model):
    created = models.DateTimeField(auto_now_add=True)

    # Data
    name = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag)
    links = models.ManyToManyField(ProjectLink)
    stats = models.ManyToManyField(ProjectStat)

    # Display properties
    highlighted = models.BooleanField(default=False)
    background_gradient = models.CharField(
        max_length=100,
        default="background: linear-gradient(to right, #0f0c29, #302b63, #24243e);",
    )

    def __str__(self):
        return self.name


class Experience(models.Model):
    company_name = models.CharField(max_length=50)
    job_role = models.CharField(max_length=50)
    employment_period = models.CharField(max_length=50)
    description = models.TextField()  # List of your roles & activities split by <br>

    def __str__(self):
        return f"{self.job_role} @ {self.company_name}"
