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

FEES = 30  # flat booking and service fee per trip (EGP)

ATTRACTION_FIELDS = [
    "name", "city", "ticket_price", "rating",
    "estimated_time", "category", "description",
]

ALLOWED_SORT_KEYS = ("ticket_price", "rating", "name")

MONTH_NAMES = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]

#  Cloud Saving
USERS_FILE = "data/users.json"
ATTRACTIONS_FILE = "data/attractions.json"
HOTELS_FILE = "data/hotels.json"
PLACES_FILE    = "data/places.json"
CONFIG_FILE    = "data/config.json"
DRIVE_FOLDER   = ""  # local Drive folder path; set from admin menu, persisted in config.json


# 2) Classes
class Attraction:
    def __init__(self, name, city, ticket_price, rating,
                 estimated_time, category, description="",
                 best_season_months=None):

        self.name = name
        self.city = city
        self.ticket_price = ticket_price
        self.rating = rating
        self.estimated_time = estimated_time
        self.category = category
        self.description = description
        self.best_season_months = best_season_months or []  # best months of the YEAR, e.g. [10, 11, 12, 1]


class Hotel:
    def __init__(self, name, city, price_per_night,
                 rating, description=""):
        self.name = name
        self.city = city
        self.price_per_night = price_per_night
        self.rating = rating
        self.description = description


