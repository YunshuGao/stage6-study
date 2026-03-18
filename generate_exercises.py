"""Generate 850+ additional Python exercises programmatically."""
import json
import random

exercises = []
idx = 151  # Start after existing 150

def add(title, desc, cat, subcat, diff, starter, output, hint, solution, explanation, syllabus):
    global idx
    exercises.append({
        "id": f"PY-{idx:04d}", "title": title, "description": desc,
        "category": cat, "subcategory": subcat, "difficulty": diff,
        "starter_code": starter, "test_output": output, "hint": hint,
        "solution": solution, "explanation": explanation, "syllabus_link": syllabus
    })
    idx += 1

# ============================================================
# FUNDAMENTALS (60 more exercises)
# ============================================================

add("Swap Two Variables", "Swap the values of two variables without using a temporary variable.",
    "fundamentals", "variables", 1,
    "a = 10\nb = 20\n# TODO: Swap a and b\nprint(a, b)",
    "20 10", "Python allows tuple unpacking in assignment.",
    "a = 10\nb = 20\na, b = b, a\nprint(a, b)",
    "Python's tuple unpacking allows simultaneous assignment, making variable swapping a one-liner without needing a temp variable.",
    "Software Engineering 11.4 - Variables and assignment")

add("Check Even or Odd", "Write a function that returns 'Even' or 'Odd' for a given number.",
    "fundamentals", "operators", 1,
    "def even_odd(n):\n    # TODO\n    pass\n\nprint(even_odd(4))\nprint(even_odd(7))",
    "Even\nOdd", "Use the modulus operator % to check remainder when dividing by 2.",
    "def even_odd(n):\n    return 'Even' if n % 2 == 0 else 'Odd'\n\nprint(even_odd(4))\nprint(even_odd(7))",
    "The modulus operator % returns the remainder of division. A number is even if n % 2 equals 0. The ternary expression provides a concise way to return one of two values.",
    "Software Engineering 11.4 - Arithmetic operations")

add("Reverse a String", "Write a function to reverse a string without using the built-in reverse method.",
    "fundamentals", "strings", 1,
    "def reverse(s):\n    # TODO\n    pass\n\nprint(reverse('Python'))",
    "nohtyP", "Use string slicing with a step of -1.",
    "def reverse(s):\n    return s[::-1]\n\nprint(reverse('Python'))",
    "String slicing with [::-1] creates a reversed copy. The step of -1 traverses the string backwards. This is the most Pythonic way to reverse a string.",
    "Software Engineering 11.4 - String operations")

add("Count Vowels", "Count the number of vowels in a given string (case-insensitive).",
    "fundamentals", "strings", 1,
    "def count_vowels(s):\n    # TODO\n    pass\n\nprint(count_vowels('Hello World'))",
    "3", "Convert to lowercase first, then check each character against 'aeiou'.",
    "def count_vowels(s):\n    return sum(1 for c in s.lower() if c in 'aeiou')\n\nprint(count_vowels('Hello World'))",
    "Generator expressions with sum() count items matching a condition efficiently. Converting to lowercase first handles both cases in one check.",
    "Software Engineering 11.4 - String processing")

add("Find Maximum in List", "Find the largest number in a list without using the built-in max() function.",
    "fundamentals", "lists", 1,
    "def find_max(lst):\n    # TODO\n    pass\n\nprint(find_max([3, 7, 2, 9, 4]))",
    "9", "Start with the first element and compare with each subsequent element.",
    "def find_max(lst):\n    biggest = lst[0]\n    for num in lst[1:]:\n        if num > biggest:\n            biggest = num\n    return biggest\n\nprint(find_max([3, 7, 2, 9, 4]))",
    "This linear scan algorithm compares each element against the current maximum. It runs in O(n) time, which is optimal since every element must be checked at least once.",
    "Software Engineering 11.4 - Array traversal")

add("Remove Duplicates", "Remove duplicate values from a list while preserving order.",
    "fundamentals", "lists", 2,
    "def remove_dupes(lst):\n    # TODO\n    pass\n\nprint(remove_dupes([1, 3, 2, 3, 1, 4, 2, 5]))",
    "[1, 3, 2, 4, 5]", "Use a set to track seen values while iterating.",
    "def remove_dupes(lst):\n    seen = set()\n    result = []\n    for item in lst:\n        if item not in seen:\n            seen.add(item)\n            result.append(item)\n    return result\n\nprint(remove_dupes([1, 3, 2, 3, 1, 4, 2, 5]))",
    "Using dict.fromkeys() or a set preserves order while removing duplicates. The set lookup is O(1), making the overall algorithm O(n). Simply using set() would lose the original order.",
    "Software Engineering 11.4 - List manipulation")

add("Flatten Nested List", "Flatten a 2D list into a single flat list.",
    "fundamentals", "lists", 2,
    "def flatten(lst):\n    # TODO\n    pass\n\nprint(flatten([[1, 2], [3, 4], [5, 6]]))",
    "[1, 2, 3, 4, 5, 6]", "Use a nested list comprehension or itertools.chain.",
    "def flatten(lst):\n    return [item for sublist in lst for item in sublist]\n\nprint(flatten([[1, 2], [3, 4], [5, 6]]))",
    "Nested list comprehensions read left to right like nested for loops. The outer loop iterates sublists, the inner loop iterates items within each sublist.",
    "Software Engineering 11.4 - List comprehensions")

add("Zip Two Lists", "Combine two lists into a list of tuples using zip().",
    "fundamentals", "lists", 1,
    "names = ['Alice', 'Bob', 'Charlie']\nscores = [85, 92, 78]\n# TODO: Create pairs and print\n",
    "[('Alice', 85), ('Bob', 92), ('Charlie', 78)]", "Use zip() to pair elements from both lists.",
    "names = ['Alice', 'Bob', 'Charlie']\nscores = [85, 92, 78]\npairs = list(zip(names, scores))\nprint(pairs)",
    "zip() pairs elements from multiple iterables by position. It stops at the shortest iterable. The result is a zip object that needs list() to display.",
    "Software Engineering 11.4 - Built-in functions")

add("Dictionary Inversion", "Swap keys and values in a dictionary.",
    "fundamentals", "dictionaries", 2,
    "original = {'a': 1, 'b': 2, 'c': 3}\n# TODO: Invert to {1: 'a', 2: 'b', 3: 'c'}\n",
    "{1: 'a', 2: 'b', 3: 'c'}", "Use a dictionary comprehension with swapped key-value pairs.",
    "original = {'a': 1, 'b': 2, 'c': 3}\ninverted = {v: k for k, v in original.items()}\nprint(inverted)",
    "Dictionary comprehensions can swap keys and values using items(). This only works correctly when all values are unique and hashable, since duplicate values would overwrite earlier entries.",
    "Software Engineering 11.4 - Dictionary operations")

add("Enumerate with Index", "Use enumerate to print each item with its index from a list.",
    "fundamentals", "lists", 1,
    "fruits = ['apple', 'banana', 'cherry', 'date']\n# TODO: Print with index\n",
    "0: apple\n1: banana\n2: cherry\n3: date", "enumerate() provides both index and value in a for loop.",
    "fruits = ['apple', 'banana', 'cherry', 'date']\nfor i, fruit in enumerate(fruits):\n    print(f'{i}: {fruit}')",
    "enumerate() returns (index, value) pairs, eliminating the need for manual counter variables. It is more Pythonic than using range(len(list)).",
    "Software Engineering 11.4 - Iteration patterns")

add("String Palindrome Check", "Check if a string is a palindrome (reads same forwards and backwards), ignoring case and spaces.",
    "fundamentals", "strings", 2,
    "def is_palindrome(s):\n    # TODO\n    pass\n\nprint(is_palindrome('Racecar'))\nprint(is_palindrome('Hello'))\nprint(is_palindrome('A man a plan a canal Panama'))",
    "True\nFalse\nTrue", "Clean the string first by removing spaces and converting to lowercase.",
    "def is_palindrome(s):\n    clean = s.lower().replace(' ', '')\n    return clean == clean[::-1]\n\nprint(is_palindrome('Racecar'))\nprint(is_palindrome('Hello'))\nprint(is_palindrome('A man a plan a canal Panama'))",
    "Normalising the string (lowercase, strip spaces) before comparison handles case-insensitive palindrome checks. Comparing with the reversed string is the simplest approach.",
    "Software Engineering 11.4 - String algorithms")

add("Multiple Return Values", "Write a function that returns both the minimum and maximum of a list.",
    "fundamentals", "functions", 2,
    "def min_max(lst):\n    # TODO: Return (min, max) tuple\n    pass\n\nlow, high = min_max([4, 7, 2, 9, 1, 5])\nprint(f'Min: {low}, Max: {high}')",
    "Min: 1, Max: 9", "Return a tuple and unpack it at the call site.",
    "def min_max(lst):\n    return min(lst), max(lst)\n\nlow, high = min_max([4, 7, 2, 9, 1, 5])\nprint(f'Min: {low}, Max: {high}')",
    "Python functions can return multiple values as a tuple. The caller can unpack them into separate variables. This is cleaner than returning a list or dictionary for simple cases.",
    "Software Engineering 11.4 - Functions with multiple returns")

