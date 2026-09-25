"""
# TODO  -----------------------جزء الحصري-------------------------------------
"""

from structures_and_algorithms import Stack, HashTable, binary_search, quick_sort

#-------------------------------------------------------------
# 1) CONSTS
#-------------------------------------------------------------

ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASS = "admin123"

CATEGORIES = [
    "Historical",
    "Beaches",
    "Adventure",
    "Religious",
    "Entertainment",
]

TRANSPORTATION_COST = {
    "Cairo": 50,
    "Giza": 60,
    "Alexandria": 80,
    "Luxor": 120,
    "Aswan": 130,
    "Red Sea": 150,
    "Sinai": 160,
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
all_users = []

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
    # Sort and compare case-insensitively so "pyramids" matches "Pyramids".
    sorted_list = quick_sort(category_list.copy(), key=lambda x: x.name.lower())

    index = binary_search(sorted_list, name.lower(), key=lambda x: x.name.lower())

    if index != -1:
        return sorted_list[index]

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

    transportation_cost = 0
    for governorate, cost in TRANSPORTATION_COST.items():
        if governorate.lower() == user_governorate.lower():
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
    """Validate a phone number globally (must include the country code, e.g. +201234567890)."""
    import phonenumbers
    try:
        parsed = phonenumbers.parse(str(phone), None)
        return phonenumbers.is_valid_number(parsed)
    except phonenumbers.NumberParseException:
        return False


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


def save_data_to_cloud():
    import json, os

    os.makedirs(os.path.dirname(USERS_FILE) or ".", exist_ok=True)

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

    for filepath, data in [(USERS_FILE, users_data),
                           (ATTRACTIONS_FILE, attractions_data),
                           (HOTELS_FILE, hotels_data)]:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)


def load_data_from_cloud():
    import json, os

    def load(filepath):
        if not os.path.exists(filepath):
            return []
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    for item in load(ATTRACTIONS_FILE):
        all_attractions.append(Attraction(
            item["name"], item["governorate"], item["ticket_price"],
            item["rating"], item["estimated_time"], item["category"],
            item.get("description", ""), item.get("best_time", "")
        ))

    for item in load(HOTELS_FILE):
        all_hotels.append(Hotel(
            item["name"], item["governorate"], item["price_per_night"],
            item["rating"], item.get("description", "")
        ))

    for item in load(USERS_FILE):
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

def suggest_related_attractions(selected_attraction, attractions_list):
    result = []
    for attraction in attractions_list:
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
            if attraction.governorate.lower() == current.governorate.lower():
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

# ============================================================
# TODO — Pending work (scaffolding only, nothing above is edited)
# ============================================================

# --- 2) National ID / Passport / Nationality ------------------------------
# TODO: User class above needs two new attributes: nationality, passport_id
#       (not adding them directly, keeping the class untouched for now)

def validate_national_id_strict(national_id):
    """
    TODO: stronger check than "14 digits":
          - century digit (2 or 3)
          - birth date part (YYMMDD) is a real date
          - governorate code part is valid
    """
    pass


def validate_passport_id(passport_id):
    """
    TODO: validate passport format for foreign users
          (alphanumeric, length depends on issuing country)
    """
    pass


def register_user_with_nationality(name, phone, email, gender, governorate,
                                    password, age, nationality,
                                    national_id=None, passport_id=None):
    """
    TODO: replacement/extension for register_user() once nationality is
          added to User:
          - nationality == "Egyptian" -> require + validate national_id
          - otherwise                 -> require + validate passport_id
    """
    pass


# --- 3) General validation + better error messages ------------------------

def validate_sort_key(sort_key):
    """
    TODO: check sort_key is one of the allowed Attraction fields
          (e.g. "ticket_price", "rating") before it's used with getattr(),
          so a bad value doesn't crash with AttributeError.
    """
    pass

# TODO: sort_attractions() above should call validate_sort_key(sort_key)
#       first and return a friendly error instead of crashing.
# TODO: every other input() value passed straight into a function that
#       assumes a specific value needs the same kind of guard + a clear
#       message instead of letting the raw exception surface.


# --- 4) places.json ---------------------------------------------------------

PLACES_FILE = "data/places.json"  # TODO: not used yet

