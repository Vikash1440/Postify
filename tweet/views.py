from django.shortcuts import render, get_object_or_404, redirect  
from .models import Tweet  
from .forms import TweetForms,UserRejistrationForm
from django.contrib.auth.decorators import login_required  
from django.contrib.auth import login
def index(req):
    return render(req,'tweet/index.html')

def tweet_list(req):
    tweets=Tweet.objects.all().order_by('create_at')
    return render(req,'tweet/tweet_list.html',{'tweets':tweets})

@login_required
def tweet_create(req):
    if req.method=='POST':
        form=TweetForms(req.POST,req.FILES)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user=req.user
            tweet.save()
            return redirect('tweet_list')
    else:
     form=TweetForms()
    return render(req,'tweet/tweet_forms.html',{'form':form})

@login_required
def tweet_edit(req, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id,user=req.user) 

    if req.method == 'POST':
        form = TweetForms(req.POST, req.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = req.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForms(instance=tweet)  

    return render(req, 'tweet/tweet_forms.html', {'form': form})

@login_required
def tweet_delete(req,tweet_id):
    tweet=get_object_or_404(Tweet,pk=tweet_id,user=req.user) 
    if req.method=='POST':
        tweet.delete()
        return redirect('tweet_list')
    return render(req,'tweet/tweet_conform_delete.html',{'tweet':tweet})
    
def register(req):
    if req.method=='POST':
        form=UserRejistrationForm(req.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(req,user)
            return redirect('tweet_list')
    else:
       form=UserRejistrationForm()

    return render(req,'registration/register.html',{'form':form})

    
    