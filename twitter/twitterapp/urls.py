from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('logout/', login_required(views.Logout.as_view()), name='logout'),
    path('postCreate/', login_required(views.PostCreate.as_view()), name='postCreate'),
    path('', login_required(views.Main.as_view()), name='main'),
    path('Profile/<int:id>/', login_required(views.Profile.as_view()), name='Profile'),
    path('postPage/<int:id>/', login_required(views.PostPage.as_view()), name='postPage'),
    path('Poisk/', login_required(views.Poisk.as_view()), name='Poisk'),
    path('Profile/', login_required(views.SelfProfile.as_view()), name='SelfProfile'),
    path('Profile/Media', login_required(views.AllImages.as_view()), name='Media'),
    path('Profile/Liked', login_required(views.AllLikes.as_view()), name='Liked'),
    path('Profile/Comments', login_required(views.AllComments.as_view()), name='Comments'),
    path('newajax/', login_required(views.Newbase.as_view()), name='Newbase'),
    path('Profile/<int:id>/Media/', login_required(views.AllImagesUser.as_view()), name='MediaUser'),
    path('Profile/<int:id>/Liked/', login_required(views.AllLikesUser.as_view()), name='LikedUser'),
    path('Profile/<int:id>/Comments/', login_required(views.AllCommentsUser.as_view()), name='CommentsUser')
]
