# 🇪🇬 Egypt Explorer – Smart Tourism & Trip Planning System

## 📌 Project Overview

**Egypt Explorer – Smart Tourism & Trip Planning System** is a Python academic project designed to provide a smart tourism experience for users who want to explore tourist attractions, search and filter destinations, build personalized trips, and calculate trip costs.

The project demonstrates practical applications of:

- Object-Oriented Programming (OOP)
- Data Structures
- Algorithms
- Searching
- Sorting
- Stack-based navigation
- Input validation
- Dynamic calculations
- File/data management
- Git & GitHub collaboration

The project is organized into multiple modules so that the team can develop different parts independently and then integrate them into one complete application.

---

# 🎯 Project Objectives

The main objectives of the system are to:

1. Help users discover tourist attractions.
2. Organize attractions according to categories and governorates.
3. Allow users to search for attractions.
4. Allow users to sort and filter available attractions.
5. Display useful information about attractions.
6. Allow users to create a personalized trip.
7. Add and remove attractions from the trip.
8. Calculate the estimated trip cost.
9. Calculate transportation costs.
10. Provide hotel-related functionality.
11. Validate user information.
12. Provide page navigation using a Stack.
13. Demonstrate the use of Data Structures and Algorithms in a practical application.
14. Provide a structure that can be extended later with smarter recommendation and tourism features.

---

# ✨ Main Features

## 1. 👤 User & Authentication

The system contains user-related functionality for handling users and their information.

A user may have information such as:

- Name
- Phone number
- Email
- Gender
- Governorate
- Password
- Age
- National ID
- Nationality

The system should validate important information before accepting it.

### User Validation

The current validation area includes:

```python
validate_email(email)
validate_phone(phone)
validate_national_id(national_id)
validate_age(age)
```

### Validation Requirements

#### Email
The email should follow the expected email format.

#### Phone
The phone number should be validated according to the required format.

#### National ID
The original project requirement specifies a 14-digit Egyptian national ID.

#### Age
The age must be a valid numeric and reasonable value.

### 🔧 Validation TODOs from the project notes

The following improvements are **planned TODOs and are not claimed as already implemented**:

- Use the `phonenumbers` library instead of relying only on manual phone-number regular expressions.
- Make national ID validation stronger instead of checking only `"14 digits"`.
- Support passports for non-Egyptian users.
- Add a `passport_id` field for foreign users.
- Add a `nationality` attribute.
- Use the following logic:
  - Egyptian → `national_id`
  - Foreign → `passport_id`

---

# 🏛️ 2. Tourist Attractions

The main tourism entity is the **Attraction**.

An attraction can contain information such as:

- Name
- Governorate
- Category
- Ticket price
- Rating
- Description

The system stores attractions and provides operations for managing and retrieving them.

## Attraction Operations

```python
add_attraction()
update_attraction()
remove_attraction()
get_by_category()
get_attraction_by_name()
```

### Add Attraction

Allows an attraction to be added to the available attractions.

### Update Attraction

Allows existing attraction information to be modified.

### Remove Attraction

Removes an attraction from the available attractions.

### Get by Category

Returns attractions belonging to a selected category.

### Search by Name

Searches for an attraction using its name.

---

# 🔎 3. Search

The system provides attraction searching so users can quickly find a destination.

The search functionality can be used to find an attraction by name and retrieve its complete attraction object.

Example:

```text
User enters:
"Pyramids"

System searches:
all_attractions

Result:
Pyramids attraction
```

The project should use the required searching/data-structure approach specified by the course project.

---

# ↕️ 4. Sorting

The system supports sorting attraction results according to supported attributes.

Examples may include:

- Ticket price
- Rating

The sorting functionality should allow the user to select a valid sorting key.

### 🔧 Sorting Validation TODO

The project notes identify a current improvement:

> Validate `sort_key` input because invalid values can currently cause an `AttributeError`.

Therefore, the final implementation should validate the requested sorting key before attempting to access the corresponding attraction attribute.

For example:

```text
Valid:
ticket_price
rating

Invalid:
anything_else
```

The system should return a clear error instead of crashing.

---

# 🗂️ 5. Filtering

The system supports filtering attractions according to available project criteria.

Examples include:

- Category
- Governorate
- Budget-related criteria where the bonus functionality is implemented

Filtering helps users reduce the number of displayed attractions and find destinations that match their preferences.

---

# 🧳 6. Trip Planning

Trip planning is one of the main features of the system.

Users can create a personalized trip by selecting attractions.

## Trip Operations

```python
create_empty_trip()
add_to_trip(trip, attraction)
remove_from_trip(trip, attraction_name)
calculate_final_summary(trip, user_governorate)
```

### Create Empty Trip

Creates a new trip without selected attractions.

### Add to Trip

Adds a selected attraction to the user's current trip.

### Remove from Trip

Removes a selected attraction from the trip.

### Example

```text
My Trip

1. Pyramids
2. Egyptian Museum
3. Khan El Khalili
```

