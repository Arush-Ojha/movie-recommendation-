import tkinter as tk
from tkinter import messagebox
import math

class Movie:
    def __init__(self, title, genre, movie_length, ML, FL, age_restriction, country, production_house, score):
        self.title = title
        self.genre = genre
        self.movie_length = movie_length
        self.ML = ML
        self.FL = FL
        self.age_restriction = age_restriction
        self.country = country
        self.production_house = production_house
        self.score = score

class CineMatch:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, genre, movie_length, ML, FL, age_restriction, country, production_house):
        score = self.score(genre, movie_length, ML, FL, age_restriction, country, production_house)
        new_movie = Movie(title, genre, movie_length, ML, FL, age_restriction, country, production_house, score)
        self.movies.append(new_movie)

    def score(self, genre, movie_length, ML, FL, age_restriction, country, production_house):
        genre_arr = ['Action', 'Drama', 'Comedy', 'Horror', 'Sci-Fi']
        movie_length_arr = ['Short', 'Feature']
        ML_arr = ['60', '90', '120']
        FL_arr = ['Feature', 'Short']
        age_restriction_arr = ['G', 'PG', 'PG-13', 'R']
        country_arr = ['USA', 'UK', 'Canada', 'Australia']
        production_house_arr = ['Production X', 'Production Y', 'Production Z']
        
        custom_genre = 1.0
        custom_movie_length = 1.0
        custom_ML = 1.0
        custom_FL = 1.0
        custom_age_restriction = 1.0
        custom_country = 1.0
        custom_production_house = 1.0

        total_score = 0.0

        if genre in genre_arr:
            index = genre_arr.index(genre)
            score_genre = math.log(((index + 1) ** 2) * custom_genre)
            total_score += score_genre

        if movie_length in movie_length_arr:
            index = movie_length_arr.index(movie_length)
            score_movie_length = math.log(((index + 1) ** 2) * custom_movie_length)
            total_score += score_movie_length

        if ML in ML_arr:
            index = ML_arr.index(ML)
            score_ML = math.log(((index + 1) ** 2) * custom_ML)
            total_score += score_ML

        if FL in FL_arr:
            index = FL_arr.index(FL)
            score_FL = math.log(((index + 1) ** 2) * custom_FL)
            total_score += score_FL

        if age_restriction in age_restriction_arr:
            index = age_restriction_arr.index(age_restriction)
            score_age_restriction = math.log(((index + 1) ** 2) * custom_age_restriction)
            total_score += score_age_restriction

        if country in country_arr:
            index = country_arr.index(country)
            score_country = math.log(((index + 1) ** 2) * custom_country)
            total_score += score_country

        if production_house in production_house_arr:
            index = production_house_arr.index(production_house)
            score_production_house = math.log(((index + 1) ** 2) * custom_production_house)
            total_score += score_production_house

        return total_score

    def search_by_title(self, title):
        results = [movie for movie in self.movies if movie.title.lower() == title.lower()]
        return results

    def search_by_genre(self, genre):
        results = [movie for movie in self.movies if movie.genre.lower() == genre.lower()]
        return results

    def recommend_top_n_movies(self, n):
        if n <= 0:
            return []
        sorted_movies = sorted(self.movies, key=lambda movie: movie.score, reverse=True)
        return sorted_movies[:n]

    def delete_movie(self, title):
        movie_to_delete = None
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                movie_to_delete = movie
                break
        if movie_to_delete:
            self.movies.remove(movie_to_delete)
            return True
        return False