def load_places_from_json():
    """
    TODO: load full attraction data (name, governorate, category, price,
          rating, description, best_time, coordinates, ...) from
          PLACES_FILE into all_attractions on startup.
    """
    pass


# --- 5) Time-based suggestions -----------------------------------------------

def suggest_places_by_current_time():
    """
    TODO: use datetime.now() and each attraction's best_time to suggest
          places that fit right now (morning / evening / etc.).
    """
    pass


# --- 6) Real worldwide data ---------------------------------------------------

def seed_sample_data():
    """Populate all_attractions and all_hotels with real sample data for testing/demos."""
    if all_attractions or all_hotels:
        return  # already seeded (or loaded from cloud) — don't duplicate

    # Egypt
    add_attraction("Pyramids of Giza", "Giza", 400, 4.8, "3 hours", "Historical",
                    "The last surviving wonder of the ancient world, next to the Great Sphinx.", "Morning")
    add_attraction("Egyptian Museum", "Cairo", 300, 4.6, "2 hours", "Historical",
                    "Home to the world's largest collection of Pharaonic antiquities.", "Morning")
    add_attraction("Karnak Temple", "Luxor", 350, 4.7, "2 hours", "Religious",
                    "A vast temple complex built over 2,000 years for the god Amun.", "Morning")
    add_attraction("Abu Simbel", "Aswan", 400, 4.9, "2 hours", "Religious",
                    "Two massive rock temples built by Ramesses II.", "Morning")
    add_attraction("Hurghada Red Sea Beach", "Red Sea", 0, 4.5, "Full day", "Beaches",
                    "Clear turquoise water and coral reefs on the Red Sea coast.", "Afternoon")
    add_attraction("Ras Mohammed National Park", "Sinai", 300, 4.6, "Full day", "Adventure",
                    "Snorkeling and diving at one of the world's top reef sites.", "Morning")
    add_attraction("Khan El Khalili", "Cairo", 0, 4.4, "2 hours", "Entertainment",
                    "A centuries-old bazaar packed with shops, cafes, and street food.", "Evening")

    # International
    add_attraction("Eiffel Tower", "Paris", 26, 4.7, "2 hours", "Entertainment",
                    "Paris' iconic iron tower with panoramic city views.", "Evening")
    add_attraction("Colosseum", "Rome", 18, 4.8, "2 hours", "Historical",
                    "The largest ancient amphitheatre ever built.", "Morning")
    add_attraction("Santorini Caldera", "Santorini", 0, 4.9, "Full day", "Beaches",
                    "Whitewashed villages perched above a volcanic caldera.", "Afternoon")
    add_attraction("Ubud Jungle Swing", "Bali", 25, 4.5, "2 hours", "Adventure",
                    "Giant rope swings over rice terraces and jungle canopy.", "Morning")
    add_attraction("Sagrada Familia", "Barcelona", 30, 4.8, "2 hours", "Religious",
                    "Gaudi's still-unfinished basilica, a masterpiece of design.", "Morning")
    add_attraction("Great Wall of China", "Beijing", 10, 4.9, "4 hours", "Historical",
                    "An ancient fortification stretching thousands of kilometers.", "Morning")

    # Hotels — Egypt
    add_hotel("Marriott Mena House", "Giza", 3500, 4.7,
              "Historic hotel with direct views of the Pyramids.")
    add_hotel("Steigenberger Nile Palace", "Luxor", 2200, 4.5,
              "Riverside hotel close to Luxor and Karnak temples.")
    add_hotel("Four Seasons Aswan", "Aswan", 4000, 4.8,
              "Nile-view resort near Elephantine Island.")
    add_hotel("Hilton Hurghada Plaza", "Red Sea", 1800, 4.4,
              "Beachfront resort with private lagoon access.")

    # Hotels — International
    add_hotel("Ritz Paris", "Paris", 12000, 4.9,
              "Legendary luxury hotel steps from Place Vendome.")
    add_hotel("The St. Regis Rome", "Rome", 9000, 4.8,
              "Classic 5-star hotel near the Spanish Steps.")
    add_hotel("Santorini Grace Hotel", "Santorini", 7000, 4.9,
              "Cliffside boutique hotel overlooking the caldera.")
    add_hotel("Mandarin Oriental Barcelona", "Barcelona", 6000, 4.7,
              "Modern luxury hotel on Passeig de Gracia.")