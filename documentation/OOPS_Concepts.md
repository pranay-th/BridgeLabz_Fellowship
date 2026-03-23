# Object-Oriented Programming, Object Modeling & JSON Handling in Python

## Core OOP Principles

### 1. Encapsulation
Binding data and methods together within a class, controlling access to internal state.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
```

### 2. Abstraction
Hiding internal implementation details and exposing only necessary functionality.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(rect.area())  # 15
```

### 3. Inheritance
Reusing code through parent-child class relationships, allowing derived classes to inherit properties and methods.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!
```

### 4. Polymorphism
Using the same function name with different behaviors across different classes or contexts.

```python
class Bird:
    def fly(self):
        return "Flying high in the sky"

class Penguin:
    def fly(self):
        return "I can't fly, but I can swim!"

def let_it_fly(bird):
    print(bird.fly())

sparrow = Bird()
penguin = Penguin()
let_it_fly(sparrow)   # Flying high in the sky
let_it_fly(penguin)   # I can't fly, but I can swim!
```

## Basic Class Structure

Classes in Python are defined using the `class` keyword and typically include:
- `__init__` method for initialization
- Instance attributes (self.attribute)
- Instance methods for behavior

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start_engine(self):
        return f"{self.brand} {self.model}'s engine started!"

my_car = Car("Tesla", "Model 3")
print(my_car.start_engine())  # Tesla Model 3's engine started!
```
```python
import uuid

# Generate a random UUID (UUID4)
random_uuid = uuid.uuid4()
print(random_uuid)  # e.g. 550e8400-e29b-41d4-a716-446655440000

# Generate a UUID based on host and time (UUID1)
time_uuid = uuid.uuid1()
print(time_uuid)

# Convert UUID to string
uuid_str = str(random_uuid)
print(uuid_str)

# Create UUID from string
parsed_uuid = uuid.UUID("550e8400-e29b-41d4-a716-446655440000")
print(parsed_uuid.version)  # None (not generated, just parsed)

# UUID properties
u = uuid.uuid4()
print(u.hex)    # UUID as 32-char hex string without dashes
print(u.int)    # UUID as 128-bit integer
print(u.bytes)  # UUID as 16-byte string
```

## Object Modeling

Object modeling represents real-world entities as objects in software:
- Identify entities (e.g., Customer, Product, Order)
- Define attributes and relationships
- Implement methods for behavior
- Model interactions between objects

### Example: E-Commerce System
- **Product**: name, price
- **Customer**: name, email
- **Order**: customer, products, total_price()

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Order:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products
    
    def total_price(self):
        return sum(p.price for p in self.products)

# Example Usage
cust = Customer("Alice", "alice@example.com")
items = [Product("Book", 300), Product("Pen", 20)]
order = Order(cust, items)
print("Total Order Price:", order.total_price())  # 320
```

## JSON & Nested Data Handling

### What is JSON?
JavaScript Object Notation - a lightweight data interchange format used for:
- Data exchange between applications
- API responses
- Configuration files

### Working with JSON in Python
- `json.loads()` - Parse JSON string to Python dict
- `json.dumps()` - Convert Python dict to JSON string
- Accessing nested data using bracket notation
- Traversing complex nested structures recursively

```python
import json

# Example JSON string
json_data = '''
{
  "employee": {
    "name": "John",
    "age": 30,
    "skills": ["Python", "ML", "SQL"],
    "address": {"city": "Mumbai", "zip": 400001}
  }
}
'''

# Parse JSON to Python dict
data = json.loads(json_data)

# Access nested data
print("Employee Name:", data["employee"]["name"])  # John
print("City:", data["employee"]["address"]["city"])  # Mumbai

# Modify data
data["employee"]["skills"].append("Docker")
data["employee"]["address"]["city"] = "Delhi"

# Convert back to JSON
updated_json = json.dumps(data, indent=2)
print(updated_json)
```

### Common Operations
- Reading and parsing JSON data
- Accessing nested keys and values
- Modifying JSON structures
- Converting between JSON and Python objects
- Pretty printing JSON with indentation

### Nested JSON Traversal

```python
def traverse_json(data, indent=0):
    for key, value in data.items():
        print("  " * indent + str(key), ":", end=" ")
        if isinstance(value, dict):
            print()
            traverse_json(value, indent+1)
        else:
            print(value)

traverse_json(data)
```


## Dunder Methods (Magic Methods)

Dunder methods (double underscore methods) are special methods in Python that enable custom behavior for built-in operations.

### Common Dunder Methods

#### Object Initialization and Representation
- `__init__(self, ...)` - Constructor, initializes object
- `__str__(self)` - String representation for users (used by `str()` and `print()`)
- `__repr__(self)` - Official string representation for developers (used by `repr()`)
- `__del__(self)` - Destructor, called when object is garbage collected

#### Comparison Operators
- `__eq__(self, other)` - Equality (`==`)
- `__ne__(self, other)` - Inequality (`!=`)
- `__lt__(self, other)` - Less than (`<`)
- `__le__(self, other)` - Less than or equal (`<=`)
- `__gt__(self, other)` - Greater than (`>`)
- `__ge__(self, other)` - Greater than or equal (`>=`)

#### Arithmetic Operators
- `__add__(self, other)` - Addition (`+`)
- `__sub__(self, other)` - Subtraction (`-`)
- `__mul__(self, other)` - Multiplication (`*`)
- `__truediv__(self, other)` - Division (`/`)
- `__floordiv__(self, other)` - Floor division (`//`)
- `__mod__(self, other)` - Modulo (`%`)
- `__pow__(self, other)` - Power (`**`)