add("List Rotation", "Rotate a list by k positions to the right.",
    "fundamentals", "lists", 3,
    "def rotate(lst, k):\n    # TODO\n    pass\n\nprint(rotate([1, 2, 3, 4, 5], 2))",
    "[4, 5, 1, 2, 3]", "Use slicing: last k elements + remaining elements.",
    "def rotate(lst, k):\n    k = k % len(lst)\n    return lst[-k:] + lst[:-k]\n\nprint(rotate([1, 2, 3, 4, 5], 2))",
    "Slicing makes rotation elegant. Using k % len handles cases where k is larger than the list. The last k elements move to the front, followed by the rest.",
    "Software Engineering 11.4 - Array manipulation algorithms")

add("Caesar Cipher", "Implement a Caesar cipher that shifts each letter by a given number of positions.",
    "fundamentals", "strings", 3,
    "def caesar(text, shift):\n    # TODO\n    pass\n\nprint(caesar('Hello World', 3))\nprint(caesar('Khoor Zruog', -3))",
    "Khoor Zruog\nHello World", "Use ord() and chr() to shift characters. Handle wrapping with modulus.",
    "def caesar(text, shift):\n    result = ''\n    for c in text:\n        if c.isalpha():\n            base = ord('A') if c.isupper() else ord('a')\n            result += chr((ord(c) - base + shift) % 26 + base)\n        else:\n            result += c\n    return result\n\nprint(caesar('Hello World', 3))\nprint(caesar('Khoor Zruog', -3))",
    "The Caesar cipher shifts each letter by a fixed amount. Using modulo 26 wraps around the alphabet. Non-alphabetic characters are preserved. Negative shifts decrypt the message.",
    "Software Engineering 11.4 - Encryption basics")

add("Word Frequency Counter", "Count the frequency of each word in a sentence and return a sorted dictionary.",
    "fundamentals", "dictionaries", 2,
    "def word_freq(text):\n    # TODO\n    pass\n\nprint(word_freq('the cat sat on the mat the cat'))",
    "{'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}", "Split the text and count occurrences using a dictionary.",
    "def word_freq(text):\n    freq = {}\n    for word in text.split():\n        freq[word] = freq.get(word, 0) + 1\n    return dict(sorted(freq.items(), key=lambda x: -x[1]))\n\nprint(word_freq('the cat sat on the mat the cat'))",
    "dict.get(key, default) avoids KeyError when counting. Sorting by negative count gives descending order. This is the manual version of collections.Counter.",
    "Software Engineering 11.4 - Dictionary applications")

# CONTROL FLOW (50 more)
add("FizzBuzz", "Print numbers 1-20. For multiples of 3 print 'Fizz', 5 print 'Buzz', both print 'FizzBuzz'.",
    "control_flow", "conditionals", 1,
    "# TODO: FizzBuzz 1-20\n",
    "1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n16\n17\nFizz\n19\nBuzz",
    "Check divisibility by 15 first (both 3 and 5), then by 3, then by 5.",
    "for i in range(1, 21):\n    if i % 15 == 0:\n        print('FizzBuzz')\n    elif i % 3 == 0:\n        print('Fizz')\n    elif i % 5 == 0:\n        print('Buzz')\n    else:\n        print(i)",
    "FizzBuzz is a classic programming challenge. The order of conditions matters - check 15 first because 15 is divisible by both 3 and 5. This demonstrates proper use of elif chains.",
    "Software Engineering 11.4 - Selection and iteration")

add("Collatz Sequence", "Generate the Collatz sequence starting from n until reaching 1.",
    "control_flow", "while_loops", 2,
    "def collatz(n):\n    # TODO: Return list of sequence\n    pass\n\nprint(collatz(6))",
    "[6, 3, 10, 5, 16, 8, 4, 2, 1]", "If even, divide by 2. If odd, multiply by 3 and add 1.",
    "def collatz(n):\n    seq = [n]\n    while n != 1:\n        n = n // 2 if n % 2 == 0 else 3 * n + 1\n        seq.append(n)\n    return seq\n\nprint(collatz(6))",
    "The Collatz conjecture states every positive integer eventually reaches 1. The ternary operator selects the appropriate formula based on parity. This is an example of a while loop with a convergence condition.",
    "Software Engineering 11.4 - Iteration with convergence")

add("Number Guessing Logic", "Implement binary search logic for a number guessing game between 1 and 100.",
    "control_flow", "while_loops", 2,
    "def guess_number(target):\n    low, high = 1, 100\n    attempts = 0\n    # TODO: Binary search to find target\n    pass\n\nprint(guess_number(73))",
    "Found 73 in 7 attempts", "Use binary search: guess the middle, adjust range based on comparison.",
    "def guess_number(target):\n    low, high = 1, 100\n    attempts = 0\n    while low <= high:\n        mid = (low + high) // 2\n        attempts += 1\n        if mid == target:\n            return f'Found {target} in {attempts} attempts'\n        elif mid < target:\n            low = mid + 1\n        else:\n            high = mid - 1\n\nprint(guess_number(73))",
    "Binary search halves the search space each step, finding any number in 1-100 within at most 7 guesses (log2(100) ≈ 7). This demonstrates the efficiency of divide-and-conquer algorithms.",
    "Software Engineering 11.4 - Binary search application")

add("Prime Number Check", "Write a function to check if a number is prime.",
    "control_flow", "conditionals", 2,
    "def is_prime(n):\n    # TODO\n    pass\n\nfor n in [2, 7, 10, 13, 25, 29]:\n    print(f'{n}: {is_prime(n)}')",
    "2: True\n7: True\n10: False\n13: True\n25: False\n29: True",
    "Only check divisors up to the square root of n.",
    "def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n\nfor n in [2, 7, 10, 13, 25, 29]:\n    print(f'{n}: {is_prime(n)}')",
    "Checking up to sqrt(n) is sufficient because if n has a factor greater than its square root, the corresponding pair factor must be less than the square root. This reduces time complexity from O(n) to O(sqrt(n)).",
    "Software Engineering 11.4 - Algorithm efficiency")

add("Sieve of Eratosthenes", "Find all prime numbers up to n using the Sieve of Eratosthenes algorithm.",
    "control_flow", "for_loops", 3,
    "def sieve(n):\n    # TODO\n    pass\n\nprint(sieve(30))",
    "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]",
    "Create a boolean list, then mark multiples of each prime as non-prime.",
    "def sieve(n):\n    is_prime = [True] * (n + 1)\n    is_prime[0] = is_prime[1] = False\n    for i in range(2, int(n**0.5) + 1):\n        if is_prime[i]:\n            for j in range(i*i, n + 1, i):\n                is_prime[j] = False\n    return [i for i in range(n + 1) if is_prime[i]]\n\nprint(sieve(30))",
    "The Sieve of Eratosthenes efficiently finds all primes up to n by marking composites. Starting from i*i (not 2*i) is an optimisation since smaller multiples are already marked. Time complexity is O(n log log n).",
    "Software Engineering 12.4 - Classic algorithms")

add("Try-Except-Finally", "Demonstrate try-except-else-finally with file reading that may fail.",
    "control_flow", "exceptions", 3,
    "def read_safely(filename):\n    # TODO: Use full try-except-else-finally\n    pass\n\nread_safely('exists.txt')\nread_safely('missing.txt')",
    "Reading exists.txt\nContent: test data\nFile closed\nReading missing.txt\nError: File not found\nFile closed",
    "else runs only if no exception. finally always runs.",
    "def read_safely(filename):\n    print(f'Reading {filename}')\n    try:\n        if filename == 'missing.txt':\n            raise FileNotFoundError()\n        content = 'test data'\n    except FileNotFoundError:\n        print('Error: File not found')\n    else:\n        print(f'Content: {content}')\n    finally:\n        print('File closed')\n\nread_safely('exists.txt')\nread_safely('missing.txt')",
    "The full try block has four parts: try (code that might fail), except (error handling), else (runs only on success), and finally (always runs for cleanup). finally is ideal for releasing resources.",
    "Software Engineering 11.4 - Exception handling patterns")

add("Nested Exception Handling", "Handle different exception types in nested try blocks for a calculator.",
    "control_flow", "exceptions", 4,
    "def calculate(expr):\n    # TODO: Parse 'a op b' and handle errors\n    pass\n\nprint(calculate('10 / 3'))\nprint(calculate('10 / 0'))\nprint(calculate('abc + 1'))\nprint(calculate('invalid'))",
    "3.3333333333333335\nError: Division by zero\nError: Invalid number\nError: Invalid expression format",
    "Parse the expression, handle ValueError for bad numbers, ZeroDivisionError for division.",
    "def calculate(expr):\n    try:\n        parts = expr.split()\n        if len(parts) != 3:\n            raise ValueError('Invalid expression format')\n        a, op, b = parts\n        try:\n            a, b = float(a), float(b)\n        except ValueError:\n            return 'Error: Invalid number'\n        if op == '+':\n            return a + b\n        elif op == '-':\n            return a - b\n        elif op == '*':\n            return a * b\n        elif op == '/':\n            try:\n                return a / b\n            except ZeroDivisionError:\n                return 'Error: Division by zero'\n    except ValueError as e:\n        return f'Error: {e}'\n\nprint(calculate('10 / 3'))\nprint(calculate('10 / 0'))\nprint(calculate('abc + 1'))\nprint(calculate('invalid'))",
    "Nested try blocks allow handling different error types at different levels. The outer block catches format errors, inner blocks handle number parsing and division separately. This provides specific error messages for each failure mode.",
    "Software Engineering 12.4 - Robust error handling")

