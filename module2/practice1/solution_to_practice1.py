# classify movies based on their ratings
def classify_movie(ratings):
    if ratings >= 8.5:
        return "Super Hit"
    elif ratings >= 8.0:
        return "Hit"
    elif ratings >= 7.0:
        return "Average"
    elif ratings >= 6:
        return "Flop"
    else:
        return "Bad"

# sort movie list based on their ratings
def sort_movies_by_ratings(movies):
    return sorted(movies, key=lambda movie: movie['ratings'], reverse=True)


# write unit tests for the above functions
def test_classify_movie():
    assert classify_movie(8.5) == "Super Hit"
    assert classify_movie(8.0) == "Hit"
    assert classify_movie(7.0) == "Average"
    assert classify_movie(6.0) == "Flop"
    assert classify_movie(5.0) == "Bad"

# please change movie name to match your implementation
def test_sort_movies_by_ratings():
    movies = [
        {'name': 'movie1', 'ratings': 8.5},
        {'name': 'movie2', 'ratings': 8.0},
        {'name': 'movie3', 'ratings': 7.0},
        {'name': 'movie4', 'ratings': 6.0},
        {'name': 'movie5', 'ratings': 5.0},
    ]
    expected = [
        {'name': 'movie1', 'ratings': 8.5},
        {'name': 'movie2', 'ratings': 8.0},
        {'name': 'movie3', 'ratings': 7.0},
        {'name': 'movie4', 'ratings': 6.0},
        {'name': 'movie5', 'ratings': 5.0},
    ]
    assert sort_movies_by_ratings(movies) == expected
    