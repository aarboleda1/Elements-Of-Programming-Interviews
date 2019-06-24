"""
An online movie ticket booking system facilitates the purchasing of movie
tickets to its customers. E-ticketing systems allow customers to browse
through movies currently playing and book seats, anywhere and anytime.

How to implement seat booking process?
Use Cases

V2
A user can search for a movie make sure to handle concurrency!
1) define actors and use cases
2) go through high level class diagram
3) go into a few functions

Use cases/class hierarchy
- User should be able to search for movies
    - searchByLocation
    - searchByMovie
    - searchByTime

# Movie Info
class Theater:
    location
    auditoriums

class Show:
    auditorium: Auditorium

class Movie:
    shows: List[Show]
    start_time
    end_time

# Search API
class SearchCatalog(Search):
    movies_by_title: Dict[str: Movie]
    movies_by_city: Dict[str: Movie]

    def search_by_movie(self, movie_name):
        return self.movies_by_title.get(movie_name)

class Search(ABC):
    def search_by_title(self):
        pass
    def search_by_location(self):
        pass

# Booking a seat. For this model, we can have the user take in a booking a booking
# class, attempt to reserve. Handle concurrency
class Booking:
    num_seats
    booking_number
    booking_id

class User:
    def make_booking(booking):
        conn = await get_conn(ConnectionType.SERIALIZABLE)
        rows = await conn.query(
            "SELECT * FROM seat where id IN (%s) AND reserved = 0 FOR UPDATE",
            [seat_ids]
        )
        # rows are locked
        if len(rows) != booking.num_seats:
            return False
        try:
            await conn.query("UPDATE seat SET reserved = 1 WHERE id in ()", seat_ids)
        catch Exception as e:
            conn.rollback()













V1 First implementation, got lost in connecting the pieces and what is really
important
Actors
    - Admin(Front Desk Officer)
    - User/Guest

Functionality
 - Search Movies

class Person:
    - name
    - id
    def makeBooking():
        pass

class Customer(Person):
    pass

class FrontDeskAdmin(Person):
    pass
class Theater:

class Show
    time
    theater: Theater
    movie: Movie

class Movie:
    A movie can have many shows

    time
    language
    shows: List[Show]






User
    Manage all info and actions for the user
    - name, id
    actions
        - look_for_shows
        - book_show
        - cancel_show
Theater
    - list of shows
    - weekly schedule
    - daily schedule
    - get_all_shows_by_time
    - get_all_times_by_show
Movie
    A movie will
Show
    Everything related to a specific theater/room/movie room within a movie theater
    Attributes
        - start time
        - movie
        - movie
    Actions
        - play movie
        - stop movie
        - seats
        - number of seats
Seats

Ticket
MovieTicketSystem

A user should be able to book a seat in this movie
- look for shows
- book a seat

- search
- book
SearchType:
    - TIME
    - MOVIE
    - LOCATION

User:
    def search(search_type: SearchType) -> List[Theater]:
        switch search_type:
            case SearchType.MOVIE:
                search = SearchManager()
                await search.get_all_shows_by_movie(
                    location, range
                )

    book()

SearchManager
    def get_all_shows_by_movie(location: coord, movie_name: str):
        theaters = await get_all_theaters(location, distance)
        return [theater for theater in theaters if theater.is_playing_movie(movie_name)]

    async def get_all_theaters(location: zipCode, range):
        await query_theaters_near_location(location, range)

class Booking:
    book_seat


"""
