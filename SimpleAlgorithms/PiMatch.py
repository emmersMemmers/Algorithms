"""
Pi Match score is defined by how close the digits in a number are to the approximation of Pi, 3.14.

To calculate drop the decimal in Pi approximation to get 314, start from leftmost digits and calculate the
difference between those 3 digits and 314.

we keep shifting over one digit to the right until we have no 3 digit numbers left.

If 2 digits or less the score is 0.

The total score is the average of each 3 digit score.

We may assume 12 digits is the max.

example 1: 3149 is calculated as: (314 - 314 = 0) + (149 - 314 = -165)/2 = -82.5

example 2: 357878 (357-314=43)+(578-314=264)+(787-314=473)+(878-314=564)/4 = 336
"""


def calc_pi_match(value):
    str_value = repr(value)
    no_dec_str = str_value.replace(".", "")
    if len(no_dec_str) < 3:
        return 0
    digit_array = list(no_dec_str)
    total = 0
    num_of_checks = 0
    cur_last_digit = 2
    while cur_last_digit < len(digit_array):
        first_digit = digit_array[cur_last_digit - 2]
        second_digit = digit_array[cur_last_digit - 1]
        third_digit = digit_array[cur_last_digit]
        number = int(first_digit + second_digit + third_digit)
        total += number - 314
        num_of_checks += 1
        cur_last_digit += 1
    return total / num_of_checks