#### Container Methods
- `__len__(self)` - Length (used by `len()`)
- `__getitem__(self, key)` - Get item (`obj[key]`)
- `__setitem__(self, key, value)` - Set item (`obj[key] = value`)
- `__delitem__(self, key)` - Delete item (`del obj[key]`)
- `__contains__(self, item)` - Membership test (`item in obj`)
- `__iter__(self)` - Make object iterable
- `__next__(self)` - Get next item in iteration

#### Callable Objects
- `__call__(self, ...)` - Makes object callable like a function

#### Context Managers
- `__enter__(self)` - Enter context (used with `with` statement)
- `__exit__(self, exc_type, exc_val, exc_tb)` - Exit context

### Example Usage
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __len__(self):
        return 2  # Point has 2 dimensions

# Usage
p1 = Point(3, 4)
p2 = Point(1, 2)

print(p1)              # Point(3, 4)
print(repr(p1))        # Point(x=3, y=4)
p3 = p1 + p2           # Uses __add__
print(p3)              # Point(4, 6)
print(p1 == p2)        # False
print(len(p1))         # 2
```

### More Dunder Examples

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __len__(self):
        return self.pages
    
    def __getitem__(self, page):
        return f"Content of page {page}"
    
    def __contains__(self, keyword):
        return keyword.lower() in self.title.lower()

book = Book("Python Programming", 500)
print(len(book))           # 500
print(book[10])            # Content of page 10
print("Python" in book)    # True
```

```python
class Counter:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        return self.count

counter = Counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

## Regular Expressions (Regex)

Regular expressions are patterns used to match character combinations in strings.

### Python `re` Module

Import: `import re`

### Common Functions

#### Pattern Matching
- `re.match(pattern, string)` - Match at beginning of string
- `re.search(pattern, string)` - Search anywhere in string
- `re.findall(pattern, string)` - Find all occurrences, return list
- `re.finditer(pattern, string)` - Find all occurrences, return iterator

#### String Manipulation
- `re.sub(pattern, replacement, string)` - Replace matches
- `re.split(pattern, string)` - Split string by pattern

#### Compilation
- `re.compile(pattern)` - Compile pattern for reuse

### Common Regex Patterns

#### Character Classes
- `.` - Any character except newline
- `\d` - Digit (0-9)
- `\D` - Non-digit
- `\w` - Word character (alphanumeric + underscore)
- `\W` - Non-word character
- `\s` - Whitespace (space, tab, newline)
- `\S` - Non-whitespace
- `[abc]` - Any character in set
- `[^abc]` - Any character not in set
- `[a-z]` - Character range

#### Quantifiers
- `*` - 0 or more occurrences
- `+` - 1 or more occurrences
- `?` - 0 or 1 occurrence
- `{n}` - Exactly n occurrences
- `{n,}` - n or more occurrences
- `{n,m}` - Between n and m occurrences

#### Anchors
- `^` - Start of string
- `$` - End of string
- `\b` - Word boundary
- `\B` - Non-word boundary

#### Groups and Alternation
- `(...)` - Capturing group
- `(?:...)` - Non-capturing group
- `|` - Alternation (OR)

### Example Usage
```python
import re

# Email validation
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = "user@example.com"
if re.match(pattern, email):
    print("Valid email")

# Extract phone numbers
text = "Call me at 123-456-7890 or 987-654-3210"
phones = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(phones)  # ['123-456-7890', '987-654-3210']

# Replace patterns
text = "Hello World"
result = re.sub(r'\s+', '_', text)
print(result)  # "Hello_World"

# Search for pattern
text = "The price is $50"
match = re.search(r'\$(\d+)', text)
if match:
    print(f"Found price: {match.group(1)}")  # Found price: 50

# Split by pattern
text = "apple,banana;orange|grape"
fruits = re.split(r'[,;|]', text)
print(fruits)  # ['apple', 'banana', 'orange', 'grape']
```

### More Regex Examples

```python
import re

# Validate password (8+ chars, 1 uppercase, 1 lowercase, 1 digit)
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
password = "SecurePass123"
if re.match(password_pattern, password):
    print("Strong password")

# Extract URLs from text
text = "Visit https://example.com or http://test.org"
urls = re.findall(r'https?://[^\s]+', text)
print(urls)  # ['https://example.com', 'http://test.org']

# Find all words starting with capital letter
text = "Alice and Bob went to Paris"
names = re.findall(r'\b[A-Z][a-z]+\b', text)
print(names)  # ['Alice', 'Bob', 'Paris']

# Replace multiple spaces with single space
text = "Too    many     spaces"
cleaned = re.sub(r'\s+', ' ', text)
print(cleaned)  # "Too many spaces"

# Compile pattern for reuse
email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
print(email_pattern.match("test@example.com"))  # Match object
print(email_pattern.match("invalid-email"))     # None
```

### Common Use Cases
- Email validation
- Phone number extraction
- URL parsing
- Data cleaning and formatting
- Log file parsing
- Input validation
- Text search and replace
