from django.urls import path, include

from .views import home, ProjectList, HighlightedProjectList


urlpatterns = [
    path('', home),

    path('list-projects/', ProjectList.as_view())
]