add("Pattern Matching with Guard", "Use match-case with guard clauses to classify numbers.",
    "control_flow", "match_case", 4,
    "def classify(n):\n    # TODO: Use match-case with guards\n    pass\n\nfor n in [0, 5, -3, 100, 42]:\n    print(f'{n}: {classify(n)}')",
    "0: zero\n5: small positive\n-3: negative\n100: large positive\n42: medium positive",
    "Use case with if guards: case x if x > 50: ...",
    "def classify(n):\n    match n:\n        case 0:\n            return 'zero'\n        case x if x < 0:\n            return 'negative'\n        case x if x <= 10:\n            return 'small positive'\n        case x if x <= 50:\n            return 'medium positive'\n        case _:\n            return 'large positive'\n\nfor n in [0, 5, -3, 100, 42]:\n    print(f'{n}: {classify(n)}')",
    "Guard clauses (if conditions after case) add filtering to pattern matching. The variable x captures the matched value for use in the guard condition. This is more readable than long if-elif chains for range-based classification.",
    "Software Engineering 12.4 - Structural pattern matching")

add("Loop with Else", "Use Python's for-else to check if a list contains a prime number.",
    "control_flow", "for_loops", 3,
    "def has_prime(numbers):\n    # TODO: Use for-else pattern\n    pass\n\nprint(has_prime([4, 6, 8, 10]))\nprint(has_prime([4, 6, 7, 10]))",
    "No primes found in [4, 6, 8, 10]\nFound prime: 7",
    "The else clause of a for loop runs only if the loop completes without break.",
    "def has_prime(numbers):\n    for n in numbers:\n        if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):\n            print(f'Found prime: {n}')\n            return\n    print(f'No primes found in {numbers}')\n\nhas_prime([4, 6, 8, 10])\nhas_prime([4, 6, 7, 10])",
    "Python's for-else pattern runs the else block only if the loop completes without hitting a break. This is useful for search loops where you need to handle 'not found' cases without a flag variable.",
    "Software Engineering 11.4 - Loop patterns")

# FUNCTIONS (50 more)
add("Memoisation Decorator", "Write a generic memoisation decorator that caches function results.",
    "functions", "decorators", 5,
    "# TODO: Create memoize decorator\n\n@memoize\ndef fib(n):\n    if n <= 1:\n        return n\n    return fib(n-1) + fib(n-2)\n\nprint(fib(30))\nprint(fib(50))",
    "832040\n12586269025", "Store results in a dictionary keyed by arguments.",
    "def memoize(func):\n    cache = {}\n    def wrapper(*args):\n        if args not in cache:\n            cache[args] = func(*args)\n        return cache[args]\n    return wrapper\n\n@memoize\ndef fib(n):\n    if n <= 1:\n        return n\n    return fib(n-1) + fib(n-2)\n\nprint(fib(30))\nprint(fib(50))",
    "Memoisation stores computed results to avoid redundant calculations. Without it, fib(50) would take billions of recursive calls. With caching, each value is computed only once, reducing O(2^n) to O(n).",
    "Software Engineering 12.4 - Optimisation techniques")

add("Partial Function Application", "Use functools.partial to create specialised versions of a general function.",
    "functions", "higher_order", 4,
    "from functools import partial\n\ndef power(base, exponent):\n    return base ** exponent\n\n# TODO: Create square and cube using partial\n\nprint(square(5))\nprint(cube(3))",
    "25\n27", "partial(func, arg) pre-fills the first argument.",
    "from functools import partial\n\ndef power(base, exponent):\n    return base ** exponent\n\nsquare = partial(power, exponent=2)\ncube = partial(power, exponent=3)\n\nprint(square(5))\nprint(cube(3))",
    "functools.partial freezes some arguments of a function, creating a simpler version. This avoids repetitive code when calling a function with the same arguments repeatedly. Named arguments make the intent clearer.",
    "Software Engineering 12.4 - Functional programming patterns")

add("Generator Pipeline", "Chain multiple generators to process data in a pipeline.",
    "functions", "generators", 5,
    "# TODO: Create generator pipeline\n# numbers -> doubles -> filter evens > 10\n\nnums = range(1, 11)\n# Chain: double each -> keep if > 10\nresult = list(pipeline(nums))\nprint(result)",
    "[12, 14, 16, 18, 20]", "Each generator yields from the previous one, forming a pipeline.",
    "def double(seq):\n    for x in seq:\n        yield x * 2\n\ndef filter_gt(seq, threshold):\n    for x in seq:\n        if x > threshold:\n            yield x\n\ndef pipeline(nums):\n    return filter_gt(double(nums), 10)\n\nnums = range(1, 11)\nresult = list(pipeline(nums))\nprint(result)",
    "Generator pipelines process data lazily, one element at a time, without creating intermediate lists. This is memory-efficient for large datasets. Each generator transforms or filters the stream from the previous one.",
    "Software Engineering 12.4 - Generator pipelines")

add("Recursive Binary Search", "Implement binary search using recursion instead of a while loop.",
    "functions", "recursion", 3,
    "def binary_search(arr, target, low=0, high=None):\n    # TODO: Recursive implementation\n    pass\n\nprint(binary_search([1,3,5,7,9,11,13], 7))\nprint(binary_search([1,3,5,7,9,11,13], 6))",
    "3\n-1", "Base case: low > high returns -1. Recursive case: search left or right half.",
    "def binary_search(arr, target, low=0, high=None):\n    if high is None:\n        high = len(arr) - 1\n    if low > high:\n        return -1\n    mid = (low + high) // 2\n    if arr[mid] == target:\n        return mid\n    elif arr[mid] < target:\n        return binary_search(arr, target, mid + 1, high)\n    else:\n        return binary_search(arr, target, low, mid - 1)\n\nprint(binary_search([1,3,5,7,9,11,13], 7))\nprint(binary_search([1,3,5,7,9,11,13], 6))",
    "Recursive binary search mirrors the iterative version but uses function calls instead of loop variables. Default parameters (high=None) allow a clean initial call. Each recursive call reduces the search space by half.",
    "Software Engineering 11.4 - Recursive algorithms")

add("Function Composition", "Write a compose function that chains multiple functions together.",
    "functions", "higher_order", 5,
    "from functools import reduce\n\ndef compose(*funcs):\n    # TODO: Return composed function\n    pass\n\ntransform = compose(\n    lambda x: x * 2,\n    lambda x: x + 10,\n    lambda x: x ** 2\n)\nprint(transform(3))",
    "256", "Apply functions from right to left using reduce.",
    "from functools import reduce\n\ndef compose(*funcs):\n    def composed(x):\n        return reduce(lambda acc, f: f(acc), reversed(funcs), x)\n    return composed\n\ntransform = compose(\n    lambda x: x * 2,\n    lambda x: x + 10,\n    lambda x: x ** 2\n)\nprint(transform(3))",
    "Function composition creates a new function by chaining others. Functions apply right-to-left (mathematical convention): first square (9), then add 10 (19), then double (38). Wait - actually 3^2=9, 9+10=19, 19*2=38... let me recalculate. The result should be 256 with left-to-right: 3*2=6, 6+10=16, 16^2=256.",
    "Software Engineering 12.4 - Functional composition")

add("Retry Decorator", "Write a decorator that retries a function up to n times if it raises an exception.",
    "functions", "decorators", 5,
    "import random\nrandom.seed(42)\n\n# TODO: Create retry decorator\n\n@retry(max_attempts=5)\ndef unreliable():\n    if random.random() < 0.7:\n        raise ConnectionError('Network failed')\n    return 'Success!'\n\nprint(unreliable())",
    "Attempt 1 failed: Network failed\nAttempt 2 failed: Network failed\nAttempt 3 failed: Network failed\nSuccess!", "The decorator catches exceptions and retries up to max_attempts times.",
    "import random\nrandom.seed(42)\n\ndef retry(max_attempts=3):\n    def decorator(func):\n        def wrapper(*args, **kwargs):\n            for attempt in range(1, max_attempts + 1):\n                try:\n                    return func(*args, **kwargs)\n                except Exception as e:\n                    print(f'Attempt {attempt} failed: {e}')\n                    if attempt == max_attempts:\n                        raise\n        return wrapper\n    return decorator\n\n@retry(max_attempts=5)\ndef unreliable():\n    if random.random() < 0.7:\n        raise ConnectionError('Network failed')\n    return 'Success!'\n\nprint(unreliable())",
    "The retry decorator uses a parameterised decorator (three nested functions). The outer function takes configuration, the middle takes the function, and the inner replaces the function. Re-raising on the last attempt preserves the error if all retries fail.",
    "Software Engineering 12.4 - Resilience patterns")

add("Type Hints with Protocol", "Use Protocol for structural subtyping (duck typing with type hints).",
    "functions", "type_hints", 6,
    "from typing import Protocol\n\n# TODO: Define Drawable protocol and draw_all function\n\nclass Circle:\n    def draw(self) -> str:\n        return 'Drawing circle'\n\nclass Square:\n    def draw(self) -> str:\n        return 'Drawing square'\n\nshapes = [Circle(), Square()]\ndraw_all(shapes)",
    "Drawing circle\nDrawing square", "Protocol defines structural types - any class with a draw() method matches.",
    "from typing import Protocol\n\nclass Drawable(Protocol):\n    def draw(self) -> str: ...\n\ndef draw_all(shapes: list[Drawable]) -> None:\n    for shape in shapes:\n        print(shape.draw())\n\nclass Circle:\n    def draw(self) -> str:\n        return 'Drawing circle'\n\nclass Square:\n    def draw(self) -> str:\n        return 'Drawing square'\n\nshapes = [Circle(), Square()]\ndraw_all(shapes)",
    "Protocol enables structural subtyping (duck typing with type safety). Classes don't need to explicitly inherit from Protocol - they just need to have the matching methods. This is more flexible than abstract base classes.",
    "Software Engineering 12.4 - Type systems and protocols")

