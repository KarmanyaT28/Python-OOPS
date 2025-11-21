'''

The os.path is another Python module, which also provides a big range of useful methods to manipulate files and directories. Most of the useful methods are listed here −

Sr.No.	Methods with Description
1	os.path.abspath(path)
Returns a normalized absolutized version of the pathname path.

2	os.path.basename(path)
Returns the base name of pathname path.

3	os.path.commonprefix(list)
Returns the longest path prefix (taken character-by-character) that is a prefix of all paths in list.

4	os.path.dirname(path)
Returns the directory name of pathname path.

5	os.path.exists(path)
Returns True if path refers to an existing path. Returns False for broken symbolic links.

6	os.path.lexists(path)
Returns True if path refers to an existing path. Returns True for broken symbolic links.

7	os.path.expanduser(path)
On Unix and Windows, returns the argument with an initial component of ~ or ~user replaced by that user's home directory.

8	os.path.expandvars(path)
Returns the argument with environment variables expanded.

9	os.path.getatime(path)
Returns the time of last access of path.

10	os.path.getmtime(path)
Returns the time of last modification of path.

11	os.path.getctime(path)
Returns the system's ctime, which on some systems (like Unix) is the time of the last change, and, on others (like Windows), is the creation time for path.

12	os.path.getsize(path)
Returns the size, in bytes, of path.

13	os.path.isabs(path)
Returns True if path is an absolute pathname.

14	os.path.isfile(path)
Returns True if path is an existing regular file.

15	os.path.isdir(path)
Returns True if path is an existing directory.

16	os.path.islink(path)
Returns True if path refers to a directory entry that is a symbolic link.

17	os.path.ismount(path)
Returns True if pathname path is a mount point: a point in a file system where a different file system has been mounted.

18	os.path.join(path1[, path2[, ...]])
Joins one or more path components intelligently.

19	os.path.normcase(path)
Normalizes the case of a pathname.

20	os.path.normpath(path)
Normalizes a pathname.

21	os.path.realpath(path)
Returns the canonical path of the specified filename, eliminating any symbolic links encountered in the path

22	os.path.relpath(path[, start])
Returns a relative filepath to path either from the current directory or from an optional start point.

23	os.path.samefile(path1, path2)
Returns True if both pathname arguments refer to the same file or directory

24	os.path.sameopenfile(fp1, fp2)
Returns True if the file descriptors fp1 and fp2 refer to the same file.

25	os.path.samestat(stat1, stat2)
Returns True if the stat tuples stat1 and stat2 refer to the same file.

26	os.path.split(path)
Splits the pathname path into a pair, (head, tail) where tail is the last pathname component and head is everything leading up to that.

27	os.path.splitdrive(path)
Splits the pathname path into a pair (drive, tail) where drive is either a drive specification or the empty string.

28	os.path.splitext(path)
Splits the pathname path into a pair (root, ext) such that root + ext == path, and ext is empty or begins with a period and contains at most one period.

29	os.path.walk(path, visit, arg)
Calls the function visit with arguments (arg, dirname, names) for each directory in the directory tree rooted at path (including path itself, if it is a directory).

'''