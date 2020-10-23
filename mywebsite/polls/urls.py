from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(),name='index_url'),
    path('<int:pk>/answers/', views.DetailView.as_view(), name='detail_url'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results_url'),
    path('<int:question_id>/vote/', views.vote, name='vote_url'),
    path('<int:question_id>/answers/<str:choice_text>/votes_amount/', views.votes_amount, name='votes_amount_url')
]
