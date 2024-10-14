from django.urls import path, include

from .views import home, ProjectList, ExperienceList


urlpatterns = [
    path('', home),

    path('list-projects/', ProjectList.as_view()),
    path('list-experiences/', ExperienceList.as_view())
]
