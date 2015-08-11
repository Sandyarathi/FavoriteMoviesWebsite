__author__ = 'sandyarathidas'
#Movies class to hold the properties of each movie in the movie-list
#Import the webbrowser class for the program to interact with the system web browser
import webbrowser
class Movie():
    #define constructor to load the Movie properties upon instantiation
    def __init__(self,movie_title,movie_storyLine,movie_posterImage,movie_trailerlink):
        self.title=movie_title
        self.storyLine=movie_storyLine
        self.poster_image_url=movie_posterImage
        self.trailer_youtube_url=movie_trailerlink

    #define a show_trailer method to display the trailer when clicked on any movie poster
    def show_trailer(self):
        webbrowser.open(self.trailerlink)



