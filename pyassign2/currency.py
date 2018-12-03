#!/usr/bin/env python3



"""currency.py: A simple currency exchange routine \

using an online currency service.



__author__ = "Sunpengwei"

__pkuid__  = "1800011718"

__email__  = "1800011718@pku.edu.cn"

"""



from urllib.request import urlopen





# A部分

def before_space(s):

    """Give the substring of s; up to, \

    but not including, the first space.

    """

    l = s.split(" ")

    return l[0]





# B部分

def first_inside_quotes(s):

    """Give the first substring of s \

    between two double quote characters.

    """

    l = s.split('"')

    return l[1]





def go_to(JSON):

    """Give the string inside double quotes \

    immediately following the keyword 'to'.

    """

    num = JSON.index('to') + 3

    new = JSON[num:]

    return first_inside_quotes(new)





def has_error(JSON):

    """True if the query has an error; False otherwise.

    """

    return 'false' in JSON





# C部分

def currency_response(currency_from, currency_to, amount_from):

    """Returns: a JSON string that is a response to a currency query.

    A currency query converts amount_from money in currency currency_from \

    to the currency currency_to. The response should be a string of the form \

        '{"from":"<old-amt>","to":"<new-amt>","success":true, "error":""}'

    where the values old-amount and new-amount contain the value and name \

    for the original and new currencies. If the query is invalid, both \

    old-amount and new-amount will be empty, while "success" will be followed \

    by the value false.

    """

    website = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' \

              + currency_from + '&to=' + currency_to + '&amt=' + str(amount_from)

    doc = urlopen(website)

    docstr = doc.read()

    doc.close()

    jstr = docstr.decode('ascii')

    return jstr





# D部分

def iscurrency(currency):

    """Returns: True if currency is a valid (3 letter code for a) currency.

    It returns False otherwise.

    """

    sentence = currency_response(currency, 'USD', 1.0)

    return has_error(sentence) == False 





def exchange(currency_from, currency_to, amount_from):

    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in \

    currency currency_from to the currency currency_to. The value \

    returned represents the amount in currency currency_to.

    """

    JSON = currency_response(currency_from, currency_to, amount_from)

    inf = go_to(JSON)

    return float(before_space(inf))





# 测试函数部分

def testA():

    """Test procedure for before_space().

    """

    # Test case 1

    assert('0.8963' == before_space('0.8963 Euros'))

    # Test case 2

    assert('' == before_space(' 0.8963 Euros'))

    # Test case 3

    assert('0.8963' == before_space('0.8963  Euros'))





def testB():

    """Test procedure for the split for JSON.

    """

    # Test case 1

    assert(True == has_error('{"from":"","to":"","success":false, \

                             "error":"Source currency code is invalid."}'))

    # Test case 2

    assert('1.825936 Euros' == go_to('{"from":"2 United States Dollars", \

                                      "to":"1.825936 Euros","success":true,"error":""}'))





def testC():

    """Test procedure for exchange().

    """

    # Test case 1

    assert('{ "from" : "200 Uruguayan Pesos", "to" : "668.41898835558 Vanuatu Vatu", "success" : true, "error" : "" }'

           == currency_response('UYU', 'VUV', 200))    # 输入值均有效

    # Test case 2

    assert('{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'

           == currency_response('MTP', 'MOP', 16))    # 第一个输入值无效

    # Test case 3

    assert('{ "from" : "", "to" : "", "success" : false, "error" : "Exchange currency code is invalid." }'

           == currency_response('IQD', 'AND', 50))    # 第二个输入值无效





def testD():

    """Test procedure for iscurrency() and exchange().

    """

    # Test case 1

    assert(False == iscurrency('TMO'))    #TMO是无效的输入值

    # Test case 2

    assert(True == iscurrency('XAF'))    #XAF是有效的输入值

    # Test case 3

    assert(0.19152569254984 == exchange('TZS', 'ISK', 4.0))

    # Test case 4

    assert(1979.6672442812 == exchange('ILS', 'IQD', 6.0))

    # Test case 5

    assert(3.6969751452572 == exchange('CAD', 'CHF', 5.0))





def testAll():

    """Test all cases.

    """

    testA()

    testB()

    testC()

    testD()

    print('All tests passed.')





def main():

    """Judge if the input is valid.

    Give the currency exchange result.

    """

    currency_from = input('please input the currency on hand')

    currency_to = input('please input the currency to convert to')

    amount_from = input('please input amount of currency to convert')

    if iscurrency(currency_from) == False:    #第一输入值无效

        print("Your currency on hand is invalid. \

              Please input a valid currency code. e.g. USD")

    elif iscurrency(currency_to) == False:    #第二输入值无效

        print("Your currency to convert to is invalid. \

              Please input a valid currency code. e.g. USD")

    else:

        testAll()

        JSON = currency_response(currency_from, currency_to, amount_from)

        inf = go_to(JSON)

        print(before_space(inf))





if __name__ == '__main__':

    main()
