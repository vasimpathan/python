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

#1. Student Marks Dictionary
marks = {"Alice": 85, "Bob": 92, "Charlie": 78}
# Print all student names and marks.
for key, value in marks.items():
    print(f"{key} : {value}")

# Add a new student "David" with 88 marks.
marks['David'] = 88
print(marks)

#Update "Alice"'s marks to 90.
marks['Alice'] = 90
print(marks)

#Calculate the average marks of all students.
total = sum(marks.values())
avg = total / len(marks)
print(avg)

#Print names of students who scored above 80.
for m in marks:
    if(marks[m] > 80):
        print(f"{m} scored above 80")

#2. Nested Dictionary – Employee Data
employees = {
    101: {"name": "John", "dept": "HR"},
    102: {"name": "Sara", "dept": "IT"},
    103: {"name": "Mike", "dept": "Finance"}
}
#Print name and department of each employee.
for k,v in employees.items():
        for a,b in employees[k].items():
            print(f"{a} : {b}")
#way2 
for emp_id, info in employees.items():
    print(f"Emp Id: {emp_id}, Name : {info['name']}, 'Dept : {info['dept']}")

#Add new employee 104: "Anna", dept: "Marketing".
employees['104'] = {'name':'Anna','dept':'Marketing'}
print(employees)

#Update employee 102’s dept to "Development".
employees[102]['dept'] = "Development"
print(employees)

#3. Inventory Management
inventory = {"apple": 10, "banana": 5, "orange": 8}
#Add 5 apples to inventory.
inventory['apple'] += 5
print(inventory)
#Sell 3 bananas (reduce count).
inventory['banana'] -= 3
print(inventory)
#Add new item "mango" with quantity 15.
inventory['mango'] = 15
print(inventory)
#Remove "orange" from inventory.
inventory.pop('orange')
print(inventory)
#Print final inventory using items().
for k,v in inventory.items():
    print(f"{k} : {v}")

#4. Word Counter Assignment 
sentence = "Python is easy. Python is powerful. Python is popular."
#Count how many times each word appears (case-insensitive) using a dictionary.
#Example Output:
#{"python": 3, "is": 3, "easy.": 1, "powerful.": 1, "popular.": 1}
sentence = sentence.lower()
words = sentence.split()
print(words)

wordCnt = {}
for word in words:
    word = word.strip('.')
    if word in wordCnt:
        wordCnt[word] +=1
    else:
        wordCnt[word] = 1

print(wordCnt)