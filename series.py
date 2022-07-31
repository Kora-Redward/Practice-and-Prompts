# Rawlin Redfield
# 07-31-2022


# Find the total sum of a series
def total(math_series):
    # I took what is arguably the simplest approach with this operation which is simply cycling through the
    # variables and repeatedly appending them to the sum of the previous entries.
    seriessum = 0
    length = len(math_series)
    for i in range(length):
        seriessum = seriessum + math_series[i]
    return seriessum


# Find the mean value of a series
def mean(math_series):
    # I'm using the previously established total function to simplify the process.
    seriessum = total(math_series)
    mn = seriessum/len(math_series)
    return mn


# Find the largest value in the series
def highest_value(math_series):
    i = 0
    high = series[0]
    length = len(math_series)
    # Setting the high variable to the first index in the array rather than zero so that,
    # should the array consist solely of negative variables, the process will still operate.
    while length != i:
        if series[i] > high:
            high = series[i]
        i = i + 1
    return high
    # I switched away from using the for statements so that I could practice my if syntax


# Find the smallest value in the series
def lowest_value(math_series):
    # The methodology seen here is clearly an exact mirror of the preceding operation
    i = 0
    low = series[0]
    length = len(math_series)
    while length != i:
        if series[i] < low:
            low = series[i]
        i = i + 1
    return low


# Order the series from low to high
def low_high(math_series):
    length = len(math_series)
    lh = math_series.copy()
    #  My initial plan was to use the smallest_value() operation to determine the smallest value from one list
    #  and apply it to a new one, while removing it from the previous list. While it worked in practice, the 
    #  method wiped the series clear, and thus required the series to be redeclared for subsequent operations,
    #  (copying the list led to implementation errors) so I switched over to a more self contained approach using Python swaps.
    for i1 in range(length):
        for i2 in range(length):
            if lh[i1] < lh[i2]:
                lh[i2], lh[i1] = lh[i1], lh[i2]
    return lh


# Order the series from high to low
def high_low(math_series):
    hl = math_series.copy()
    #  By switching the relationship from less than to greater than, the code to low_high
    #  can be quickly switched over to perform the inverse operation.
    length = len(math_series)
    for i1 in range(length):
        for i2 in range(length):
            if hl[i1] > hl[i2]:
                hl[i2], hl[i1] = hl[i1], hl[i2]
    return hl


# Determine which numbers are divisible by three
def div_by_three(math_series):
    proxy = math_series.copy()
    bythree = []
    # Employ the remained operation to determine which numbers are divisible by using the remainder operation.
    for i in range(len(proxy)):
        if (proxy[i] % 3) == 0:
            bythree.append(proxy[i])
    if len(bythree) != 0:
        return bythree
    else:
        # I set up the return as an if-else, just so that an empty array wouldn't be returned if solely
        # non-divisible variables were placed in the list.
        return "None"


# Determine which numbers in the array are even.
def is_even(math_series):
    proxy = math_series.copy()
    even = []
    for i in range(len(proxy)):
        if (proxy[i] % 2) == 0:
            even.append(proxy[i])
    if len(even) != 0:
        return even
    else:
        return "None"


# Determine the first occurrence of a character in a string
def string_finder(lang_series, char):
    for i in range(len(lang_series)):
        if lang_series[i] == char[0]:
            return i+1
    # Establishing a backup condition in case the character in question was not contained within.
    return 'The character does not appear.'


# Capitalize all alphabetical characters in a string
def capitalization(lang_series):
    proxy = ''
    for i in range(len(lang_series)):
        proxy = proxy + lang_series[i].capitalize()
    return proxy


# Find the last character in the string when sorted alphabetically.
def last_letter(lang_series):
    final = ''
    for i in range(len(lang_series)):
        if lang_series[i] > final:
            final = lang_series[i]
    return final


# Determine how many characters in the string are non-alphabetical.
def non_alpha(lang_series):
    count = 0
    for i in range(len(lang_series)):
        if not lang_series[i].isalpha():
            count = count + 1
    return count


# Determine the character contained in an index provided in relation to the words in the string.
def retrieve_letter(lang_series, rword, rletter):
    rseries = 1
    i = 0
    if lang_series[0].isspace():
        rseries = 0
    while i < len(lang_series) and rseries != rword:
        b = i+1
        #  I included a process to confirm that if there is simply a double space, the program does
        #  not assume a new word has begun until it detects a non-space in the next position.
        if lang_series[i].isspace() and not lang_series[b].isspace():
            rseries = rseries + 1
        i = i+1
    #  Now that the function has located the word in question, it will simply add the original character
    #  listing to its index count to find the letter being sought.
    locale = i-1 + rletter
    return lang_series[locale]


series = [24, 43, 50, 27]
print('The sum of the array values is: ', total(series))
print('The mean of the array values is: ', mean(series))
print('The largest value in the array is: ', highest_value(series))
print('The smallest value in the array is: ', lowest_value(series))
print('The array ordered from low to high is: ', low_high(series))
print('The array ordered from high to low is: ', high_low(series))
print('The entries in the array divisible by three are: ', div_by_three(series))
print('The entries in the array that are even are: ', is_even(series))

print('')

statement = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'
letter = 'm'
word = 5
character = 4
print('The first appearance of ', letter, ' is as character number: ', string_finder(statement, letter))
print('The capitalized version of the statement is: ', capitalization(statement))
print('Alphabetically, the last letter in the statement is: ', last_letter(statement))
print('The number of non-alphabetical characters in the string is: ', non_alpha(statement))
print('Character #', character, 'in word #', word, 'is: ', retrieve_letter(statement, word, character))
