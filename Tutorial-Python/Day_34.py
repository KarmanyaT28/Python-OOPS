# Dictionary Methods

# Update method

emp_reviews = {
    122340203: 4.0,
    122340204: 3.0,
    122340205: 2.0,
    122340206: 1.0,
    122340207: 5.0,
    122340208: 4.0,
    122340209: 4.0,
    1223402010: 4.2,
}

print(emp_reviews)

emp_reviews_1 = {
    1223402011: 5.0,
    1223402012: 4.0,
}

emp_reviews.update(emp_reviews_1)
print(emp_reviews)

'''
Set is unordered
Dictionaries are ordered from python3.7
'''

print(emp_reviews_1.clear())

print(emp_reviews.pop(122340203))
print(emp_reviews.popitem())
print(emp_reviews)


# del emp_reviews
del emp_reviews[122340205]
print(emp_reviews)


# databases - mongo or pymongo or django


