"""Generate ~800 more Python exercises to reach 1000 total."""
import json, os

existing = json.load(open('data/python_exercises.json','r',encoding='utf-8'))
start_id = len(existing) + 1
exercises = []

def ex(title, desc, cat, subcat, diff, starter, output, hint, solution, explanation, syllabus=""):
    global start_id
    exercises.append({
        "id": f"PY-{start_id:04d}",
        "title": title,
        "description": desc,
        "category": cat,
        "subcategory": subcat,
        "difficulty": diff,
        "starter_code": starter,
        "test_output": output,
        "hint": hint,
        "solution": solution,
        "explanation": explanation,
        "syllabus_link": syllabus
    })
    start_id += 1

# ============ FUNDAMENTALS ============
ex("Swap Two Variables", "Swap the values of two variables without using a temporary variable.",
   "fundamentals", "variables", 1,
   "a = 5\nb = 10\n# TODO: Swap a and b\nprint(a, b)", "10 5",
   "Python supports tuple unpacking for swaps.",
   "a = 5\nb = 10\na, b = b, a\nprint(a, b)",
   "Python's tuple unpacking allows simultaneous assignment, making variable swapping a one-liner without needing a temp variable.",
   "SE: P6 — applies understanding of data types and operations")

ex("Temperature Converter", "Convert a temperature from Celsius to Fahrenheit using the formula F = C * 9/5 + 32.",
   "fundamentals", "variables", 1,
   "celsius = 100\n# TODO: Convert to fahrenheit\nprint(f'{celsius}°C = {fahrenheit}°F')", "100°C = 212.0°F",
   "The formula is F = C * 9/5 + 32.",
   "celsius = 100\nfahrenheit = celsius * 9/5 + 32\nprint(f'{celsius}°C = {fahrenheit}°F')",
   "This exercise practises arithmetic operators and f-string formatting. The division produces a float result.",
   "SE: P3 — designs algorithms")

ex("String Repetition", "Create a string that repeats 'Python' 5 times separated by dashes.",
   "fundamentals", "strings", 1,
   "# TODO: Create the repeated string\nprint(result)", "Python-Python-Python-Python-Python",
   "Use the join() method with a list.",
   "result = '-'.join(['Python'] * 5)\nprint(result)",
   "The * operator on a list creates repetitions, and join() concatenates them with a separator.",
   "SE: P6 — applies understanding of data types")

ex("Count Vowels", "Count the number of vowels in a given string (case-insensitive).",
   "fundamentals", "strings", 2,
   "text = 'Hello World'\n# TODO: Count vowels\nprint(count)", "3",
   "Convert to lowercase first, then check each character.",
   "text = 'Hello World'\ncount = sum(1 for c in text.lower() if c in 'aeiou')\nprint(count)",
   "Using a generator expression with sum() is a Pythonic way to count items matching a condition.",
   "SE: P6 — applies understanding of data types and operations")

ex("Reverse a String", "Reverse a string using slicing.",
   "fundamentals", "strings", 1,
   "text = 'Python'\n# TODO: Reverse it\nprint(reversed_text)", "nohtyP",
   "Use slice notation with a step of -1.",
   "text = 'Python'\nreversed_text = text[::-1]\nprint(reversed_text)",
   "Python's slice notation [start:stop:step] with step=-1 reverses any sequence.",
   "SE: P6 — applies understanding of data types")

ex("Check Palindrome", "Check if a string is a palindrome (reads the same forwards and backwards).",
   "fundamentals", "strings", 2,
   "word = 'racecar'\n# TODO: Check if palindrome\nprint(is_palindrome)", "True",
   "Compare the string with its reverse.",
   "word = 'racecar'\nis_palindrome = word == word[::-1]\nprint(is_palindrome)",
   "Comparing a string to its reverse is the simplest palindrome check. For case-insensitive checks, use .lower() first.",
   "SE: P3 — designs algorithms")

ex("Title Case Converter", "Convert a sentence to title case where each word starts with a capital letter.",
   "fundamentals", "strings", 1,
   "text = 'hello world from python'\n# TODO: Convert to title case\nprint(result)", "Hello World From Python",
   "Python has a built-in string method for this.",
   "text = 'hello world from python'\nresult = text.title()\nprint(result)",
   "The .title() method capitalises the first letter of each word. For more control, use .capitalize() on individual words.",
   "SE: P6 — applies understanding of data types")

ex("Remove Duplicates from List", "Remove duplicate elements from a list while preserving order.",
   "fundamentals", "lists", 2,
   "items = [1, 3, 2, 3, 1, 4, 2, 5]\n# TODO: Remove duplicates, keep order\nprint(result)", "[1, 3, 2, 4, 5]",
   "Use dict.fromkeys() to preserve order while removing duplicates.",
   "items = [1, 3, 2, 3, 1, 4, 2, 5]\nresult = list(dict.fromkeys(items))\nprint(result)",
   "dict.fromkeys() preserves insertion order (Python 3.7+) while eliminating duplicates, unlike set() which doesn't guarantee order.",
   "SE: P6 — applies understanding of data types")

ex("Flatten Nested List", "Flatten a 2D list into a single list.",
   "fundamentals", "lists", 2,
   "nested = [[1, 2], [3, 4], [5, 6]]\n# TODO: Flatten\nprint(flat)", "[1, 2, 3, 4, 5, 6]",
   "Use a list comprehension with nested loops.",
   "nested = [[1, 2], [3, 4], [5, 6]]\nflat = [item for sublist in nested for item in sublist]\nprint(flat)",
   "Nested list comprehensions read left-to-right like nested for loops. This pattern is common for flattening one level of nesting.",
   "SE: P6 — applies understanding of data types")

ex("Dictionary Merge", "Merge two dictionaries, with values from the second overriding the first.",
   "fundamentals", "dictionaries", 2,
   "d1 = {'a': 1, 'b': 2}\nd2 = {'b': 3, 'c': 4}\n# TODO: Merge\nprint(merged)", "{'a': 1, 'b': 3, 'c': 4}",
   "Use the | operator (Python 3.9+) or ** unpacking.",
   "d1 = {'a': 1, 'b': 2}\nd2 = {'b': 3, 'c': 4}\nmerged = d1 | d2\nprint(merged)",
   "The | operator merges dicts in Python 3.9+. For older versions, use {**d1, **d2}. Right-side values override left-side.",
   "SE: P6 — applies understanding of data types")

ex("Set Operations", "Find the intersection, union, and difference of two sets.",
   "fundamentals", "sets", 2,
   "a = {1, 2, 3, 4, 5}\nb = {4, 5, 6, 7, 8}\n# TODO: Find intersection, union, difference\nprint(f'Intersection: {inter}')\nprint(f'Union: {uni}')\nprint(f'Difference: {diff}')",
   "Intersection: {4, 5}\nUnion: {1, 2, 3, 4, 5, 6, 7, 8}\nDifference: {1, 2, 3}",
   "Sets have &, |, and - operators.",
   "a = {1, 2, 3, 4, 5}\nb = {4, 5, 6, 7, 8}\ninter = a & b\nuni = a | b\ndiff = a - b\nprint(f'Intersection: {inter}')\nprint(f'Union: {uni}')\nprint(f'Difference: {diff}')",
   "Set operators &, |, - correspond to intersection, union, and difference. These are fundamental operations in set theory and useful for data comparison.",
   "SE: P6 — applies understanding of data types")

ex("Enumerate with Index", "Use enumerate to print each item in a list with its index.",
   "fundamentals", "lists", 1,
   "fruits = ['apple', 'banana', 'cherry']\n# TODO: Print each with index\n", "0: apple\n1: banana\n2: cherry",
   "enumerate() returns both index and value.",
   "fruits = ['apple', 'banana', 'cherry']\nfor i, fruit in enumerate(fruits):\n    print(f'{i}: {fruit}')",
   "enumerate() is preferred over range(len()) for iterating with indices. It's more Pythonic and less error-prone.",
   "SE: P6 — applies understanding of data types")

ex("Zip Two Lists", "Combine two lists into a list of tuples using zip().",
   "fundamentals", "lists", 1,
   "names = ['Alice', 'Bob', 'Charlie']\nscores = [85, 92, 78]\n# TODO: Zip them together\nprint(result)", "[('Alice', 85), ('Bob', 92), ('Charlie', 78)]",
   "Use the zip() built-in function.",
   "names = ['Alice', 'Bob', 'Charlie']\nscores = [85, 92, 78]\nresult = list(zip(names, scores))\nprint(result)",
   "zip() pairs elements from multiple iterables. It stops at the shortest iterable. Use itertools.zip_longest() to include all elements.",
   "SE: P6 — applies understanding of data types")

ex("Dictionary Comprehension", "Create a dictionary mapping numbers 1-5 to their squares using a comprehension.",
   "fundamentals", "dictionaries", 2,
   "# TODO: Create squares dict\nprint(squares)", "{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}",
   "Dict comprehensions use {key: value for item in iterable} syntax.",
   "squares = {n: n**2 for n in range(1, 6)}\nprint(squares)",
   "Dictionary comprehensions are a concise way to create dictionaries. They follow the same pattern as list comprehensions but produce key-value pairs.",
   "SE: P6 — applies understanding of data types")

ex("Unpack Nested Tuple", "Unpack a nested tuple structure into individual variables.",
   "fundamentals", "tuples", 2,
   "data = ('Yunshu', (2026, 3, 17), 'teacher')\n# TODO: Unpack into name, year, month, day, role\nprint(f'{name} is a {role}, date: {day}/{month}/{year}')",
   "Yunshu is a teacher, date: 17/3/2026",
   "Python supports nested unpacking in assignment.",
   "data = ('Yunshu', (2026, 3, 17), 'teacher')\nname, (year, month, day), role = data\nprint(f'{name} is a {role}, date: {day}/{month}/{year}')",
   "Python's destructuring assignment works with nested structures. The parentheses in the left side mirror the structure of the right side.",
   "SE: P6 — applies understanding of data types")