The user can remove an attraction if they no longer want it.

---

# 💰 7. Final Trip Summary

The final summary calculates the cost based on the user's current selections.

The result contains:

```text
attractions_cost
transportation_cost
total
```

The calculation should be dynamic.

```text
Total Cost
=
Attractions Cost
+
Transportation Cost
```

The result must depend on the attractions actually selected by the user rather than using a fixed hard-coded value.

---

# 🏨 8. Hotels

Hotel functionality is included in the project skeleton as a bonus feature.

Hotels can contain:

- Hotel name
- Governorate
- Price per night
- Rating
- Description

## Hotel Operations

```python
add_hotel()
update_hotel()
remove_hotel()
get_hotels_by_governorate()
```

### Add Hotel

Adds a new hotel.

### Update Hotel

Updates the information of an existing hotel.

### Remove Hotel

Removes a hotel.

### Get Hotels by Governorate

Returns hotels located in the selected governorate.

This can be used to suggest accommodation related to a user's destination.

---

# 🧭 9. Navigation System

The application includes a `PageNavigator` responsible for page navigation.

The navigation history is implemented using a **Stack**.

## Main Operations

```python
go_to(page_name)
go_back()
current_page()
```

### Example

```text
Home
  ↓
Categories
  ↓
Attraction Details
  ↓
Trip
```

If the user presses Back:

```text
Trip
  ↓
Attraction Details
```

The Stack stores previous pages and allows the application to return to the previous page.

---

# 🧱 10. Object-Oriented Programming

The project uses classes to represent real-world entities.

Important entities can include:

```text
User
Attraction
Hotel
Trip
PageNavigator
```

Using classes provides:

- Encapsulation
- Reusable objects
- Clear separation of responsibilities
- Easier maintenance
- Better project organization

---

# 🧮 11. Data Structures & Algorithms

The project demonstrates practical use of Data Structures and Algorithms.

Concepts include:

- Lists
- Stack
- Searching
- Sorting
- Filtering
- Object-oriented data modeling
- Validation
- Dynamic calculations

## Stack

Used for:

```text
Page Navigation History
```

## Searching

Used for:

```text
Finding attractions by name
```

## Sorting

Used for:

```text
Ordering attractions by supported properties
```

---

# 📁 12. Project Structure

The expected repository structure is:

```text
SIC-Tourism-Trip-Planning/
│
├── README.md
├── core.py
├── main.py
├── structures_and_algorithms.py
├── requirements.txt
└── .gitignore
```

## `core.py`

Contains the main project entities and business logic, including:

- Users
- Attractions
- Hotels
- Trips
- Navigation
- Validation
- Related helper functions

## `main.py`

Acts as the application entry point and connects the project components.

It is responsible for starting the program and presenting the main application flow/menu according to the team's implementation.

## `structures_and_algorithms.py`

Contains data structures and algorithm implementations used by the project.

## `requirements.txt`

Contains external Python libraries required to run the project.

## `.gitignore`

Prevents unnecessary or sensitive files from being committed to GitHub.

---

# 📦 13. Data Management

The system can use structured data to store attraction and hotel information.

### 🔧 Data TODO: `places.json`

One of the project notes specifies:

> Create `places.json` with full data for every place.

The planned structure is to keep complete information for every tourist place in a dedicated JSON file.

Example conceptual structure:

```json
{
  "name": "Pyramids of Giza",
  "governorate": "Giza",
  "category": "Historical",
  "ticket_price": 200,
  "rating": 4.8,
  "description": "..."
}
```

This is listed as a **TODO / planned enhancement** unless the team has already created and integrated `places.json`.

---

# 🕒 14. Time-Based Recommendations

A planned smart feature is to use Python's `datetime` functionality to suggest places based on the current time.

### 🔧 TODO: Datetime Recommendations

The system can later consider:

- Current time
- Opening/closing time
- Suitable attractions
- Day/night activities

Example concept:

```text
Current time → 10:00 AM
       ↓
Check suitable places
       ↓
Suggest attractions currently suitable for visiting
```

This feature is listed as a **TODO / future enhancement** unless already implemented by the team.

---

# 🌍 15. Real Tourism Data & Testing

Another project note specifies adding more realistic data for testing.

### 🔧 TODO: Real Data

Planned improvements include:

- More real tourist places
- More hotels
- More realistic prices
- More realistic ratings
- More complete descriptions
- More destinations worldwide
- Larger datasets for testing searching and sorting

The purpose is to make testing more realistic and demonstrate the algorithms on a larger dataset.

This is a **planned enhancement** unless the team has already added the data.

---

# 💬 16. Error Handling

The project should provide clear error messages when users enter invalid information.

Examples:

```text
Invalid email.
Invalid phone number.
National ID must contain 14 digits.
Invalid age.
Attraction not found.
Hotel not found.
Invalid sorting key.
```

### 🔧 Error Message TODO

The project notes specifically request:

> Better error messages everywhere in general.

