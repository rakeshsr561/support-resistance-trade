def supres(ltp, n):

    from scipy.signal import savgol_filter as smooth

    if n % 2 != 0:
        n += 1

    n_ltp = ltp.shape[0]

    ltp_s = smooth(ltp, (n + 1), 3)

    ltp_d = np.zeros(n_ltp)
    ltp_d[1:] = np.subtract(ltp_s[1:], ltp_s[:-1])

    resistance = []
    support = []

    for i in xrange(n_ltp - n):
        arr_sl = ltp_d[i:(i + n)]
        first = arr_sl[:(n / 2)]
        last = arr_sl[(n / 2):]  

        r_1 = np.sum(first > 0)
        r_2 = np.sum(last < 0)

        s_1 = np.sum(first < 0)
        s_2 = np.sum(last > 0)

        if (r_1 == (n / 2)) and (r_2 == (n / 2)):
            resistance.append(ltp[i + ((n / 2) - 1)])

        if (s_1 == (n / 2)) and (s_2 == (n / 2)):
            support.append(ltp[i + ((n / 2) - 1)])

    return support, resistance