ex("F-String Formatting", "Use f-strings to format a number as currency with 2 decimal places and thousand separators.",
   "fundamentals", "strings", 2,
   "amount = 1234567.8\n# TODO: Format as currency\nprint(result)", "$1,234,567.80",
   "F-strings support format specifiers after a colon.",
   "amount = 1234567.8\nresult = f'${amount:,.2f}'\nprint(result)",
   "F-string format specs use : followed by format codes. The comma adds thousand separators, .2f means 2 decimal places as float.",
   "SE: P6 — applies understanding of data types")

ex("Multiple Return Values", "Write a function that returns the min, max, and average of a list.",
   "fundamentals", "functions_basics", 3,
   "def stats(numbers):\n    # TODO: Return min, max, average\n    pass\n\nresult = stats([4, 7, 2, 9, 1])\nprint(result)", "(1, 9, 4.6)",
   "Return a tuple of three values.",
   "def stats(numbers):\n    return min(numbers), max(numbers), sum(numbers)/len(numbers)\n\nresult = stats([4, 7, 2, 9, 1])\nprint(result)",
   "Python functions can return multiple values as a tuple. The caller can unpack them or use them as a single tuple.",
   "SE: P6 — applies understanding of data types")

ex("Walrus Operator", "Use the walrus operator := to find the first number greater than 10 in a list.",
   "fundamentals", "operators", 4,
   "numbers = [3, 7, 12, 5, 18, 2]\n# TODO: Use walrus operator to find first > 10\nprint(f'Found: {result}')", "Found: 12",
   "The walrus operator := assigns and returns a value in an expression.",
   "numbers = [3, 7, 12, 5, 18, 2]\nresult = next(n for n in numbers if (result := n) > 10)\nprint(f'Found: {result}')",
   "The walrus operator (:=) introduced in Python 3.8 allows assignment within expressions. It's useful in comprehensions, while loops, and conditional expressions.",
   "SE: P6 — applies understanding of data types")

ex("Type Checking", "Write a function that checks if an input is a number (int or float) and returns its square, or 'Not a number' otherwise.",
   "fundamentals", "type_casting", 2,
   "def safe_square(value):\n    # TODO: Check type and return square or error message\n    pass\n\nprint(safe_square(5))\nprint(safe_square('hello'))\nprint(safe_square(3.14))",
   "25\nNot a number\n9.8596",
   "Use isinstance() to check multiple types at once.",
   "def safe_square(value):\n    if isinstance(value, (int, float)):\n        return value ** 2\n    return 'Not a number'\n\nprint(safe_square(5))\nprint(safe_square('hello'))\nprint(safe_square(3.14))",
   "isinstance() is preferred over type() for type checking because it supports inheritance. Passing a tuple checks against multiple types.",
   "SE: P6 — applies understanding of data types")

ex("String Compression", "Compress a string by counting consecutive repeated characters. 'aaabbbcc' becomes 'a3b3c2'.",
   "fundamentals", "strings", 3,
   "def compress(s):\n    # TODO: Compress the string\n    pass\n\nprint(compress('aaabbbcc'))\nprint(compress('aabcccdd'))",
   "a3b3c2\na2b1c3d2",
   "Track the current character and its count as you iterate.",
   "def compress(s):\n    if not s:\n        return ''\n    result = []\n    count = 1\n    for i in range(1, len(s)):\n        if s[i] == s[i-1]:\n            count += 1\n        else:\n            result.append(f'{s[i-1]}{count}')\n            count = 1\n    result.append(f'{s[-1]}{count}')\n    return ''.join(result)\n\nprint(compress('aaabbbcc'))\nprint(compress('aabcccdd'))",
   "This is a classic string algorithm. Tracking consecutive characters requires comparing each character with the previous one and maintaining a counter.",
   "SE: P3 — designs algorithms")

# ============ CONTROL FLOW ============
ex("FizzBuzz", "Print numbers 1-20. For multiples of 3 print 'Fizz', multiples of 5 print 'Buzz', both print 'FizzBuzz'.",
   "control_flow", "conditionals", 1,
   "# TODO: FizzBuzz for 1-20", "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz",
   "Check for both (15) first, then 3, then 5.",
   "for i in range(1, 21):\n    if i % 15 == 0:\n        print('FizzBuzz')\n    elif i % 3 == 0:\n        print('Fizz')\n    elif i % 5 == 0:\n        print('Buzz')\n    else:\n        print(i)",
   "FizzBuzz is a classic interview problem. The key insight is checking the combined condition (% 15) before individual ones to avoid printing just 'Fizz' or 'Buzz' for numbers divisible by both.",
   "SE: P3 — designs algorithms")

ex("Grade Calculator", "Convert a numerical score (0-100) to a letter grade: A (90+), B (80-89), C (70-79), D (60-69), F (<60).",
   "control_flow", "conditionals", 1,
   "def get_grade(score):\n    # TODO: Return letter grade\n    pass\n\nfor s in [95, 83, 72, 61, 45]:\n    print(f'{s} -> {get_grade(s)}')",
   "95 -> A\n83 -> B\n72 -> C\n61 -> D\n45 -> F",
   "Use if/elif/else chain checking from highest to lowest.",
   "def get_grade(score):\n    if score >= 90:\n        return 'A'\n    elif score >= 80:\n        return 'B'\n    elif score >= 70:\n        return 'C'\n    elif score >= 60:\n        return 'D'\n    else:\n        return 'F'\n\nfor s in [95, 83, 72, 61, 45]:\n    print(f'{s} -> {get_grade(s)}')",
   "When using elif chains for ranges, check from highest to lowest so each condition implicitly handles the upper bound of the next range.",
   "SE: P3 — designs algorithms")

ex("Pattern Printing - Triangle", "Print a right triangle pattern of stars with n rows.",
   "control_flow", "loops", 1,
   "n = 5\n# TODO: Print triangle\n", "*\n**\n***\n****\n*****",
   "Use string multiplication inside a loop.",
   "n = 5\nfor i in range(1, n + 1):\n    print('*' * i)",
   "String multiplication (*) repeats a string. This pattern is a building block for more complex patterns like diamonds and pyramids.",
   "SE: P3 — designs algorithms")

ex("Multiplication Table", "Print a multiplication table for numbers 1-5.",
   "control_flow", "nested_loops", 2,
   "# TODO: Print 5x5 multiplication table", "  1  2  3  4  5\n  2  4  6  8 10\n  3  6  9 12 15\n  4  8 12 16 20\n  5 10 15 20 25",
   "Use nested loops with formatted string output.",
   "for i in range(1, 6):\n    row = ''\n    for j in range(1, 6):\n        row += f'{i*j:3d}'\n    print(row)",
   "Nested loops generate all combinations of row and column. The format specifier :3d right-aligns numbers in a 3-character field.",
   "SE: P3 — designs algorithms")

ex("Collatz Sequence", "Generate the Collatz sequence from a starting number until it reaches 1. If even, divide by 2; if odd, multiply by 3 and add 1.",
   "control_flow", "while_loops", 2,
   "def collatz(n):\n    # TODO: Generate sequence\n    pass\n\nprint(collatz(6))", "[6, 3, 10, 5, 16, 8, 4, 2, 1]",
   "Use a while loop that continues until n equals 1.",
   "def collatz(n):\n    seq = [n]\n    while n != 1:\n        n = n // 2 if n % 2 == 0 else 3 * n + 1\n        seq.append(n)\n    return seq\n\nprint(collatz(6))",
   "The Collatz conjecture states that this sequence always reaches 1, but this hasn't been proven for all numbers. The ternary operator makes the even/odd logic concise.",
   "SE: P3 — designs algorithms")

ex("Prime Number Checker", "Write a function that checks if a number is prime.",
   "control_flow", "loops", 2,
   "def is_prime(n):\n    # TODO: Check if prime\n    pass\n\nfor n in [2, 7, 10, 13, 1]:\n    print(f'{n}: {is_prime(n)}')", "2: True\n7: True\n10: False\n13: True\n1: False",
   "Only check divisors up to the square root of n.",
   "def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n\nfor n in [2, 7, 10, 13, 1]:\n    print(f'{n}: {is_prime(n)}')",
   "Checking up to sqrt(n) is sufficient because if n has a factor larger than its square root, it must also have one smaller. This reduces time complexity from O(n) to O(sqrt(n)).",
   "SE: P3 — designs algorithms")

ex("Match-Case Statement", "Use Python's match-case to classify HTTP status codes into categories.",
   "control_flow", "match_case", 3,
   "def classify_status(code):\n    # TODO: Use match-case\n    pass\n\nfor code in [200, 301, 404, 500]:\n    print(f'{code}: {classify_status(code)}')",
   "200: Success\n301: Redirect\n404: Client Error\n500: Server Error",
   "Use match-case with range patterns or value guards.",
   "def classify_status(code):\n    match code // 100:\n        case 2:\n            return 'Success'\n        case 3:\n            return 'Redirect'\n        case 4:\n            return 'Client Error'\n        case 5:\n            return 'Server Error'\n        case _:\n            return 'Unknown'\n\nfor code in [200, 301, 404, 500]:\n    print(f'{code}: {classify_status(code)}')",
   "Match-case (Python 3.10+) provides structural pattern matching. Integer division by 100 groups HTTP codes by their category (2xx, 3xx, etc.).",
   "SE: P6 — applies understanding of control structures")

ex("Custom Exception", "Create a custom exception class and raise it when age is negative.",
   "control_flow", "exceptions", 3,
   "# TODO: Create NegativeAgeError and validate_age function\n\ntry:\n    validate_age(-5)\nexcept NegativeAgeError as e:\n    print(f'Error: {e}')\n\ntry:\n    result = validate_age(25)\n    print(f'Valid age: {result}')\nexcept NegativeAgeError as e:\n    print(f'Error: {e}')",
   "Error: Age cannot be negative: -5\nValid age: 25",
   "Inherit from ValueError or Exception.",
   "class NegativeAgeError(ValueError):\n    def __init__(self, age):\n        super().__init__(f'Age cannot be negative: {age}')\n        self.age = age\n\ndef validate_age(age):\n    if age < 0:\n        raise NegativeAgeError(age)\n    return age\n\ntry:\n    validate_age(-5)\nexcept NegativeAgeError as e:\n    print(f'Error: {e}')\n\ntry:\n    result = validate_age(25)\n    print(f'Valid age: {result}')\nexcept NegativeAgeError as e:\n    print(f'Error: {e}')",
   "Custom exceptions should inherit from a relevant built-in exception. Storing the problematic value as an attribute helps with error handling upstream.",
   "SE: P4 — applies testing and debugging")

