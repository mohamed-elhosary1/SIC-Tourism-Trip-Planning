import core


def login_page(navigator):
    print("---- Login ----")
    email = input("Email: ")
    password = input("Password: ")

    result = core.login(email, password)

    if result == "admin":
        print("Welcome, admin")
        navigator.go_to("admin")
        admin_menu(navigator)
    elif result is not None:
        print(f"Welcome, {result.name}")
        current_trip = core.create_empty_trip()
        navigator.go_to("home")
        home_page(navigator, result, current_trip)
    else:
        print("Wrong email or password")


def register_page(navigator):
    print("---- Register ----")
    name = input("Name: ")
    phone = input("Phone number (include country code, e.g. +201234567890): ")
    email = input("Email: ")
    gender = input("Gender: ")
    governorate = input("Governorate: ")
    password = input("Password: ")
    age = input("Age: ")
    national_id = input("National ID: ")

    if not core.validate_email(email):
        print("Invalid email")
        return

    if not core.validate_phone(phone):
        print("Invalid phone number")
        return

    if not core.validate_national_id(national_id):
        print("Invalid national ID")
        return

    if not core.validate_age(age):
        print("Invalid age")
        return

    success = core.register_user(name, phone, email, gender, governorate,
                                  password, int(age), national_id)

    if success:
        print("Registered successfully")
        login_page(navigator)
    else:
        print("This email is already registered")


def home_page(navigator, current_user, current_trip):
    while True:
        print("---- Categories ----")
        for i, category in enumerate(core.CATEGORIES, start=1):
            print(f"{i}) {category}")
        print("T) My Trip")
        print("F) Finish Trip (Summary)")
        print("0) Exit")

        choice = input("Choose an option: ").strip().upper()

        if choice == "0":
            return

        if choice == "T":
            navigator.go_to("my_trip")
            my_trip_page(navigator, current_trip)
        elif choice == "F":
            navigator.go_to("final_summary")
            final_summary_page(navigator, current_trip, current_user)
        else:
            try:
                index = int(choice) - 1
            except ValueError:
                print("Invalid choice")
                continue

            if 0 <= index < len(core.CATEGORIES):
                navigator.go_to("category")
                category_page(navigator, core.CATEGORIES[index], current_user, current_trip)
            else:
                print("Invalid choice")


def category_page(navigator, category_name, current_user, current_trip):
    attractions = core.get_by_category(category_name)

    print(f"---- {category_name} ----")
    for attraction in attractions:
        print(f"- {attraction.name} | {attraction.ticket_price} EGP")

    print("1) Search by name")
    print("2) Sort")
    print("0) Back")

    choice = input("Your choice: ")

    if choice == "1":
        name = input("Enter the name: ")
        result = core.search_attraction_by_name(attractions, name)
        if result:
            navigator.go_to("attraction_detail")
            attraction_detail_page(navigator, result, current_trip)
        else:
            print("No attraction found with this name")

    elif choice == "2":
        sort_key = input("Sort by (ticket_price / rating): ")
        sorted_list = core.sort_attractions(attractions, sort_key)
        for attraction in sorted_list:
            print(f"- {attraction.name} | {getattr(attraction, sort_key)}")

    elif choice == "0":
        navigator.go_back()


def attraction_detail_page(navigator, attraction, current_trip):
    print(f"Name: {attraction.name}")
    print(f"Governorate: {attraction.governorate}")
    print(f"Price: {attraction.ticket_price}")
    print(f"Rating: {attraction.rating}")
    print(f"Estimated time: {attraction.estimated_time}")
    print(f"Description: {attraction.description}")

    choice = input("1) Add to trip  2) Remove from trip  0) Back: ")

    if choice == "1":
        core.add_to_trip(current_trip, attraction)
        print("Added to trip")
    elif choice == "2":
        core.remove_from_trip(current_trip, attraction.name)
        print("Removed from trip")
    elif choice == "0":
        navigator.go_back()