class CineMatchGUI:
    def __init__(self, root, cine_match):
        self.cine_match = cine_match
        self.root = root
        self.root.title("CineMatch - Movie Recommendation System")

        # Add movie
        self.add_frame = tk.Frame(root)
        self.add_frame.pack(pady=10)

        self.add_label = tk.Label(self.add_frame, text="Add Movie")
        self.add_label.pack(side=tk.LEFT, padx=5)

        self.title_entry = tk.Entry(self.add_frame, width=15)
        self.title_entry.pack(side=tk.LEFT, padx=5)
        self.title_entry.insert(0, "Title")

        self.genre_entry = tk.Entry(self.add_frame, width=10)
        self.genre_entry.pack(side=tk.LEFT, padx=5)
        self.genre_entry.insert(0, "Genre")

        self.movie_length_entry = tk.Entry(self.add_frame, width=10)
        self.movie_length_entry.pack(side=tk.LEFT, padx=5)
        self.movie_length_entry.insert(0, "Movie Length")

        self.ML_entry = tk.Entry(self.add_frame, width=5)
        self.ML_entry.pack(side=tk.LEFT, padx=5)
        self.ML_entry.insert(0, "ML")

        self.FL_entry = tk.Entry(self.add_frame, width=10)
        self.FL_entry.pack(side=tk.LEFT, padx=5)
        self.FL_entry.insert(0, "FL")

        self.age_restriction_entry = tk.Entry(self.add_frame, width=5)
        self.age_restriction_entry.pack(side=tk.LEFT, padx=5)
        self.age_restriction_entry.insert(0, "Age")

        self.country_entry = tk.Entry(self.add_frame, width=10)
        self.country_entry.pack(side=tk.LEFT, padx=5)
        self.country_entry.insert(0, "Country")

        self.production_house_entry = tk.Entry(self.add_frame, width=15)
        self.production_house_entry.pack(side=tk.LEFT, padx=5)
        self.production_house_entry.insert(0, "Production House")

        self.add_button = tk.Button(self.add_frame, text="Add", command=self.add_movie)
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Search by title
        self.search_title_frame = tk.Frame(root)
        self.search_title_frame.pack(pady=10)

        self.search_title_label = tk.Label(self.search_title_frame, text="Search by Title")
        self.search_title_label.pack(side=tk.LEFT, padx=5)

        self.search_title_entry = tk.Entry(self.search_title_frame, width=30)
        self.search_title_entry.pack(side=tk.LEFT, padx=5)

        self.search_title_button = tk.Button(self.search_title_frame, text="Search", command=self.search_by_title)
        self.search_title_button.pack(side=tk.LEFT, padx=5)

        # Search by genre
        self.search_genre_frame = tk.Frame(root)
        self.search_genre_frame.pack(pady=10)

        self.search_genre_label = tk.Label(self.search_genre_frame, text="Search by Genre")
        self.search_genre_label.pack(side=tk.LEFT, padx=5)

        self.search_genre_entry = tk.Entry(self.search_genre_frame, width=30)
        self.search_genre_entry.pack(side=tk.LEFT, padx=5)

        self.search_genre_button = tk.Button(self.search_genre_frame, text="Search", command=self.search_by_genre)
        self.search_genre_button.pack(side=tk.LEFT, padx=5)

        # Recommend movies
        self.recommend_frame = tk.Frame(root)
        self.recommend_frame.pack(pady=10)

        self.recommend_label = tk.Label(self.recommend_frame, text="Recommend Top N Movies")
        self.recommend_label.pack(side=tk.LEFT, padx=5)

        self.recommend_entry = tk.Entry(self.recommend_frame, width=10)
        self.recommend_entry.pack(side=tk.LEFT, padx=5)

        self.recommend_button = tk.Button(self.recommend_frame, text="Recommend", command=self.recommend_top_n_movies)
        self.recommend_button.pack(side=tk.LEFT, padx=5)

        # Delete movie
        self.delete_frame = tk.Frame(root)
        self.delete_frame.pack(pady=10)

        self.delete_label = tk.Label(self.delete_frame, text="Delete Movie by Title")
        self.delete_label.pack(side=tk.LEFT, padx=5)

        self.delete_entry = tk.Entry(self.delete_frame, width=30)
        self.delete_entry.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.delete_frame, text="Delete", command=self.delete_movie)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Output
        self.output_text = tk.Text(root, height=10, width=100)
        self.output_text.pack(pady=10)

    def add_movie(self):
        title = self.title_entry.get()
        genre = self.genre_entry.get()
        movie_length = self.movie_length_entry.get()
        ML = self.ML_entry.get()
        FL = self.FL_entry.get()
        age_restriction = self.age_restriction_entry.get()
        country = self.country_entry.get()
        production_house = self.production_house_entry.get()
        
        try:
            if title and genre and movie_length and ML and FL and age_restriction and country and production_house:
                self.cine_match.add_movie(title, genre, movie_length, ML, FL, age_restriction, country, production_house)
                messagebox.showinfo("Success", f"Movie '{title}' added successfully.")
                self.title_entry.delete(0, tk.END)
                self.genre_entry.delete(0, tk.END)
                self.movie_length_entry.delete(0, tk.END)
                self.ML_entry.delete(0, tk.END)
                self.FL_entry.delete(0, tk.END)
                self.age_restriction_entry.delete(0, tk.END)
                self.country_entry.delete(0, tk.END)
                self.production_house_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "All fields must be filled.")
        except ValueError:
            messagebox.showerror("Error", "Error adding movie.")


    def search_by_title(self):
        title = self.search_title_entry.get()
        if title:
            results = self.cine_match.search_by_title(title)
            self.output_text.delete(1.0, tk.END)
            if results:
                for movie in results:
                    self.output_text.insert(tk.END, f"Found: {movie.title}, Genre: {movie.genre}, Movie Length: {movie.movie_length}, "
                                                   f"ML: {movie.ML}, FL: {movie.FL}, Age Restriction: {movie.age_restriction}, "
                                                   f"Country: {movie.country}, Production House: {movie.production_house}, Score: {movie.score:.2f}\n")
            else:
                self.output_text.insert(tk.END, f"No movie found with title '{title}'.\n")
        else:
            messagebox.showerror("Error", "Title cannot be empty.")

    def search_by_genre(self):
        genre = self.search_genre_entry.get()
        if genre:
            results = self.cine_match.search_by_genre(genre)
            self.output_text.delete(1.0, tk.END)
            if results:
                for movie in results:
                    self.output_text.insert(tk.END, f"Found: {movie.title}, Genre: {movie.genre}, Movie Length: {movie.movie_length}, "
                                                   f"ML: {movie.ML}, FL: {movie.FL}, Age Restriction: {movie.age_restriction}, "
                                                   f"Country: {movie.country}, Production House: {movie.production_house}, Score: {movie.score:.2f}\n")
            else:
                self.output_text.insert(tk.END, f"No movies found in genre '{genre}'.\n")
        else:
            messagebox.showerror("Error", "Genre cannot be empty.")

    def recommend_top_n_movies(self):
        try:
            n = int(self.recommend_entry.get())
            results = self.cine_match.recommend_top_n_movies(n)
            self.output_text.delete(1.0, tk.END)
            if results:
                for movie in results:
                    self.output_text.insert(tk.END, f"Recommended: {movie.title}, Genre: {movie.genre}, Movie Length: {movie.movie_length}, "
                                                   f"ML: {movie.ML}, FL: {movie.FL}, Age Restriction: {movie.age_restriction}, "
                                                   f"Country: {movie.country}, Production House: {movie.production_house}, Score: {movie.score:.2f}\n")
            else:
                self.output_text.insert(tk.END, "No movies available to recommend.\n")
        except ValueError:
            messagebox.showerror("Error", "N must be an integer.")

    def delete_movie(self):
        title = self.delete_entry.get()
        if title:
            success = self.cine_match.delete_movie(title)
            if success:
                messagebox.showinfo("Success", f"Movie '{title}' deleted successfully.")
                self.delete_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", f"No movie found with title '{title}'.")
        else:
            messagebox.showerror("Error", "Title cannot be empty.")

if __name__ == "__main__":
    root = tk.Tk()
    cine_match = CineMatch()
    app = CineMatchGUI(root, cine_match)
    root.mainloop()
