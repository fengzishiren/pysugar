# coding: utf-8
'''
Created on 2014年7月25日

@author: fengzishiren
'''

DATABASE = {'host':'127.0.0.1',
            'port': 3306,
            'username': 'root',
            'password': 'root',
            'database': 'mysite'}

TEMPLATES_DIR = 'templates'
OUTPUT_DIR = 'output'

IO_FILE_LIST = {'bean.tpl':     '%(bean_name)sInfo.java',
                'cnter.tpl':    '%(bean_name)sController.java',
                'service.tpl':  '%(bean_name)sService.java',
                'dao.tpl':      '%(bean_name)sDao.java',
                'mapper.tpl':   '%(bean_name)sDaoMapper.xml'}
# 仅对以add, upd,...开头的生成sql语句
OP_TYPE_DICT = {'add':'insert', 'upd':'update', 'del':'delete', 'get':'select'}
# DataBase Type -> Object Type
# Oracle
# DO_TYPE_DICT = {'STRING':'String', 'NUMBER':'int', 'DATETIME':'Timestamp', 'TIMESTAMP':'Timestamp'}

"""MySQL FIELD_TYPE Constants

These constants represent the various column (field) types that are
supported by MySQL.


DECIMAL = 0
TINY = 1
SHORT = 2
LONG = 3
FLOAT = 4
DOUBLE = 5
NULL = 6
TIMESTAMP = 7
LONGLONG = 8
INT24 = 9
DATE = 10
TIME = 11
DATETIME = 12
YEAR = 13
NEWDATE = 14
VARCHAR = 15
BIT = 16
NEWDECIMAL = 246
ENUM = 247
SET = 248
TINY_BLOB = 249
MEDIUM_BLOB = 250
LONG_BLOB = 251
BLOB = 252
VAR_STRING = 253
STRING = 254
GEOMETRY = 255

CHAR = TINY
INTERVAL = ENUM
"""
  
DO_TYPE_DICT = {1:'int', 2: 'int', 3:'long', 4:'float', 5:'double', 7:'Timestamp', 8:'long', 10:'String', 11:'String', 12:'String', 15:'String', 253:'String', 254:'String'}

SQL_CODE = {
    "delete": 
    """
    <delete id="%(method_name)s" parameterType="%(arg_type)s">
        delete from %(table_name)s
    </delete>
    """,
    "insert": 
     """
    <insert id="%(method_name)s" parameterType="%(arg_type)s">
        insert into %(table_name)s %(insert_suffix)s
    </insert>
    """,
    "select": 
       """
    <select id="%(method_name)s" parameterType="%(arg_type)s" resultMap="%(var_name)sMap">
        select * from %(table_name)s
    </select>
    """,
    "update": 
     """
    <update id="%(method_name)s" parameterType="%(arg_type)s">
        update %(table_name)s 
        <set>
         %(update_set)s 
        </set>
    </update>
    """
    }
