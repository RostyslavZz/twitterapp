from django.shortcuts import render
from .forms import Registration, Login, Comments
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.core.files import File
from pathlib import Path
from .models import Post, User, Follow, Comment, Like
from django.http import JsonResponse
from django.template.loader import render_to_string


class RegistrationView(CreateView):
    form_class = Registration
    template_name = 'registration.html'
    def get_success_url(self):
        follow = Follow(user=self.object)
        follow.save()
        return reverse('login')


class Log_in(LoginView):
    form_class = Login
    template_name = 'login.html'
    redirect_authenticated_user = True


class Logout(LogoutView):
    pass


class PostCreate(TemplateView):
    def post(self, request):
        datapost = request.POST
        datafile = request.FILES['image']
        with open('twitterapp/static/images/file12345.png', 'wb') as file:
            file.write(datafile.read())
        path = Path('twitterapp/static/images/file12345.png')
        with path.open(mode='rb') as path1:
            pathfile = File(path1, path1.name)
            post1 = Post(text=datapost['text'], image=pathfile, user=self.request.user)
            post1.save()
            return JsonResponse('', safe=False)


class Main(TemplateView):
    template_name = 'main.html'

    def post(self, request):
        data = request.POST
        post1 = Post.objects.get(id=data['key'])
        likes = Like.objects.filter(post=post1)
        user = self.request.user
        for a in likes:
            if a.user == user:
                a.delete()
                return JsonResponse({'like': 0, 'kol': len(likes) - 1}, safe=False)
        else:
            like = Like(user=user, post=post1)
            like.save()
            return JsonResponse({'like': 1, 'kol': len(likes) + 1}, safe=False)


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        posts = []
        allposts = Post.objects.all()
        followed = Follow.objects.get(user=self.request.user)
        for a in allposts:
            if a.user in followed.following.all():
                alllikes = Like.objects.filter(post=a)
                for b in alllikes:
                    if b.user == self.request.user:
                        posts.append([a, len(alllikes), 1, a.createat.strftime('%d.%b.%Y')])
                        break
                else:
                    posts.append([a, len(alllikes), 0, a.createat.strftime('%d.%b.%Y')])
        context['following'] = posts
        return context

class Profile(TemplateView):
    template_name = 'Profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(id=self.kwargs['id'])
        usersPosts = Post.objects.filter(user=user)
        follow = Follow.objects.get(user=self.request.user)
        if user in follow.following.all():
            context['followed'] = 'followed'
        else:
            context['followed'] = 'notfollowed'
        context['user'] = user
        context['post'] = usersPosts
        return context
    def post(self, request, **kwargs):
        data = request.POST
        user = self.request.user
        fuser = User.objects.get(id=self.kwargs['id'])
        if 'follow' in data.keys():
            follow = Follow.objects.get(user=user)
            hisuser = Follow.objects.get(user = fuser)
            if fuser in follow.following.all():
                follow.following.remove(fuser)
                follow.save()
                hisuser.followers.remove(user)
                hisuser.save()
                return JsonResponse({'key': 'unfollowed'}, safe=False)
            else:
                follow.following.add(fuser)
                follow.save()
                hisuser.followers.add(user)
                hisuser.save()
                return JsonResponse({'key': 'followed'}, safe=False)
class PostPage(TemplateView):
    template_name = 'postPage.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        posts = Post.objects.get(id=self.kwargs['id'])
        context['post'] = posts
        user = posts.user
        context['user'] = user
        context['form'] = Comments()
        context['comments'] = Comment.objects.filter(post=posts)
        likes = Like.objects.filter(post=posts)
        context['keylike'] = len(likes)
        for a in likes:
            if self.request.user == a.user:
                context['like'] = 0
                break
        else:
            context['like'] = 1


        return context
    def post(self, request, **kwargs):
        data = request.POST
        postt = Post.objects.get(id=self.kwargs['id'])
        user = self.request.user
        if 'id_text' in data.keys():
            comment = Comment(user=user, text=data['id_text'], post=postt)
            comment.save()
            same = f'<p><b>{user.username}</b> {data["id_text"]}</p>'
            return JsonResponse(same, safe=False)
        elif 'like' in data.keys():
            like = Like.objects.filter(post=postt)
            for a in like:
                if user == a.user:
                    a.delete()
                    return JsonResponse({'like': 0, 'kol': len(like) - 1}, safe=False)
            else:
                newlike = Like(user=user, post=postt)
                newlike.save()
                return JsonResponse({'like': 1, 'kol': len(like) + 1}, safe=False)


