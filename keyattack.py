#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
暴力生成字典    
"""
import os
import argparse
import itertools


def getargs():
    """获取命令参数
    """
    parser = argparse.ArgumentParser(description='用于生成指定长度和字符空间的密码字典')
    parser.add_argument('minlength', type=int, help='用于指定生成密码的最小位数')
    parser.add_argument('maxlength', type=int, help='用于指定生成密码的最大位数')
    parser.add_argument('-o', '--outfile', help='指定字典文件的保存路径')
    parser.add_argument(
        '-c',
        '--choices',
        default='0123456789',
        help='指定字符串，密码中的字符从字符串中选择，默认为 "0123456789"')
    return parser.parse_args()


def getkeyslist(minlength, maxlength, choices='0123456789'):
    """生成 minlength ~ maxlength 位密码列表，并返回列表
    Args:
        minlength: 密码最小位数
        maxlength: 密码最大位数
        choices: 候选字符，密码使用的字符从候选字符中得到
    Returns:
        keyslist: 密码列表
    """
    if choices is None:
        choices = '0123456789'
    keyslist = []
    for i in range(minlength, maxlength + 1):
        keyiter = itertools.product(choices, repeat=i)
        keys = [''.join(c) + '\n' for c in keyiter]
        keyslist.append(keys)
    print(f'[+] 已生成 {minlength} ~ {maxlength} 位密码字典 [+]')
    return keyslist


def save_keys_dict(keyslist, outfile):
    """保存密码字典
    Args:
        keyslist: 密码列表
        outfile: 要保存的密码字典文件
    """
    if outfile is None:
        homepath = os.path.expanduser('~')
        outfile = os.path.join(homepath, 'Desktop/keys.txt')
    else:
        outfile = os.path.abspath(outfile)
    with open(outfile, 'w') as f:
        for keys in keyslist:
            f.writelines(keys)
    print(f'[+] 已保存密码字典到 {outfile} [+]')


if __name__ == '__main__':
    args = getargs()
    if args.minlength < args.maxlength:
        keyslist = getkeyslist(args.minlength, args.maxlength, args.choices)
    else:
        keyslist = getkeyslist(args.maxlength, args.minlength, args.choices)
    save_keys_dict(keyslist, args.outfile)
