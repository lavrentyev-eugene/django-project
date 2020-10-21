from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index,name='index_url'),
    path('<str:question_text>/answers/', views.detail, name='detail_url'),
    path('<str:question_text>/results/', views.results, name='results_url'),
    path('<str:question_text>/vote/', views.vote, name='vote_url'),
    path('<str:question_text>/answers/<str:choice_text>/votes_amount/', views.votes_amount, name='votes_amount_url')
]
