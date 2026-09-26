import core


def nationality_prompt():
    nationality = input("Nationality (Egyptian / Foreign): ").strip()

    if nationality.lower() == "egyptian":
        national_id = input("National ID (14 digits): ")
        return nationality, national_id, None

    passport_id = input("Passport ID: ")
    return nationality, None, passport_id


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
    city = input("City / Region: ")
    password = input("Password: ")
    age = input("Age: ")
    nationality, national_id, passport_id = nationality_prompt()

    if not core.validate_email(email):
        print("Invalid email. Please use a format like name@example.com")
        return

    if not core.validate_phone(phone):
        print("Invalid phone number. Make sure to include the country code, e.g. +201234567890")
        return

    if not core.validate_age(age):
        print("Invalid age. Please enter a number between 1 and 120")
        return

    if nationality.lower() == "egyptian":
        if not core.validate_national_id(national_id):
            print("Invalid national ID. It must be 14 digits with a valid birth date and governorate code")
            return
    else:
        if not core.validate_passport_id(passport_id):
            print("Invalid passport ID. It should be 6-9 letters/numbers")
            return

    success = core.register_user(name, phone, email, gender, city,
                                  password, int(age), nationality,
                                  national_id, passport_id)

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
        print("B) Best Season")
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
        elif choice == "B":
            navigator.go_to("best_season")
            best_season_page(navigator, current_user, current_trip)
        else:
            try:
                index = int(choice) - 1
            except ValueError:
                print("Invalid choice. Enter a category number, B, T, F, or 0.")
                continue

            if 0 <= index < len(core.CATEGORIES):
                navigator.go_to("category")
                category_page(navigator, core.CATEGORIES[index], current_user, current_trip)
            else:
                print("Invalid choice. That category number doesn't exist.")


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
        sort_key = input("Sort by (ticket_price / rating / name): ").strip()

        if not core.validate_sort_key(sort_key):
            print(f"Invalid sort option. Choose one of: {', '.join(core.ALLOWED_SORT_KEYS)}")
        else:
            sorted_list = core.sort_attractions(attractions, sort_key)
            for attraction in sorted_list:
                print(f"- {attraction.name} | {getattr(attraction, sort_key)}")

    elif choice == "0":
        navigator.go_back()
    else:
        print("Invalid choice")


def attraction_detail_page(navigator, attraction, current_trip):
    print(f"Name: {attraction.name}")
    print(f"City: {attraction.city}")
    print(f"Price: {attraction.ticket_price}")
    print(f"Rating: {attraction.rating}")
    print(f"Estimated time: {attraction.estimated_time}")
    print(f"Description: {attraction.description}")

    choice = input("1) Add to trip  2) Remove from trip  0) Back: ")

    if choice == "1":
        added = core.add_to_trip(current_trip, attraction)
        print("Added to trip" if added else "This attraction is already in your trip")
    elif choice == "2":
        removed = core.remove_from_trip(current_trip, attraction.name)
        print("Removed from trip" if removed else "This attraction isn't in your trip")
    elif choice == "0":
        navigator.go_back()
    else:
        print("Invalid choice")


def my_trip_page(navigator, current_trip):
    print("---- My Trip ----")
    if not current_trip:
        print("Your trip is empty")
        return

    for attraction in current_trip:
        print(f"- {attraction.name} | {attraction.ticket_price} EGP")


def final_summary_page(navigator, current_trip, current_user):
    summary = core.calculate_final_summary(current_trip)

    print("---- Final Summary ----")
    print(f"Attractions cost: {summary['attractions_cost']} EGP")
    print(f"Fees: {summary['fees']} EGP")
    print(f"Total: {summary['total']} EGP")




def best_season_page(navigator, current_user, current_trip):
    print("---- Best Season ----")
    print("1) See what's good to visit this month")
    print("2) Enter a travel month to plan ahead")
    print("0) Back")

    choice = input("Your choice: ").strip()

    if choice == "1":
        matches, month_name = core.suggest_places_for_current_month()
    elif choice == "2":
        month_input = input("Which month are you planning to travel? (name or number): ")
        month = core.validate_month(month_input)
        if month is None:
            print("Invalid month. Enter a month name (e.g. October) or a number 1-12.")
            return
        matches = core.suggest_places_by_month(month)
        month_name = core.MONTH_NAMES[month - 1]
    elif choice == "0":
        navigator.go_back()
        return
    else:
        print("Invalid choice")
        return

    print(f"---- Good to visit in {month_name} ----")
    if not matches:
        print("No attractions are marked as best visited in this month yet.")
        return

    for i, attraction in enumerate(matches, start=1):
        print(f"{i}) {attraction.name} | {attraction.city} | {attraction.ticket_price} EGP")
    print("0) Back")

    pick = input("View details (number) or 0 to go back: ").strip()

    if pick == "0":
        return

    try:
        index = int(pick) - 1
    except ValueError:
        print("Invalid choice")
        return

    if 0 <= index < len(matches):
        navigator.go_to("attraction_detail")
        attraction_detail_page(navigator, matches[index], current_trip)
    else:
        print("Invalid choice")


def admin_menu(navigator):
    while True:
        print("---- Admin Panel ----")
        print("1) Add attraction")
        print("2) Update attraction")
        print("3) Remove attraction")
        print("4) Set backup folder")
        print("0) Exit")

        choice = input("Your choice: ")

        if choice == "1":
            name = input("Name: ")
            city = input("City / Region: ")

            try:
                ticket_price = float(input("Price: "))
                rating = float(input("Rating: "))
            except ValueError:
                print("Price and rating must be numbers")
                continue

            estimated_time = input("Estimated time: ")
            category = input(f"Category ({', '.join(core.CATEGORIES)}): ")

            core.add_attraction(name, city, ticket_price, rating,
                                 estimated_time, category)
            print("Added successfully")

        elif choice == "2":
            name = input("Name of the attraction to update: ")
            field = input(f"Field to change ({', '.join(core.ATTRACTION_FIELDS)}): ").strip()

            if field not in core.ATTRACTION_FIELDS:
                print(f"Invalid field. Choose one of: {', '.join(core.ATTRACTION_FIELDS)}")
                continue

            value = input("New value: ")

            # ticket_price and rating must stay numeric, not strings.
            if field in ("ticket_price", "rating"):
                try:
                    value = float(value)
                except ValueError:
                    print("Invalid numeric value")
                    continue

            success = core.update_attraction(name, **{field: value})
            print("Updated successfully" if success else "Attraction not found")

        elif choice == "3":
            name = input("Name of the attraction to remove: ")
            success = core.remove_attraction(name)
            print("Removed successfully" if success else "Attraction not found")

        elif choice == "4":
            print(f"Current backup folder: {core.DRIVE_FOLDER or '(not set)'}")
            path = input("Enter folder path (or Enter to clear): ").strip()
            if core.set_drive_folder(path):
                print("Backup folder updated" if path else "Backup folder cleared")
            else:
                print("Directory not found")

        elif choice == "0":
            return
        else:
            print("Invalid choice")


def run():
    navigator = core.PageNavigator()
    navigator.go_to("login")
    core.load_config()
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