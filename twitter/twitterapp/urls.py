from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.Log_in.as_view(), name='login'),
    path('logout/', login_required(views.Logout.as_view()), name='logout'),
    path('postCreate/', login_required(views.PostCreate.as_view()), name='postCreate'),
    path('', login_required(views.Main.as_view()), name='main'),
    path('Profile/<int:id>/', login_required(views.Profile.as_view()), name='Profile'),
    path('postPage/<int:id>/', login_required(views.PostPage.as_view()), name='postPage'),
    path('Poisk/', login_required(views.Poisk.as_view()), name='Poisk'),
    path('Profile/', login_required(views.SelfProfile.as_view()), name='SelfProfile'),
    path('Profile/Media', login_required(views.AllImages.as_view()), name='Media'),
    path('Profile/Liked', login_required(views.AllLikes.as_view()), name='Liked'),
    path('Profile/Comments', login_required(views.AllComments.as_view()), name='Comments')
]