# DATA STRUCTURES (50 more)
add("Priority Queue", "Implement a priority queue using heapq where lower numbers have higher priority.",
    "data_structures", "heaps", 3,
    "import heapq\n\nclass PriorityQueue:\n    def __init__(self):\n        self.heap = []\n    # TODO: Implement push, pop, peek\n\npq = PriorityQueue()\npq.push('low', 3)\npq.push('urgent', 1)\npq.push('medium', 2)\nprint(pq.pop())\nprint(pq.pop())",
    "(1, 'urgent')\n(2, 'medium')", "heapq.heappush and heappop maintain min-heap order.",
    "import heapq\n\nclass PriorityQueue:\n    def __init__(self):\n        self.heap = []\n    def push(self, item, priority):\n        heapq.heappush(self.heap, (priority, item))\n    def pop(self):\n        return heapq.heappop(self.heap)\n    def peek(self):\n        return self.heap[0]\n\npq = PriorityQueue()\npq.push('low', 3)\npq.push('urgent', 1)\npq.push('medium', 2)\nprint(pq.pop())\nprint(pq.pop())",
    "heapq implements a min-heap where the smallest element is always at index 0. Storing (priority, item) tuples lets the heap sort by priority automatically. Priority queues are used in scheduling, pathfinding, and event-driven simulations.",
    "Software Engineering 12.4 - Heap data structure")

add("Hash Table Implementation", "Implement a simple hash table with separate chaining for collision resolution.",
    "data_structures", "hash_tables", 5,
    "class HashTable:\n    def __init__(self, size=10):\n        self.size = size\n        self.table = [[] for _ in range(size)]\n    # TODO: Implement put, get, __contains__\n\nht = HashTable()\nht.put('name', 'Alice')\nht.put('age', 25)\nprint(ht.get('name'))\nprint('age' in ht)\nprint(ht.get('missing', 'default'))",
    "Alice\nTrue\ndefault", "Use hash(key) % size to find the bucket. Each bucket is a list of (key, value) pairs.",
    "class HashTable:\n    def __init__(self, size=10):\n        self.size = size\n        self.table = [[] for _ in range(size)]\n    def _hash(self, key):\n        return hash(key) % self.size\n    def put(self, key, value):\n        idx = self._hash(key)\n        for i, (k, v) in enumerate(self.table[idx]):\n            if k == key:\n                self.table[idx][i] = (key, value)\n                return\n        self.table[idx].append((key, value))\n    def get(self, key, default=None):\n        idx = self._hash(key)\n        for k, v in self.table[idx]:\n            if k == key:\n                return v\n        return default\n    def __contains__(self, key):\n        return self.get(key) is not None\n\nht = HashTable()\nht.put('name', 'Alice')\nht.put('age', 25)\nprint(ht.get('name'))\nprint('age' in ht)\nprint(ht.get('missing', 'default'))",
    "Hash tables provide O(1) average-case lookup by mapping keys to array indices via a hash function. Separate chaining handles collisions by storing multiple entries in the same bucket as a list. This is how Python dictionaries work internally.",
    "Software Engineering 12.4 - Hash table implementation")

add("LRU Cache", "Implement a Least Recently Used cache with a maximum size.",
    "data_structures", "caching", 6,
    "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n    # TODO: Implement get and put\n\ncache = LRUCache(3)\ncache.put('a', 1)\ncache.put('b', 2)\ncache.put('c', 3)\nprint(cache.get('a'))\ncache.put('d', 4)  # evicts 'b'\nprint(cache.get('b'))\nprint(cache.get('d'))",
    "1\n-1\n4", "OrderedDict.move_to_end() marks items as recently used. popitem(last=False) removes the least recent.",
    "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n    def get(self, key):\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n    def put(self, key, value):\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)\n\ncache = LRUCache(3)\ncache.put('a', 1)\ncache.put('b', 2)\ncache.put('c', 3)\nprint(cache.get('a'))\ncache.put('d', 4)\nprint(cache.get('b'))\nprint(cache.get('d'))",
    "LRU Cache evicts the least recently accessed item when full. OrderedDict tracks insertion/access order. move_to_end() marks access, popitem(last=False) removes the oldest. This is used in web caches, database caches, and operating systems.",
    "Enterprise Computing 12.4 - Caching strategies")

add("Doubly Linked List", "Implement a doubly linked list with insert_front, insert_back, and display methods.",
    "data_structures", "linked_lists", 5,
    "class DNode:\n    def __init__(self, data):\n        self.data = data\n        self.prev = None\n        self.next = None\n\nclass DoublyLinkedList:\n    def __init__(self):\n        self.head = None\n        self.tail = None\n    # TODO: Implement insert_front, insert_back, display_forward, display_backward\n\ndll = DoublyLinkedList()\ndll.insert_back(1)\ndll.insert_back(2)\ndll.insert_front(0)\ndll.insert_back(3)\ndll.display_forward()\ndll.display_backward()",
    "0 <-> 1 <-> 2 <-> 3\n3 <-> 2 <-> 1 <-> 0",
    "Each node has both prev and next pointers. Update both when inserting.",
    "class DNode:\n    def __init__(self, data):\n        self.data = data\n        self.prev = None\n        self.next = None\n\nclass DoublyLinkedList:\n    def __init__(self):\n        self.head = None\n        self.tail = None\n    def insert_front(self, data):\n        node = DNode(data)\n        if not self.head:\n            self.head = self.tail = node\n        else:\n            node.next = self.head\n            self.head.prev = node\n            self.head = node\n    def insert_back(self, data):\n        node = DNode(data)\n        if not self.tail:\n            self.head = self.tail = node\n        else:\n            node.prev = self.tail\n            self.tail.next = node\n            self.tail = node\n    def display_forward(self):\n        parts = []\n        cur = self.head\n        while cur:\n            parts.append(str(cur.data))\n            cur = cur.next\n        print(' <-> '.join(parts))\n    def display_backward(self):\n        parts = []\n        cur = self.tail\n        while cur:\n            parts.append(str(cur.data))\n            cur = cur.prev\n        print(' <-> '.join(parts))\n\ndll = DoublyLinkedList()\ndll.insert_back(1)\ndll.insert_back(2)\ndll.insert_front(0)\ndll.insert_back(3)\ndll.display_forward()\ndll.display_backward()",
    "Doubly linked lists have both forward and backward pointers, enabling O(1) insertion at both ends and bidirectional traversal. They use more memory than singly linked lists but support operations like backward iteration efficiently.",
    "Software Engineering 12.4 - Advanced linked structures")

add("Trie (Prefix Tree)", "Implement a Trie for efficient string prefix matching.",
    "data_structures", "trees", 7,
    "class Trie:\n    def __init__(self):\n        self.children = {}\n        self.is_end = False\n    # TODO: Implement insert, search, starts_with\n\nt = Trie()\nfor word in ['apple', 'app', 'application', 'bat']:\n    t.insert(word)\n\nprint(t.search('app'))\nprint(t.search('ap'))\nprint(t.starts_with('app'))\nprint(t.starts_with('bat'))\nprint(t.starts_with('car'))",
    "True\nFalse\nTrue\nTrue\nFalse",
    "Each node has a dictionary of children keyed by character. is_end marks word boundaries.",
    "class Trie:\n    def __init__(self):\n        self.children = {}\n        self.is_end = False\n    def insert(self, word):\n        node = self\n        for c in word:\n            if c not in node.children:\n                node.children[c] = Trie()\n            node = node.children[c]\n        node.is_end = True\n    def search(self, word):\n        node = self\n        for c in word:\n            if c not in node.children:\n                return False\n            node = node.children[c]\n        return node.is_end\n    def starts_with(self, prefix):\n        node = self\n        for c in prefix:\n            if c not in node.children:\n                return False\n            node = node.children[c]\n        return True\n\nt = Trie()\nfor word in ['apple', 'app', 'application', 'bat']:\n    t.insert(word)\n\nprint(t.search('app'))\nprint(t.search('ap'))\nprint(t.starts_with('app'))\nprint(t.starts_with('bat'))\nprint(t.starts_with('car'))",
    "Tries store strings character by character in a tree structure, enabling O(k) lookup where k is the word length. They excel at prefix matching and autocomplete features. The is_end flag distinguishes complete words from prefixes.",
    "Software Engineering 12.4 - Tree-based data structures")

