# -------------------kendi exception sinifimizi olusturduk ---------------------
class AgeException(Exception):
    def __init__(self, msg="age can not be negative"):
        self.msg=msg
        super().__init__(self.msg)

# -------------------bu method ile kontrolden gecer--------------------------
def check_Age(yas):
    if yas<0:
        raise AgeException()
    print("your age is fine")

try:
    check_Age(-1)
except AgeException as e:
    print(f"MY ERROR : {e}")