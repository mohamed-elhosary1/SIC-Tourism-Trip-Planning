"""
# TODO  -----------------------جزء الحصري-------------------------------------
"""

from structures_and_algorithms import Stack, HashTable, binary_search, quick_sort

#-------------------------------------------------------------
# 1) CONSTS
#-------------------------------------------------------------

ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASS = "admin123"

# TODO:
CATEGORIES = [
]
#todo
places = []

# TODO:  تكلفة
TRANSPORTATION_COST = {
    # "Cairo": 50,
}

#  Cloud Saving
USERS_FILE = "data/users.json"
ATTRACTIONS_FILE = "data/attractions.json"
HOTELS_FILE = "data/hotels.json"
# TODO  -----------------------جزء نورا -------------------------------------


# 2) Classes
class Attraction:
    def __init__(self, name, governorate, ticket_price, rating,
                 estimated_time, category, description="",
                 best_time=""):

        self.name = name
        self.governorate = governorate
        self.ticket_price = ticket_price
        self.rating = rating
        self.estimated_time = estimated_time
        self.category = category
        self.description = description
        self.best_time = best_time


class Hotel:
    def __init__(self, name, governorate, price_per_night,
                 rating, description=""):
        self.name = name
        self.governorate = governorate
        self.price_per_night = price_per_night
        self.rating = rating
        self.description = description


class User:
    def __init__(self, name, phone, email, gender, governorate,
                 password, age, national_id):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.governorate = governorate
        self.password = password
        self.age = age
        self.national_id = national_id
        self.favourite_attractions = []

# 3) Auth

users_table = HashTable()
all_users = []  # parallel list used by save_data_to_cloud

def register_user(name, phone, email, gender, governorate,
                  password, age, national_id):
    if users_table.get(email) is not None:
        return False
    if not validate_email(email):
        return False
    if not validate_phone(phone):
        return False
    user = User(name, phone, email, gender, governorate,
                password, age, national_id)
    users_table.insert(email, user)
    all_users.append(user)
    return True

def login(email, password):

    if email == "admin@gmail.com" and password == "admin123":
        return "admin"

    user = users_table.get(email)

    if user is not None and user.password == password:
        return user

    return None

# 4) Attractions

all_attractions = []  # TODO:  ؟  HashTable هنا كمان
def add_attraction(name, governorate, ticket_price, rating,
                    estimated_time, category, description="",
                    best_time=""):
    attraction = Attraction(name, governorate, ticket_price, rating,
                            estimated_time, category, description,
                            best_time)
    all_attractions.append(attraction)
    return attraction


def update_attraction(name, **fields):
    attraction = get_attraction_by_name(name)

    if attraction is None:
        return False

    for field in fields:
        if hasattr(attraction, field):
            setattr(attraction, field, fields[field])

    return True


def remove_attraction(name):
    attraction = get_attraction_by_name(name)

    if attraction is None:
        return False

    all_attractions.remove(attraction)

    return True


def get_by_category(category):
    result = []
    for attraction in all_attractions:
        if attraction.category.lower() == category.lower():
            result.append(attraction)

    return result


def get_attraction_by_name(name):
    for attraction in all_attractions:
        if attraction.name.lower() == name.lower():
            return attraction

    return None


def search_attraction_by_name(category_list, name):
    category_list = sort_attractions(category_list, "name")

    index = binary_search(category_list, name, key=lambda x: x.name)

    if index != -1:
        return category_list[index]

    return None


def sort_attractions(category_list, sort_key="ticket_price", ascending=True):
    new_list = category_list.copy()

    return quick_sort(new_list,
                      key=lambda x: getattr(x, sort_key),
                      ascending=ascending)

# TODO  -----------------------جزء اروى-------------------------------------
#-------------------------------------------------------------
# 5) Hotels  (بونص 7)
#-------------------------------------------------------------

all_hotels = []  # TODO


def add_hotel(name, governorate, price_per_night, rating, description=""):
    """[Admin] Add a Hotel and store it in all_hotels."""
    hotel = Hotel(name, governorate, price_per_night, rating, description)
    all_hotels.append(hotel)
    return hotel


