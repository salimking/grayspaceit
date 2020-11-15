from django.shortcuts import render
import requests

# POSTS VIEW ENDPOINT
def posts(request):
    
    return render(request, 'blog-listing.html')


# POST DETAILS VIEW ENDPOINT
def post_details(request):
    data=requests.get('https://jsonplaceholder.typicode.com')
    l=data.json()
    con={
        'data':l
    }
    return render(request, 'blog-post.html',con)