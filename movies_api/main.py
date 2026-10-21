from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel
from dotenv import load_dotenv
import json, os

load_dotenv() 
API_KEY = os.getenv("API_KEY")

app = FastAPI()

FILENAME = "movies.json"

def load_movies():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return [
        {"id": 1, "title": "The Matrix", "director": "Wachowski's", "year": 1965},
        {"id": 2, "title": "Total Recall", "director": "William Gibson", "year": 1984},
        {"id": 3, "title": "Neon Genesis Evangelion: The End of Evangelion", "director": "J.R.R. Tolkien", "year": 1937},
        {"id": 4, "title": "Finding Francis", "director": "Isaac Asimov", "year": 1951},
    ]

def save_movies():
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2)

movies = load_movies()

class Movie(BaseModel):
    title: str
    director: str
    year: int

class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None

def check_key(x_api_key: str | None = Header(default=None)):
    if not API_KEY or x_api_key != API_KEY:
        raise HTTPException(status_code=401)

def find_movie(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="Book not found")    

""" @app.get("/movies/")
def get_movies():
    return movies """

@app.patch("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def patch_movie(movie_id: int, changes: MovieUpdate):
    existing = find_movie(movie_id)
    
    update_data = changes.model_dump(exclude_unset=True)
    
    existing.update(update_data)
    
    save_movies()
    return existing

@app.get("/movies/{movies_id}")
def get_movie(movie_id: int):
    return find_movie(movie_id)

@app.get("/movies/")
def get_movies(director: str | None = None, year: int | None = None):
    if director:
        return [movie for movie in movies if director.lower() in movie["director"].lower()]
    elif year:
        return [movie for movie in movies if year == movie["year"]]
    return movies

@app.post("/movies/", status_code=204, dependencies=[Depends(check_key)])
def create_movie(movie: Movie):
    new_id = max((m["id"] for m in movies), default=0) + 1
    new_movie = {'id': new_id, 'title': movie.title, 'director': movie.director, 'year': movie.year}
    movies.append(new_movie)

    save_movies()
    return new_movie

@app.delete("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def delete_movie(movie_id: int):
    existing = find_movie(movie_id)
    movies.remove(existing)
    save_movies()

@app.put("/movies/{movie_id}", status_code=204, dependencies=[Depends(check_key)])
def replace_movie(movie_id: int, movie: Movie):
    existing = find_movie(movie_id)
    existing['title'] = movie.title
    existing['director'] = movie.director
    existing['year'] = movie.year
    
    save_movies()
    return existing


#PUT FOR REPLACE ME, ALL OF ME
#PATCH TO PATCH UP THE HOLE YOU LEFT IN MY HEART.............

#422 Unprocessable Content
#404 not found

#IF TWO PEOPLE WRITE AT THE SAME TIME? I DONT KNOW. MAYBE... YOU CAN PUT THEM IN A CUE. OR SOME KIND OF WRITE AHEAD... Hmmm..
