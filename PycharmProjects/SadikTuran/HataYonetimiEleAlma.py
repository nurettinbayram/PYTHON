
# try:
#     a=int("abc")
# except ValueError:
#     print("verinin tutunu kontrol et")
# except Exception as e:
#     print(f"Bir hata olustu -->  {e}")


# --------------hata mesajini ve turunuyakalama ------------------------
# try:
#     #a=int("a")
#     c=4/0
# except Exception as e:
#     print(f"bir hata olustu --> {e}")
#     print(f"hata tipi --> {type(e)}")
#     print(f"hata sinifi ismi --> {type(e).__name__}")
#
# # else: Hata yoksa çalışır.
# # finally: Ne olursa olsun çalışır.

# -------------------------- raise ------------------------
# x=int(input("yasini gir : " ))
# if x<0:
#     raise ValueError("negatif edeger girilemez.")#hata mesaji olarak yazdirilir
# print(f"yasiniz {x}")
#

import logging

logging.basicConfig(filename='log.txt', level=logging.ERROR)

try:
    result = 10 / "a"
except ZeroDivisionError as e:
    logging.error(f"My ERROR: Zerro Divition Error : {e} Error Type : {type(e)}")

except TypeError as e:
    logging.error(f"Check Type of your variable : {e} Error Type : {type(e)}")

except Exception as e:
    logging.error(f"General Exception : {e} Error Type : {type(e)}")