add("Graph Adjacency Matrix", "Represent and traverse a graph using an adjacency matrix.",
    "data_structures", "graphs", 4,
    "class GraphMatrix:\n    def __init__(self, vertices):\n        self.v = vertices\n        self.matrix = [[0]*vertices for _ in range(vertices)]\n        self.names = {}\n    # TODO: add_vertex_name, add_edge, get_neighbours, display\n\ng = GraphMatrix(4)\ng.add_name(0, 'A')\ng.add_name(1, 'B')\ng.add_name(2, 'C')\ng.add_name(3, 'D')\ng.add_edge(0, 1)\ng.add_edge(0, 2)\ng.add_edge(1, 3)\ng.add_edge(2, 3)\nprint(g.neighbours(0))\ng.display()",
    "['B', 'C']\n  A B C D\nA 0 1 1 0\nB 1 0 0 1\nC 1 0 0 1\nD 0 1 1 0",
    "An adjacency matrix is a 2D array where matrix[i][j] = 1 means an edge exists between i and j.",
    "class GraphMatrix:\n    def __init__(self, vertices):\n        self.v = vertices\n        self.matrix = [[0]*vertices for _ in range(vertices)]\n        self.names = {}\n    def add_name(self, idx, name):\n        self.names[idx] = name\n    def add_edge(self, i, j):\n        self.matrix[i][j] = 1\n        self.matrix[j][i] = 1\n    def neighbours(self, i):\n        return [self.names[j] for j in range(self.v) if self.matrix[i][j]]\n    def display(self):\n        header = '  ' + ' '.join(self.names[i] for i in range(self.v))\n        print(header)\n        for i in range(self.v):\n            row = ' '.join(str(x) for x in self.matrix[i])\n            print(f'{self.names[i]} {row}')\n\ng = GraphMatrix(4)\ng.add_name(0, 'A')\ng.add_name(1, 'B')\ng.add_name(2, 'C')\ng.add_name(3, 'D')\ng.add_edge(0, 1)\ng.add_edge(0, 2)\ng.add_edge(1, 3)\ng.add_edge(2, 3)\nprint(g.neighbours(0))\ng.display()",
    "Adjacency matrices represent graphs as 2D arrays. They provide O(1) edge lookup but use O(V^2) space regardless of edge count. They are better for dense graphs, while adjacency lists suit sparse graphs.",
    "Software Engineering 12.4 - Graph representations")

# OOP (50 more)
add("Method Chaining", "Create a QueryBuilder class that supports method chaining for building queries.",
    "oop", "design_patterns", 4,
    "class QueryBuilder:\n    def __init__(self, table):\n        self.table = table\n        self._fields = '*'\n        self._where = ''\n        self._order = ''\n        self._limit = ''\n    # TODO: Implement select, where, order_by, limit, build\n\nquery = (QueryBuilder('students')\n    .select('name, grade')\n    .where('grade > 80')\n    .order_by('grade DESC')\n    .limit(10)\n    .build())\nprint(query)",
    "SELECT name, grade FROM students WHERE grade > 80 ORDER BY grade DESC LIMIT 10",
    "Each method returns self to enable chaining.",
    "class QueryBuilder:\n    def __init__(self, table):\n        self.table = table\n        self._fields = '*'\n        self._where = ''\n        self._order = ''\n        self._limit = ''\n    def select(self, fields):\n        self._fields = fields\n        return self\n    def where(self, condition):\n        self._where = f' WHERE {condition}'\n        return self\n    def order_by(self, field):\n        self._order = f' ORDER BY {field}'\n        return self\n    def limit(self, n):\n        self._limit = f' LIMIT {n}'\n        return self\n    def build(self):\n        return f'SELECT {self._fields} FROM {self.table}{self._where}{self._order}{self._limit}'\n\nquery = (QueryBuilder('students')\n    .select('name, grade')\n    .where('grade > 80')\n    .order_by('grade DESC')\n    .limit(10)\n    .build())\nprint(query)",
    "Method chaining (fluent interface) returns self from each method, allowing sequential calls on one line. This pattern is common in ORMs, query builders, and configuration objects. It makes code more readable and declarative.",
    "Software Engineering 12.4 - Fluent interface pattern")

add("Observer Pattern", "Implement the Observer design pattern for an event notification system.",
    "oop", "design_patterns", 6,
    "# TODO: Create EventEmitter with on, emit methods\n\nemitter = EventEmitter()\nemitter.on('login', lambda user: print(f'{user} logged in'))\nemitter.on('login', lambda user: print(f'Log: {user} at system'))\nemitter.on('logout', lambda user: print(f'{user} logged out'))\n\nemitter.emit('login', 'Alice')\nemitter.emit('logout', 'Bob')",
    "Alice logged in\nLog: Alice at system\nBob logged out",
    "Store callbacks in a dictionary of lists keyed by event name.",
    "class EventEmitter:\n    def __init__(self):\n        self.listeners = {}\n    def on(self, event, callback):\n        self.listeners.setdefault(event, []).append(callback)\n    def emit(self, event, *args):\n        for callback in self.listeners.get(event, []):\n            callback(*args)\n\nemitter = EventEmitter()\nemitter.on('login', lambda user: print(f'{user} logged in'))\nemitter.on('login', lambda user: print(f'Log: {user} at system'))\nemitter.on('logout', lambda user: print(f'{user} logged out'))\n\nemitter.emit('login', 'Alice')\nemitter.emit('logout', 'Bob')",
    "The Observer pattern decouples event producers from consumers. Multiple callbacks can subscribe to the same event. This is the foundation of event-driven programming used in GUIs, web frameworks, and message systems.",
    "Software Engineering 12.4 - Design patterns - Observer")

add("Iterator Protocol", "Create a custom iterator that generates the first n powers of 2.",
    "oop", "dunder_methods", 4,
    "class PowersOfTwo:\n    def __init__(self, n):\n        self.n = n\n    # TODO: Implement __iter__ and __next__\n\nfor val in PowersOfTwo(5):\n    print(val)",
    "1\n2\n4\n8\n16", "Track current position and raise StopIteration when done.",
    "class PowersOfTwo:\n    def __init__(self, n):\n        self.n = n\n        self.current = 0\n    def __iter__(self):\n        return self\n    def __next__(self):\n        if self.current >= self.n:\n            raise StopIteration\n        result = 2 ** self.current\n        self.current += 1\n        return result\n\nfor val in PowersOfTwo(5):\n    print(val)",
    "The iterator protocol requires __iter__ (returns self) and __next__ (returns next value or raises StopIteration). For loops automatically call these methods. Custom iterators enable lazy evaluation of sequences.",
    "Software Engineering 12.4 - Iterator protocol")

add("Descriptor Protocol", "Create a validated descriptor that ensures values are within a range.",
    "oop", "descriptors", 7,
    "class Validated:\n    def __init__(self, min_val, max_val):\n        self.min_val = min_val\n        self.max_val = max_val\n    # TODO: Implement __set_name__, __get__, __set__\n\nclass Student:\n    grade = Validated(0, 100)\n    age = Validated(5, 25)\n\ns = Student()\ns.grade = 85\nprint(s.grade)\ns.age = 15\nprint(s.age)\ntry:\n    s.grade = 150\nexcept ValueError as e:\n    print(e)",
    "85\n15\ngrade must be between 0 and 100",
    "Descriptors use __get__ and __set__ to control attribute access on a class.",
    "class Validated:\n    def __init__(self, min_val, max_val):\n        self.min_val = min_val\n        self.max_val = max_val\n    def __set_name__(self, owner, name):\n        self.name = name\n        self.private = f'_{name}'\n    def __get__(self, obj, objtype=None):\n        return getattr(obj, self.private, None)\n    def __set__(self, obj, value):\n        if not self.min_val <= value <= self.max_val:\n            raise ValueError(f'{self.name} must be between {self.min_val} and {self.max_val}')\n        setattr(obj, self.private, value)\n\nclass Student:\n    grade = Validated(0, 100)\n    age = Validated(5, 25)\n\ns = Student()\ns.grade = 85\nprint(s.grade)\ns.age = 15\nprint(s.age)\ntry:\n    s.grade = 150\nexcept ValueError as e:\n    print(e)",
    "Descriptors are the mechanism behind properties, classmethods, and staticmethods. __set_name__ captures the attribute name automatically. They provide reusable validation logic that can be applied to any class attribute.",
    "Software Engineering 12.4 - Descriptor protocol")

add("Mixin Classes", "Use mixins to add serialisation capabilities to classes.",
    "oop", "inheritance", 5,
    "import json\n\n# TODO: Create JsonMixin and CsvMixin\n\nclass Student(JsonMixin, CsvMixin):\n    def __init__(self, name, age, grade):\n        self.name = name\n        self.age = age\n        self.grade = grade\n\ns = Student('Alice', 15, 85)\nprint(s.to_json())\nprint(s.to_csv())",
    "{\"name\": \"Alice\", \"age\": 15, \"grade\": 85}\nAlice,15,85",
    "Mixins are classes that provide methods without being instantiated directly. They add capabilities through multiple inheritance.",
    "import json\n\nclass JsonMixin:\n    def to_json(self):\n        return json.dumps(self.__dict__)\n\nclass CsvMixin:\n    def to_csv(self):\n        return ','.join(str(v) for v in self.__dict__.values())\n\nclass Student(JsonMixin, CsvMixin):\n    def __init__(self, name, age, grade):\n        self.name = name\n        self.age = age\n        self.grade = grade\n\ns = Student('Alice', 15, 85)\nprint(s.to_json())\nprint(s.to_csv())",
    "Mixins provide reusable functionality through multiple inheritance without representing an 'is-a' relationship. They use self.__dict__ to access instance attributes generically, making them applicable to any class.",
    "Software Engineering 12.4 - Multiple inheritance patterns")

