import sqlite3
from datamodel.movie import Movie


class View:

    def __init__(self, name):
        self.name = name

    def movies(self):
        # TODO:
        # Potrebno je implementirati metodu `movies`.
        # Zadatak metode je spojiti se na bazu podataka imena `self.name`.
        # Metoda zatim mora iz baze dohvatiti sve filmove iz tablice `movies`.
        # Stupci u tablici se zovu `title` i `year`.
        # Metoda mora vratiti listu objekata klase `Movies`.
        # Primjer baze podataka nalazi se u `test_data/movies.db`
        # Baza podataka je Sqlite.



        movies = []
        # Spoji se na bazu podataka
        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()
        # Dohvati sve filmove iz tablice 'movies'
        cursor.execute("SELECT title, year FROM movies")
        rows = cursor.fetchall()
        # Pretvori rezultate u objekte klase Movie
        for row in rows:
            title, year = row
            movie = Movie(title, year)
            movies.append(movie)
        # Zatvori vezu s bazom podataka
        connection.close()
        # Vrati listu filmova
        return movies
