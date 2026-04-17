#rating

def get_rating():
        min_rating = 0
        max_rating = 10
        while True:
            try:
                rating = input("Enter your score: ")
                rating = int(rating)
            except ValueError:
                 print("This isn't a number between 0 and 10")
                 continue
            if validate_rating(rating, min_rating, max_rating):
                return rating
            else:
                 print("Please, put a number between 0 and 10")
                 continue


def validate_rating(rating, min_rating, max_rating):
     return min_rating <= rating <= max_rating