class Poisk(TemplateView):
    template_name = 'Poisk.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['user'] = self.request.user
        return context

    def post(self, request):
        data = request.POST
        getuser = User.objects.filter(username__icontains=data['pole'])
        kysok = render_to_string('kysok p.html', {'kkey' : getuser})
        return JsonResponse(kysok, safe=False)


class SelfProfile(TemplateView):
    template_name = 'SelfProfile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        usersPosts = Post.objects.filter(user=user)
        follow = Follow.objects.get(user=self.request.user)
        if user in follow.following.all():
            context['followed'] = 'followed'
        else:
            context['followed'] = 'notfollowed'
        context['user'] = user
        posts = []
        context['manyposts'] = len(usersPosts)
        context['usersdata'] = user.date_joined.strftime('%B %Y')
        context['koldata'] = len(follow.followers.all())
        context['kolsub'] = len(follow.following.all())
        for a in usersPosts:
            alllikes = Like.objects.filter(post=a)
            for b in alllikes:
                if b.user == self.request.user:
                    posts.append([a, len(alllikes), 1])
                    break
            else:
                posts.append([a, len(alllikes), 0])
        context['posts'] = posts
        return context


class AllComments(TemplateView):
    template_name = 'SelfProfile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        selfComment = Comment.objects.filter(user=user)
        selfPosts = set()
        comments = []
        usersPosts = Post.objects.filter(user=user)
        for a in selfComment:
            selfPosts.add(a.post)
        for b in selfPosts:
            alllikes = Like.objects.filter(post=b)
            for b in alllikes:
                if b.user == self.request.user:
                    comments.append([b, len(alllikes), 1])
                    break
            else:
                comments.append([b, len(alllikes), 0])
        follow = Follow.objects.get(user=user)
        context['posts'] = comments
        context['manyposts'] = len(usersPosts)
        context['usersdata'] = user.date_joined.strftime('%B %Y')
        context['koldata'] = len(follow.followers.all())
        context['kolsub'] = len(follow.following.all())
        return context

class AllLikes(TemplateView):
    template_name = 'SelfProfile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        selfLikes = Like.objects.filter(user=user)
        selflike = set()
        usersPosts = Post.objects.filter(user=user)
        likes = []
        for a in selfLikes:
            selflike.add(a.post)
        for b in selflike:
            alllikes = Like.objects.filter(post=b)
            for b in alllikes:
                if b.user == self.request.user:
                    likes.append([b, len(alllikes), 1])
                    break
            else:
                likes.append([b, len(alllikes), 0])
        follow = Follow.objects.get(user=user)
        context['posts'] = likes
        context['manyposts'] = len(usersPosts)
        context['usersdata'] = user.date_joined.strftime('%B %Y')
        context['koldata'] = len(follow.followers.all())
        context['kolsub'] = len(follow.following.all())
        return context


class AllImages(TemplateView):
    template_name = 'SelfProfile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        selfposts = Post.objects.filter(user=user)
        selfImages = []
        usersPosts = Post.objects.filter(user=user)
        for a in selfposts:
            if a.image is not None:
                selfImages.append(a.image)
        follow = Follow.objects.get(user=user)
        context['selfImages'] = selfImages
        context['manyposts'] = len(usersPosts)
        context['usersdata'] = user.date_joined.strftime('%B %Y')
        context['koldata'] = len(follow.followers.all())
        context['kolsub'] = len(follow.following.all())
        return context










