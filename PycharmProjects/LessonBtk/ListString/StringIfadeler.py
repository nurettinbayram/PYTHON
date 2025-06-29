website = "http://www.sadikturan.com"
course = "Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"

print(len(course))
print(website[7:10])
print(website[-3:])
print(course[:15])
print(course[-15:])
print(course[::-1])

repl = course.replace(' ', '->').replace('i','/')
print(course)
print(repl)
print(course.center(100, '*'))