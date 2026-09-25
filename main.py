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
        navigator.go_to("home")
        home_page(navigator, result)
    else:
        print("Wrong email or password")


def register_page(navigator):
    print("---- Register ----")
    name = input("Name: ")
    phone = input("Phone number: ")
    email = input("Email: ")
    gender = input("Gender: ")
    governorate = input("Governorate: ")
    password = input("Password: ")
    age = input("Age: ")
    #national_id = input("National ID: ")
    #passport_id = input("Passport ID : ")


    if not core.validate_email(email):
        print("Invalid email")
        return

    if not core.validate_phone(phone):
        print("Invalid phone number")
        return

   # if not core.validate_national_id(national_id):
      #  print("Invalid national ID")
      #  return

    if not core.validate_age(age):
        print("Invalid age")
        return

    success = core.register_user(name, phone, email, gender, governorate,
                                  password, int(age)) # national ID , Passport , Nationality

    if success:
        print("Registered successfully")
        login_page(navigator)
    else:
        print("This email is already registered")


def home_page(navigator, current_user):
    print("---- Categories ----")
    for i, category in enumerate(core.CATEGORIES, start=1):
        print(f"{i}) {category}")
    print("0) Exit")

    choice = input("Choose a category: ")

    if choice == "0":
        return

    index = int(choice) - 1
    if 0 <= index < len(core.CATEGORIES):
        navigator.go_to("category")
        category_page(navigator, core.CATEGORIES[index], current_user)
    else:
        print("Invalid choice")
        home_page(navigator, current_user)


def category_page(navigator, category_name, current_user):
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
            attraction_detail_page(navigator, result, current_user)
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