class User:
    def __init__(self, name, phone, email, gender, city,
                 password, age, nationality, national_id=None, passport_id=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.city = city
        self.password = password
        self.age = age
        self.nationality = nationality
        self.national_id = national_id
        self.passport_id = passport_id
        self.favourite_attractions = []

# 3) Auth

users_table = HashTable()
all_users = []

def register_user(name, phone, email, gender, city,
                  password, age, nationality, national_id=None, passport_id=None):
    if users_table.get(email) is not None:
        return False
    if not validate_email(email):
        return False
    if not validate_phone(phone):
        return False

    if str(nationality).strip().lower() == "egyptian":
        if not validate_national_id(national_id):
            return False
    else:
        if not validate_passport_id(passport_id):
            return False

    user = User(name, phone, email, gender, city,
                password, age, nationality, national_id, passport_id)
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
def add_attraction(name, city, ticket_price, rating,
                    estimated_time, category, description="",
                    best_season_months=None):
    attraction = Attraction(name, city, ticket_price, rating,
                            estimated_time, category, description,
                            best_season_months)
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


def validate_sort_key(sort_key):
    """Check sort_key is one of the allowed Attraction fields before it's used with getattr()."""
    return sort_key in ALLOWED_SORT_KEYS


def sort_attractions(category_list, sort_key="ticket_price", ascending=True):
    new_list = category_list.copy()

    return quick_sort(new_list,
                      key=lambda x: getattr(x, sort_key),
                      ascending=ascending)

#-------------------------------------------------------------
# 5) Hotels  (بونص 7)
#-------------------------------------------------------------

all_hotels = []


def add_hotel(name, city, price_per_night, rating, description=""):
    """[Admin] Add a Hotel and store it in all_hotels."""
    hotel = Hotel(name, city, price_per_night, rating, description)
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


def get_hotels_by_city(city):
    """Return all hotels located in the requested city."""
    return [
        hotel for hotel in all_hotels
        if hotel.city.lower() == city.lower()
    ]

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


def calculate_final_summary(trip):
    """
    Calculate the final trip summary.

    Returns a dictionary containing:
        attractions_cost
        fees
        total
    """
    attractions_cost = sum(attraction.ticket_price for attraction in trip)

    return {
        "attractions_cost": attractions_cost,
        "fees":             FEES,
        "total":            attractions_cost + FEES,
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
    try:
        import phonenumbers
        parsed = phonenumbers.parse(str(phone), None)
        return phonenumbers.is_valid_number(parsed)
    except ImportError:
        import re
        # Fallback E.164 international format check: '+' followed by 7 to 15 digits
        return bool(re.fullmatch(r"^\+[1-9]\d{6,14}$", str(phone).strip()))
    except Exception:
        return False


def validate_national_id(national_id):
    """
    Validate an Egyptian national ID (14 digits) beyond just the length:
      - century digit is 2 (1900s) or 3 (2000s)
      - the birth date encoded in it (YYMMDD) is a real calendar date
      - the governorate code is a known one (01-35, or 88 for born abroad)
    """
    import datetime

    national_id = str(national_id)
    if not national_id.isdigit() or len(national_id) != 14:
        return False

    century_digit = national_id[0]
    if century_digit not in ("2", "3"):
        return False

    century = 1900 if century_digit == "2" else 2000
    year = century + int(national_id[1:3])
    month = int(national_id[3:5])
    day = int(national_id[5:7])

    try:
        datetime.date(year, month, day)
    except ValueError:
        return False

    governorate_code = national_id[7:9]
    valid_governorate_codes = {f"{i:02d}" for i in range(1, 36)} | {"88"}
    if governorate_code not in valid_governorate_codes:
        return False

    return True


def validate_passport_id(passport_id):
    """Validate a passport number for foreign users: 6-9 letters/digits."""
    import re
    return bool(re.fullmatch(r"[A-Za-z0-9]{6,9}", str(passport_id)))


def validate_age(age):
    """Validate that age is a reasonable positive integer."""
    try:
        age = int(age)
    except (TypeError, ValueError):
        return False

    return 1 <= age <= 120

#-------------------------------------------------------------
# 9) Bonus Features
#-------------------------------------------------------------


def load_config():
    """Load saved settings (DRIVE_FOLDER) from config.json at startup."""
    import json, os
    global DRIVE_FOLDER
    if not os.path.exists(CONFIG_FILE):
        return
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            config = json.load(f)
        DRIVE_FOLDER = config.get("drive_folder", "")
    except Exception as e:
        print(f"[Warning] Config load failed: {e}")


def set_drive_folder(path):
    """Set and persist the Drive backup folder path. Returns False if path doesn't exist."""
    import json, os
    global DRIVE_FOLDER
    if path and not os.path.isdir(path):
        return False
    DRIVE_FOLDER = path
    try:
        os.makedirs(os.path.dirname(CONFIG_FILE) or ".", exist_ok=True)
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump({"drive_folder": DRIVE_FOLDER}, f, ensure_ascii=False)
    except Exception as e:
        print(f"[Warning] Config save failed: {e}")
    return True


def save_data_to_cloud():
    import json, os, shutil

    users_data = [
        {"name": u.name, "phone": u.phone, "email": u.email, "gender": u.gender,
         "city": u.city, "password": u.password, "age": u.age,
         "nationality": u.nationality, "national_id": u.national_id,
         "passport_id": u.passport_id,
         "favourite_attractions": [a.name for a in u.favourite_attractions]}
        for u in all_users
    ]
    attractions_data = [
        {"name": a.name, "city": a.city, "ticket_price": a.ticket_price,
         "rating": a.rating, "estimated_time": a.estimated_time, "category": a.category,
         "description": a.description,
         "best_season_months": a.best_season_months}
        for a in all_attractions
    ]
    hotels_data = [
        {"name": h.name, "city": h.city, "price_per_night": h.price_per_night,
         "rating": h.rating, "description": h.description}
        for h in all_hotels
    ]

    datasets = [
        (USERS_FILE,       users_data),
        (ATTRACTIONS_FILE, attractions_data),
        (HOTELS_FILE,      hotels_data),
    ]

    # local save
    local_ok = False
    try:
        os.makedirs(os.path.dirname(USERS_FILE) or ".", exist_ok=True)
        for filepath, data in datasets:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False)
        local_ok = True
    except Exception as e:
        print(f"[Warning] Local save failed: {e}")

    # Drive folder backup (only runs if local save succeeded)
    if local_ok and DRIVE_FOLDER and os.path.isdir(DRIVE_FOLDER):
        for filepath, _ in datasets:
            filename = os.path.basename(filepath)
            try:
                shutil.copy2(filepath, os.path.join(DRIVE_FOLDER, filename))
            except Exception as e:
                print(f"[Warning] Drive backup failed ({filename}): {e}")


def load_data_from_cloud():
    import json, os

    def load(filepath):
        """Try Drive folder first, then local. Returns a list (empty on total failure)."""
        filename = os.path.basename(filepath)

        if DRIVE_FOLDER:
            drive_path = os.path.join(DRIVE_FOLDER, filename)
            try:
                if os.path.exists(drive_path):
                    with open(drive_path, "r", encoding="utf-8") as f:
                        return json.load(f)
            except Exception as e:
                print(f"[Warning] Drive load failed ({filename}): {e}")

        try:
            if not os.path.exists(filepath):
                return []
            with open(filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[Warning] Local load failed ({filepath}): {e}")
            return []

    for item in load(ATTRACTIONS_FILE):
        all_attractions.append(Attraction(
            item["name"], item.get("city") or item.get("governorate", ""), item["ticket_price"],
            item["rating"], item["estimated_time"], item["category"],
            item.get("description", ""),
            item.get("best_season_months", [])
        ))

    for item in load(HOTELS_FILE):
        all_hotels.append(Hotel(
            item["name"], item.get("city") or item.get("governorate", ""), item["price_per_night"],
            item["rating"], item.get("description", "")
        ))

    for item in load(USERS_FILE):
        user = User(item["name"], item["phone"], item["email"], item["gender"],
                    item.get("city") or item.get("governorate", ""), item["password"], item["age"],
                    item.get("nationality", "Egyptian"), item.get("national_id"),
                    item.get("passport_id"))
        for name in item.get("favourite_attractions", []):
            attraction = get_attraction_by_name(name)
            if attraction:
                user.favourite_attractions.append(attraction)
        users_table.insert(user.email, user)
        all_users.append(user)


def load_places_from_json():
    """Load full attraction data from PLACES_FILE into all_attractions. Returns True if it loaded anything."""
    import json, os

    target_file = PLACES_FILE
    if not os.path.exists(target_file):
        if os.path.exists("Places.json"):
            target_file = "Places.json"
        elif os.path.exists("places.json"):
            target_file = "places.json"
        else:
            return False

    with open(target_file, "r", encoding="utf-8") as f:
        places = json.load(f)

    for item in places:
        add_attraction(
            item["name"], item.get("city") or item.get("governorate", ""), item["ticket_price"],
            item["rating"], item["estimated_time"], item["category"],
            item.get("description", ""),
            item.get("best_season_months", [])
        )

    return len(places) > 0


def validate_month(month_input):
    """Parse a month name (e.g. 'October') or number (1-12) into an int. Returns None if invalid."""
    month_input = str(month_input).strip()

    if month_input.isdigit():
        month = int(month_input)
        return month if 1 <= month <= 12 else None

    for i, name in enumerate(MONTH_NAMES, start=1):
        if name.lower() == month_input.lower():
            return i

    return None


def suggest_places_by_month(month):
    """Return attractions whose best_season_months includes the given month (1-12)."""
    return [
        attraction for attraction in all_attractions
        if month in attraction.best_season_months
    ]


def suggest_places_for_current_month():
    """Return (matches, month_name) for the current calendar month."""
    import datetime
    month = datetime.datetime.now().month
    return suggest_places_by_month(month), MONTH_NAMES[month - 1]


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
        if (attraction.city.lower() == selected_attraction.city.lower()
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
        same_city = []
        for attraction in remaining:
            if attraction.city.lower() == current.city.lower():
                same_city.append(attraction)
        if same_city:
            next_attraction = same_city[0]
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
    print("City:", attraction1.city, "-", attraction2.city)
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


# ---- Sample / seed data for testing and demos ----

def seed_sample_data():
    """
    Populate all_attractions and all_hotels with real data for testing/demos.
    Attractions are loaded from PLACES_FILE first; if that file isn't found,
    a hardcoded fallback list is used instead. Hotels are always hardcoded.
    """
    if not all_attractions:
        if not load_places_from_json():
            # Fallback attractions (used only if data/places.json is missing)
            add_attraction("Pyramids of Giza", "Giza", 400, 4.8, "3 hours", "Historical",
                            "The last surviving wonder of the ancient world, next to the Great Sphinx.",
                            [10, 11, 12, 1, 2, 3, 4])
            add_attraction("Egyptian Museum", "Cairo", 300, 4.6, "2 hours", "Historical",
                            "Home to the world's largest collection of Pharaonic antiquities.",
                            [10, 11, 12, 1, 2, 3, 4])
            add_attraction("Karnak Temple", "Luxor", 350, 4.7, "2 hours", "Religious",
                            "A vast temple complex built over 2,000 years for the god Amun.",
                            [10, 11, 12, 1, 2, 3, 4])
            add_attraction("Abu Simbel", "Aswan", 400, 4.9, "2 hours", "Religious",
                            "Two massive rock temples built by Ramesses II.",
                            [10, 11, 12, 1, 2, 3, 4])
            add_attraction("Hurghada Red Sea Beach", "Red Sea", 0, 4.5, "Full day", "Beaches",
                            "Clear turquoise water and coral reefs on the Red Sea coast.",
                            [3, 4, 5, 6, 7, 8, 9, 10, 11])
            add_attraction("Ras Mohammed National Park", "Sinai", 300, 4.6, "Full day", "Adventure",
                            "Snorkeling and diving at one of the world's top reef sites.",
                            [3, 4, 5, 6, 7, 8, 9, 10, 11])
            add_attraction("Khan El Khalili", "Cairo", 0, 4.4, "2 hours", "Entertainment",
                            "A centuries-old bazaar packed with shops, cafes, and street food.",
                            [10, 11, 12, 1, 2, 3, 4])
            add_attraction("Eiffel Tower", "Paris", 26, 4.7, "2 hours", "Entertainment",
                            "Paris' iconic iron tower with panoramic city views.",
                            [4, 5, 6, 9, 10])
            add_attraction("Colosseum", "Rome", 18, 4.8, "2 hours", "Historical",
                            "The largest ancient amphitheatre ever built.",
                            [4, 5, 6, 9, 10])
            add_attraction("Santorini Caldera", "Santorini", 0, 4.9, "Full day", "Beaches",
                            "Whitewashed villages perched above a volcanic caldera.",
                            [5, 6, 7, 8, 9])
            add_attraction("Ubud Jungle Swing", "Bali", 25, 4.5, "2 hours", "Adventure",
                            "Giant rope swings over rice terraces and jungle canopy.",
                            [4, 5, 6, 7, 8, 9, 10])
            add_attraction("Sagrada Familia", "Barcelona", 30, 4.8, "2 hours", "Religious",
                            "Gaudi's still-unfinished basilica, a masterpiece of design.",
                            [5, 6, 9])
            add_attraction("Great Wall of China", "Beijing", 10, 4.9, "4 hours", "Historical",
                            "An ancient fortification stretching thousands of kilometers.",
                            [4, 5, 6, 9, 10])

    if not all_hotels:
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