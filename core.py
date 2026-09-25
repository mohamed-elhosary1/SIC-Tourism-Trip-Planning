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

#-------------------------------------------------------------
# 2) Classes
#-------------------------------------------------------------

class Attraction:
    """
     name, governorate, ticket_price, rating,
    estimated_time, category, description, best_time
    TODO:
    """
    # description و best_time (بونص 5 و8) — بيانات إضافية بس

    def __init__(self, name, governorate, ticket_price, rating,
                 estimated_time, category, description="",
                 best_time=""):
        pass  # TODO


class Hotel:
    """
    بونص 7: كيان منفصل تمامًا عن Attraction (مش وراثة).

     name, governorate, price_per_night, rating, description
    TODO:
    """

    def __init__(self, name, governorate, price_per_night,
                 rating, description=""):
        pass  # TODO


class User:
    """
     name, phone, email, gender, governorate,
    password, age, national_id. , favourite_attractions
    TODO:
    """
    # favourite_attractions (بونص 9): TODO متنساش self.favourite_attractions = []

    def __init__(self, name, phone, email, gender, governorate,
                 password, age, national_id):
        pass  # TODO


#-------------------------------------------------------------
# 3) Auth
#-------------------------------------------------------------

users_table = HashTable()


def register_user(name, phone, email, gender, governorate,
                   password, age, national_id):
    """
    TODO:
        1) Make sure the email isnt used
        2) use the validations functions under
        3) reg a new user
    """
    pass


def login(email, password):
    """
    TODO:
        1) لو الإيميل/الباسورد بتوع الأدمن  هات "admin"
        2) لو مش كده شوف في users_table وشوف من الباسورد
        3) رجع None لو غلط
    """
    pass


#-------------------------------------------------------------
# 4) Attractions
#-------------------------------------------------------------

all_attractions = []  # TODO:  ؟  HashTable هنا كمان


def add_attraction(name, governorate, ticket_price, rating,
                    estimated_time, category, description="",
                    best_time=""):
    """[Admin] TODO: اعمل Attraction وضيفه  all_attractions"""
    pass


def update_attraction(name, **fields):
    """[Admin] TODO: سيرش بالاسم وغير الفيلدز """
    pass


def remove_attraction(name):
    """[Admin] TODO: دور  واحذفه من all_attractions"""
    pass


def get_by_category(category):
    """TODO: فلترة all_attractions حسب category"""
    pass


def get_attraction_by_name(name):
    """TODO: رجع الـ Attraction بالاسم (هتحتاجها في Compare/Favourites)"""
    pass


def search_attraction_by_name(category_list, name):
    """
    TODO: رتب القائمة بالاسم (لو مش متسورتة) واستخدم
          binary_search من structures_and_algorithms.py
    """
    pass


def sort_attractions(category_list, sort_key="ticket_price", ascending=True):
    """
    TODO: استخدم quick_sort
    # TODO : ممكن تتعمل باكتر من شكل عشان البونص
    """
    pass

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