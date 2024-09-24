movies = [
    # Malayalam Movies
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2009,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]


# total no of movies

movies_count=len(movies)

# print("movies count" , movies_count)

#  movies with genre drama

genre_filter=[m.get("title") for m in movies if "Drama" in m.get ("genres")]

# print(genre_filter)

# top movie (movies with rating)
def get_year(mov):

    return mov.get("year")
latest_movies=max(movies,key=get_year)
# print(latest_movies)

movie_year_filter=[m.get("title")for m in movies if m.get("year")==latest_movies.get("year")]
# print(movie_year_filter)

# movies wich malayalam
language=[m.get("title") for m in movies if "Malayalam" in m.get("language")]

# print(language)

# top rating

def get_rating(mov):
    return mov.get("rating")

top_movie_data=max(movies,key=get_rating)

top_rating_movies=[m.get("title") for m in movies if m.get("rating")==top_movie_data.get("rating")]
# print(top_rating_movies)
# movies released after year 2016
relased=[m.get("title") for m in  movies if m.get("year")>2016]
# print(relased)

# movies with lowest rating

def get_rating(mov):
    return mov.get("rating")

lowest_movie_data=min(movies,key=get_rating)
least_rating_movies=[m.get("title") for m in movies if m.get("rating")==lowest_movie_data.get("rating")]
# print(least_rating_movies)

# malayalam movies with genre action 

malayalam_action_movies=[m.get("title") for m in movies if "Drama "in m.get("genres") and m.get("language")=="Malayalam"]

# print(malayalam_action_movies).


 # oldest movies

movies_ditionary={}
for m in movies:
    relase_year=m.get("year")

    if relase_year in movies_ditionary:

        movies_ditionary.get(relase_year).append(m.get("title"))

        pass


    else:
        movies_ditionary[relase_year]=[m.get("title")]


print(movies_ditionary)


oldest_movie_data=min(movies,key=get_year)

oldest_movie_name=[m.get("title") for m in movies if m.get("year")==oldest_movie_data.get("year")]

print(oldest_movie_name)

# num of movies realeased in each year

years=[m.get("year")for m in movies]

print(years)

years_count={y:years.count(y)for y in years}
print(years_count)

# genres={g for m in movies for g in m.get("genres")}

# print(genres)

all_genres=[g for m in movies for g in m.get("genres")]


genres_count={g:all_genres.count(g) for g in all_genres}

print(genres_count)

def get_title(m):
    return m.get("title")

sorted_movies=sorted(movies,key=get_title)
sorted_movies_title=[m.get("title") for m in sorted_movies]

print(sorted_movies_title)