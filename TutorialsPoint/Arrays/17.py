# Adding and Removing Elements
# Below methods are used for appending, extending, inserting, and removing elements from arrays −
#
# Sr.No.	Methods with Description
# 1
# append(x)
#
# Appends a new item with value x to the end of the array.
#
# 2
# extend(iterable)
#
# Appends items from iterable to the end of the array.
#
# 3
# insert(i, x)
#
# Inserts a new item with value x before position i.
#
# 4
# pop([i])
#
# Removes and returns the item with index i. If i is not specified, removes and returns the last item.
#
# 5
# remove(x)
#
# Removes the first occurrence of x from the array.
#
# Information and Utility Methods
# These methods are used for obtaining information about arrays and to perform utility operations −
#
# Sr.No.	Methods with Description
# 1
# buffer_info()
#
# Returns a tuple (address, length) giving the current memory address and the length in elements of the buffer used to hold the arrays contents.
#
# 2
# count(x)
#
# Returns the number of occurrences of x in the array.
#
# 3
# index(x[, start[, stop]])
#
# Returns the smallest index where x is found in the array. Optional start and stop arguments can specify a sub-range to search.
#
# Manipulating Array Elements
# Following methods are used for manipulating array elements, such as reversing the array or byteswapping values.
#
# Sr.No.	Methods with Description
# 1
# reverse()
#
# Reverses the order of the items in the array.
#
# 2
# byteswap()
#
# "Byteswaps" all items of the array, useful for reading data from a file written on a machine with a different byte order.
#
# Conversion Methods
# These methods are used to convert arrays to and from bytes, files, lists, and Unicode strings.
#
# Sr.No.	Methods with Description
# 1
# frombytes(buffer)
#
# Appends items from the bytes-like object, interpreting its content as an array of machine values.
#
# 2
# tobytes()
#
# Converts the array to a bytes representation.
#
# 3
# fromfile(f, n)
#
# Reads n items from the file object f and appends them to the array.
#
# 4
# tofile(f)
#
# Writes all items to the file object f.
#
# 5
# fromlist(list)
#
# Appends items from the list to the array.
#
# 6
# tolist()
#
# Converts the array to a list with the same items.
#
# 7
# fromunicode(s)
#
# Extends the array with data from the given Unicode string. The array must have type code 'u'.
#
# 8
# tounicode()
#
# Converts the array to a Unicode string. The array must have type code 'u'.