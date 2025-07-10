from django.shortcuts import render

def post_list(repuest):
  return render(repuest, 'blog/post_list.html', {})

# Create your views here.