def update_hotel(name, **fields):
    """[Admin] Find a hotel by name and update its existing fields."""
    hotel = next((h for h in all_hotels if h.name.lower() == name.lower()), None)

    if hotel is None:
        return False

    for field, value in fields.items():
        if hasattr(hotel, field):
            setattr(hotel, field, value)

    return True


def remove_hotel(name):
    """[Admin] Find a hotel by name and remove it from all_hotels."""
    hotel = next((h for h in all_hotels if h.name.lower() == name.lower()), None)

    if hotel is None:
        return False

    all_hotels.remove(hotel)
    return True


def get_hotels_by_governorate(governorate):
    """Return all hotels located in the requested governorate."""
    return [
        hotel for hotel in all_hotels
        if hotel.governorate.lower() == governorate.lower()
    ]

# TODO  -----------------------جزء اروى-------------------------------------
#-------------------------------------------------------------
# 6) Trip
#-------------------------------------------------------------

def create_empty_trip():
    """Create and return an empty My Trip plan."""
    return []


def add_to_trip(trip, attraction):
    """Add an attraction to the trip if it is not already selected."""
    if attraction not in trip:
        trip.append(attraction)
        return True
    return False


def remove_from_trip(trip, attraction_name):
    """Remove an attraction from the trip by name."""
    for attraction in trip:
        if attraction.name.lower() == attraction_name.lower():
            trip.remove(attraction)
            return True

    return False


def calculate_final_summary(trip, user_governorate):
    """
    Calculate the final trip summary.

    Returns a dictionary containing:
        attractions_cost
        transportation_cost
        total
    """
    attractions_cost = sum(attraction.ticket_price for attraction in trip)

    transportation_cost = TRANSPORTATION_COST.get(user_governorate, 0)

    if transportation_cost == 0:
        governorate_key = user_governorate.lower()
        for governorate, cost in TRANSPORTATION_COST.items():
            if governorate.lower() == governorate_key:
                transportation_cost = cost
                break

    return {
        "attractions_cost": attractions_cost,
        "transportation_cost": transportation_cost,
        "total": attractions_cost + transportation_cost
    }


#-------------------------------------------------------------
# 7) Navigation
#-------------------------------------------------------------

class PageNavigator:
    """Manage page navigation using the required Stack data structure."""

    def __init__(self):
        self.history = Stack()

    def go_to(self, page_name):
        self.history.push(page_name)
        return page_name

    def go_back(self):
        if self.history.is_empty():
            return None
        self.history.pop()
        return self.current_page()

    def current_page(self):
        if self.history.is_empty():
            return None
        return self.history.peek()


#-------------------------------------------------------------
# 8) Validation
#-------------------------------------------------------------