Therefore, error messages should be reviewed across the whole application and made:

- Clear
- Specific
- User-friendly
- Consistent
- Helpful enough to explain what went wrong

Instead of:

```text
Error
```

Prefer:

```text
Invalid sorting key. Please choose 'ticket_price' or 'rating'.
```

This is a project improvement/TODO unless already implemented consistently.

---

# ⭐ 17. Bonus Features

The project skeleton contains optional bonus functionality.

Possible bonus features include:

- Hotel management
- Cloud data saving/loading
- Budget filtering
- Related attraction suggestions
- Trip route optimization
- Attraction comparison
- Favorites

## Favorites

Possible operations:

```python
add_to_favourites(user, attraction_name)
remove_from_favourites(user, attraction_name)
view_favourites(user)
```

If Favorites is implemented, the user model also needs a suitable favorites collection such as:

```python
self.favourite_attractions = []
```

Bonus features should only be described as completed after they are actually implemented and tested.

---

# 🧪 18. Testing Plan

Before final submission, the complete project should be tested.

## User Tests

- Valid registration
- Invalid registration
- Valid login
- Invalid login
- Email validation
- Phone validation
- Age validation
- National ID validation
- Foreign user/passport validation after implementation

## Attraction Tests

- Add attraction
- Update attraction
- Remove attraction
- Search by name
- Search for missing attraction
- Filter by category
- Filter by governorate
- Sort by ticket price
- Sort by rating
- Invalid sorting key

## Trip Tests

- Create empty trip
- Add one attraction
- Add multiple attractions
- Remove attraction
- Remove missing attraction
- Calculate attraction cost
- Calculate transportation cost
- Calculate total cost
- Test an empty trip

## Hotel Tests

- Add hotel
- Update hotel
- Remove hotel
- Search hotels by governorate

## Navigation Tests

- `go_to()`
- `go_back()`
- `current_page()`
- Multiple page transitions
- Empty navigation history

## Data Tests

- Load attraction data
- Validate complete place information
- Test larger datasets
- Test realistic tourism data


# 🔄 20. Example User Flow

```text
Start
  ↓
Register / Login
  ↓
Home
  ↓
Browse Categories
  ↓
View Attractions
  ↓
Search / Filter / Sort
  ↓
View Attraction Details
  ↓
Add Attractions to Trip
  ↓
Review Trip
  ↓
Remove Attractions if Needed
  ↓
Calculate Final Summary
  ↓
Display Total Cost
```

---

# 👥 21. Team Responsibilities

The project is divided among three team members.

### 👤 Team Member 1

Responsible for the first assigned project section according to the team's division.

### 👤 Team Member 2

Responsible for the second assigned project section according to the team's division.

Responsible for:

### Hotels
```text
add_hotel()
update_hotel()
remove_hotel()
get_hotels_by_governorate()
```

### Trip
```text
create_empty_trip()
add_to_trip()
remove_from_trip()
calculate_final_summary()
```

### Navigation
```text
PageNavigator
go_to()
go_back()
current_page()
```

### Validation
```text
validate_email()
validate_phone()
validate_national_id()
validate_age()
```



---

# 📝 22. Known TODOs / Future Improvements

The following items are taken from the project's TODO notes and are documented here without claiming that they are already implemented:

1. **Phone validation**
   - Use the `phonenumbers` library instead of manual regex-only validation.

2. **Stronger National ID validation**
   - Do not rely only on checking that the value contains 14 digits.

3. **Passport support**
   - Add passport ID support for non-Egyptian users.

4. **`passport_id` attribute**
   - Add a dedicated passport identifier to the user model.

5. **`nationality` attribute**
   - Add nationality to the user model.
   - Egyptian → national ID.
   - Foreign → passport ID.

6. **Sorting key validation**
   - Validate the `sort_key`.
   - Prevent `AttributeError` when an unsupported key is supplied.

7. **Better error messages**
   - Improve error messages throughout the application.

8. **`places.json`**
   - Create a complete JSON dataset containing full information for every place.

9. **Datetime-based recommendations**
   - Use `datetime` to suggest places based on the current time.

10. **More realistic data**
    - Add more real tourist places, hotels, and realistic test data.

These items should be moved from TODO to the completed Features sections only after they are actually implemented and tested.

---

# 📌 23. Important Project Notes

- The README describes the **whole project**, not only one team member's section.
- A README does not contain every line of project code; it documents what the project does and how it is organized.
- Features should not be marked as completed unless they are actually implemented and tested.
- Bonus features should be clearly distinguished from required features.
- The final team should integrate all branches/changes and test the complete project before submission.
- The repository should contain one main `README.md` in the root directory.

---

# 📊 24. Project Status

**Project:** Egypt Explorer – Smart Tourism & Trip Planning System

**Language:** Python

**Project Type:** Academic Data Structures & Algorithms / OOP Project

**Development Status:** Team Development & Integration

---

# 📜 License

This project was created as an academic/team project.
