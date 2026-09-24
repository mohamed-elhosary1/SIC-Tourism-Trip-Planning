from structures_and_algorithms import Stack, HashTable, binary_search, quick_sort

#-------------------------------------------------------------
# 1) CONSTS
#-------------------------------------------------------------

ADMIN_EMAIL = "admin@gmail.com"
ADMIN_PASS = "admin123"

# TODO:
CATEGORIES = [
    "Museums",
    "Historical Sites",
    "Nature",
    "Adventure",
    "Cultural Attractions",
]
#todo
GOVERNORATES = []

# TODO:  تكلفة
TRANSPORTATION_COST = {
    # "Cairo": 50,
}


#-------------------------------------------------------------
# 2) Classes
#-------------------------------------------------------------

class Attraction:
    """
     name, governorate, ticket_price, rating,
    estimated_time, category.
    TODO:
    """

    def __init__(self, name, governorate, ticket_price, rating,
                 estimated_time, category):
        pass  # TODO


class User:
    """
     name, phone, email, gender, governorate,
    password, age, national_id.
    TODO:
    """

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

all_attractions = []  # TODO:   HashTable هنا كمان


def add_attraction(name, governorate, ticket_price, rating,
                    estimated_time, category):
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


def search_attraction_by_name(category_list, name):
    """
    TODO: رتب القائمة بالاسم (لو مش متسورتة) واستخدم
          binary_search من structures_and_algorithms.py
    """
    pass


def sort_attractions(category_list, sort_key="ticket_price", ascending=True):
    """
    TODO: استخدم quick_sort
    """
    pass


#-------------------------------------------------------------
# 5) Trip
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
# 6) Navigation
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
# 7) Validation
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


#-------------------------------------------------------------
# 8) Bonus Feature
#-------------------------------------------------------------

def suggest_related_attractions(selected_attraction, all_attractions):
    pass
    #TODO : محتاجين نفكر فيها
