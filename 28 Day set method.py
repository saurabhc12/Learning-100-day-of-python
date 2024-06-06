s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))

print(s1,  s2)

s1.update(s2)

s3 = {1,2,3,4}
s4 = {1,2,3,4,5}
s3.intersection_update(s4)
print(s3)

s3.symmetric_difference_update(s4)
print(s3)

s3.symmetric_difference_update(s4)
print(s3)

s3.isdisjoint(s4)
print(s3)

s3.issuperset(s4)
print(s3)

s3.add(6)
print(s3)
