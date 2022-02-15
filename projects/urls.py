from django.urls import path
from . import views
from .views import *

urlpatterns = [
     path('viewproject/<int:id>',viewdataofproject,name="detail"),
     path('addproject',addproject,name='addproject'),
     path('djero2351ellsdagnabknaslkhgponvdslnds;ejw/<int:id>',views.delete,name='delete'),
     path('',index),
     path('report/<int:id>',report,name='report'),
     path('rate/<int:id>',rate,name='rate'),
     path('donate/<int:id>',donate,name='donate'),
     path('comment/<int:id>',comment,name='comment'),
     path('reportComment/<int:id>/<int:project_id>',reportComment,name='reportComment'),
     path('deleteComment/<int:id>/<int:project_id>',deleteComment,name='deleteComment'),
     path('category/<int:id>',category_projects,name='category_projects'),
     path('search',search,name='search')
]