def validate_email(email):
    """Validate a basic email address format."""
    import re
    return bool(re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", str(email)))


def validate_phone(phone):
    """Validate an Egyptian mobile number: 11 digits starting with 010/011/012/015."""
    import re
    phone = str(phone)
    return bool(re.fullmatch(r"01[0125]\d{8}", phone))


def validate_national_id(national_id):
    """Validate that the Egyptian national ID contains exactly 14 digits."""
    return str(national_id).isdigit() and len(str(national_id)) == 14


def validate_age(age):
    """Validate that age is a reasonable positive integer."""
    try:
        age = int(age)
    except (TypeError, ValueError):
        return False

    return 1 <= age <= 120

#TODO ##################################################
# TODO جزء الحصري
#-------------------------------------------------------------
# 9) Bonus Features
#-------------------------------------------------------------


DRIVE_FOLDER = r"G:\My Drive\SIC_Tourism_Data"


def save_data_to_cloud():
    import json, os
    os.makedirs(DRIVE_FOLDER, exist_ok=True)

    users_data = [
        {"name": u.name, "phone": u.phone, "email": u.email, "gender": u.gender,
         "governorate": u.governorate, "password": u.password, "age": u.age,
         "national_id": u.national_id,
         "favourite_attractions": [a.name for a in u.favourite_attractions]}
        for u in all_users
    ]
    attractions_data = [
        {"name": a.name, "governorate": a.governorate, "ticket_price": a.ticket_price,
         "rating": a.rating, "estimated_time": a.estimated_time, "category": a.category,
         "description": a.description, "best_time": a.best_time}
        for a in all_attractions
    ]
    hotels_data = [
        {"name": h.name, "governorate": h.governorate, "price_per_night": h.price_per_night,
         "rating": h.rating, "description": h.description}
        for h in all_hotels
    ]

    for filename, data in [("users.json", users_data),
                           ("attractions.json", attractions_data),
                           ("hotels.json", hotels_data)]:
        with open(os.path.join(DRIVE_FOLDER, filename), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)


def load_data_from_cloud():
    import json, os

    def load(filename):
        path = os.path.join(DRIVE_FOLDER, filename)
        if not os.path.exists(path):
            return []
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    for item in load("attractions.json"):
        all_attractions.append(Attraction(
            item["name"], item["governorate"], item["ticket_price"],
            item["rating"], item["estimated_time"], item["category"],
            item.get("description", ""), item.get("best_time", "")
        ))

    for item in load("hotels.json"):
        all_hotels.append(Hotel(
            item["name"], item["governorate"], item["price_per_night"],
            item["rating"], item.get("description", "")
        ))

    for item in load("users.json"):
        user = User(item["name"], item["phone"], item["email"], item["gender"],
                    item["governorate"], item["password"], item["age"], item["national_id"])
        for name in item.get("favourite_attractions", []):
            attraction = get_attraction_by_name(name)
            if attraction:
                user.favourite_attractions.append(attraction)
        users_table.insert(user.email, user)
        all_users.append(user)


# ---- Bonus 2: Budget Filter ----

def filter_by_budget(attractions_list, max_budget):
    attractions_list = sort_attractions(attractions_list, "ticket_price")
    result = []
    total = 0
    for attraction in attractions_list:
        if total + attraction.ticket_price <= max_budget:
            result.append(attraction)
            total += attraction.ticket_price

    return result


# ---- Bonus 3: Related Attractions ----

def suggest_related_attractions(selected_attraction, all_attractions):
    result = []
    for attraction in all_attractions:
        if attraction.name.lower() == selected_attraction.name.lower():
            continue
        if (attraction.governorate.lower() == selected_attraction.governorate.lower()
                or attraction.category.lower() == selected_attraction.category.lower()):
            result.append(attraction)
    return result

# ---- Bonus 4 Route Optimization  ----

def optimize_trip_route(trip):
    if len(trip) <= 1:
        return trip
    result = [trip[0]]
    remaining = trip[1:]
    while remaining:
        current = result[-1]
        same_governorate = []
        for attraction in remaining:
            if attraction.governorate == current.governorate:
                same_governorate.append(attraction)
        if same_governorate:
            next_attraction = same_governorate[0]
        else:
            next_attraction = remaining[0]
        result.append(next_attraction)
        remaining.remove(next_attraction)
    return result


# ---- Bonus 6 Compare Mode ----

def compare_attractions(name1, name2):
    attraction1 = get_attraction_by_name(name1)
    attraction2 = get_attraction_by_name(name2)
    if attraction1 is None or attraction2 is None:
        return None
    print("Name:", attraction1.name, "-", attraction2.name)
    print("Governorate:", attraction1.governorate, "-", attraction2.governorate)
    print("Ticket Price:", attraction1.ticket_price, "-", attraction2.ticket_price)
    print("Rating:", attraction1.rating, "-", attraction2.rating)
    print("Estimated Time:", attraction1.estimated_time, "-", attraction2.estimated_time)
    print("Category:", attraction1.category, "-", attraction2.category)


 

# ---- Bonus 9 Favourites ----

def add_to_favourites(user, attraction_name):

    attraction = get_attraction_by_name(attraction_name)

    if attraction is None:
        return False

    if attraction not in user.favourite_attractions:
        user.favourite_attractions.append(attraction)

    return True


def remove_from_favourites(user, attraction_name):
    attraction = get_attraction_by_name(attraction_name)
    if attraction is None:
        return False

    if attraction in user.favourite_attractions:
        user.favourite_attractions.remove(attraction)
        return True
    return False


def view_favourites(user):
    return user.favourite_attractions