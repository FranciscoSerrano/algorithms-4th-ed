'''
Sorting Three Numbers
Suppose that variables a, b, c, and t, are all of the same numeric primartive type.
Show that the following code puts a, b, and c in acending order.

if (a > b) { t = a; a = b; b = t; }
if (a > c) { t = a; a = c; c = t; }
if (b > c) { t = b; b = c; c = t; }
'''

a = 22
b = 42
c = 31
t = 0

if a > b:
    t = a
    a = b
    t = b
if a > c:
    t = a
    a = c
    c = t
if b > c:
    t = b
    b = c
    c = t

print(a, b, c)

# This seems pretty straight forward. T is acting as a Temporary variable to hold the orginal value
# of a variable because when its changed the original value is obvioiusly lost.
