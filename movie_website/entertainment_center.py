import media
import fresh_tomatoes


toy_story = media.Movie("Inglourious Basterds",
                        "https://upload.wikimedia.org/wikipedia/en/c/c3/Inglourious_Basterds_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=KnrRy6kSFF0",
                        "August 21, 2009")

avatar = media.Movie("The Wolf of Wall Street",
                     "https://upload.wikimedia.org/wikipedia/en/1/1f/WallStreet2013poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=iszwuX1AK6A",
                     "December 25, 2013")

inception = media.Movie("Inception",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=YoHD9XEInc0",
                        "July 13, 2010")

school_of_rock = media.Movie("The Martian",
                             "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=Ue4PCI0NamI",
                             "October 2, 2015")

ratatoulli = media.Movie("The Dark Knight",
                         "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=_PZpmTj1Q8Q",
                         "July 18, 2008")

hunger_games = media.Movie("La La Land",
                           "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",  # NOQA
                           "https://www.youtube.com/watch?v=0pdqf4P9MB8",
                           "December 9, 2016")

movies = [toy_story, avatar, inception, school_of_rock, ratatoulli,
          hunger_games]
fresh_tomatoes.open_movies_page(movies)