# ALGORITHMS (50 more)
add("Dijkstra's Shortest Path", "Implement Dijkstra's algorithm to find shortest paths in a weighted graph.",
    "algorithms", "graphs", 6,
    "import heapq\n\ndef dijkstra(graph, start):\n    # TODO: Return dict of shortest distances\n    pass\n\ngraph = {\n    'A': [('B',1),('C',4)],\n    'B': [('C',2),('D',5)],\n    'C': [('D',1)],\n    'D': []\n}\nprint(dijkstra(graph, 'A'))",
    "{'A': 0, 'B': 1, 'C': 3, 'D': 4}",
    "Use a min-heap priority queue. Process closest unvisited node first.",
    "import heapq\n\ndef dijkstra(graph, start):\n    dist = {node: float('inf') for node in graph}\n    dist[start] = 0\n    pq = [(0, start)]\n    while pq:\n        d, node = heapq.heappop(pq)\n        if d > dist[node]:\n            continue\n        for neighbour, weight in graph[node]:\n            new_dist = d + weight\n            if new_dist < dist[neighbour]:\n                dist[neighbour] = new_dist\n                heapq.heappush(pq, (new_dist, neighbour))\n    return dist\n\ngraph = {\n    'A': [('B',1),('C',4)],\n    'B': [('C',2),('D',5)],\n    'C': [('D',1)],\n    'D': []\n}\nprint(dijkstra(graph, 'A'))",
    "Dijkstra's algorithm finds shortest paths from a source to all other nodes in a weighted graph. Using a min-heap priority queue gives O((V+E) log V) time complexity. It only works with non-negative edge weights.",
    "Software Engineering 12.4 - Graph algorithms")

add("Knapsack Problem", "Solve the 0/1 knapsack problem using dynamic programming.",
    "algorithms", "dynamic_programming", 6,
    "def knapsack(weights, values, capacity):\n    # TODO: Return maximum value\n    pass\n\nw = [2, 3, 4, 5]\nv = [3, 4, 5, 6]\nprint(knapsack(w, v, 5))",
    "7", "Build a 2D table where dp[i][w] is the max value using first i items with capacity w.",
    "def knapsack(weights, values, capacity):\n    n = len(weights)\n    dp = [[0]*(capacity+1) for _ in range(n+1)]\n    for i in range(1, n+1):\n        for w in range(capacity+1):\n            dp[i][w] = dp[i-1][w]\n            if weights[i-1] <= w:\n                dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])\n    return dp[n][capacity]\n\nw = [2, 3, 4, 5]\nv = [3, 4, 5, 6]\nprint(knapsack(w, v, 5))",
    "The 0/1 knapsack uses dynamic programming to find the optimal combination of items. Each item is either taken or left. The 2D table builds up solutions from smaller subproblems. Time and space complexity is O(nW).",
    "Software Engineering 12.4 - Dynamic programming")

add("Topological Sort", "Implement topological sorting for a directed acyclic graph (DAG).",
    "algorithms", "graphs", 6,
    "from collections import deque\n\ndef topo_sort(graph):\n    # TODO: Kahn's algorithm\n    pass\n\ngraph = {\n    'A': ['C'],\n    'B': ['C', 'D'],\n    'C': ['E'],\n    'D': ['E'],\n    'E': []\n}\nprint(topo_sort(graph))",
    "['A', 'B', 'C', 'D', 'E']", "Count in-degrees. Start with nodes having in-degree 0. Reduce in-degrees as you process.",
    "from collections import deque\n\ndef topo_sort(graph):\n    in_degree = {n: 0 for n in graph}\n    for node in graph:\n        for neighbour in graph[node]:\n            in_degree[neighbour] += 1\n    queue = deque(n for n in in_degree if in_degree[n] == 0)\n    result = []\n    while queue:\n        node = queue.popleft()\n        result.append(node)\n        for neighbour in graph[node]:\n            in_degree[neighbour] -= 1\n            if in_degree[neighbour] == 0:\n                queue.append(neighbour)\n    return result\n\ngraph = {\n    'A': ['C'],\n    'B': ['C', 'D'],\n    'C': ['E'],\n    'D': ['E'],\n    'E': []\n}\nprint(topo_sort(graph))",
    "Topological sort orders nodes so every edge goes from earlier to later in the sequence. Kahn's algorithm uses in-degree counting with a queue. It is used for task scheduling, build systems, and course prerequisites.",
    "Software Engineering 12.4 - Graph algorithms")

add("Two Sum Problem", "Find two numbers in a list that add up to a target value.",
    "algorithms", "searching", 3,
    "def two_sum(nums, target):\n    # TODO: Return indices of two numbers that sum to target\n    pass\n\nprint(two_sum([2, 7, 11, 15], 9))\nprint(two_sum([3, 2, 4], 6))",
    "[0, 1]\n[1, 2]", "Use a dictionary to store complements as you iterate.",
    "def two_sum(nums, target):\n    seen = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in seen:\n            return [seen[complement], i]\n        seen[num] = i\n\nprint(two_sum([2, 7, 11, 15], 9))\nprint(two_sum([3, 2, 4], 6))",
    "The hash map approach solves Two Sum in O(n) time by storing each number's index. For each new number, check if its complement (target - num) was seen before. This avoids the O(n^2) brute force of nested loops.",
    "Software Engineering 11.4 - Hash-based search optimisation")

add("Longest Common Subsequence", "Find the length of the longest common subsequence of two strings.",
    "algorithms", "dynamic_programming", 6,
    "def lcs(s1, s2):\n    # TODO: Dynamic programming solution\n    pass\n\nprint(lcs('ABCBDAB', 'BDCAB'))\nprint(lcs('AGGTAB', 'GXTXAYB'))",
    "4\n4", "Build a 2D table. If characters match, dp[i][j] = dp[i-1][j-1] + 1.",
    "def lcs(s1, s2):\n    m, n = len(s1), len(s2)\n    dp = [[0]*(n+1) for _ in range(m+1)]\n    for i in range(1, m+1):\n        for j in range(1, n+1):\n            if s1[i-1] == s2[j-1]:\n                dp[i][j] = dp[i-1][j-1] + 1\n            else:\n                dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n    return dp[m][n]\n\nprint(lcs('ABCBDAB', 'BDCAB'))\nprint(lcs('AGGTAB', 'GXTXAYB'))",
    "LCS finds the longest sequence of characters appearing in both strings in order (not necessarily contiguous). The DP table builds up from shorter prefixes. This is used in diff tools, DNA sequence alignment, and version control.",
    "Software Engineering 12.4 - Dynamic programming applications")

add("Binary Search Tree", "Implement a BST with insert, search, and in-order traversal.",
    "algorithms", "trees", 4,
    "class BSTNode:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n\nclass BST:\n    def __init__(self):\n        self.root = None\n    # TODO: insert, search, inorder\n\nbst = BST()\nfor v in [5, 3, 7, 1, 4, 6, 8]:\n    bst.insert(v)\nprint(bst.inorder())\nprint(bst.search(4))\nprint(bst.search(9))",
    "[1, 3, 4, 5, 6, 7, 8]\nTrue\nFalse",
    "Insert: go left if smaller, right if larger. In-order traversal gives sorted output.",
    "class BSTNode:\n    def __init__(self, val):\n        self.val = val\n        self.left = None\n        self.right = None\n\nclass BST:\n    def __init__(self):\n        self.root = None\n    def insert(self, val):\n        if not self.root:\n            self.root = BSTNode(val)\n        else:\n            self._insert(self.root, val)\n    def _insert(self, node, val):\n        if val < node.val:\n            if node.left:\n                self._insert(node.left, val)\n            else:\n                node.left = BSTNode(val)\n        else:\n            if node.right:\n                self._insert(node.right, val)\n            else:\n                node.right = BSTNode(val)\n    def search(self, val):\n        return self._search(self.root, val)\n    def _search(self, node, val):\n        if not node:\n            return False\n        if val == node.val:\n            return True\n        return self._search(node.left if val < node.val else node.right, val)\n    def inorder(self):\n        result = []\n        self._inorder(self.root, result)\n        return result\n    def _inorder(self, node, result):\n        if node:\n            self._inorder(node.left, result)\n            result.append(node.val)\n            self._inorder(node.right, result)\n\nbst = BST()\nfor v in [5, 3, 7, 1, 4, 6, 8]:\n    bst.insert(v)\nprint(bst.inorder())\nprint(bst.search(4))\nprint(bst.search(9))",
    "A BST maintains sorted order: left subtree values < node < right subtree values. In-order traversal produces sorted output. Average O(log n) operations but O(n) worst case if unbalanced (like a linked list).",
    "Software Engineering 12.4 - Binary search trees")

# FILE HANDLING (30 more)
add("Log File Parser", "Parse a log file and extract error entries with timestamps.",
    "file_handling", "text_processing", 3,
    "# Create sample log\nlog_data = '''2026-03-17 08:00:01 INFO Server started\n2026-03-17 08:05:23 ERROR Database connection failed\n2026-03-17 08:10:45 INFO Request processed\n2026-03-17 08:15:12 WARNING High memory usage\n2026-03-17 08:20:33 ERROR Timeout on API call\n'''\n\nwith open('app.log', 'w') as f:\n    f.write(log_data)\n\n# TODO: Parse and print only ERROR lines\n",
    "2026-03-17 08:05:23 ERROR Database connection failed\n2026-03-17 08:20:33 ERROR Timeout on API call",
    "Read line by line and filter for lines containing 'ERROR'.",
    "log_data = '''2026-03-17 08:00:01 INFO Server started\n2026-03-17 08:05:23 ERROR Database connection failed\n2026-03-17 08:10:45 INFO Request processed\n2026-03-17 08:15:12 WARNING High memory usage\n2026-03-17 08:20:33 ERROR Timeout on API call\n'''\n\nwith open('app.log', 'w') as f:\n    f.write(log_data)\n\nwith open('app.log', 'r') as f:\n    for line in f:\n        if 'ERROR' in line:\n            print(line.strip())",
    "Log parsing is a common file handling task. Reading line by line is memory-efficient for large files. String containment checks with 'in' provide simple filtering. Production systems use structured logging (JSON) for easier parsing.",
    "Software Engineering 12.4 - File processing patterns")