ex("Context Manager", "Create a context manager that times code execution.",
   "control_flow", "context_managers", 5,
   "import time\n# TODO: Create Timer context manager\n\nwith Timer('test'):\n    time.sleep(0.1)\n    total = sum(range(1000000))",
   "test took 0.1",
   "Use __enter__ and __exit__ methods, or contextlib.",
   "import time\n\nclass Timer:\n    def __init__(self, name):\n        self.name = name\n    def __enter__(self):\n        self.start = time.time()\n        return self\n    def __exit__(self, *args):\n        elapsed = time.time() - self.start\n        print(f'{self.name} took {elapsed:.1f}')\n\nwith Timer('test'):\n    time.sleep(0.1)\n    total = sum(range(1000000))",
   "Context managers ensure cleanup code runs even if exceptions occur. __enter__ runs at the start of the with block, __exit__ at the end.",
   "SE: P6 — applies understanding of control structures")

ex("Retry Decorator", "Write a decorator that retries a function up to 3 times if it raises an exception.",
   "control_flow", "exceptions", 5,
   "import random\n# TODO: Create retry decorator\n\n@retry(max_attempts=3)\ndef unreliable():\n    if random.random() < 0.7:\n        raise ConnectionError('Network failed')\n    return 'Success!'\n\nresult = unreliable()\nprint(result)",
   "Attempt 1 failed: Network failed\nAttempt 2 failed: Network failed\nSuccess!",
   "The decorator should catch exceptions and loop.",
   "import random\nimport functools\n\ndef retry(max_attempts=3):\n    def decorator(func):\n        @functools.wraps(func)\n        def wrapper(*args, **kwargs):\n            for attempt in range(1, max_attempts + 1):\n                try:\n                    return func(*args, **kwargs)\n                except Exception as e:\n                    print(f'Attempt {attempt} failed: {e}')\n                    if attempt == max_attempts:\n                        raise\n        return wrapper\n    return decorator\n\nrandom.seed(42)\n\n@retry(max_attempts=3)\ndef unreliable():\n    if random.random() < 0.7:\n        raise ConnectionError('Network failed')\n    return 'Success!'\n\nresult = unreliable()\nprint(result)",
   "This is a parameterised decorator (three levels of nesting). functools.wraps preserves the original function's metadata. Re-raising on the last attempt propagates the error.",
   "SE: P4 — applies testing and debugging")

# ============ FUNCTIONS ============
ex("Default Parameters", "Write a function that greets a user with a customisable greeting and punctuation.",
   "functions", "parameters", 1,
   "def greet(name, greeting='Hello', punctuation='!'):\n    # TODO: Return formatted greeting\n    pass\n\nprint(greet('Alice'))\nprint(greet('Bob', 'Hi'))\nprint(greet('Charlie', 'Hey', '...'))",
   "Hello Alice!\nHi Bob!\nHey Charlie...",
   "Use f-string with the parameters.",
   "def greet(name, greeting='Hello', punctuation='!'):\n    return f'{greeting} {name}{punctuation}'\n\nprint(greet('Alice'))\nprint(greet('Bob', 'Hi'))\nprint(greet('Charlie', 'Hey', '...'))",
   "Default parameters make functions flexible. They're evaluated once at definition time — avoid mutable defaults like lists or dicts.",
   "SE: P6 — applies understanding of functions")

ex("Args and Kwargs", "Write a function that accepts any number of positional and keyword arguments and prints them.",
   "functions", "args_kwargs", 2,
   "def show_args(*args, **kwargs):\n    # TODO: Print args and kwargs\n    pass\n\nshow_args(1, 2, 3, name='Alice', age=25)",
   "Positional: (1, 2, 3)\nKeyword: {'name': 'Alice', 'age': 25}",
   "*args collects positional args as tuple, **kwargs as dict.",
   "def show_args(*args, **kwargs):\n    print(f'Positional: {args}')\n    print(f'Keyword: {kwargs}')\n\nshow_args(1, 2, 3, name='Alice', age=25)",
   "*args and **kwargs allow functions to accept arbitrary arguments. This is essential for writing wrapper functions and decorators.",
   "SE: P6 — applies understanding of functions")

ex("Lambda Sort", "Sort a list of tuples by the second element using a lambda function.",
   "functions", "lambda", 2,
   "students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('Diana', 95)]\n# TODO: Sort by score\nprint(students)",
   "[('Charlie', 78), ('Alice', 85), ('Bob', 92), ('Diana', 95)]",
   "Use sorted() with a key parameter.",
   "students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('Diana', 95)]\nstudents = sorted(students, key=lambda x: x[1])\nprint(students)",
   "Lambda functions are anonymous single-expression functions. They're commonly used as sort keys, filter predicates, and map transformations.",
   "SE: P6 — applies understanding of functions")

ex("Map and Filter", "Use map() to double numbers and filter() to keep only even results.",
   "functions", "map_filter", 2,
   "numbers = [1, 2, 3, 4, 5, 6, 7, 8]\n# TODO: Double all, then keep only those divisible by 4\nprint(result)",
   "[4, 8, 12, 16]",
   "Chain map() then filter(), or use a list comprehension.",
   "numbers = [1, 2, 3, 4, 5, 6, 7, 8]\ndoubled = map(lambda x: x * 2, numbers)\nresult = list(filter(lambda x: x % 4 == 0, doubled))\nprint(result)",
   "map() and filter() are functional programming tools. In practice, list comprehensions are often preferred for readability: [x*2 for x in numbers if x*2 % 4 == 0].",
   "SE: P6 — applies understanding of functions")

ex("Closure Counter", "Create a closure that maintains a running count.",
   "functions", "closures", 4,
   "def make_counter(start=0):\n    # TODO: Return a counter function\n    pass\n\ncounter = make_counter()\nprint(counter())  # 1\nprint(counter())  # 2\nprint(counter())  # 3\n\ncounter2 = make_counter(10)\nprint(counter2())  # 11",
   "1\n2\n3\n11",
   "Use nonlocal to modify the enclosed variable.",
   "def make_counter(start=0):\n    count = start\n    def counter():\n        nonlocal count\n        count += 1\n        return count\n    return counter\n\ncounter = make_counter()\nprint(counter())\nprint(counter())\nprint(counter())\n\ncounter2 = make_counter(10)\nprint(counter2())",
   "Closures capture variables from their enclosing scope. The nonlocal keyword is needed to modify (not just read) enclosed variables. Each call to make_counter creates an independent closure.",
   "SE: P6 — applies understanding of functions")

ex("Generator Function", "Write a generator that yields Fibonacci numbers up to a limit.",
   "functions", "generators", 3,
   "def fibonacci(limit):\n    # TODO: Yield Fibonacci numbers up to limit\n    pass\n\nprint(list(fibonacci(50)))",
   "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]",
   "Use yield instead of building a list. Track two previous values.",
   "def fibonacci(limit):\n    a, b = 0, 1\n    while a <= limit:\n        yield a\n        a, b = b, a + b\n\nprint(list(fibonacci(50)))",
   "Generators use yield to produce values lazily — they don't compute all values upfront. This is memory-efficient for large or infinite sequences.",
   "SE: P6 — applies understanding of functions")

ex("Decorator with Arguments", "Write a decorator that repeats a function's output n times.",
   "functions", "decorators", 5,
   "# TODO: Create repeat decorator\n\n@repeat(3)\ndef say_hello(name):\n    print(f'Hello {name}!')\n\nsay_hello('World')",
   "Hello World!\nHello World!\nHello World!",
   "You need three levels of nesting: decorator factory -> decorator -> wrapper.",
   "import functools\n\ndef repeat(n):\n    def decorator(func):\n        @functools.wraps(func)\n        def wrapper(*args, **kwargs):\n            for _ in range(n):\n                result = func(*args, **kwargs)\n            return result\n        return wrapper\n    return decorator\n\n@repeat(3)\ndef say_hello(name):\n    print(f'Hello {name}!')\n\nsay_hello('World')",
   "Parameterised decorators require an extra layer of nesting. The outermost function takes the parameter, returns the actual decorator, which returns the wrapper.",
   "SE: P6 — applies understanding of functions")

ex("Type Hints", "Add type hints to a function that processes student records.",
   "functions", "type_hints", 3,
   "# TODO: Add proper type hints\ndef process_students(students, min_score):\n    return [s for s in students if s['score'] >= min_score]\n\ndata = [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 72}]\nresult = process_students(data, 80)\nprint(result)",
   "[{'name': 'Alice', 'score': 85}]",
   "Use list, dict, and Union or TypedDict for complex types.",
   "from typing import TypedDict\n\nclass Student(TypedDict):\n    name: str\n    score: int\n\ndef process_students(students: list[Student], min_score: int) -> list[Student]:\n    return [s for s in students if s['score'] >= min_score]\n\ndata: list[Student] = [{'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 72}]\nresult = process_students(data, 80)\nprint(result)",
   "TypedDict defines the expected structure of dictionaries. Type hints don't enforce types at runtime but help with IDE support, documentation, and static analysis tools like mypy.",
   "SE: P6 — applies understanding of functions")

ex("Recursive Directory Size", "Write a recursive function to calculate the total size of nested items.",
   "functions", "recursion", 4,
   "def total_size(structure):\n    # TODO: Recursively sum all sizes\n    pass\n\nfiles = {\n    'type': 'dir', 'name': 'root',\n    'children': [\n        {'type': 'file', 'name': 'a.txt', 'size': 100},\n        {'type': 'dir', 'name': 'sub', 'children': [\n            {'type': 'file', 'name': 'b.txt', 'size': 200},\n            {'type': 'file', 'name': 'c.txt', 'size': 300}\n        ]}\n    ]\n}\nprint(total_size(files))",
   "600",
   "Check if item is a file (return size) or dir (recurse into children).",
   "def total_size(structure):\n    if structure['type'] == 'file':\n        return structure['size']\n    return sum(total_size(child) for child in structure.get('children', []))\n\nfiles = {\n    'type': 'dir', 'name': 'root',\n    'children': [\n        {'type': 'file', 'name': 'a.txt', 'size': 100},\n        {'type': 'dir', 'name': 'sub', 'children': [\n            {'type': 'file', 'name': 'b.txt', 'size': 200},\n            {'type': 'file', 'name': 'c.txt', 'size': 300}\n        ]}\n    ]\n}\nprint(total_size(files))",
   "Tree traversal is a natural fit for recursion. The base case is a file (leaf node), and the recursive case sums children of directories (branch nodes).",
   "SE: P3 — designs algorithms")

