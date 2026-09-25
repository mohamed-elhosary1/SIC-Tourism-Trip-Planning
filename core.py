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
    return quick_sort(category_list,
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

    """
    pass


def load_data_from_cloud():
    """

    """
    pass


# ---- Bonus 2: Budget Filter ----

def filter_by_budget(attractions_list, max_budget):
    """
    TODO: من قائمة مرتبة بالسعر (استخدم sort_attractions)، جمّع
          أماكن مجموع أسعارها ماينفعش يتعدى max_budget
    """
    pass


# ---- Bonus 3: Related Attractions ----

def suggest_related_attractions(selected_attraction, all_attractions):
    """
    TODO: رجع أماكن تانية في نفس governorate أو نفس category
          بتاعة selected_attraction (وماتكررش نفس المكان)
    """
    pass


# ---- Bonus 4 Route Optimization  ----

def optimize_trip_route(trip):

    pass


# ---- Bonus 6 Compare Mode ----

def compare_attractions(name1, name2):
    """
    """
    pass


# ---- Bonus 9 Favourites ----

def add_to_favourites(user, attraction_name):
    pass


def remove_from_favourites(user, attraction_name):
    pass


def view_favourites(user):
    pass