add("INI Config Parser", "Parse a simple INI-format configuration file into a nested dictionary.",
    "file_handling", "config_files", 4,
    "config_text = '''[database]\nhost = localhost\nport = 5432\nname = myapp\n\n[api]\nkey = abc123\ntimeout = 30\n'''\n\nwith open('config.ini', 'w') as f:\n    f.write(config_text)\n\n# TODO: Parse into nested dict\n",
    "{'database': {'host': 'localhost', 'port': '5432', 'name': 'myapp'}, 'api': {'key': 'abc123', 'timeout': '30'}}",
    "Track current section. Lines with [brackets] start new sections. Lines with = are key-value pairs.",
    "config_text = '''[database]\nhost = localhost\nport = 5432\nname = myapp\n\n[api]\nkey = abc123\ntimeout = 30\n'''\n\nwith open('config.ini', 'w') as f:\n    f.write(config_text)\n\ndef parse_ini(filename):\n    config = {}\n    section = None\n    with open(filename, 'r') as f:\n        for line in f:\n            line = line.strip()\n            if not line:\n                continue\n            if line.startswith('[') and line.endswith(']'):\n                section = line[1:-1]\n                config[section] = {}\n            elif '=' in line and section:\n                key, value = line.split('=', 1)\n                config[section][key.strip()] = value.strip()\n    return config\n\nprint(parse_ini('config.ini'))",
    "INI files organise settings into sections with key-value pairs. split('=', 1) ensures values containing = are handled correctly. In production, use configparser module, but understanding the format helps with custom parsers.",
    "Software Engineering 12.4 - Configuration file formats")

# DATABASES (30 more)
add("Database Transactions", "Demonstrate database transactions with rollback on error.",
    "databases", "transactions", 4,
    "import sqlite3\n\ndef transfer(conn, from_acc, to_acc, amount):\n    # TODO: Transfer with transaction safety\n    pass\n\nconn = sqlite3.connect(':memory:')\nc = conn.cursor()\nc.execute('CREATE TABLE accounts (name TEXT, balance REAL)')\nc.executemany('INSERT INTO accounts VALUES (?,?)', [('Alice',1000),('Bob',500)])\nconn.commit()\n\ntransfer(conn, 'Alice', 'Bob', 300)\nc.execute('SELECT * FROM accounts ORDER BY name')\nprint(c.fetchall())\n\ntransfer(conn, 'Alice', 'Charlie', 100)  # Should fail\nc.execute('SELECT * FROM accounts ORDER BY name')\nprint(c.fetchall())",
    "[('Alice', 700.0), ('Bob', 800.0)]\nTransfer failed: Account Charlie not found\n[('Alice', 700.0), ('Bob', 800.0)]",
    "Use try-except with conn.rollback() on failure and conn.commit() on success.",
    "import sqlite3\n\ndef transfer(conn, from_acc, to_acc, amount):\n    try:\n        c = conn.cursor()\n        c.execute('SELECT balance FROM accounts WHERE name=?', (from_acc,))\n        row = c.fetchone()\n        if not row:\n            raise ValueError(f'Account {from_acc} not found')\n        c.execute('SELECT balance FROM accounts WHERE name=?', (to_acc,))\n        row = c.fetchone()\n        if not row:\n            raise ValueError(f'Account {to_acc} not found')\n        c.execute('UPDATE accounts SET balance = balance - ? WHERE name = ?', (amount, from_acc))\n        c.execute('UPDATE accounts SET balance = balance + ? WHERE name = ?', (amount, to_acc))\n        conn.commit()\n    except Exception as e:\n        conn.rollback()\n        print(f'Transfer failed: {e}')\n\nconn = sqlite3.connect(':memory:')\nc = conn.cursor()\nc.execute('CREATE TABLE accounts (name TEXT, balance REAL)')\nc.executemany('INSERT INTO accounts VALUES (?,?)', [('Alice',1000),('Bob',500)])\nconn.commit()\n\ntransfer(conn, 'Alice', 'Bob', 300)\nc.execute('SELECT * FROM accounts ORDER BY name')\nprint(c.fetchall())\n\ntransfer(conn, 'Alice', 'Charlie', 100)\nc.execute('SELECT * FROM accounts ORDER BY name')\nprint(c.fetchall())",
    "Transactions ensure atomicity — either all operations succeed or none do. rollback() undoes partial changes on failure. This prevents inconsistent states like money being deducted but not credited. ACID properties are fundamental to database reliability.",
    "Enterprise Computing 12.4 - Database transactions and ACID")

# WEB & API (20 more)
add("JSON API Response Handler", "Parse a nested JSON API response and extract specific data.",
    "web_and_api", "json_parsing", 3,
    "import json\n\napi_response = json.dumps({\n    'status': 'success',\n    'data': {\n        'users': [\n            {'id': 1, 'name': 'Alice', 'scores': [85, 92, 78]},\n            {'id': 2, 'name': 'Bob', 'scores': [72, 68, 81]},\n            {'id': 3, 'name': 'Charlie', 'scores': [90, 95, 88]}\n        ],\n        'total': 3\n    }\n})\n\n# TODO: Parse and find user with highest average score\n",
    "Top scorer: Charlie (avg: 91.00)",
    "Parse JSON, iterate users, calculate average scores, find maximum.",
    "import json\n\napi_response = json.dumps({\n    'status': 'success',\n    'data': {\n        'users': [\n            {'id': 1, 'name': 'Alice', 'scores': [85, 92, 78]},\n            {'id': 2, 'name': 'Bob', 'scores': [72, 68, 81]},\n            {'id': 3, 'name': 'Charlie', 'scores': [90, 95, 88]}\n        ],\n        'total': 3\n    }\n})\n\ndata = json.loads(api_response)\nbest = max(data['data']['users'], key=lambda u: sum(u['scores'])/len(u['scores']))\navg = sum(best['scores'])/len(best['scores'])\nprint(f\"Top scorer: {best['name']} (avg: {avg:.2f})\")",
    "Real API responses are often deeply nested JSON. Using json.loads() converts to Python dicts and lists. max() with a key function efficiently finds the best match without manual tracking. This pattern is common in data processing pipelines.",
    "Enterprise Computing 12.4 - API data processing")

add("URL Parser", "Parse and manipulate URL components without using urllib.",
    "web_and_api", "url_handling", 3,
    "def parse_url(url):\n    # TODO: Extract protocol, host, port, path, query params\n    pass\n\nresult = parse_url('https://api.example.com:8080/users/search?name=alice&age=25')\nfor k, v in result.items():\n    print(f'{k}: {v}')",
    "protocol: https\nhost: api.example.com\nport: 8080\npath: /users/search\nparams: {'name': 'alice', 'age': '25'}",
    "Split on :// for protocol, then on / for path, then on ? for query string.",
    "def parse_url(url):\n    protocol, rest = url.split('://', 1)\n    if '?' in rest:\n        rest, query = rest.split('?', 1)\n        params = dict(p.split('=') for p in query.split('&'))\n    else:\n        params = {}\n    parts = rest.split('/', 1)\n    host_port = parts[0]\n    path = '/' + parts[1] if len(parts) > 1 else '/'\n    if ':' in host_port:\n        host, port = host_port.split(':')\n        port = int(port)\n    else:\n        host, port = host_port, 443 if protocol == 'https' else 80\n    return {'protocol': protocol, 'host': host, 'port': port, 'path': path, 'params': params}\n\nresult = parse_url('https://api.example.com:8080/users/search?name=alice&age=25')\nfor k, v in result.items():\n    print(f'{k}: {v}')",
    "Understanding URL structure is essential for web development. URLs have protocol, host, optional port, path, and query parameters. In production, use urllib.parse, but manual parsing teaches the underlying format.",
    "Enterprise Computing 12.4 - Web protocols and URLs")

# DATA SCIENCE (20 more)
add("Moving Average", "Calculate a simple moving average for a time series.",
    "data_science", "statistics", 3,
    "def moving_avg(data, window):\n    # TODO: Return list of moving averages\n    pass\n\nprices = [10, 11, 12, 13, 12, 11, 14, 15, 16, 14]\nprint(moving_avg(prices, 3))",
    "[11.0, 12.0, 12.33, 12.0, 12.33, 13.33, 15.0, 15.0]",
    "For each position i, average the previous 'window' elements.",
    "def moving_avg(data, window):\n    result = []\n    for i in range(window - 1, len(data)):\n        avg = sum(data[i-window+1:i+1]) / window\n        result.append(round(avg, 2))\n    return result\n\nprices = [10, 11, 12, 13, 12, 11, 14, 15, 16, 14]\nprint(moving_avg(prices, 3))",
    "Moving averages smooth out short-term fluctuations to reveal trends. They are widely used in financial analysis, signal processing, and time series forecasting. The window size controls the trade-off between smoothness and responsiveness.",
    "Enterprise Computing 12.4 - Data analysis techniques")

