from django.shortcuts import render, HttpResponse, redirect
from blog.models import Contact
from django.contrib import messages
from ali.models import Post, PostComment
from django.shortcuts import get_object_or_404
from blog.templatetags import get_dict




# Create your views here.


def bloghome(request):
    all_posts = Post.objects.all()
    return render(request, 'ali/bloghome.html', {"all_posts": all_posts})


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    # messages.error(request, "Welcome here in Contact Page of ALI")
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']

        if len(name) < 2 or len(email) < 3 or len(phone) < 11 or len(content) < 4:
            messages.error(request, "Please Fill the form correctly")
        else:
            contact = Contact(name=name, phone=phone,
                              email=email, content=content)
            contact.save()
            messages.success(
                request, "Thank you for contacting us. We will get back to you ASAP.")

    return render(request, 'blog/contact.html')


def search(request):
    # all_posts = Post.objects.all()
    query = request.GET['query']
    if len(query) > 78 or len(query) < 1:
        all_posts = Post.objects.none()
    else:
        all_posts_title = Post.objects.filter(title__icontains=query)
        all_posts_content = Post.objects.filter(content__icontains=query)
        all_posts = all_posts_title.union(all_posts_content, all_posts_title)
    params = {"all_posts": all_posts, "query": query}
    return render(request, 'ali/search.html', params)


def blogpost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = PostComment.objects.filter(post=post, parent=None)
    replies = PostComment.objects.filter(post=post).exclude(parent=None)
    repDict = {}
    for reply in replies:
        if reply.parent.postSno not in repDict.keys():
            repDict[reply.parent.postSno] = [reply]
        else:
            repDict[reply.parent.postSno].append(reply)
    # print(repDict)
    return render(request, 'ali/blogpost.html', {'post': post, "comments": comments, "user": request.user, "count": len(comments), "repDict": repDict})


def postComment(request):
    if request.method == "POST":
        # Check if this is a reply to another comment
        comment_text = request.POST.get('comment') or request.POST.get('reply')
        postid = request.POST.get('postSno')
        post = get_object_or_404(Post, sno=postid)

        # Handling reply to another comment
        commentreply = request.POST.get('parentsno')
        user = request.user

        if comment_text.strip():
            if commentreply:
                parent_comment = get_object_or_404(PostComment, postSno=commentreply)
                comment = PostComment(comment=comment_text, user=user, post=post, parent=parent_comment)
                comment.save()
                messages.success(request, "Your reply has been posted successfully")
            else:
                comment = PostComment(comment=comment_text, user=user, post=post)
                comment.save()
                messages.success(request, "Your comment has been posted successfully")

        else:
            messages.error(request, "Comment cannot be empty.")
        
        return redirect(f"/blog/{post.slug}/")
    
    return redirect("/blog/")