# ============ DATA STRUCTURES ============
ex("Stack Implementation", "Implement a stack with push, pop, peek, and is_empty methods.",
   "data_structures", "stacks", 2,
   "class Stack:\n    # TODO: Implement stack\n    pass\n\ns = Stack()\ns.push(1)\ns.push(2)\ns.push(3)\nprint(s.peek())\nprint(s.pop())\nprint(s.pop())\nprint(s.is_empty())",
   "3\n3\n2\nFalse",
   "Use a list as the underlying storage.",
   "class Stack:\n    def __init__(self):\n        self._items = []\n    def push(self, item):\n        self._items.append(item)\n    def pop(self):\n        return self._items.pop()\n    def peek(self):\n        return self._items[-1]\n    def is_empty(self):\n        return len(self._items) == 0\n\ns = Stack()\ns.push(1)\ns.push(2)\ns.push(3)\nprint(s.peek())\nprint(s.pop())\nprint(s.pop())\nprint(s.is_empty())",
   "A stack is a LIFO (Last In, First Out) data structure. Python lists already support stack operations with append() and pop(), but wrapping them in a class provides a clean interface.",
   "SE: P6 — applies understanding of data structures")

ex("Queue Implementation", "Implement a queue using collections.deque with enqueue, dequeue, and size methods.",
   "data_structures", "queues", 2,
   "from collections import deque\n\nclass Queue:\n    # TODO: Implement queue\n    pass\n\nq = Queue()\nq.enqueue('A')\nq.enqueue('B')\nq.enqueue('C')\nprint(q.dequeue())\nprint(q.size())\nprint(q.dequeue())",
   "A\n2\nB",
   "deque is more efficient than list for queue operations.",
   "from collections import deque\n\nclass Queue:\n    def __init__(self):\n        self._items = deque()\n    def enqueue(self, item):\n        self._items.append(item)\n    def dequeue(self):\n        return self._items.popleft()\n    def size(self):\n        return len(self._items)\n\nq = Queue()\nq.enqueue('A')\nq.enqueue('B')\nq.enqueue('C')\nprint(q.dequeue())\nprint(q.size())\nprint(q.dequeue())",
   "A queue is FIFO (First In, First Out). deque.popleft() is O(1) whereas list.pop(0) is O(n), making deque the correct choice for queue implementations.",
   "SE: P6 — applies understanding of data structures")

ex("Linked List", "Implement a singly linked list with append, display, and length methods.",
   "data_structures", "linked_lists", 3,
   "class Node:\n    def __init__(self, data):\n        self.data = data\n        self.next = None\n\nclass LinkedList:\n    # TODO: Implement linked list\n    pass\n\nll = LinkedList()\nll.append(10)\nll.append(20)\nll.append(30)\nll.display()\nprint(f'Length: {ll.length()}')",
   "10 -> 20 -> 30 -> None\nLength: 3",
   "Track head node. Traverse to find the tail for append.",
   "class Node:\n    def __init__(self, data):\n        self.data = data\n        self.next = None\n\nclass LinkedList:\n    def __init__(self):\n        self.head = None\n    def append(self, data):\n        new_node = Node(data)\n        if not self.head:\n            self.head = new_node\n            return\n        current = self.head\n        while current.next:\n            current = current.next\n        current.next = new_node\n    def display(self):\n        current = self.head\n        parts = []\n        while current:\n            parts.append(str(current.data))\n            current = current.next\n        print(' -> '.join(parts) + ' -> None')\n    def length(self):\n        count = 0\n        current = self.head\n        while current:\n            count += 1\n            current = current.next\n        return count\n\nll = LinkedList()\nll.append(10)\nll.append(20)\nll.append(30)\nll.display()\nprint(f'Length: {ll.length()}')",
   "Linked lists store elements in nodes connected by references. Unlike arrays, they allow O(1) insertion at known positions but require O(n) access by index.",
   "SE: P6 — applies understanding of data structures")

ex("Binary Search Tree", "Implement a BST with insert and in-order traversal.",
   "data_structures", "trees", 4,
   "class BSTNode:\n    def __init__(self, value):\n        self.value = value\n        self.left = None\n        self.right = None\n\nclass BST:\n    # TODO: Implement insert and inorder\n    pass\n\ntree = BST()\nfor val in [5, 3, 7, 1, 4, 6, 8]:\n    tree.insert(val)\nprint(tree.inorder())",
   "[1, 3, 4, 5, 6, 7, 8]",
   "Insert: go left if smaller, right if larger. Inorder: left, root, right.",
   "class BSTNode:\n    def __init__(self, value):\n        self.value = value\n        self.left = None\n        self.right = None\n\nclass BST:\n    def __init__(self):\n        self.root = None\n    def insert(self, value):\n        if not self.root:\n            self.root = BSTNode(value)\n        else:\n            self._insert(self.root, value)\n    def _insert(self, node, value):\n        if value < node.value:\n            if node.left is None:\n                node.left = BSTNode(value)\n            else:\n                self._insert(node.left, value)\n        else:\n            if node.right is None:\n                node.right = BSTNode(value)\n            else:\n                self._insert(node.right, value)\n    def inorder(self):\n        result = []\n        self._inorder(self.root, result)\n        return result\n    def _inorder(self, node, result):\n        if node:\n            self._inorder(node.left, result)\n            result.append(node.value)\n            self._inorder(node.right, result)\n\ntree = BST()\nfor val in [5, 3, 7, 1, 4, 6, 8]:\n    tree.insert(val)\nprint(tree.inorder())",
   "BSTs maintain sorted order: left < root < right. In-order traversal visits nodes in ascending order. Average operations are O(log n) but degrade to O(n) if unbalanced.",
   "SE: P6 — applies understanding of data structures")

ex("Graph Adjacency List", "Implement an undirected graph using an adjacency list with add_vertex, add_edge, and get_neighbours.",
   "data_structures", "graphs", 4,
   "class Graph:\n    # TODO: Implement graph\n    pass\n\ng = Graph()\nfor v in ['A', 'B', 'C', 'D']:\n    g.add_vertex(v)\ng.add_edge('A', 'B')\ng.add_edge('A', 'C')\ng.add_edge('B', 'D')\nprint(g.get_neighbours('A'))\nprint(g.get_neighbours('B'))",
   "['B', 'C']\n['A', 'D']",
   "Use a dictionary mapping vertices to lists of neighbours.",
   "class Graph:\n    def __init__(self):\n        self.adj = {}\n    def add_vertex(self, v):\n        if v not in self.adj:\n            self.adj[v] = []\n    def add_edge(self, v1, v2):\n        self.adj[v1].append(v2)\n        self.adj[v2].append(v1)\n    def get_neighbours(self, v):\n        return self.adj.get(v, [])\n\ng = Graph()\nfor v in ['A', 'B', 'C', 'D']:\n    g.add_vertex(v)\ng.add_edge('A', 'B')\ng.add_edge('A', 'C')\ng.add_edge('B', 'D')\nprint(g.get_neighbours('A'))\nprint(g.get_neighbours('B'))",
   "Adjacency lists are space-efficient for sparse graphs. For undirected graphs, each edge is stored twice (once for each vertex). Dictionary-based implementation allows O(1) vertex lookup.",
   "SE: P6 — applies understanding of data structures")

ex("Priority Queue with Heap", "Implement a priority queue using heapq for task scheduling.",
   "data_structures", "heaps", 4,
   "import heapq\n\nclass PriorityQueue:\n    # TODO: Implement with heapq\n    pass\n\npq = PriorityQueue()\npq.add_task('low priority', 5)\npq.add_task('high priority', 1)\npq.add_task('medium priority', 3)\nprint(pq.get_task())\nprint(pq.get_task())\nprint(pq.get_task())",
   "high priority\nmedium priority\nlow priority",
   "heapq is a min-heap, so lower numbers = higher priority.",
   "import heapq\n\nclass PriorityQueue:\n    def __init__(self):\n        self._heap = []\n        self._counter = 0\n    def add_task(self, task, priority):\n        heapq.heappush(self._heap, (priority, self._counter, task))\n        self._counter += 1\n    def get_task(self):\n        return heapq.heappop(self._heap)[2]\n\npq = PriorityQueue()\npq.add_task('low priority', 5)\npq.add_task('high priority', 1)\npq.add_task('medium priority', 3)\nprint(pq.get_task())\nprint(pq.get_task())\nprint(pq.get_task())",
   "The counter serves as a tiebreaker when priorities are equal, ensuring FIFO order among same-priority items. Without it, Python would try to compare the task strings, which could fail.",
   "SE: P6 — applies understanding of data structures")

ex("Named Tuple", "Use namedtuple to create a Point type with x, y coordinates and a distance method.",
   "data_structures", "named_tuples", 3,
   "from collections import namedtuple\nimport math\n\n# TODO: Create Point namedtuple and distance function\n\np1 = Point(3, 4)\np2 = Point(0, 0)\nprint(f'Point: {p1}')\nprint(f'Distance from origin: {distance(p2, p1)}')",
   "Point: Point(x=3, y=4)\nDistance from origin: 5.0",
   "namedtuple creates immutable objects with named fields.",
   "from collections import namedtuple\nimport math\n\nPoint = namedtuple('Point', ['x', 'y'])\n\ndef distance(p1, p2):\n    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)\n\np1 = Point(3, 4)\np2 = Point(0, 0)\nprint(f'Point: {p1}')\nprint(f'Distance from origin: {distance(p2, p1)}')",
   "Named tuples provide lightweight, immutable objects with named field access. They're more readable than regular tuples and more memory-efficient than full classes.",
   "SE: P6 — applies understanding of data structures")

