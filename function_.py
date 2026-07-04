"""
function_.py

Covers:
- Defining and calling functions (def, function())
- Parameters vs arguments
- Local variables vs global variables
- Positional arguments vs keyword arguments (and mixing them - positional first)
- Default parameter values
- *args (variable positional arguments, becomes a tuple)
- **kwargs (variable keyword arguments, becomes a dict)
- return statement, functions with no return (returns None by default)
- Multiple return statements, returning multiple values (as a tuple)
- Function categories: action, transformation, validation, orchestrator
"""

user = input("write any greeting- good morning / good afternoon / good night:")

if user =="gm":
    name = "good morning"
elif user == "good afternoon":
    name = "good afternoon"
else:
    name = " good night"
 
def greet():
    print(f"hello {name}")

greet()

text = "   i Want to CLean THIS text"
def clean_text(text):
    print(text.strip().lower())

clean_text(text)

def clean_text(text):
    cleaned = text.strip().lower()
    print(cleaned)

clean_text("ANY value Can Be cLEANed..   ")

def my_name(first_name  , last_name):
    first = text.strip().lower()
    last = text.strip().lower()
    print(first +  " " + last)

my_name("vINita  " , "patidar")
my_name(last_name="patidar",first_name= "vINita  " )


def your_currentclass(clas , roll_no , school = "DPS"):
    print(f"i study in {clas} class, and my roll number is {roll_no}, and my school name is {school}")


your_currentclass(2,201)


def add_no(*args):
    print(type(args))
    print(sum(args))

add_no(1,2,3)
add_no(1,2,3,4,5,6,7)


def user_profile(**kwargs):
    print(type(kwargs))
    print(kwargs)

user_profile(name="vinita", age=21 , country="India")


def my_full_name(first_name  , last_name):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    return first +  " " + last

my_namee = my_full_name("vinita   " , "PatidaR ")
print(my_namee)

def my_full_name(first_name  , last_name):
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    #return first +  " " + last

my_namee = my_full_name("vinita   " , "PatidaR ")
print(my_namee) 

def my_full_name(first_name  , last_name):
    if not name:
        return None
    else:
        first = first_name.strip().lower()
        last = last_name.strip().lower()
        return first +  " " + last
my_namee = my_full_name("vinita   " , "PatidaR ")
print(my_namee)

def my_full_name(first_name  , last_name):
    lo_first = first_name.strip().lower()
    lo_last = last_name.strip().lower()
    lower_name = lo_first +  " " + lo_last 
    up_first = first_name.strip().upper()
    up_last = last_name.strip().upper()
    upper_name = up_first +  " " + up_last 
    return lower_name, upper_name

x = my_full_name("vinita", "PATIDAR")
print(x)


def clean_split(email):
    cl_email = email.strip().lower()
    username , domain = cl_email.split("@")
    return {"username" : username , "domain" : domain}

pr_gmail = clean_split("   vinita@gmail.coM")
print(pr_gmail)