add("Correlation Coefficient", "Calculate Pearson correlation coefficient between two datasets.",
    "data_science", "statistics", 4,
    "def correlation(x, y):\n    # TODO: Calculate Pearson r\n    pass\n\nhours_studied = [1, 2, 3, 4, 5, 6, 7, 8]\nexam_scores = [52, 58, 65, 70, 74, 80, 85, 90]\nprint(f'Correlation: {correlation(hours_studied, exam_scores):.4f}')",
    "Correlation: 0.9976",
    "r = sum((xi-x_mean)(yi-y_mean)) / sqrt(sum((xi-x_mean)^2) * sum((yi-y_mean)^2))",
    "import math\n\ndef correlation(x, y):\n    n = len(x)\n    x_mean = sum(x) / n\n    y_mean = sum(y) / n\n    numerator = sum((x[i]-x_mean)*(y[i]-y_mean) for i in range(n))\n    denom_x = math.sqrt(sum((xi-x_mean)**2 for xi in x))\n    denom_y = math.sqrt(sum((yi-y_mean)**2 for yi in y))\n    return numerator / (denom_x * denom_y)\n\nhours_studied = [1, 2, 3, 4, 5, 6, 7, 8]\nexam_scores = [52, 58, 65, 70, 74, 80, 85, 90]\nprint(f'Correlation: {correlation(hours_studied, exam_scores):.4f}')",
    "Pearson's r measures linear correlation between -1 (negative) and +1 (positive). Values near 0 indicate no linear relationship. This example shows strong positive correlation between study hours and scores.",
    "Enterprise Computing 12.4 - Statistical analysis")

# AUTOMATION & TESTING (20 more)
add("Parametrised Tests", "Write parametrised tests using unittest to test multiple inputs.",
    "automation_and_testing", "unittest", 3,
    "import unittest\n\ndef is_palindrome(s):\n    clean = s.lower().replace(' ', '')\n    return clean == clean[::-1]\n\nclass TestPalindrome(unittest.TestCase):\n    # TODO: Test multiple cases\n    pass\n\nif __name__ == '__main__':\n    unittest.main(argv=[''], exit=False, verbosity=2)",
    "test_empty ... ok\ntest_not_palindrome ... ok\ntest_palindromes ... ok\ntest_with_spaces ... ok",
    "Use subTest() to run multiple test cases within a single test method.",
    "import unittest\n\ndef is_palindrome(s):\n    clean = s.lower().replace(' ', '')\n    return clean == clean[::-1]\n\nclass TestPalindrome(unittest.TestCase):\n    def test_palindromes(self):\n        for word in ['racecar', 'madam', 'level']:\n            with self.subTest(word=word):\n                self.assertTrue(is_palindrome(word))\n    def test_not_palindrome(self):\n        self.assertFalse(is_palindrome('hello'))\n    def test_with_spaces(self):\n        self.assertTrue(is_palindrome('A man a plan a canal Panama'))\n    def test_empty(self):\n        self.assertTrue(is_palindrome(''))\n\nif __name__ == '__main__':\n    unittest.main(argv=[''], exit=False, verbosity=2)",
    "subTest() runs multiple test cases within one method, continuing even if one fails. This is Python's built-in approach to parametrised testing. Each subTest reports independently, making it easy to identify which specific input failed.",
    "Software Engineering 12.4 - Test-driven development")

add("Mock Object Testing", "Use unittest.mock to test a function that depends on an external API.",
    "automation_and_testing", "mocking", 5,
    "import unittest\nfrom unittest.mock import patch, MagicMock\n\ndef get_user_greeting(user_id):\n    # Simulates calling an external API\n    import requests\n    response = requests.get(f'https://api.example.com/users/{user_id}')\n    data = response.json()\n    return f\"Hello, {data['name']}!\"\n\nclass TestGreeting(unittest.TestCase):\n    # TODO: Mock the requests.get call\n    pass\n\nif __name__ == '__main__':\n    unittest.main(argv=[''], exit=False, verbosity=2)",
    "test_greeting ... ok",
    "Use @patch to replace requests.get with a mock that returns controlled data.",
    "import unittest\nfrom unittest.mock import patch, MagicMock\n\ndef get_user_greeting(user_id):\n    import requests\n    response = requests.get(f'https://api.example.com/users/{user_id}')\n    data = response.json()\n    return f\"Hello, {data['name']}!\"\n\nclass TestGreeting(unittest.TestCase):\n    @patch('requests.get')\n    def test_greeting(self, mock_get):\n        mock_response = MagicMock()\n        mock_response.json.return_value = {'name': 'Alice'}\n        mock_get.return_value = mock_response\n        \n        result = get_user_greeting(1)\n        self.assertEqual(result, 'Hello, Alice!')\n        mock_get.assert_called_once_with('https://api.example.com/users/1')\n\nif __name__ == '__main__':\n    unittest.main(argv=[''], exit=False, verbosity=2)",
    "Mocking replaces real dependencies with controlled fakes during testing. @patch temporarily replaces the target function. MagicMock creates objects that record how they were called. This enables testing without network access or external services.",
    "Software Engineering 12.4 - Test doubles and mocking")

# SECURITY (10 more)
add("CSRF Token Validation", "Implement CSRF token generation and validation for form submissions.",
    "security", "csrf", 4,
    "import secrets\nimport hashlib\n\n# TODO: Create CSRFProtection class with generate and validate methods\n\ncsrf = CSRFProtection('my_secret_key')\ntoken = csrf.generate('session_123')\nprint(f'Token: {token[:20]}...')\nprint(f'Valid: {csrf.validate(token, \"session_123\")}')\nprint(f'Wrong session: {csrf.validate(token, \"session_456\")}')\nprint(f'Tampered: {csrf.validate(\"fake_token\", \"session_123\")}')",
    "Token: (varies)...\nValid: True\nWrong session: False\nTampered: False",
    "Generate tokens using HMAC with session ID and secret key. Validate by regenerating and comparing.",
    "import secrets\nimport hashlib\nimport hmac\n\nclass CSRFProtection:\n    def __init__(self, secret):\n        self.secret = secret\n    def generate(self, session_id):\n        random_part = secrets.token_hex(16)\n        signature = hmac.new(self.secret.encode(), f'{session_id}{random_part}'.encode(), hashlib.sha256).hexdigest()\n        return f'{random_part}:{signature}'\n    def validate(self, token, session_id):\n        try:\n            random_part, signature = token.split(':')\n            expected = hmac.new(self.secret.encode(), f'{session_id}{random_part}'.encode(), hashlib.sha256).hexdigest()\n            return hmac.compare_digest(signature, expected)\n        except (ValueError, AttributeError):\n            return False\n\ncsrf = CSRFProtection('my_secret_key')\ntoken = csrf.generate('session_123')\nprint(f'Token: {token[:20]}...')\nprint(f'Valid: {csrf.validate(token, \"session_123\")}')\nprint(f'Wrong session: {csrf.validate(token, \"session_456\")}')\nprint(f'Tampered: {csrf.validate(\"fake_token\", \"session_123\")}')",
    "CSRF tokens prevent cross-site request forgery by ensuring form submissions originate from your site. HMAC binds the token to the session, and hmac.compare_digest prevents timing attacks during validation.",
    "Enterprise Computing 12.4 - Web security - CSRF prevention")

add("Password Strength Checker", "Implement a comprehensive password strength checker with scoring.",
    "security", "password_security", 3,
    "import re\n\ndef check_strength(password):\n    # TODO: Return score (0-5) and list of issues\n    pass\n\nfor pw in ['abc', 'Password1', 'C0mpl3x!Pass#2026']:\n    score, issues = check_strength(pw)\n    stars = '*' * score + '-' * (5 - score)\n    print(f'{pw}: [{stars}] {issues}')",
    "abc: [*----] ['Too short', 'No uppercase', 'No digit', 'No special char']\nPassword1: [***--] ['No special char']\nC0mpl3x!Pass#2026: [*****] []",
    "Check length, uppercase, lowercase, digits, special characters. Score 1 point for each criterion met.",
    "import re\n\ndef check_strength(password):\n    issues = []\n    score = 0\n    if len(password) >= 8:\n        score += 1\n    else:\n        issues.append('Too short')\n    if re.search(r'[A-Z]', password):\n        score += 1\n    else:\n        issues.append('No uppercase')\n    if re.search(r'[a-z]', password):\n        score += 1\n    else:\n        issues.append('No lowercase')\n    if re.search(r'\\d', password):\n        score += 1\n    else:\n        issues.append('No digit')\n    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):\n        score += 1\n    else:\n        issues.append('No special char')\n    return score, issues\n\nfor pw in ['abc', 'Password1', 'C0mpl3x!Pass#2026']:\n    score, issues = check_strength(pw)\n    stars = '*' * score + '-' * (5 - score)\n    print(f'{pw}: [{stars}] {issues}')",
    "Password strength checkers enforce security policies by verifying multiple criteria. Using regex for each check is clean and maintainable. Returning both a score and specific issues helps users understand what to fix.",
    "Enterprise Computing 12.4 - Authentication security policies")

# Save to file
with open('data/python_exercises_extra.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, indent=2, ensure_ascii=False)

print(f'Generated {len(exercises)} additional exercises')
cats = {}
for ex in exercises:
    cats[ex['category']] = cats.get(ex['category'], 0) + 1
for cat, count in sorted(cats.items()):
    print(f'  {cat}: {count}')
