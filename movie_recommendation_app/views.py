from django.http import request
from django.shortcuts import render
from movie_recommendation_app.recommend_model import recommend

def movie_recommendation(request):
    if 'movie' in request.POST:
        movie_name = request.POST['movie']
        recommended_movies = recommend(movie_name)
        if request.method == 'POST':
            return render(request, 'home.html', {'recommended_movies': recommended_movies})

    else:
        return render(request, 'home.html')

