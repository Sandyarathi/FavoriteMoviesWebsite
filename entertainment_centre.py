__author__ = 'sandyarathidas'
import media
import movie_WebPageLauncher
#instatiating movie1: toy story
toy_story=media.Movie("Toy Story","Story of boys and toys","http://www.disneymania.com.br/wp-content/uploads/2010/04/toy-story-3-personagens-final-1.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

#instatiating movie2: avatar
avatar=media.Movie("Avatar","Scientists and aliens","http://www.masculinity-movies.com/wp-content/uploads/2010/02/avatar-movie-poster.jpg","https://www.youtube.com/watch?v=d1_JBMrrYw8")

#instatiating movie3: interstellar
interstellar=media.Movie("Interstellar","Space drama","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQt6Z71dDSl04F3G1OCff21vRh8i26RVEXfMzK2UchzyJJyzF1F","https://www.youtube.com/watch?v=0vxOhd4qlnA")

#instatiating movie4: Bahubali
bahubali=media.Movie("Bahubali","Mythological story of a great king","http://bollywoodflick.in/wp-content/uploads/2015/07/baahubali-movie-posters.jpg","https://www.youtube.com/watch?v=sOEg_YZQsTI");

#instatiating movie5: Tangled
tangled=media.Movie("Tangled","Princess with long hair","http://i01.i.aliimg.com/wsphoto/v0/32321942623/-font-b-Tangled-b-font-Rapunzel-font-b-Movie-b-font-Fabric-font-b-poster.jpg","https://www.youtube.com/watch?v=ip_0CFKTO9E")

#instatiating movie6: Minions
minions=media.Movie("Minions","Minions Mania","http://www.aroundhawaii.com/wp-content/uploads/2015/07/minions-2015-movie-wallpaper-poster-bob-kevin-stuart-poster-wallpaper-scarlet-overkill-sandra-bullock-despicable-me.jpg","https://www.youtube.com/watch?v=dVDk7PXNXB8")

#defining a list of all the movie objects
movie_list=[toy_story,avatar,interstellar,bahubali,tangled,minions]

#Pass the list of movies to the open_movies_page method in movie_WebPageLauncher.py
movie_WebPageLauncher.open_movies_page(movie_list)


