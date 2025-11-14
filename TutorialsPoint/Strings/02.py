# --- Initial Variables for Demonstration ---
var2 = " \tpython OOp & F-sTRINGs\n "
var_num = "123456"
var_prefix = "FILE_report.txt"
var_list = ['user', 'data', 'file']
var_tab = "Col1\tCol2\tCol3"
var_sentence = "This Is A Title"
var_encoding = "Café"
var_bytes = b"decoded string"
var_mapping = {'name': 'Alice', 'age': 30}
var_unicode_num = "½"

print("--- Initial Test String (var2) ---")
print(f"'{var2}'")
print("-" * 30)

# ====================================================================
# 1. Basic Case and Alignment (1-3)
# ====================================================================

print("\n--- Basic Case and Alignment ---")
print(f"1. capitalize():   '{var2.capitalize()}'")
print(f"2. casefold():     '{var2.casefold()}'")
# Note: Use a larger width for 'center' since var2 is long
print(f"3. center(40, '='): '{var2.strip().center(40, '=')}'")
print("-" * 30)

# ====================================================================
# 2. Search, Count, and Validation (4, 7, 9, 12, 13-24, 34, 35, 42)
# ====================================================================

print("\n--- Search, Count, and Validation ---")
print(f"4. count('OOp'):   {var2.count('OOp')}")
print(f"7. endswith('s\\n '): {var2.endswith('s\n ')}")
print(f"9. find('OOp'):    {var2.find('OOp')}")
print(f"12. index('OOp'):  {var2.index('OOp')}")
# 13-24 Validation Methods (Applied to cleaned or specific strings)
print(f"13. 'A1'.isalnum(): { 'A1'.isalnum() }")
print(f"14. 'Alpha'.isalpha(): { 'Alpha'.isalpha() }")
print(f"15. 'Ascii'.isascii(): { 'Ascii'.isascii() }")
print(f"16. '{var_unicode_num}'.isdecimal(): { var_unicode_num.isdecimal() }")
print(f"17. '{var_num}'.isdigit(): { var_num.isdigit() }")
print(f"18. 'valid_id'.isidentifier(): { 'valid_id'.isidentifier() }")
print(f"19. 'lower'.islower(): { 'lower'.islower() }")
print(f"20. '{var_unicode_num}'.isnumeric(): { var_unicode_num.isnumeric() }")
print(f"21. isprintable(): { 'hello'.isprintable() }")
print(f"22. isspace(): { ' \t\n'.isspace() }")
print(f"23. istitle(): { var_sentence.istitle() }")
print(f"24. isupper(): { 'UPPER'.isupper() }")
print(f"34. rfind('OOp'):  {var2.rfind('OOp')}")
print(f"35. rindex('OOp'): {var2.rindex('OOp')}")
print(f"42. startswith(' \\t'): {var2.startswith(' \t')}")
print("-" * 30)


# ====================================================================
# 3. Manipulation (5, 6, 8, 25-33, 36-41, 43-48)
# ====================================================================

print("\n--- Manipulation and Formatting ---")
# Encoding/Decoding (Requires bytes for decode)
print(f"5. decode():       {var_bytes.decode('utf-8')}")
print(f"6. encode():       {var_encoding.encode('utf-8')}")
print(f"8. expandtabs():   {var_tab.expandtabs(2)}")
# Formatting
print(f"10. format():      {'Name: {0}, Age: {1}'.format('Alice', 30)}")
print(f"11. format_map():  {'Name: {name}, Age: {age}'.format_map(var_mapping)}")
# Join
print(f"25. join(list):    {'-'.join(var_list)}")
# Alignment
print(f"26. ljust(30, '-'):  '{var2.strip().ljust(30, '-')}'")
print(f"36. rjust(30, '@'):  '{var2.strip().rjust(30, '@')}'")
# Case changes
print(f"27. lower():       '{var2.lower()}'")
print(f"44. swapcase():    '{var2.swapcase()}'")
print(f"45. title():       '{var2.title()}'")
print(f"47. upper():       '{var2.upper()}'")
# Stripping and Replacement
print(f"28. lstrip():      '{var2.lstrip()}'")
print(f"39. rstrip():      '{var2.rstrip()}'")
print(f"43. strip():       '{var2.strip()}'")
print(f"31. removeprefix():'{var_prefix.removeprefix('FILE_')}'")
print(f"32. removesuffix():'{var_prefix.removesuffix('.txt')}'")
print(f"33. replace(' ', '-'): '{var2.strip().replace(' ', '-', 2)}'")
# Partitioning and Splitting
print(f"30. partition('OOp'):{var2.partition('OOp')}")
print(f"37. rpartition('OOp'):{var2.rpartition('OOp')}")
print(f"38. rsplit(' ', 1):  {var2.rsplit(' ', 1)}")
print(f"40. split():       {var2.split()}")
print(f"41. splitlines():  {'L1\\nL2'.splitlines()}")
# Translation
translation_table = str.maketrans('pS', 'qT') # 29. maketrans
print(f"46. translate():   {var2.translate(translation_table)}")
print(f"48. zfill(10):     {var_num.zfill(10)}")
print("-" * 30)

# ====================================================================
# 4. Built-in Functions
# ====================================================================

print("\n--- Built-in Functions ---")
print(f"1. len(var2): {len(var2)}")
print(f"2. max(var2): '{max(var2)}'")
print(f"3. min(var2): '{min(var2)}'")
print("-" * 30)