ex("Matrix Operations", "Implement matrix addition and multiplication for 2D lists.",
   "data_structures", "matrices", 4,
   "def matrix_add(a, b):\n    # TODO: Add two matrices\n    pass\n\ndef matrix_multiply(a, b):\n    # TODO: Multiply two matrices\n    pass\n\nm1 = [[1, 2], [3, 4]]\nm2 = [[5, 6], [7, 8]]\nprint(matrix_add(m1, m2))\nprint(matrix_multiply(m1, m2))",
   "[[6, 8], [10, 12]]\n[[19, 22], [43, 50]]",
   "Addition is element-wise. Multiplication uses dot product of rows and columns.",
   "def matrix_add(a, b):\n    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]\n\ndef matrix_multiply(a, b):\n    rows_a, cols_b, cols_a = len(a), len(b[0]), len(a[0])\n    result = [[0] * cols_b for _ in range(rows_a)]\n    for i in range(rows_a):\n        for j in range(cols_b):\n            for k in range(cols_a):\n                result[i][j] += a[i][k] * b[k][j]\n    return result\n\nm1 = [[1, 2], [3, 4]]\nm2 = [[5, 6], [7, 8]]\nprint(matrix_add(m1, m2))\nprint(matrix_multiply(m1, m2))",
   "Matrix multiplication requires three nested loops: row of A × column of B. The time complexity is O(n³). For production use, numpy is significantly faster.",
   "SE: P3 — designs algorithms")

# ============ OOP ============
ex("Bank Account Class", "Create a BankAccount class with deposit, withdraw, and balance checking.",
   "oop", "classes", 2,
   "class BankAccount:\n    # TODO: Implement\n    pass\n\nacc = BankAccount('Alice', 1000)\nacc.deposit(500)\nprint(acc.get_balance())\nacc.withdraw(200)\nprint(acc.get_balance())\nacc.withdraw(2000)",
   "1500\n1300\nInsufficient funds",
   "Use an instance variable for balance. Check for sufficient funds.",
   "class BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self._balance = balance\n    def deposit(self, amount):\n        self._balance += amount\n    def withdraw(self, amount):\n        if amount > self._balance:\n            print('Insufficient funds')\n            return\n        self._balance -= amount\n    def get_balance(self):\n        return self._balance\n\nacc = BankAccount('Alice', 1000)\nacc.deposit(500)\nprint(acc.get_balance())\nacc.withdraw(200)\nprint(acc.get_balance())\nacc.withdraw(2000)",
   "The underscore prefix (_balance) indicates a private attribute by convention. Methods provide controlled access to the balance, preventing direct manipulation.",
   "SE: P6 — applies understanding of OOP")

ex("Inheritance - Shapes", "Create a Shape base class with area() and Circle/Rectangle subclasses.",
   "oop", "inheritance", 3,
   "import math\n\nclass Shape:\n    # TODO: Base class\n    pass\n\nclass Circle(Shape):\n    # TODO: Implement\n    pass\n\nclass Rectangle(Shape):\n    # TODO: Implement\n    pass\n\nc = Circle(5)\nr = Rectangle(4, 6)\nprint(f'Circle area: {c.area():.2f}')\nprint(f'Rectangle area: {r.area():.2f}')\nprint(c)\nprint(r)",
   "Circle area: 78.54\nRectangle area: 24.00\nCircle(radius=5)\nRectangle(width=4, height=6)",
   "Override area() in each subclass. Use __repr__ for string representation.",
   "import math\n\nclass Shape:\n    def area(self):\n        raise NotImplementedError\n\nclass Circle(Shape):\n    def __init__(self, radius):\n        self.radius = radius\n    def area(self):\n        return math.pi * self.radius ** 2\n    def __repr__(self):\n        return f'Circle(radius={self.radius})'\n\nclass Rectangle(Shape):\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    def area(self):\n        return self.width * self.height\n    def __repr__(self):\n        return f'Rectangle(width={self.width}, height={self.height})'\n\nc = Circle(5)\nr = Rectangle(4, 6)\nprint(f'Circle area: {c.area():.2f}')\nprint(f'Rectangle area: {r.area():.2f}')\nprint(c)\nprint(r)",
   "This demonstrates polymorphism — both shapes have area() but implement it differently. NotImplementedError in the base class enforces that subclasses must override the method.",
   "SE: P6 — applies understanding of OOP")

ex("Dataclass", "Use @dataclass to create a Student record with automatic __init__, __repr__, and comparison.",
   "oop", "dataclasses", 3,
   "from dataclasses import dataclass, field\n\n# TODO: Create Student dataclass\n\ns1 = Student('Alice', 85, 'Y10')\ns2 = Student('Bob', 92, 'Y10')\ns3 = Student('Alice', 85, 'Y10')\nprint(s1)\nprint(s1 == s3)\nprint(sorted([s2, s1], key=lambda s: s.score))",
   "Student(name='Alice', score=85, year='Y10')\nTrue\n[Student(name='Alice', score=85, year='Y10'), Student(name='Bob', score=92, year='Y10')]",
   "Use @dataclass(eq=True) for automatic equality.",
   "from dataclasses import dataclass, field\n\n@dataclass\nclass Student:\n    name: str\n    score: int\n    year: str\n\ns1 = Student('Alice', 85, 'Y10')\ns2 = Student('Bob', 92, 'Y10')\ns3 = Student('Alice', 85, 'Y10')\nprint(s1)\nprint(s1 == s3)\nprint(sorted([s2, s1], key=lambda s: s.score))",
   "Dataclasses auto-generate __init__, __repr__, and __eq__ from type-annotated fields. They reduce boilerplate significantly compared to regular classes.",
   "SE: P6 — applies understanding of OOP")

ex("Property Decorator", "Use @property to create a Temperature class that validates Celsius values and provides Fahrenheit conversion.",
   "oop", "properties", 4,
   "class Temperature:\n    # TODO: Use @property for celsius and fahrenheit\n    pass\n\nt = Temperature(25)\nprint(f'{t.celsius}°C = {t.fahrenheit}°F')\nt.celsius = 100\nprint(f'{t.celsius}°C = {t.fahrenheit}°F')\ntry:\n    t.celsius = -300\nexcept ValueError as e:\n    print(e)",
   "25°C = 77.0°F\n100°C = 212.0°F\nTemperature below absolute zero",
   "Use @property for getter, @name.setter for setter with validation.",
   "class Temperature:\n    def __init__(self, celsius):\n        self.celsius = celsius\n    @property\n    def celsius(self):\n        return self._celsius\n    @celsius.setter\n    def celsius(self, value):\n        if value < -273.15:\n            raise ValueError('Temperature below absolute zero')\n        self._celsius = value\n    @property\n    def fahrenheit(self):\n        return self._celsius * 9/5 + 32\n\nt = Temperature(25)\nprint(f'{t.celsius}°C = {t.fahrenheit}°F')\nt.celsius = 100\nprint(f'{t.celsius}°C = {t.fahrenheit}°F')\ntry:\n    t.celsius = -300\nexcept ValueError as e:\n    print(e)",
   "Properties allow attribute-like access with getter/setter logic. The setter validates input before storage, and computed properties (fahrenheit) derive from stored data.",
   "SE: P6 — applies understanding of OOP")

ex("Abstract Base Class", "Create an abstract Animal class that forces subclasses to implement speak() and move().",
   "oop", "abstract_classes", 4,
   "from abc import ABC, abstractmethod\n\n# TODO: Create Animal ABC and Dog/Bird subclasses\n\ndog = Dog('Rex')\nbird = Bird('Tweety')\nfor animal in [dog, bird]:\n    print(f'{animal.name}: {animal.speak()}, {animal.move()}')",
   "Rex: Woof!, Runs\nTweety: Tweet!, Flies",
   "Use ABC and @abstractmethod from the abc module.",
   "from abc import ABC, abstractmethod\n\nclass Animal(ABC):\n    def __init__(self, name):\n        self.name = name\n    @abstractmethod\n    def speak(self):\n        pass\n    @abstractmethod\n    def move(self):\n        pass\n\nclass Dog(Animal):\n    def speak(self):\n        return 'Woof!'\n    def move(self):\n        return 'Runs'\n\nclass Bird(Animal):\n    def speak(self):\n        return 'Tweet!'\n    def move(self):\n        return 'Flies'\n\ndog = Dog('Rex')\nbird = Bird('Tweety')\nfor animal in [dog, bird]:\n    print(f'{animal.name}: {animal.speak()}, {animal.move()}')",
   "Abstract base classes define interfaces that subclasses must implement. Attempting to instantiate an ABC directly raises TypeError. This enforces a contract across the class hierarchy.",
   "SE: P6 — applies understanding of OOP")

ex("Dunder Methods", "Implement __add__, __len__, __contains__, and __iter__ for a custom Playlist class.",
   "oop", "dunder_methods", 5,
   "class Playlist:\n    # TODO: Implement with dunder methods\n    pass\n\np1 = Playlist('Rock', ['Song A', 'Song B'])\np2 = Playlist('Pop', ['Song C'])\np3 = p1 + p2\nprint(len(p3))\nprint('Song A' in p3)\nfor song in p3:\n    print(song)",
   "3\nTrue\nSong A\nSong B\nSong C",
   "Each dunder method maps to a Python operator or built-in function.",
   "class Playlist:\n    def __init__(self, name, songs=None):\n        self.name = name\n        self.songs = list(songs) if songs else []\n    def __add__(self, other):\n        return Playlist(f'{self.name} + {other.name}', self.songs + other.songs)\n    def __len__(self):\n        return len(self.songs)\n    def __contains__(self, song):\n        return song in self.songs\n    def __iter__(self):\n        return iter(self.songs)\n\np1 = Playlist('Rock', ['Song A', 'Song B'])\np2 = Playlist('Pop', ['Song C'])\np3 = p1 + p2\nprint(len(p3))\nprint('Song A' in p3)\nfor song in p3:\n    print(song)",
   "Dunder methods let custom classes work with Python operators. __add__ enables +, __len__ enables len(), __contains__ enables 'in', and __iter__ enables for loops.",
   "SE: P6 — applies understanding of OOP")

