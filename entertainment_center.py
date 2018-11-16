import media
import fresh_tomatoes

title = "Toy Story"

toy_story = media.Movie(title,
                        "A film about a boy and his toys who "
                        "have life and he doesn't know",
                        "https://upload.wikimedia.org/wikipedia"
                        "/pt/d/dc/Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=KYz2"
                        "wyBy3kc")

deadpool = media.Movie("Deadpool",
                       "A filme about a very nice and respect"
                       "ful anti-hero.. kk just kidding!",
                       "https://m.media-amazon.com/images/M/M"
                       "V5BYzE5MjY1ZDgtMTkyNC00MTMyLThhMjAtZG"
                       "I5OTE1NzFlZGJjXkEyXkFqcGdeQXVyNjU0OTQ"
                       "0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=Q9X-bAE8KTc")

interestellar = media.Movie("Interestellar",
                            "The best film of all times about space"
                            "traveling and time",
                            "https://upload.wikimedia.org/wikipedia"
                            "/pt/3/3a/Interstellar_Filme.png",
                            "https://www.youtube.com/watch?v=N67wLtpN-Sc")

hackers = media.Movie("Hackers",
                      "A old but a very nice filme about a group "
                      "of young hackers",
                      "http://cdn.collider.com/wp-content/uploads"
                      "/2015/10/hackers-blu-ray-20th-anniversary-edition.jpg",
                      "https://www.youtube.com/watch?v=Rn2cf_wJ4f4")

movies = [toy_story, deadpool, interestellar, hackers]
fresh_tomatoes.open_movies_page(movies)
