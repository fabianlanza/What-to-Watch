import random
import os
from colored import fg, bg, attr
class colors:
    green = fg('green')
    red = fg('red')
    reset = attr('reset')



# streaming sites
streaming_site = ["Netflix"]

# movie types
movie_type = ["Action", 
"Trending Now",
"Hollywood Comedy Movies",
"Goofy Comedies",
"Comedies",
"Dramas",
"Action Thrillers",
"Award-Winning Films",
"Action & Adventure",
"Popular on Netflix",
"Suspenseful Movies",
"Feel-good Movies",
"Crime Action",
"Exciting Sci-Fi & Fantasy",
"Get in On the Action",
"Top 10 today"]

# movie number
movie_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


random_streaming_site = random.choice(streaming_site)
random_movie_type = random.choice(movie_type)
random_movie_number = random.choice(movie_number)

print("Created by: Fabian")
print(f"{colors.red}Streaming site: {colors.reset}{random_streaming_site}\n{colors.green}Movie Type: {colors.reset}{random_movie_type}\n{colors.green}Movie Number: {colors.reset}{random_movie_number}")
os.system("pause")