ex("Singleton Pattern", "Implement the Singleton design pattern to ensure only one database connection exists.",
   "oop", "design_patterns", 6,
   "class Database:\n    # TODO: Implement singleton\n    pass\n\ndb1 = Database()\ndb2 = Database()\nprint(db1 is db2)\nprint(db1.connection)\nprint(db2.connection)",
   "True\nConnected\nConnected",
   "Override __new__ to control instance creation.",
   "class Database:\n    _instance = None\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n            cls._instance.connection = 'Connected'\n        return cls._instance\n\ndb1 = Database()\ndb2 = Database()\nprint(db1 is db2)\nprint(db1.connection)\nprint(db2.connection)",
   "The Singleton pattern ensures a class has exactly one instance. __new__ controls object creation before __init__ runs. This is useful for shared resources like database connections or configuration.",
   "EC: H5.2 — describes the features of software")

# ============ ALGORITHMS ============
ex("Binary Search", "Implement binary search to find a target in a sorted list.",
   "algorithms", "searching", 2,
   "def binary_search(arr, target):\n    # TODO: Implement binary search\n    pass\n\nnums = [1, 3, 5, 7, 9, 11, 13, 15]\nprint(binary_search(nums, 7))\nprint(binary_search(nums, 6))",
   "3\n-1",
   "Maintain low and high pointers, check the middle element.",
   "def binary_search(arr, target):\n    low, high = 0, len(arr) - 1\n    while low <= high:\n        mid = (low + high) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            low = mid + 1\n        else:\n            high = mid - 1\n    return -1\n\nnums = [1, 3, 5, 7, 9, 11, 13, 15]\nprint(binary_search(nums, 7))\nprint(binary_search(nums, 6))",
   "Binary search halves the search space each iteration, giving O(log n) time complexity. It requires sorted input. This is dramatically faster than linear search for large datasets.",
   "SE: P3 — designs algorithms")

ex("Bubble Sort", "Implement bubble sort with early termination if no swaps occur.",
   "algorithms", "sorting", 2,
   "def bubble_sort(arr):\n    # TODO: Implement optimised bubble sort\n    pass\n\nnums = [64, 34, 25, 12, 22, 11, 90]\nbubble_sort(nums)\nprint(nums)",
   "[11, 12, 22, 25, 34, 64, 90]",
   "Use a swapped flag to detect if the list is already sorted.",
   "def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        swapped = False\n        for j in range(0, n - i - 1):\n            if arr[j] > arr[j + 1]:\n                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n                swapped = True\n        if not swapped:\n            break\n\nnums = [64, 34, 25, 12, 22, 11, 90]\nbubble_sort(nums)\nprint(nums)",
   "Bubble sort repeatedly swaps adjacent elements. The optimised version breaks early if no swaps occur in a pass. Time complexity is O(n²) worst case but O(n) best case with the flag.",
   "SE: P3 — designs algorithms")

ex("Merge Sort", "Implement merge sort using divide and conquer.",
   "algorithms", "sorting", 4,
   "def merge_sort(arr):\n    # TODO: Implement merge sort\n    pass\n\nnums = [38, 27, 43, 3, 9, 82, 10]\nprint(merge_sort(nums))",
   "[3, 9, 10, 27, 38, 43, 82]",
   "Split in half recursively, then merge two sorted halves.",
   "def merge_sort(arr):\n    if len(arr) <= 1:\n        return arr\n    mid = len(arr) // 2\n    left = merge_sort(arr[:mid])\n    right = merge_sort(arr[mid:])\n    return merge(left, right)\n\ndef merge(left, right):\n    result = []\n    i = j = 0\n    while i < len(left) and j < len(right):\n        if left[i] <= right[j]:\n            result.append(left[i])\n            i += 1\n        else:\n            result.append(right[j])\n            j += 1\n    result.extend(left[i:])\n    result.extend(right[j:])\n    return result\n\nnums = [38, 27, 43, 3, 9, 82, 10]\nprint(merge_sort(nums))",
   "Merge sort is a divide-and-conquer algorithm with guaranteed O(n log n) time complexity. It's stable (preserves order of equal elements) but requires O(n) extra space.",
   "SE: P3 — designs algorithms")

ex("BFS Graph Traversal", "Implement breadth-first search to find the shortest path between two nodes.",
   "algorithms", "graph_algorithms", 5,
   "from collections import deque\n\ndef bfs_path(graph, start, end):\n    # TODO: Find shortest path using BFS\n    pass\n\ngraph = {\n    'A': ['B', 'C'],\n    'B': ['A', 'D', 'E'],\n    'C': ['A', 'F'],\n    'D': ['B'],\n    'E': ['B', 'F'],\n    'F': ['C', 'E']\n}\nprint(bfs_path(graph, 'A', 'F'))",
   "['A', 'C', 'F']",
   "Use a queue and track the path by storing parent references.",
   "from collections import deque\n\ndef bfs_path(graph, start, end):\n    queue = deque([(start, [start])])\n    visited = {start}\n    while queue:\n        node, path = queue.popleft()\n        if node == end:\n            return path\n        for neighbour in graph[node]:\n            if neighbour not in visited:\n                visited.add(neighbour)\n                queue.append((neighbour, path + [neighbour]))\n    return None\n\ngraph = {\n    'A': ['B', 'C'],\n    'B': ['A', 'D', 'E'],\n    'C': ['A', 'F'],\n    'D': ['B'],\n    'E': ['B', 'F'],\n    'F': ['C', 'E']\n}\nprint(bfs_path(graph, 'A', 'F'))",
   "BFS explores nodes level by level, guaranteeing the shortest path in unweighted graphs. Storing the full path with each node simplifies path reconstruction.",
   "SE: P3 — designs algorithms")

ex("Dynamic Programming - Fibonacci", "Calculate the nth Fibonacci number using memoisation.",
   "algorithms", "dynamic_programming", 3,
   "def fib(n, memo={}):\n    # TODO: Implement with memoisation\n    pass\n\nprint(fib(10))\nprint(fib(50))",
   "55\n12586269025",
   "Store computed results in a dictionary to avoid redundant calculations.",
   "def fib(n, memo={}):\n    if n in memo:\n        return memo[n]\n    if n <= 1:\n        return n\n    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)\n    return memo[n]\n\nprint(fib(10))\nprint(fib(50))",
   "Memoisation transforms O(2^n) recursive Fibonacci into O(n) by caching results. Using a default mutable argument as memo is a common Python trick — the dict persists across calls.",
   "SE: P3 — designs algorithms")

# ============ FILE HANDLING ============
ex("Read and Count Lines", "Read a text file and count the number of lines, words, and characters.",
   "file_handling", "reading", 1,
   "# TODO: Create a sample file and count its contents\n# Write sample text first, then read and count",
   "Lines: 3\nWords: 9\nCharacters: 45",
   "Use with open() and iterate over lines.",
   "# Create sample file\nwith open('sample.txt', 'w') as f:\n    f.write('Hello World\\nPython is great\\nKeep learning')\n\n# Count contents\nwith open('sample.txt', 'r') as f:\n    text = f.read()\n    lines = text.strip().split('\\n')\n    words = text.split()\n    chars = len(text.strip())\n    print(f'Lines: {len(lines)}')\n    print(f'Words: {len(words)}')\n    print(f'Characters: {chars}')\n\nimport os\nos.remove('sample.txt')",
   "The with statement ensures files are properly closed. split() without arguments splits on any whitespace, while split('\\n') splits on newlines specifically.",
   "SE: P6 — applies file handling")

ex("CSV Reader", "Read a CSV file and calculate the average of a numeric column.",
   "file_handling", "csv", 2,
   "import csv\n\n# TODO: Write sample CSV then read and calculate average score",
   "Average score: 85.0",
   "Use csv.DictReader for named column access.",
   "import csv, os\n\n# Create sample CSV\nwith open('scores.csv', 'w', newline='') as f:\n    writer = csv.writer(f)\n    writer.writerow(['name', 'score'])\n    writer.writerows([['Alice', 90], ['Bob', 80], ['Charlie', 85]])\n\n# Read and calculate\nwith open('scores.csv', 'r') as f:\n    reader = csv.DictReader(f)\n    scores = [int(row['score']) for row in reader]\n    print(f'Average score: {sum(scores)/len(scores)}')\n\nos.remove('scores.csv')",
   "csv.DictReader maps each row to a dictionary using the header row as keys. This is more readable than index-based access and self-documenting.",
   "SE: P6 — applies file handling")

ex("JSON Read/Write", "Read a JSON config file, modify a value, and write it back.",
   "file_handling", "json", 2,
   "import json\n\n# TODO: Create, read, modify, and write JSON",
   "Before: {'theme': 'light', 'font_size': 14}\nAfter: {'theme': 'dark', 'font_size': 16}",
   "Use json.load() to read and json.dump() to write.",
   "import json, os\n\nconfig = {'theme': 'light', 'font_size': 14}\nwith open('config.json', 'w') as f:\n    json.dump(config, f)\n\nwith open('config.json', 'r') as f:\n    data = json.load(f)\n    print(f'Before: {data}')\n\ndata['theme'] = 'dark'\ndata['font_size'] = 16\n\nwith open('config.json', 'w') as f:\n    json.dump(data, f)\n\nwith open('config.json', 'r') as f:\n    print(f'After: {json.load(f)}')\n\nos.remove('config.json')",
   "json.load/dump work with file objects while json.loads/dumps work with strings. indent parameter in dump() makes the output human-readable.",
   "SE: P6 — applies file handling")

