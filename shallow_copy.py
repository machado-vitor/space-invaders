original = [[1, 2], [3, 4]]
shallow = original[:]  # shallow copy
# it creates a new container,
# but the elements are references to the original objects
# This is good
print("original: " + str(original))
print("shallow copy: " + str(shallow))

print("appending to shallow..")
shallow[0].append(99)

print("original: " + str(original))  # [[1, 2, 99], [3, 4]]  # inner list changed in both
print("shallow copy: " + str(shallow))  # [[1, 2, 99], [3, 4]]  # inner list changed in both

print("removing from shallow..")
shallow.pop()

print("original: " + str(original))
print("shallow copy: " + str(shallow))
