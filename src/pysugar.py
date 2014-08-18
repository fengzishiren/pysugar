# -*- coding: utf-8 -*-
'''
Created on 2014年7月23日

@author: fengzishiren
@mail: xiaoyaozi106@163.com
'''
import re
import MySQLdb
import os
import sys
from settings import *

__version__ = '0.1'
__date__ = '2014-07-23'
__updated__ = '2014-07-23'

FORMAT_ARGS = {'author': 'pysugar', 'date': __date__, 'version': __version__}

PATTERN_NAME = re.compile(r'\s(\w+)\(')
PATTERN_ARG = re.compile(r'\((\w+)|(Map<\w+,\w+>)\s(\w+)\)')

class Connection(object):
    
    def connect(self):
        host = DATABASE.get('host', '127.0.0.1')
        port = DATABASE.get('port', 3306)  # oracle default port:10033 mysql:3306
        username = DATABASE['username']
        password = DATABASE['password']
        database = DATABASE['database']
        # self.con = MySQLdb.connect(username, password, host + ':' + str(port) + '/' + database)
        self.con = MySQLdb.connect(host=host, user=username, passwd=password, db=database, port=port)
        self.cursor = self.con.cursor()
        return self.cursor

    def close(self):
        self.con.commit()
        self.cursor.close()
        self.con.close()


class Token(object):
    def __init__(self, name, _type, args):
        self.name = name
        self.type = _type  # insert update  delete select
        self.args = args  # map'or obj'


def say(x):    
    print x
    return x


def col2prop(BIG_ID):
    '''
    input eg. SEC_PASS
    return secPass
    '''
    bigA = lambda x:''.join((x[0].upper(), x[1:]))
    mid = ''.join([bigA(part) for part in BIG_ID.lower().split('_')])
    return ''.join((mid[0].lower(), mid[1:]))


def table2bean(table_name, ignore_preffix='tb_'):
    '''
    input table_name eg. tb_person_relation
    return PersonRelation
    Note: 'tb_' will be ignored
    '''
    if table_name.startswith(ignore_preffix):
        table_name = table_name[len(ignore_preffix):]
    bigA = lambda x:''.join((x[0].upper(), x[1:]))
    return  ''.join([bigA(c) for c in table_name.split('_')])

def set_format_args(**kwargs):
    global FORMAT_ARGS
    FORMAT_ARGS.update(kwargs)
    
def get_tokens(daosrc):
    '''
            分析格式化后的dao源代码 
    return Tokens
    '''
    dao_code = daosrc % FORMAT_ARGS
    lines = dao_code.split('\n')
    lines = [x.strip() for x in lines if x.strip().startswith('public')]
    return map(get_token, lines[1:])

    
def get_token(line):
    line = line[len('public'):].strip()
    
    match = PATTERN_NAME.search(line)
    assert match, 'Syntax error!'
    name = match.group(1)
    _type = OP_TYPE_DICT.get(name[0:3])
    if type == None:
        return None
    
    match = PATTERN_ARG.search(line)
    assert match, 'Illegal Parameters'
    
    return Token(name, _type, match.group(1).lower())


def gen_bean_name(bean):
    '''
    eg. UserAccount, userAccount
    '''
    set_format_args(bean_name = bean, var_name = ''.join((bean[0].lower(), bean[1:])))
    
    
def gen_sqls(table_name, tokens):
    gs = lambda table_name, token: SQL_CODE[token.type] % \
                                    dict({'method_name': token.name, 'arg_type':token.args, 'table_name':table_name}, **FORMAT_ARGS)
    sqls = [gs(table_name, tok) for tok in tokens if tok]  # Note: Ignore tok if tok == None
    set_format_args(sqls = '\n'.join(sqls))
    
    
def get_bean_content(fieldtypes):
    fields = ['private %s %s;' % (v, k) for k, v in fieldtypes.items()]
    GET_AND_SET = \
    """
    public %(type)s get%(Name)s() {
        return %(name)s;
    }
   
    public void set%(Name)s(%(type)s %(name)s) {
        this.%(name)s = %(name)s;
    }"""
    bigA = lambda x:''.join((x[0].upper(), x[1:]))
    content = '\n'.join([GET_AND_SET % {'name': f, 'Name':bigA(f), 'type': t} for f, t in fieldtypes.items()])
    return '\n'.join(('\n\t'.join(fields), content))
    
    
def gen_map_and_fields(table_name, obtain_type=lambda x: x):
    '''
    obtain_type 必须是一个函数 用来处理从数据库类型到Java类型的转换
            这里obtain_type默认什么也不做 用来处理MySql类型
    '''
    sql = 'select * from %s' % table_name 
    con = Connection()
    try:
        cursor = con.connect()
        cursor.execute(sql)
        descs = cursor.description
    finally:
        con.close()
    
    fieldtypes = {col2prop(e[0]): DO_TYPE_DICT.get(obtain_type(e[1]), 'Object') for e in descs}
    set_format_args(bean_content = get_bean_content(fieldtypes))
    
    procols = {col2prop(key): key for key in [e[0] for e in descs]}
    resultmap = ['<result property="%s" column="%s" />' % (k, v) for k, v in procols.items()]
    
    set_format_args(map = '\n\t'.join(resultmap))
    cols = '(%s)' % (','.join(procols.values()))
    vals = '(%s)' % (','.join(['#{%s}' % k for k in procols.keys()]))
    # cache it
    set_format_args(insert_suffix = ' values '.join((cols, vals)))
    
    us = [' = '.join((v, '#{%s}' % k)) for k, v in procols.items()]
    # cache it
    set_format_args(update_set = ',\n\t'.join(us))
    
    
def write_file((filename, content), _dir=OUTPUT_DIR):
    if not os.path.exists(_dir):
        os.mkdir(_dir) 
    with open(os.path.join(_dir, filename), 'w') as f:
        return f.write(content)  # Note: return None
    

def get_tpl(name):
    with open(name) as f:
        return f.read()
   
   
def main(table_name):
   
    bean = table2bean(table_name)
    daosrc = get_tpl(os.path.join(TEMPLATES_DIR, 'dao.tpl'))

    gen_bean_name(bean)
    gen_map_and_fields(table_name)
    gen_sqls(table_name, get_tokens(daosrc))
    
    formatted = {outfile % FORMAT_ARGS : (get_tpl(os.path.join(TEMPLATES_DIR, tpl)) if tpl != 'dao.tpl' else daosrc)\
                  % FORMAT_ARGS for tpl, outfile in IO_FILE_LIST.items()}
    map(write_file, formatted.items())
    

if __name__ == '__main__':
    if sys.argv.__len__() == 3:
        main(sys.argv[1])
    else:
        main('auth_user')
    say('bye-bye')
