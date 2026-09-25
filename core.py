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
    """[Admin] TODO: اعمل Hotel وضيفه all_hotels"""
    pass


def update_hotel(name, **fields):
    """[Admin] TODO: سيرش بالاسم وغير الفيلدز"""
    pass


def remove_hotel(name):
    """[Admin] TODO: دور واحذفه من all_hotels"""
    pass


def get_hotels_by_governorate(governorate):
    """TODO: فلترة all_hotels حسب المحافظة (يقترح فنادق قريبة من رحلة المستخدم)"""
    pass

# TODO  -----------------------جزء اروى-------------------------------------
#-------------------------------------------------------------
# 6) Trip
#-------------------------------------------------------------

def create_empty_trip():
    """TODO: هات ستراكشر فاضي  الأماكن """
    pass


def add_to_trip(trip, attraction):
    """TODO: ضيف المكان لو مش موجود """
    pass


def remove_from_trip(trip, attraction_name):
    """TODO: شيل المكان """
    pass


def calculate_final_summary(trip, user_governorate):
    """

    TODO:
         تكلفة الأماكن: sum()
         تكلفة المواصلات من TRANSPORTATION_COST حسب المحافظة
         dict فيه: attractions_cost, transportation_cost, total
    """
    pass


#-------------------------------------------------------------
# 7) Navigation
#-------------------------------------------------------------

class PageNavigator:
# TODO : التنقل بين الصفحات
    def __init__(self):
        pass  # TODO: self.history = Stack()

    def go_to(self, page_name):
        pass  # TODO: push

    def go_back(self):
        pass  # TODO: pop

    def current_page(self):
        pass  # TODO: peek


#-------------------------------------------------------------
# 8) Validation
#-------------------------------------------------------------

def validate_email(email):
    """TODO:   شكل الإيميل"""
    pass


def validate_phone(phone):
    """TODO:   شكل رقم الموبايل"""
    pass


def validate_national_id(national_id):
    """TODO:   الرقم القومي 14 رقم"""
    pass


def validate_age(age):
    """TODO:   السن رقم منطقي"""
    pass
#TODO ##################################################
# TODO جزء الحصري
#-------------------------------------------------------------
# 9) Bonus Features
#-------------------------------------------------------------


def save_data_to_cloud():
    """
    Saves users, attractions, and hotels to local JSON files (cloud simulation).
    Files: data/users.json, data/attractions.json, data/hotels.json
    """
    import json
    import os

    os.makedirs("data", exist_ok=True)

    # Save users
    users_data = []
    for user in all_users:
        users_data.append({
            "name": user.name,
            "phone": user.phone,
            "email": user.email,
            "gender": user.gender,
            "governorate": user.governorate,
            "password": user.password,
            "age": user.age,
            "national_id": user.national_id,
            "favourite_attractions": [a.name for a in user.favourite_attractions]
        })
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users_data, f, ensure_ascii=False, indent=2)

    # Save attractions
    attractions_data = []
    for attraction in all_attractions:
        attractions_data.append({
            "name": attraction.name,
            "governorate": attraction.governorate,
            "ticket_price": attraction.ticket_price,
            "rating": attraction.rating,
            "estimated_time": attraction.estimated_time,
            "category": attraction.category,
            "description": attraction.description,
            "best_time": attraction.best_time
        })
    with open(ATTRACTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(attractions_data, f, ensure_ascii=False, indent=2)

    # Save hotels
    hotels_data = []
    for hotel in all_hotels:
        hotels_data.append({
            "name": hotel.name,
            "governorate": hotel.governorate,
            "price_per_night": hotel.price_per_night,
            "rating": hotel.rating,
            "description": hotel.description
        })
    with open(HOTELS_FILE, "w", encoding="utf-8") as f:
        json.dump(hotels_data, f, ensure_ascii=False, indent=2)


def load_data_from_cloud():
    """
    Loads users, attractions, and hotels from local JSON files (cloud simulation).
    Files: data/users.json, data/attractions.json, data/hotels.json
    """
    import json
    import os

    # Load attractions first (needed to restore user favourites)
    if os.path.exists(ATTRACTIONS_FILE):
        with open(ATTRACTIONS_FILE, "r", encoding="utf-8") as f:
            for item in json.load(f):
                attraction = Attraction(
                    item["name"], item["governorate"], item["ticket_price"],
                    item["rating"], item["estimated_time"], item["category"],
                    item.get("description", ""), item.get("best_time", "")
                )
                all_attractions.append(attraction)

    # Load hotels
    if os.path.exists(HOTELS_FILE):
        with open(HOTELS_FILE, "r", encoding="utf-8") as f:
            for item in json.load(f):
                hotel = Hotel(
                    item["name"], item["governorate"], item["price_per_night"],
                    item["rating"], item.get("description", "")
                )
                all_hotels.append(hotel)

    # Load users
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            for item in json.load(f):
                user = User(
                    item["name"], item["phone"], item["email"], item["gender"],
                    item["governorate"], item["password"], item["age"],
                    item["national_id"]
                )
                # Restore favourite attractions by name
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