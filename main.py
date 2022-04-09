import sys

base = sys.argv[1]
user_input = list(sys.argv[2:])
conv_list = []
H_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def dec_to_base(num, b):
    if num < 0:
        neg_num = -1
    else:
        neg_num = 1
    num *= neg_num
    # create list to store the final ans
    r = []
    while num:
        # append ans of the num mod base into list
        r.append(int(num % b))

        num //= b

    if neg_num < 0:
        r.append('-')
    r.reverse()

    return r[::1]


def decimal_conv(b, num):
    dec_str = str('')
    while num != 0:
        num = abs(num)
        num *= b
        dec = int(num)
        num -= dec
        dec_str += str(dec)

    dec_str = dec_str[:4]
    return dec_str


# loop through user input and decide what function to run
def main():
    for i in range(len(user_input)):
        base_num = base
        cur = float(user_input[i])

        base_num = int(base_num)
        cur = float(cur)
        whole_num = int(cur)
        decimal = cur - whole_num
        fin_w = ''
        final_dec = ''

        # deals with hex
        while base_num == 16 and decimal != 0:
            if whole_num != 0:
                whole_num = abs(whole_num)
                remain = whole_num % base_num
                fin_w = H_LIST[remain]
            elif decimal != 0:
                dec_str = str('')
                decimal = abs(decimal)
                decimal *= base_num
                d_int = int(decimal)
                decimal -= d_int
                dec_str += H_LIST[d_int]
                final_dec += dec_str
                final_dec = final_dec[:4]

        if base_num != 16:
            # calculation for the whole number after hex conversion
            fin_w = dec_to_base(whole_num, base_num)
            # to account for the fractional part of the conversion after hex conversion
            final_dec = decimal_conv(base_num, decimal)

        if whole_num == 0:
            fin_w = '0'

        # declaring the whole num # decimal # as strings so they can be appended and outputted
        w_string = ''.join([str(elem) for elem in fin_w])
        d_string = ''.join([str(elem) for elem in final_dec])
        # if the decimal is negative add a -  to the beginning of the output, else output as normal
        if cur < 0:
            final = ('-' + w_string + '.' + d_string)
        else:
            final = (w_string + '.' + d_string)

        conv_list.append(final)

    # output
    # -------------------------------------------------------------------------------------------------------------

    print('|       Base 10      |        Base', base, '     |')
    print('|:-------------------|:-------------------|')
    for j in range(len(conv_list)):
        print('|{: <20}|{: <20}|'.format(user_input[j], conv_list[j]))


if __name__ == "__main__":
    main()
