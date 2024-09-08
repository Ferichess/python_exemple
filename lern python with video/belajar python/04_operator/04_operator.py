# OPERATOR
## Aritmatic Operator
# * pada table ini `X` bernilai 5 dan `Y` bernilai 10
# * operator | name | example
# | + | Addition | X+Y = 15 |
# | - | Subtraction | X-Y = -5 |
# | * | Multiplication | X*Y = 50 |
# | / | Division | Y/X = 2 or 0.5 |
# | % | Modulus | X%Y = 0 |
# | ** | Exponentiation | X**Y = 10**2 = 100 |
# | // | Floor Division | X//Y = 9//2 = 4 |

### Penjumlahan
# penjumalahan int
int_a = 20
int_b = 5
float_c = 3.14

print(int_a + int_b)
print(float_c + int_b)
# augmented penjumalahan
int_a += int_b
print(int_a)

### pengurangan

# pengurangan int
int_a = 8
int_b = 15
float_c = 98.9

print(int_a - int_b)
print(float_c - int_b)
# augmented pengurangan
int_a -= int_b
print(int_a)

### perkalian

# perkalian int
int_a = 8
int_b = 15
float_c = 7.5

print(int_a * int_b)
print(float_c * int_b)
# augmented perkalian
int_a *= int_b
print(int_a)

### pembagian

# pembagian int
int_a = 30
int_b = 3
float_c = 2.5

print(int_a / int_b)
print(float_c / int_b)
# augmented pembagian
int_a /= int_b
print(int_a)

### modulus

# modulus int
int_a = 50
int_b = 3

print(int_a % int_b)
# augmented modulus
int_a %= int_b
print(int_a)

### perpangkatan

# perpangkatan int
int_a = 5
int_b = 2

print(int_a**int_b)
# augmented perpangkatan
int_a **= int_b
print(int_a)

### Floor Division/Integer Division

# floor division int
int_a = 12
int_b = 6

print(int_a // int_b)
# augmented floor division
int_a //= int_b
print(int_a)

## Assignment Operator
# * Melakukan Assign ke variable dengan nilai yang ditentukan, dengan menggunakan sintax ‘=‘ .
# * Variable assignment sudah dilakukan tadi di materi variable.

## Comparison Operator
# pada table ini `X` bernilai 5 dan `Y` bernilai 10
# operator | name | example
# | < | Jika Nilai dari x kecil dari y maka akan bernilai true, jika sebaliknya bernilai false | X<Y |
# | > | Jika Nilai dari x besar dari y akan bernilai true, jika sebaliknya bernilai false | X>Y |
# | <= | Jika nilai x lebih kecil atau sama dengan y, maka bernilai true, jika lebih besar maka bernilai false | X<=Y |
# | >= | Jika nilai x lebih besar atau sama dengan y, maka bernilai true, jika lebih besar maka bernilai false | X>=Y |
# | == | Jika nilai x sama dengan y, maka bernilai true, jika tidak bernilai false | X==Y |
# | != | Jika nilai x tidak sama dengan y, maka bernilai true, jika tidak bernilai false | X!=Y |

x = 5
y = 10

print("x =", x, "y =", y, "x < y is", x < y)
print("x =", x, "y =", y, "x > y is", x > y)
print("x =", x, "y =", y, "x <= y is", x <= y)
print("x =", x, "y =", y, "x >= y is", x >= y)
print("x =", x, "y =", y, "x == y is", x == y)
print("x =", x, "y =", y, "x != y is", x != y)

## chained comparison operator

a = 5
b = 7
c = 3
print(a < b > c)
print(a < b < c)

## Logical Operator

## | x | y | x and y |
## | false | false | false |
## | false | true | false |
## | true | false | false |
## | true | true | true |

## | x | y | x or y |
## | false | false | false |
## | false | true | true |
## | true | false | true |
## | true | true | true |

## | x | not x |
## | false | true |
## | true | false |

## and oprator
a = 5
b = 7

false_value_ab = a > b
true_value_ab = a <= b

c = 3
d = 5

false_value_cd = c == d
true_value_cd = c != d

print("and =", false_value_ab and false_value_cd)
print("and =", false_value_ab and true_value_cd)
print("and =", true_value_ab and false_value_cd)
print("and =", true_value_ab and true_value_cd)

## or operator

a = 5
b = 7

false_value_ab = a > b
true_value_ab = a <= b

c = 3
d = 5

false_value_cd = c == d
true_value_cd = c != d

print("or =", false_value_ab or false_value_cd)
print("or =", false_value_ab or true_value_cd)
print("or =", true_value_ab or false_value_cd)
print("or =", true_value_ab or true_value_cd)

## not operator

a = 5
b = 7

false_value_ab = a > b
true_value_ab = a <= b

c = 3
d = 5

false_value_cd = c == d
true_value_cd = c != d

print("not =", not false_value_ab)
print("not =", not true_value_ab)
print("not =", not false_value_cd)
print("not =", not true_value_cd)