ex("Log File Parser", "Parse a log file to extract and count error types.",
   "file_handling", "text_processing", 4,
   "# TODO: Create sample log file, parse errors, show counts",
   "Error counts:\n  ConnectionError: 2\n  TimeoutError: 1\n  ValueError: 1",
   "Use string methods or regex to extract error types.",
   "import os\nfrom collections import Counter\n\nlog_data = '''2026-03-17 10:00:01 INFO Server started\n2026-03-17 10:00:05 ERROR ConnectionError: Failed to connect\n2026-03-17 10:00:10 WARNING Low memory\n2026-03-17 10:00:15 ERROR TimeoutError: Request timed out\n2026-03-17 10:00:20 ERROR ConnectionError: Connection refused\n2026-03-17 10:00:25 ERROR ValueError: Invalid input\n'''\n\nwith open('app.log', 'w') as f:\n    f.write(log_data)\n\nerrors = Counter()\nwith open('app.log', 'r') as f:\n    for line in f:\n        if 'ERROR' in line:\n            error_type = line.split('ERROR')[1].strip().split(':')[0]\n            errors[error_type] += 1\n\nprint('Error counts:')\nfor err, count in errors.most_common():\n    print(f'  {err}: {count}')\n\nos.remove('app.log')",
   "Counter from collections is perfect for counting occurrences. String splitting extracts structured data from semi-structured log formats. most_common() returns items in descending frequency order.",
   "SE: P4 — applies testing and debugging")

# ============ DATABASES ============
ex("SQLite Create and Insert", "Create a SQLite database with a students table and insert records.",
   "databases", "sqlite_basics", 1,
   "import sqlite3\n\n# TODO: Create database, table, insert students, query all",
   "(1, 'Alice', 85)\n(2, 'Bob', 92)\n(3, 'Charlie', 78)",
   "Use sqlite3.connect() with :memory: for testing.",
   "import sqlite3\n\nconn = sqlite3.connect(':memory:')\nc = conn.cursor()\nc.execute('CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, score INTEGER)')\nc.executemany('INSERT INTO students (name, score) VALUES (?, ?)',\n    [('Alice', 85), ('Bob', 92), ('Charlie', 78)])\nconn.commit()\n\nfor row in c.execute('SELECT * FROM students'):\n    print(row)\n\nconn.close()",
   "SQLite3 is built into Python — no installation needed. Using ? placeholders prevents SQL injection. :memory: creates an in-memory database perfect for testing.",
   "EC: H4.2 — uses SQL to create and modify databases")

ex("SQL Joins", "Use SQL JOIN to combine students and courses tables.",
   "databases", "joins", 3,
   "import sqlite3\n\n# TODO: Create two tables and join them",
   "Alice - Mathematics\nAlice - Physics\nBob - Mathematics\nCharlie - Physics",
   "Use INNER JOIN with a linking table or foreign key.",
   "import sqlite3\n\nconn = sqlite3.connect(':memory:')\nc = conn.cursor()\nc.execute('CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT)')\nc.execute('CREATE TABLE enrolments (student_id INTEGER, course TEXT)')\nc.executemany('INSERT INTO students VALUES (?, ?)', [(1,'Alice'),(2,'Bob'),(3,'Charlie')])\nc.executemany('INSERT INTO enrolments VALUES (?, ?)', [(1,'Mathematics'),(1,'Physics'),(2,'Mathematics'),(3,'Physics')])\nconn.commit()\n\nfor row in c.execute('''\n    SELECT s.name, e.course\n    FROM students s\n    INNER JOIN enrolments e ON s.id = e.student_id\n    ORDER BY s.name, e.course\n'''):\n    print(f'{row[0]} - {row[1]}')\n\nconn.close()",
   "INNER JOIN combines rows from two tables where the join condition is met. Table aliases (s, e) make queries more readable. This is fundamental to relational database queries.",
   "EC: H4.2 — uses SQL to query databases")

ex("Parameterised Queries", "Demonstrate safe vs unsafe SQL queries to prevent SQL injection.",
   "databases", "security", 3,
   "import sqlite3\n\n# TODO: Show safe parameterised query vs vulnerable string formatting",
   "Safe query result: [('Alice', 85)]\nNever use string formatting for SQL!",
   "Always use ? placeholders, never f-strings or .format().",
   "import sqlite3\n\nconn = sqlite3.connect(':memory:')\nc = conn.cursor()\nc.execute('CREATE TABLE users (name TEXT, score INTEGER)')\nc.executemany('INSERT INTO users VALUES (?, ?)', [('Alice', 85), ('Bob', 92)])\nconn.commit()\n\n# SAFE: Parameterised query\nname = 'Alice'\nc.execute('SELECT * FROM users WHERE name = ?', (name,))\nprint(f'Safe query result: {c.fetchall()}')\n\n# UNSAFE: Never do this!\n# query = f\"SELECT * FROM users WHERE name = '{name}'\"  # SQL INJECTION RISK!\nprint('Never use string formatting for SQL!')\n\nconn.close()",
   "Parameterised queries escape special characters automatically, preventing SQL injection attacks. This is a critical security practice — never concatenate user input into SQL strings.",
   "EC: H6.2 — describes security measures")

ex("Database CRUD Operations", "Implement full Create, Read, Update, Delete operations on a products table.",
   "databases", "crud", 3,
   "import sqlite3\n\n# TODO: Implement CRUD for products\n",
   "Created: [(1, 'Laptop', 999.99), (2, 'Mouse', 29.99), (3, 'Keyboard', 79.99)]\nUpdated: (2, 'Mouse', 24.99)\nAfter delete: [(1, 'Laptop', 999.99), (2, 'Mouse', 24.99)]",
   "Use INSERT, SELECT, UPDATE, DELETE with parameterised queries.",
   "import sqlite3\n\nconn = sqlite3.connect(':memory:')\nc = conn.cursor()\nc.execute('CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL)')\n\n# Create\nc.executemany('INSERT INTO products (name, price) VALUES (?, ?)',\n    [('Laptop', 999.99), ('Mouse', 29.99), ('Keyboard', 79.99)])\nconn.commit()\nprint(f'Created: {c.execute(\"SELECT * FROM products\").fetchall()}')\n\n# Update\nc.execute('UPDATE products SET price = ? WHERE name = ?', (24.99, 'Mouse'))\nconn.commit()\nprint(f'Updated: {c.execute(\"SELECT * FROM products WHERE name = ?\", (\"Mouse\",)).fetchone()}')\n\n# Delete\nc.execute('DELETE FROM products WHERE name = ?', ('Keyboard',))\nconn.commit()\nprint(f'After delete: {c.execute(\"SELECT * FROM products\").fetchall()}')\n\nconn.close()",
   "CRUD operations form the foundation of database interaction. Always commit after modifications and use parameterised queries for all user-supplied values.",
   "EC: H4.2 — uses SQL to create and modify databases")

# ============ WEB & API ============
ex("Simple Flask Route", "Create a basic Flask application with two routes.",
   "web_and_api", "flask", 2,
   "from flask import Flask, jsonify\n\napp = Flask(__name__)\n\n# TODO: Create routes for / and /api/hello\n\n# Don't actually run - just show the route functions\nwith app.test_client() as client:\n    print(client.get('/').data.decode())\n    print(client.get('/api/hello').data.decode())",
   "Welcome to my API!\n{\"message\":\"Hello, World!\"}",
   "Use @app.route decorator for each endpoint.",
   "from flask import Flask, jsonify\n\napp = Flask(__name__)\n\n@app.route('/')\ndef home():\n    return 'Welcome to my API!'\n\n@app.route('/api/hello')\ndef hello():\n    return jsonify(message='Hello, World!')\n\nwith app.test_client() as client:\n    r1 = client.get('/')\n    print(r1.data.decode().strip())\n    r2 = client.get('/api/hello')\n    import json\n    print(json.dumps(json.loads(r2.data), separators=(',',':')))",
   "Flask uses decorators to map URLs to functions. jsonify() creates proper JSON responses with correct Content-Type headers. The test_client allows testing without running the server.",
   "SE: P6 — applies web development concepts")

ex("REST API Design", "Design a REST API for a task manager with proper HTTP methods.",
   "web_and_api", "rest_api", 3,
   "from flask import Flask, jsonify, request\n\napp = Flask(__name__)\ntasks = []\n\n# TODO: Implement GET /tasks, POST /tasks, DELETE /tasks/<id>\n\nwith app.test_client() as client:\n    client.post('/tasks', json={'title': 'Learn Python'})\n    client.post('/tasks', json={'title': 'Build API'})\n    r = client.get('/tasks')\n    import json\n    print(json.dumps(json.loads(r.data), indent=2))",
   "[\n  {\n    \"id\": 1,\n    \"title\": \"Learn Python\"\n  },\n  {\n    \"id\": 2,\n    \"title\": \"Build API\"\n  }\n]",
   "GET to read, POST to create, DELETE to remove.",
   "from flask import Flask, jsonify, request\n\napp = Flask(__name__)\ntasks = []\nnext_id = 1\n\n@app.route('/tasks', methods=['GET'])\ndef get_tasks():\n    return jsonify(tasks)\n\n@app.route('/tasks', methods=['POST'])\ndef create_task():\n    global next_id\n    task = {'id': next_id, 'title': request.json['title']}\n    tasks.append(task)\n    next_id += 1\n    return jsonify(task), 201\n\n@app.route('/tasks/<int:task_id>', methods=['DELETE'])\ndef delete_task(task_id):\n    global tasks\n    tasks = [t for t in tasks if t['id'] != task_id]\n    return '', 204\n\nwith app.test_client() as client:\n    client.post('/tasks', json={'title': 'Learn Python'})\n    client.post('/tasks', json={'title': 'Build API'})\n    r = client.get('/tasks')\n    import json\n    print(json.dumps(json.loads(r.data), indent=2))",
   "REST APIs use HTTP methods semantically: GET reads, POST creates, PUT updates, DELETE removes. Status codes communicate outcomes: 200 OK, 201 Created, 204 No Content.",
   "SE: P6 — applies web development concepts")

