import media
import movie_WebPageLauncher
"""
__author__ = 'sandyarathidas'
Instantiates the movie objects by passing parameter
values to the Movie class constructor and then
creates a list of all objects instantiated.
"""
toy_story = media.Movie(
    "Toy Story",
    "Story of boys and toys",
    "http://www.disneymania.com.br/wp-content/uploads/2010/04/toy-story-3-personagens-final-1.jpg",  # noqa
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    "Tom Hanks",
    "John Lasseter")

avatar = media.Movie(
    "Avatar",
    "Scientists and aliens",
    "http://www.masculinity-movies.com/wp-content/uploads/2010/02/avatar-movie-poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=d1_JBMrrYw8"
    "Sam Worthington",
    "James Cameron")

interstellar = media.Movie(
    "Interstellar",
    "Space drama",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt6Z71dDSl04F3G1OCff21vRh8i26RVEXfMzK2UchzyJJyzF1F",  # noqa
    "https://www.youtube.com/watch?v=0vxOhd4qlnA"
    "Mathew McConaughey",
    "Christopher Nolan")

bahubali = media.Movie(
    "Bahubali",
    "Mythological story of a great king",
    "http://bollywoodflick.in/wp-content/uploads/2015/07/baahubali-movie-posters.jpg",  # noqa
    "https://www.youtube.com/watch?v=sOEg_YZQsTI"
    "Prabhas",
    "S.S.Rajamouli")

tangled = media.Movie(
    "Tangled",
    "Princess with long hair",
    "http://i01.i.aliimg.com/wsphoto/v0/32321942623/-font-b-Tangled-b-font-Rapunzel-font-b-Movie-b-font-Fabric-font-b-poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=ip_0CFKTO9E"
    "Mandy Moore",
    "Nathan Greno")

minions = media.Movie(
    "Minions",
    "Minions Mania",
    "http://www.aroundhawaii.com/wp-content/uploads/2015/07/minions-2015-movie-wallpaper-poster-bob-kevin-stuart-poster-wallpaper-scarlet-overkill-sandra-bullock-despicable-me.jpg",  # noqa
    "https://www.youtube.com/watch?v=dVDk7PXNXB8"
    "Sandra Bullock",
    "Kyle Balda")

# define a list of all the movie objects
movie_list = [toy_story, avatar, interstellar, bahubali, tangled, minions]

# pass the list of movies to the method in movie_WebPageLauncher.py
movie_WebPageLauncher.open_movies_page(movie_list)
