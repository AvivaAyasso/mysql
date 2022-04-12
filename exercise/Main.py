from exercise.Exercise import Data

class Main:
    co = Data().connect("SELECT COUNT(first_name) FROM actor")
    print(co)

    co1 = co = Data().connect("SELECT COUNT(title) FROM film")
    print(co1)