# ============ DATA SCIENCE ============
ex("Basic Statistics", "Calculate mean, median, mode, and standard deviation without libraries.",
   "data_science", "statistics", 2,
   "def stats(data):\n    # TODO: Calculate mean, median, mode, std dev\n    pass\n\nnums = [4, 7, 2, 9, 4, 1, 4, 8, 3]\nresult = stats(nums)\nfor k, v in result.items():\n    print(f'{k}: {v}')",
   "mean: 4.67\nmedian: 4\nmode: 4\nstd_dev: 2.55",
   "Sort for median, count for mode, use the std dev formula.",
   "def stats(data):\n    n = len(data)\n    mean = sum(data) / n\n    sorted_d = sorted(data)\n    median = sorted_d[n//2] if n % 2 else (sorted_d[n//2-1] + sorted_d[n//2]) / 2\n    counts = {}\n    for x in data:\n        counts[x] = counts.get(x, 0) + 1\n    mode = max(counts, key=counts.get)\n    variance = sum((x - mean)**2 for x in data) / n\n    std_dev = variance ** 0.5\n    return {'mean': round(mean, 2), 'median': median, 'mode': mode, 'std_dev': round(std_dev, 2)}\n\nnums = [4, 7, 2, 9, 4, 1, 4, 8, 3]\nresult = stats(nums)\nfor k, v in result.items():\n    print(f'{k}: {v}')",
   "Understanding these calculations from scratch builds intuition before using libraries. Standard deviation measures spread — it's the square root of the average squared deviation from the mean.",
   "SE: P3 — designs algorithms")

ex("Data Visualisation with Matplotlib", "Create a bar chart showing student scores.",
   "data_science", "matplotlib", 2,
   "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\n\n# TODO: Create and save a bar chart\nprint('Chart saved to scores.png')",
   "Chart saved to scores.png",
   "Use plt.bar() for bar charts. Save with plt.savefig().",
   "import matplotlib\nmatplotlib.use('Agg')\nimport matplotlib.pyplot as plt\nimport os\n\nnames = ['Alice', 'Bob', 'Charlie', 'Diana']\nscores = [85, 92, 78, 95]\n\nplt.figure(figsize=(8, 5))\nplt.bar(names, scores, color=['#2196F3', '#4CAF50', '#FF9800', '#E91E63'])\nplt.title('Student Scores')\nplt.ylabel('Score')\nplt.ylim(0, 100)\nplt.tight_layout()\nplt.savefig('scores.png')\nprint('Chart saved to scores.png')\nos.remove('scores.png')",
   "Matplotlib is Python's most widely used plotting library. The Agg backend allows saving charts without a display. tight_layout() prevents labels from being cut off.",
   "SE: P6 — applies data presentation")

# ============ AUTOMATION & TESTING ============
ex("Unit Test Basics", "Write unit tests for a calculator function using unittest.",
   "automation_and_testing", "unittest", 2,
   "import unittest\n\ndef add(a, b):\n    return a + b\n\ndef divide(a, b):\n    if b == 0:\n        raise ValueError('Cannot divide by zero')\n    return a / b\n\n# TODO: Write TestCalculator class\n\nunittest.main(argv=[''], exit=False, verbosity=2)",
   "test_add ... ok\ntest_divide ... ok\ntest_divide_by_zero ... ok",
   "Use assertEqual, assertAlmostEqual, and assertRaises.",
   "import unittest\n\ndef add(a, b):\n    return a + b\n\ndef divide(a, b):\n    if b == 0:\n        raise ValueError('Cannot divide by zero')\n    return a / b\n\nclass TestCalculator(unittest.TestCase):\n    def test_add(self):\n        self.assertEqual(add(2, 3), 5)\n        self.assertEqual(add(-1, 1), 0)\n    def test_divide(self):\n        self.assertAlmostEqual(divide(10, 3), 3.333, places=2)\n    def test_divide_by_zero(self):\n        with self.assertRaises(ValueError):\n            divide(10, 0)\n\nunittest.main(argv=[''], exit=False, verbosity=2)",
   "Unit tests verify individual functions work correctly. assertRaises checks that exceptions are properly raised. Each test method should test one specific behaviour.",
   "SE: P4 — applies testing and debugging")

ex("Regex Email Validation", "Use regular expressions to validate email addresses.",
   "automation_and_testing", "regex", 3,
   "import re\n\ndef validate_email(email):\n    # TODO: Return True if valid email format\n    pass\n\ntest_emails = ['user@example.com', 'bad@', 'no-at-sign', 'ok@sub.domain.com', '@no-user.com']\nfor email in test_emails:\n    print(f'{email}: {validate_email(email)}')",
   "user@example.com: True\nbad@: False\nno-at-sign: False\nok@sub.domain.com: True\n@no-user.com: False",
   "Use re.match() with a pattern for local@domain.tld format.",
   "import re\n\ndef validate_email(email):\n    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'\n    return bool(re.match(pattern, email))\n\ntest_emails = ['user@example.com', 'bad@', 'no-at-sign', 'ok@sub.domain.com', '@no-user.com']\nfor email in test_emails:\n    print(f'{email}: {validate_email(email)}')",
   "Regex validation provides pattern matching for structured text. The ^ and $ anchors ensure the entire string matches. In production, use a library for email validation as the full spec is complex.",
   "SE: P4 — applies testing and debugging")

ex("Command-Line Tool with Argparse", "Create a CLI tool that accepts arguments for a greeting message.",
   "automation_and_testing", "argparse", 3,
   "import argparse\nimport sys\n\n# TODO: Create argument parser\n\nsys.argv = ['greet', '--name', 'Alice', '--greeting', 'Hi', '--repeat', '2']\n# Parse and use arguments",
   "Hi Alice!\nHi Alice!",
   "Use add_argument with type, default, and help parameters.",
   "import argparse\nimport sys\n\nparser = argparse.ArgumentParser(description='Greeting tool')\nparser.add_argument('--name', required=True, help='Name to greet')\nparser.add_argument('--greeting', default='Hello', help='Greeting word')\nparser.add_argument('--repeat', type=int, default=1, help='Times to repeat')\n\nsys.argv = ['greet', '--name', 'Alice', '--greeting', 'Hi', '--repeat', '2']\nargs = parser.parse_args()\n\nfor _ in range(args.repeat):\n    print(f'{args.greeting} {args.name}!')",
   "argparse handles argument parsing, type conversion, help text, and validation. Required arguments raise errors if missing. Default values make arguments optional.",
   "SE: P6 — applies software development tools")

# ============ SECURITY ============
ex("Password Hashing", "Hash and verify passwords using hashlib.",
   "security", "hashing", 3,
   "import hashlib\nimport os\n\n# TODO: Create hash_password and verify_password functions\n\nhashed = hash_password('mypassword123')\nprint(f'Hash: {hashed[:20]}...')\nprint(f'Verify correct: {verify_password(\"mypassword123\", hashed)}')\nprint(f'Verify wrong: {verify_password(\"wrongpassword\", hashed)}')",
   "Hash: ...\nVerify correct: True\nVerify wrong: False",
   "Use a random salt combined with the password before hashing.",
   "import hashlib\nimport os\n\ndef hash_password(password):\n    salt = os.urandom(32)\n    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)\n    return salt + key\n\ndef verify_password(password, stored):\n    salt = stored[:32]\n    stored_key = stored[32:]\n    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)\n    return key == stored_key\n\nhashed = hash_password('mypassword123')\nprint(f'Hash: {hashed.hex()[:20]}...')\nprint(f'Verify correct: {verify_password(\"mypassword123\", hashed)}')\nprint(f'Verify wrong: {verify_password(\"wrongpassword\", hashed)}')",
   "Never store passwords in plain text. PBKDF2 with a random salt and many iterations makes brute-force attacks impractical. The salt prevents rainbow table attacks.",
   "EC: H6.2 — describes security measures")

ex("Input Sanitisation", "Sanitise user input to prevent XSS and injection attacks.",
   "security", "input_validation", 2,
   "import html\n\ndef sanitise(user_input):\n    # TODO: Sanitise input for safe HTML display\n    pass\n\nmalicious = '<script>alert(\"XSS\")</script>'\nsafe = sanitise(malicious)\nprint(f'Original: {malicious}')\nprint(f'Sanitised: {safe}')\n\nsql_attempt = \"'; DROP TABLE users; --\"\nprint(f'SQL attempt sanitised: {sanitise(sql_attempt)}')",
   "Original: <script>alert(\"XSS\")</script>\nSanitised: &lt;script&gt;alert(&quot;XSS&quot;)&lt;/script&gt;\nSQL attempt sanitised: &#x27;; DROP TABLE users; --",
   "Use html.escape() to convert special characters to HTML entities.",
   "import html\n\ndef sanitise(user_input):\n    return html.escape(user_input, quote=True)\n\nmalicious = '<script>alert(\"XSS\")</script>'\nsafe = sanitise(malicious)\nprint(f'Original: {malicious}')\nprint(f'Sanitised: {safe}')\n\nsql_attempt = \"'; DROP TABLE users; --\"\nprint(f'SQL attempt sanitised: {sanitise(sql_attempt)}')",
   "html.escape() converts <, >, &, and quotes to HTML entities, preventing XSS. For SQL, always use parameterised queries instead of sanitising strings.",
   "EC: H6.2 — describes security measures")

ex("Secure Random Token", "Generate cryptographically secure tokens for API keys and session IDs.",
   "security", "tokens", 2,
   "import secrets\n\n# TODO: Generate various types of secure tokens\n",
   "Hex token: (32 char hex string)\nURL-safe token: (43 char base64 string)\nAPI key: (length > 20)",
   "Use the secrets module, not random.",
   "import secrets\n\nhex_token = secrets.token_hex(16)\nprint(f'Hex token: {hex_token}')\n\nurl_token = secrets.token_urlsafe(32)\nprint(f'URL-safe token: {url_token}')\n\napi_key = f'sk-{secrets.token_urlsafe(24)}'\nprint(f'API key: {api_key}')",
   "The secrets module provides cryptographically strong random numbers suitable for security. Never use the random module for security purposes — it's predictable. token_urlsafe produces URL-safe base64 strings.",
   "EC: H6.2 — describes security measures")

# Save to file
all_exercises = existing + exercises
# Renumber all
for i, e in enumerate(all_exercises):
    e['id'] = f'PY-{i+1:04d}'

with open('data/python_exercises.json', 'w', encoding='utf-8') as f:
    json.dump(all_exercises, f, indent=2, ensure_ascii=False)

print(f'Total exercises: {len(all_exercises)}')

# Category breakdown
cats = {}
for e in all_exercises:
    cats[e['category']] = cats.get(e['category'], 0) + 1
for c, n in sorted(cats.items()):
    print(f'  {c}: {n}')
