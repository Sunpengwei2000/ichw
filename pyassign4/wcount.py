#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Sunpengwei"
__pkuid__  = "1800011718"
__email__  = "1800011718@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import re
from urllib import error

def wcount(text, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    dic = {}
    cache = re.split('[ \n]',text.lower())  # 将整段文章分割成单词，分割标志为空格和换行
    word_list = []
    valid_letter = "abcdefghijklmnopqrstuvwxyz'-"  # 单词中会含有字母和缩写“'”、连字符“-”
    for element in cache:
        if element.isalpha():
            word_list.append(element)  #保留单词
        elif element == '':
            pass  #舍弃空字符串
        else:
            new_element = ''
            for letter in element:
                if letter in valid_letter:
                    new_element = new_element + letter  #去除字符中除“'”以外的标点
                    new_element = new_element.strip("'")  #去除首尾的“'”
                    new_element = new_element.strip("-")  #去除首尾的“-”
            word_list.append(new_element)
    for word in word_list:
        if word == '':
            pass  # 舍弃空字符串
        elif word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1
    sorted_dic = sorted(dic.items(), key = lambda item:item[1])  # 按照出现频率大小排序
    if len(sorted_dic) < topn:
        topn = len(sorted_dic)  # 当topn超出单词种类数时，输出全部单词
    for sorted_word in sorted_dic[-1:-topn - 1:-1]:
        length = len(sorted_word[0])
        print(sorted_word[0] + ' ' * (30 - length) + str(sorted_word[1]))


def main():
    '''open the given url to get the text, judge if the input is valid'''
    try:
        doc = urlopen(sys.argv[1])
    except ValueError as err:
        print("Oops! Your error is ///{}///. Please try again.".format(err))
    except error.HTTPError as err:
        print("Oops! Your error is ///{}///. Please try again.".format(err))
    except error.URLError as err:
        print("Oops! Your error is ///{}///. Please try again.".format(err))
    else:
        docstr = doc.read()
        doc.close()
        jstr = docstr.decode()
        try :
            topn = int(sys.argv[2])
            if topn <= 0:
                print("Please input a positive number.")  # 检验topn是否为正数
            else:
                wcount(jstr, topn)
        except IndexError as err:
            wcount(jstr)  #用户没有给定输出的数量，按默认值topn = 10输出


if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))  #给出使用说明
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    main()
