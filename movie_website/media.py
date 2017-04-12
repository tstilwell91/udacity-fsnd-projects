import webbrowser


class Movie():
    """ Store and retrieve movie information.

    Provides a way to store movie related information and show a movie's
    trailer in a web browser.

    Attributes:
        movie_title: A string containing the title of a movie.
        poster_image_url: A string containing the URL of a poster image.
        trailer_youtube_url: A string containing the URL for a trailer's
            youtube link.
        release_date: A string containing the release date of a movie.

    Methods:
        __init__: Constructor for class Movie
        show_trailer: Opens a web browser to the trailer_youtube_url
            of a Movie object
    """

    def __init__(self, movie_title, poster_image_url, trailer_youtube_url,
                 release_date):
        """ Constructor for Movie class."""
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_date = release_date

    def show_trailer(self):
        """ Opens browser to a movie's trailer."""
        webbrowser.open(self.trailer_youtube_url)
