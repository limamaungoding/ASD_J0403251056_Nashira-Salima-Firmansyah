buah = ['Apel', 'Buah Naga', 'Ceri']
try:
    x = buah.index("Ceri")
except ValueError:
    x = -1
try:
    y = buah.index("Kedondong")
except ValueError:
    y = -1
print(x)
print(y)
# Output
# 2
# -1