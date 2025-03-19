# Write your code here.
print('\n')
print('---------------------------')
print('Task 1: Hello') 
def hello():
    return 'Hello!'

print(hello())

print('\n')
print('---------------------------')
print('Task 2: Greet with a Formatted String')
def greet(name):
    return (f"Hello, {name}!")

print(greet("Amir"))

print('\n')     
print('---------------------------')
print('Task 3: Calculator')
def calc(arg1, arg2, operator="multiply"):
    try:
        match operator:
            case 'add':
                return arg1 + arg2
            case 'subtract':
                return arg1 - arg2
            case 'multiply':
                return arg1 * arg2
            case 'divide':
                return arg1 / arg2
            case 'modulo':
                return arg1 % arg2
            case 'int_divide':
                return arg1 // arg2
            case 'power':
                return arg1 ** arg2
            case _:
                raise ValueError('Pass the correct operator')
    except ZeroDivisionError:
        return 'You can\'t divide by 0!'
    except TypeError:
        return f'You can\'t {operator} those values!'
    
print(calc(3,2,'int_divide'))
print(calc(5, 3))
print(calc(5, 0, "divide"))
print(calc(5, 0, "int_divide"))
print(calc("hello", 3))
print(calc(5, "world", "add"))


print('\n')
print('---------------------------')
print('Task 4: Data Type Conversion')
def data_type_conversion(value, data_type):

    try:
        match data_type:
            case 'float':
                return float(value)
            case 'str':
                return str(value)
            case 'int':
                return int(value)
            case _: 
                raise TypeError(f'Incorrect data type {data_type}')
     
    except (ValueError):
        return f'You can\'t convert {value} into a {data_type}.'

print(data_type_conversion('nonesense', 'float'))
print(data_type_conversion(123, "str"))
print(data_type_conversion("456", "int"))
print(data_type_conversion("3.14", "float"))
print(data_type_conversion("hello", "int"))
print(data_type_conversion("abc", "float"))


print('\n')
print('---------------------------')
print('Task 5: Grading System, Using *args')
# Create a grade function. It should collect an arbitrary number of parameters, compute the average, and return the grade. based on the following scale:
def grade(*args):
    try:
        average = sum(args)/len(args)
        # A: 90 and above
        if average >= 90:
            return 'A'
        # B: 80-89
        elif 80 <= average < 90:
            return 'B'
        # C: 70-79
        elif 70 <= average < 80:
            return 'C'
        # D: 60-69
        elif 60 <= average < 70:
            return 'D'
        # F: Below 60
        else:
            return 'F'
    except:
        return f'Invalid data was provided.'

print(grade(95, 83, 90, 47, 65, 76, 89, 98, 99))
print(grade(95, 83, 90, 47, 65, 76, 89, 98, 99, "hello"))


print('\n')
print('---------------------------')
print('Task 6: Use a For Loop with a Range')
def repeat(string, count):
    new = ''
    for i in range(count):
        new += string
    return new
    
print(repeat('*', 3))


print('\n')
print('---------------------------')
print('Task 7: Student Scores, Using **kwargs')
def student_scores(param, **kwargs):
    if param == 'best':
         return max(kwargs, key=kwargs.get)
    elif param == 'mean':
        return sum(kwargs.values())/len(kwargs)

print(student_scores('best', Amir=95, Ane=83, Kim=90, Bill=47))
print(student_scores('mean', Amir=95, Ane=83, Kim=90, Bill=47))


print('\n')
print('---------------------------')
print('Task 8: Titleize, with String and List Operations')
def titleize(string):
    words = string.split()
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word.lower() in ["a", "on", "an", "the", "of", "and", "is", "in"]:
            words[i] = word.lower()
        else:
            words[i] = word.capitalize()
    return ' '.join(words)

print(titleize("the lord of the rings"))


print('\n')
print('---------------------------')
print('Task 9: Hangman, with more String Operations')
def hangman(secret, guess):
    result = ""
    for char in secret:
        if char in guess:
            result += char
        else:
            result += "_"
    return result

print(hangman("alphabet", "ab"))
print(hangman("difficulty", "ic"))


print('\n')
print('---------------------------')
print('Task 10: Pig Latin, Another String Manipulation Exercise')

def pig_latin(text):
    vowels = "aeiou"
    result = []
    
    for word in text.split():
        if word[0] in vowels:
            # Case 1: word starts with a vowel
            result.append(word + "ay")
        elif word[:2] == "qu":
            # Case 2a: word starts with "qu"
            result.append(word[2:] + "quay")
        elif "qu" in word[:4]:
            # Case 2b: word has "qu" after initial consonants
            qu_index = word.find("qu")
            result.append(word[qu_index+2:] + word[:qu_index+2] + "ay")
        else:
            # Case 3: word starts with consonants
            i = 0
            while i < len(word) and word[i] not in vowels:
                i += 1
            result.append(word[i:] + word[:i] + "ay")
    
    return " ".join(result)

print(pig_latin("apple"))
print(pig_latin("banana"))
print(pig_latin("cherry"))
print(pig_latin("quiet"))
print(pig_latin("square"))
print(pig_latin("the quick brown fox"))


