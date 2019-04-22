from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Image, Comment, HashTag
from .forms import PostModelForm, ImageModelForm, CommentModelFrom


# Create your views here.

@login_required
@require_http_methods(['GET', 'POST'])
def create_post(request):
    # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
    if request.method == 'POST':
        # ModelFrom(data, files)
        # POST 방식으로 넘온 Data 를 ModelForm 에 넣는다.
        # input type 이 file이면 FILES로 잡아야 한다
        post_form = PostModelForm(request.POST)

        # Data 검증을 한다.
        if post_form.is_valid():
            # 통과하면 저장한다.
            # 가짜 저장
            post = post_form.save(commit=False)
            post.user = request.user
            # 진짜 저장
            post.save()

            # create hashtag
            content = post_form.cleaned_data.get('content') #
            words = content.split(' ') # 띄어쓰기 기준으로 split
            for word in words:
                if word[0] == '#':
                    word = word[1:]
                    tag = HashTag.objects.get_or_create(content=word) # (HasTagObj, True or False)
                    post.tags.add(tag[0])
                    if tag[1]: # 태그가 처음 만들어진거라면, 메세지 추가!
                        messages.add_message((request, messages.SUCCESS, f'#{tag[0].content} 태그를 처음으로 추가하셨어요! :)'))

            for image in request.FILES.getlist('file'):
                request.FILES['file'] = image
                image_form = ImageModelForm(files=request.FILES)
                if image_form.is_valid():
                    # image = Image()
                    # image.file = request.File.get('xxxx')
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect('posts:post_list')
        else:
            # 실패하면, 다시 data 입력 form 을 준다.
            pass
    # GET 방식으로 요청이 오면,
    else:
        # 새로운 POST 용 form 을 만든다.
        post_form = PostModelForm()
    image_form = ImageModelForm()

    return render(request, 'posts/form.html', {
        'post_form': post_form,
        'image_form': image_form,
    })


# # 밑에 코드 refactoring 한게 위에꺼---------------------------------------------------------------------------------------------------------
# @require_http_methods(['GET', 'POST'])
# def post_create(request):
#     # GET 방식으로 Data 를 입력할 form 요청
#     if request.method == 'GET':
#         form = PostModelForm()
#         return render(request, 'posts/form.html', {
#             'form': form,
#         })
#     # POST 방식으로 입력받은 Data 를 저장
#     else:
#         # POST 방식으로 넘어온 Data 를 ModelForm 에 넣는다.
#         form = PostModelForm(request.POST)
#         # Data 검증을 한다.
#         if form.is_valid():
#             # 통과하면 저장한다.
#             form.save()
#             return redirect('posts:post_list')
#         else:
#             # 실패하면, 다시 Data 입력을 form을 준다.
#             return render(request, 'posts/form.html', {
#                 'form': form,
#             })
# ---------------------------------------------------------------------------------------------------------------------------------------------

@login_required
@require_http_methods(['GET', 'POST'])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # 지금 수정하려는 post 작성자가 요청 본내 사람이냐?
    if post.user == request.user:
        if request.method == 'POST':
            post_form = PostModelForm(request.POST, request.FILES, instance=post)
            if post_form.is_valid():
                post_form.save()
                # update hashtag
                post.tags.clear() # 기존의 태그 다 날리기
                content = post_form.cleaned_data.get('content')  #
                words = content.split(' ')  # 띄어쓰기 기준으로 split
                for word in words:
                    if word[0] == '#':
                        word = word[1:]
                        tag = HashTag.objects.get_or_create(content=word)  # (HasTagObj, True or False)
                        post.tags.add(tag[0])

                return redirect('posts:post_list')

        else:
            post_form = PostModelForm(instance=post)
    # 작성자와 요청보낸 user 가 다르다면,
    else:
        # 403 : Forbidden 이유 때문에 거부하는 건데 그냥 말 안해주고 거부하겠다
        return redirect('posts:post_list')

    return render(request, 'posts/form.html', {
        'post_form': post_form,
    })


@require_GET
def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentModelFrom()
    return render(request, 'posts/list.html', {
        'posts': posts,
        'comment_form': comment_form,
    })


@require_POST
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('posts:post_list')


@login_required
@require_POST
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentModelFrom(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/insta/'))
    # TODO: else: => if comment is not valid, then what?


@require_POST
@login_required
def toggle_like(request, post_id):
    user = request.user
    post = get_object_or_404(Post, id=post_id)

    # if post.like_users.get(id=user.id).exist(): # 찾으면, [value] / 없으면, []
    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
    return redirect('posts:post_list')


@require_GET
def tag_posts_list(request, tag_name):
    tag = get_object_or_404(HashTag, content=tag_name)
    posts = tag.posts.all()
    comment_form = CommentModelFrom()
    return render(request, 'posts/list.html', {
        'posts': posts,
        'comment_form': comment_form,
        'h1': f'#{tag} 를 포함한 posts입니다.'
    })