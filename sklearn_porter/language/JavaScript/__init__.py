# -*- coding: utf-8 -*-

from sklearn_porter.language.LanguageABC import LanguageABC


class JavaScript(LanguageABC):
    KEY = 'js'
    LABEL = 'JavaScript'

    DEPENDENCIES = ['node']
    TEMP_DIR = 'js'
    SUFFIX = 'js'

    CMD_COMPILE = None

    # node estimator.js <args>
    CMD_EXECUTE = 'node {src_path}'

    TEMPLATES = {
        'init':         'var {{ name }} = {{ value }};',

        # if/else condition:
        'if':           'if ({{ a }} {{ op }} {{ b }}) {',
        'else':         '} else {',
        'endif':        '}',

        # Basics:
        'indent':       '    ',
        'join':         '; ',
        'type':         '{{ value }}',

        # Arrays:
        'in_brackets':  '[{{ value }}]',
        'arr[]':        'var {{ name }} = [{{ values }}];',  # var ages = [1, 2];
        'arr[][]':      'var {{ name }} = [{{ values }}];',
        'arr[][][]':    'var {{ name }} = [{{ values }}];',

        # Primitive data types:
        'int':          '',
        'double':       ''
    }