def my_trip_page(navigator, current_trip):
    print("---- My Trip ----")
    if not current_trip:
        print("Your trip is empty")
        return

    for attraction in current_trip:
        print(f"- {attraction.name} | {attraction.ticket_price} EGP")


def final_summary_page(navigator, current_trip, current_user):
    summary = core.calculate_final_summary(current_trip, current_user.governorate)

    print("---- Final Summary ----")
    print(f"Attractions cost: {summary['attractions_cost']}")
    print(f"Transportation cost: {summary['transportation_cost']}")
    print(f"Total: {summary['total']}")


def admin_menu(navigator):
    print("---- Admin Panel ----")
    print("1) Add attraction")
    print("2) Update attraction")
    print("3) Remove attraction")
    print("0) Exit")

    choice = input("Your choice: ")

    if choice == "1":
        name = input("Name: ")
        governorate = input("Governorate: ")
        ticket_price = float(input("Price: "))
        rating = float(input("Rating: "))
        estimated_time = input("Estimated time: ")
        category = input("Category: ")

        core.add_attraction(name, governorate, ticket_price, rating,
                             estimated_time, category)
        print("Added successfully")

    elif choice == "2":
        name = input("Name of the attraction to update: ")
        field = input("Field to change: ")
        value = input("New value: ")

        # ticket_price and rating must stay numeric, not strings.
        if field in ("ticket_price", "rating"):
            try:
                value = float(value)
            except ValueError:
                print("Invalid numeric value")
                admin_menu(navigator)
                return

        core.update_attraction(name, **{field: value})
        print("Updated successfully")

    elif choice == "3":
        name = input("Name of the attraction to remove: ")
        core.remove_attraction(name)
        print("Removed successfully")

    elif choice == "0":
        return

    admin_menu(navigator)


def run():
    navigator = core.PageNavigator()
    navigator.go_to("login")
    core.seed_sample_data()

    while True:
        print("\n===== SIC Tourism & Trip Planning =====")
        print("1) Login")
        print("2) Register")
        print("0) Exit")

        choice = input("Your choice: ")

        if choice == "1":
            login_page(navigator)
        elif choice == "2":
            register_page(navigator)
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    run()

"""
SIC Tourism & Trip Planning

TODO

phone validation: use phonenumbers lib instead of manual regex ✅

national id validation: make it stronger not just "14 digits" ( Passport for non egyptatin )

add passport_id for foreigners

add nationality attribute (Egyptian -> national_id, foreign -> passport_id)

validate sort_key input (crashes with AttributeError rn if not ticket_price/rating)

better error messages everywhere in general

make places.json with full data for every place

use datetime to suggest places based on current time

add more real places worldwide + hotels + real data for testing ✅
"""

# ============================================================
# TODO
# ============================================================

# --- 2) Nationality / Passport in register flow ---------------------------
# TODO: register_page() above needs to ask nationality first, then branch:
#       Egyptian > ask national_id (core.validate_national_id_strict)
#       foreign  > ask passport_id (core.validate_passport_id)
#       then call core.register_user_with_nationality(...) instead of
#       core.register_user(...). Not editing register_page() yet.

def nationality_prompt():
    """
    TODO: ask "Egyptian or foreign?" then ask national_id or passport_id
          accordingly, and return (nationality, id_value).
    """
    pass


# --- 3) sort_key validation in category_page ------------------------------
# TODO: category_page() above calls core.sort_attractions(attractions,
#       sort_key) with a raw input() value -> crashes with AttributeError
#       on a bad sort_key. Should call core.validate_sort_key(sort_key)
#       first and re-prompt / show an error instead. Not editing
#       category_page() yet.


# --- 5) Time-based suggestions page ----------------------------------------

def suggested_now_page(navigator, current_user, current_trip):
    """
    TODO: new page that calls core.suggest_places_by_current_time() and
          lets the user browse/add the suggested attractions, same as
          category_page(). Needs a menu entry added to home_page() once
          ready — not adding that entry yet since it means editing
          home_page().
    """
    pass