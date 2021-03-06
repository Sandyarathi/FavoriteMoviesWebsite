import webbrowser


class Movie():
    """
    __author__ = 'sandyarathidas'
    Defines the movie data structure to store all
    the properties associated with the movie object.
    """
    def __init__(
        self,
        movie_title,
        movie_storyLine,
        movie_posterImage,
        movie_trailerlink,
        movie_actor,
        movie_director):
        """
        Contructor Instantiates the movie object
        with the properties set by user.
        """
        self.title = movie_title
        self.storyLine = movie_storyLine
        self.poster_image_url = movie_posterImage
        self.trailer_youtube_url = movie_trailerlink
        self.actor=movie_actor
        self.director=movie_director

    def show_trailer(self):
        """
        Defines a show_trailer method to display
        the trailer when clicked on any movie poster
        """
        webbrowser.open(self.trailerlink)
