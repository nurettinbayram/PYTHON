# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!
# Here's the deal: It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# "    Hello     World   "  =>  "#HelloWorld"

def generate_hashtag(s):
    if s == "":
        return False

    myList = s.split()
    m ="#"
    for i in myList:
       m +=i.title()
    return m  if len(m)<=140 else False

print("result ---> ",  generate_hashtag(""))

# II. yol
def generate_hashtag(s):
    return s if s and len(s := "#" + s.title().replace(" ", "")) <= 140 else False