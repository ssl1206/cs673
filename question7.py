def is_leap_year(n):
    if n % 4 == 0 and n % 100 == 0 and n % 400 == 0:
        return True
    return False

print("Check 2023 year is leap year: ", is_leap_year(2023))
print("Check 2022 year is leap year: ", is_leap_year(2022))
print("Check 2021 year is leap year: ", is_leap_year(2021))
print("Check 2020 year is leap year: ", is_leap_year(2020))
print("Check 2019 year is leap year: ", is_leap_year(2019))
print("Check 2018 year is leap year: ", is_leap_year(2018))
print("Check 2000 year is leap year: ", is_leap_year(2000))