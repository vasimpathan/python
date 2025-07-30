"""
Concepts to Practice:
Creating dictionaries
Accessing values using keys
Adding, updating, deleting key-value pairs
Looping through dictionary
Dictionary methods: keys(), values(), items(), get(), pop(), update()
"""
#1. Create a dictionary of 5 countries and their capitals.
capitals = {
    "India": "New Delhi",
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "Germany": "Berlin"
}

#2. Print the capital of India using its key.
print(f"Capital of India : {capitals['India']}")

#3. Add a new country-capital pair to the dictionary.
capitals['Italy'] = "Rome"
print(f"New List : {capitals}")

#4. Update the capital of an existing country.
capitals['India'] = "Mumbai"
print(f"Updated List : {capitals}")

#5. Remove a country from the dictionary using pop()
capitals.pop('Italy')
print(f"Updated List : {capitals}")

#6. Loop through the dictionary and print each country with its capital.
for keys in capitals:
    print(f" {keys} : {capitals[keys]}")

#7. Print all keys (countries) and all values (capitals) using keys() and values().
print(f"All Keys : {capitals.keys()}")
print(f"All Values : {capitals.values()}")

#8. Check if "Japan" exists in the dictionary using in.
for c in capitals:
    if(c == 'Japan'):
        print("Is Present")
        break
#9. Use get() method to safely get the capital of "Germany".
print(f"Capital of Germany : {capitals.get('Germany')}")

#10. Clear all items in the dictionary and print it.
print(f"Clear Dict: {capitals.clear()}")

person = {"name": "John", "age": 30, "city": "New York"}
person['job'] = "Engineer"
print(person)
person['age'] = person['age']+5
print(person)
person.pop('city')
print(person)

#Print all key-value pairs using items()
for key, value in person.items():
    print(f"{key} : {value}")