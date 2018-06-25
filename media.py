import webbrowser

class Movie(): 
    """A class that representes a movie"""

    #initialize the class with the info passed in those params
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    #show the movie trailer passad in the trailer_youtube_url param
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)