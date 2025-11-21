







print("""
--------------------------
PYMEOMEO OBF 
AUTHOR : NGOCUYENCODER

Facebook : https://www.facebook.com/datishnu1907
Telegram : https://t.me/huynhngocuyenn
Zalo : 0335102378


COPYRIGHT NGOCUYENCODER
-------------------------
""")

import requests
#print(requests.get('https://google.com'))




# print("Đang vào tool...",'\r')


import sys
import random
import ast
import zlib
import marshal
import base64
import bz2
from pystyle import *
class DepTraiCoGiSai(ExceptionGroup):0
class GHIᅠCHÚ(MemoryError):0
if sys.version_info < (3, 10):
    print("Install Python Version = 3.10 or > 3.10 To Use This Code ")
    sys.exit()

def _rd():
    return "".join(__import__("random").sample(
        [chr(i) for i in range(97, 122)], k=5))


def _rd1():
    return "".join(__import__("random").sample(
        [chr(i) for i in range(97, 122)], k=1))


def rd():
    # return "_" + "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))
    return ''.join(__import__('random').choices([chr(i) for i in range(0x4e00, 0x9fff)], k=3))
    #return ''.join(__import__('random').choices([chr(i) for i in range(65, 90)], k=22))


def rd2():
    # return "_" + "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))
    return ''.join(__import__('random').choices([chr(i) for i in range(0x4e00, 0x9fff)], k=4))

def superrandom():
    # return "_" + "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))
    return ''.join(__import__('random').choices([chr(i) for i in range(1000, 3000)], k=1503))

def rditerger():
    return "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))




def _chrobf(x):
    return ord(x) + int(zlib.decompress(b'x\x9c36&\x17\x18\x99\x00!:0\x87P\xc6\xc6\x00\x0bx\x11v'))


def obfstr(v):
    global _join
    global _hexrun
    global obfint
    if v == "":
        return f"''"
    else:
        x = []
        r = list(v)
        for i in range(len(r)):
            x.append(_chrobf(r[i]))
        _str_ = f"(lambda  : (lambda : (lambda : {_join}(( {_list}({_map}({_hexrun}, {x})) )))())())()"
        return _str_


def randomchar():
    return random.sample(['<','>','==',],k=1)[0]

hexspam = f"""
"""
 

antipycdc = ''

def antibypass():
    def anti(s: str, kkk=69):
        def f(n):
            a, b = n & 0b11110000, n & 0b00001111
            return f"(({a+10000000000000000000000000}) >>  ({b+100000000000000000000000000000000000}))" if n > 15 else str(n)
        fx = [f(ord(c) ^ kkk) for c in s]
        mm = ", ".join(fx)
        return f"""((lambda __phamtuankiet__: __phamtuankiet__(*[__dat__('HELLO DECOMPILER',{mm})]))(lambda *__datcute__: ((lambda __wearelove__, __uyencoder__:__wearelove__().join([*map(lambda n: __uyencoder__().format((n ^ 64)), __datcute__)]))(lambda: getattr(''.__class__, '__add__')('__dat__', ''),lambda: "__yeuquynhngan__"))))"""

    def _anti():
        antipycdc = ''
        for i in range(1000):
            antipycdc += f"__uyencoderdeptrai__(__uyencoderdeptrai__(__uyencoderdeptrai__(__uyencoderdeptrai__(__uyencoderdeptrai__(__uyencoderdeptrai__('')))))),"
        antipycdc = "try:phamtuankiet=[" + antipycdc + "]\nexcept:pass"
        txf = f"""
def __uyencoderdeptrai__(__deptrai__):
    return __deptrai__

try:pass
except:pass
finally:pass
{antipycdc}
finally:int(2008-2006)
        """
        return f"""
try:
    def __dat__(__ok__):return "__ANTI DECOMPILER__"
    {anti("__phamtuankiet__")}
except:pass
else:pass
finally:pass
{txf}"""

    return _anti()

ANTI_PYCDC = f"""
{antibypass()}
"""
# ANTI_PYCDC = ''


import random
# def obfstr(string):
#     global _hexrun
#     global _join
#     keys = []
#     magic = random.randint(1000000, 9999999)
#     for char in string:
#         logic = random.randint(1, 4)
#         if logic == 1:
#             logic = '+'
#         elif logic == 2:
#             logic = '*'
#         elif logic == 3:
#             logic = '<<'
#         else:
#             logic = '^'
        
#         key = ord(char) + 3333333333333333333333333333333333333333333333333333333333242422222222222222222722222233    
#         key2 = magic
        
#         if logic == "^":
#             key3 = ~key ^ ~magic
#             keys.append(f"(lambda: {_hexrun}({key2} ^ {key3}))()")
#         elif logic == "<<":
#             magic = random.randint(1, 19)
#             key3 = key << magic
#             PT = ">>"
#             keys.append(f"(lambda: {_hexrun}({key3} {PT} {magic}))()")
#         else:
#             if logic == "+":
#                 PT = "-"
#             else:
#                 PT = "//"
#             key3 = eval(f"{key} {logic} {magic}")
#             keys.append(f"(lambda: {_hexrun}({key3} {PT} {key2}))()")
    
#     return f"(lambda: {_join}([{', '.join(keys)}]))()"


def _byte(v):
    byte_array = bytearray()
    byte_array.extend(v.to_bytes((v.bit_length() + 7) // 8, 'big'))
    return b"0xFFFFFFFF/" + byte_array

def obfint(v):
    n = rd()
    global _idk
    if 'bool' in str(type(v)):
        if str(v)=='True':
            return f'(lambda: (lambda {n}: {n} + (lambda : {vaicalon}({(1+0xFFFFFFFFFFFFFFFFFFFFFF)}))())(0) == 1)()'
        else:
            return f'(lambda: (lambda {n}: {n} - (lambda : {vaicalon}(({(1+0xFFFFFFFFFFFFFFFFFFFFFF)} ) ) )())(0) == 1)()'
    else:
        #return f"""{vaicalon}({(v+0xFFFFFFFFFFFFFFFFFFFFFF)}) if {_str}({_type}({_bool}({vaicalon}({(v+0xFFFFFFFFFFFFFFFFFFFFFF)})))) == {_str}({_type}({_int}({rditerger()})>{_int}({rditerger()})<{_int}({rditerger()})>{_int}({rditerger()}))) else {vaicalon}({v+0xFFFFFFFFFFFFFFFFFFFFFF})"""
        #return f"""(lambda {rd()} : {vaicalon}({(v+0xFFFFFFFFFFFFFFFFFFFFFF)})("datchuche")"""
        #return f"""(lambda : {vaicalon}({(v+0xFFFFFFFFFFFFFFFFFFFFFF)})//eval({obfstr('1')}))()"""
        #print(fr""" unhexlify('{_byte(int(v))}') """)
        #return fr"""(lambda : """
        return f'(lambda: {_idk}({_byte(int(v))}))()'


def varsobf(v):
    #return f"""({nuyenbuiltins}[(lambda : 'bool'[::-1][::-1])()]) if {nuyenbuiltins}[(lambda : 'bool'[::-1][::-1])()]({nuyenbuiltins}[(lambda : 'bool'[::-1][::-1])()]({nuyenbuiltins}[(lambda : 'bool'[::-1][::-1])()]({(v)}))) < {nuyenbuiltins}[(lambda : 'bool'[::-1][::-1])()]({nuyenbuiltins}['type']({nuyenbuiltins}['int']({rditerger()})>{nuyenbuiltins}['int']({rditerger()})<{nuyenbuiltins}['int']({rditerger()})>{nuyenbuiltins}['int']({rditerger()}))) and {nuyenbuiltins}[(lambda : 'bool'[::-1][::-1])()](str(str({rditerger()})>{nuyenbuiltins}['int']({rditerger()})<{nuyenbuiltins}['int']({rditerger()})>{nuyenbuiltins}['int']({rditerger()}))) > 2 else {v}"""
    global array
    deptrai = list(v)[::-1]
    holly=[]
    for i in deptrai:
        holly.append(f"(lambda : {array}('{superrandom()}{superrandom()}{i}'))()")
    return '+'.join(holly)




_join = rd()
_int = rd()
_str = rd()
_bool = rd()
_type = rd()
_bytes = rd()
_vars = rd()
array = rd()
_ip = rd()
_bytearray = rd()
vaicalon = rd()
___import__ = rd()
_movdiv = rd()
_hexrun = rd()
_argshexrun = rd()
_eval = rd()
_list = rd()
_map = rd()
_idk = rd()
nuyenbuiltins = rd()
_memoryerror = rd()
rpq = rd()
__print = r"tryᅠ"
__input = r"exceptᅠ"
# variables = [
#     '_join', '_int', '_str', '_bool', '_type', '_bytes', '_vars', '_ip', 'vaicalon', 
#     '__import__', 'movdiv', 'hexrun', 'argshexrun', 'eval', 'list', 'map', 
#     'idk', 'nuyenbuiltins', 'memoryerror'
# ]
# for var_name in variables:
#     globals()[var_name] = rd()
def unicodeobf(x):
    b = []
    for i in x:
        j = ord(i) + int(zlib.decompress(b'x\x9c36&\x17\x18\x99\x00!:0\x87P\xc6\xc6\x00\x0bx\x11v'))
        b.append(j)
    return b


def _uni(x):
    return unicodeobf(x)
# def makelambda(string):
#     num_loops = 25
#     lambda_str = "lambda: " + repr(string)
#     for _ in range(num_loops):
#         lambda_str = "lambda: (" + lambda_str + ")()"
    
#     return lambda_str + "()"
utf8 = rd()
__bool = rd()
__exx = rd()
_temp = rd()
_temp1 = rd()
_wt = rd()
_exp = rd()
_meh = rd()
_globals = rd()
_len = rd()
var = fr"""
try:
    class {_memoryerror}(eval("Exception")):_ : (lambda :"Tao la dat dep trai")();pass
except Exeption as TUOI_LON_DECODE:pass
else:globals()["dec_dec_cái_đầu_buồi"] = "BỐ ĐẠT"
finally:
    {utf8} = "utf8"
    {_globals} = globals()
{array} = lambda {array}: {array}[(lambda : -1)()]
def {_join}({_wt}):
    {__exx} = ""
    for {_globals}['{_temp1}'], {_globals}['{_temp}'] in enumerate({_wt}):
        if {_globals}['{_temp1}'] > 0:
            {__exx} += ""
        {__exx} += str({_globals}['{_temp}'])
    return {__exx}
{nuyenbuiltins} = vars(globals()['__builtins__'])
{_eval} =  eval({_join}({varsobf('eval')})[::-1])
{_bool} = {_eval}({_join}({varsobf('bool')})[::-1])
{_str} =  {_eval}({_join}({varsobf('str')})[::-1])
{_type} =  {_eval}({_join}({varsobf('type')})[::-1])
{_int} =  {_eval}({_join}({varsobf('int')})[::-1])
{_bytes} =  {_eval}({_join}({varsobf('bytes')})[::-1])
{_vars} =  {_eval}({_join}({varsobf('vars')})[::-1])
{_movdiv} =  {_eval}({_join}({varsobf('callable')})[::-1])
{_list} =  {_eval}({_join}({varsobf('list')})[::-1])
{_map} =  {_eval}({_join}({varsobf('map')})[::-1])
{___import__} =  {_eval}({_join}({varsobf('__import__')})[::-1])
{_bytearray} = {_eval}({_join}({varsobf('bytearray')})[::-1])
{_len} = {_eval}({_join}({varsobf('len')})[::-1])

exceptᅠ =  {_eval}({_join}({varsobf('input')})[::-1])
def {_join}({__exx},*k):
    if k:
        {_meh} = '+'
        op = "+"
    else:
        {_meh} = ''
        op = ''
    {_globals}['{__exx}'] = {obfint(True)}
    {_globals}['{_join}'] = {_join}
    {_globals}['{_str}'] = {_str}
    {_globals}['{__exx}'] = {__exx}
    for {_globals}['{_meh}_'] in {_globals}['{__exx}']:
        if not {__exx}:{_globals}['{_meh}_'] += (lambda : '')()
        {_meh} += {_str}({_meh}_)
    return {_meh}
def {vaicalon}({_wt}):
    return {_int}({_wt}-0xFFFFFFFFFFFFFFFFFFFFFF)
def {_idk}({_wt}):
    {__exx} = {_bytearray}({_wt}[{_len}(b'0xFFFFFFFF/'):])
    {_temp} = 0
    for {_temp1} in {__exx}:
        {_temp} = {_temp} * 256 + {_temp1}
    return {_temp}
def {_hexrun}({_argshexrun}):
    {_argshexrun} = {_argshexrun}-3333333333333333333333333333333333333333333333333333333333242422222222222222222722222233  
    if {_argshexrun} <= 0x7F:
                return {_str}({_bytes}([{_argshexrun}]),{utf8})
    elif {_argshexrun} <= 0x7FF:
                if 1<2:
                        {_globals}['{_temp}'] = 0xC0 | ({_argshexrun} >> 6)
                {_globals}['{_temp1}'] = 0x80 | ({_argshexrun} & 0x3F)
                return {_str}({_bytes}([{_globals}['{_temp}'], {_globals}['{_temp1}']]),{utf8})
    elif {_argshexrun} <= 0xFFFF:
            {_globals}['{_temp}'] = 0xE0 | ({_argshexrun} >> 12)
            if 2>1:
                {_globals}['{_temp1}'] = 0x80 | (({_argshexrun} >> 6) & 0x3F)
            {_globals}['{_wt}'] = 0x80 | ({_argshexrun} & 0x3F)
            return {_str}({_bytes}([{_globals}['{_temp}'], {_globals}['{_temp1}'], {_globals}['{_wt}']]),{utf8})
    else:
        {_globals}['{_temp}'] = 0xF0 | ({_argshexrun} >> 18)
        if 2==2:
            {_globals}['{_temp1}'] = 0x80 | (({_argshexrun} >> 12) & 0x3F)
        if 1<2<3:
            {_globals}['{_wt}'] = 0x80 | (({_argshexrun} >> 6) & 0x3F)
        {_globals}['{_exp}'] = 0x80 | ({_argshexrun} & 0x3F)
        return {_str}({_bytes}([{_globals}['{_temp}'], {_globals}['{_temp1}'], {_globals}['{_wt}'], {_globals}['{_exp}']]),{utf8})


tryᅠ = {_eval}({_join}({varsobf('print')})[::-1])
"""

dell = f"""

__import__('sys').exit()
__import__('sys').exit()
"""
import ast
def _moreobf(tree):
    import random


    def junk(en, max_value):
        cases = []
        line = max_value + 1
        for i in range(random.randint(1, 5)):
            case_name = "__"+rd()
            case_body = [
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=line)]
                    ), 
                    body=[
                        ast.Assign(
                            targets=[ast.Name(id=case_name)], 
                            value=ast.Constant(value=random.randint(0xFFFFF, 0xFFFFFFFFFFFF)), 
                            lineno=None
                        )
                    ], 
                    orelse=[]
                )
            ]
            cases.extend(case_body)
            line += 1
        return cases

    def bl(body):
        var = "__"+rd()
        en = "__"+rd()

        tb = [
            ast.AugAssign(
                target=ast.Name(id=var), 
                op=ast.Add(), 
                value=ast.Constant(value=1)
            ),
            ast.Try(
                body=[
                    ast.Raise(
                        exc=ast.Call(func=ast.Name(id=_memoryerror), 
                                     args=[ast.Name(id=var)], 
                                     keywords=[])
                    )
                ],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id=_memoryerror), 
                        name=en, 
                        body=[]
                    )
                ],
                orelse=[],
                finalbody=[]
            )
        ]
        
        for i in body:
            tb[1].handlers[0].body.append(
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=1)]
                    ), 
                    body=[i], 
                    orelse=[]
                )
            )
        
        tb[1].handlers[0].body.extend(junk(en, len(body) + 1))
        
        node = ast.Assign(
            targets=[ast.Name(id=var)], 
            value=ast.Constant(value=0), 
            lineno=None
        )
        
        return [node] + tb

    def _bl(node):
        olb = node.body

        var = rd()
        en = rd()

        tb = [
            ast.AugAssign(
                target=ast.Name(id=var), 
                op=ast.Add(), 
                value=ast.Constant(value=1)
            ),
            ast.Try(
                body=[
                    ast.Raise(
                        exc=ast.Call(func=ast.Name(id=_memoryerror), 
                                     args=[ast.Name(id=var)], 
                                     keywords=[])
                    )
                ],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id=_memoryerror), 
                        name=en, 
                        body=[]
                    )
                ],
                orelse=[],
                finalbody=[]
            )
        ]
        for i in olb:
            tb[1].handlers[0].body.append(
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=1)]
                    ), 
                    body=[i], 
                    orelse=[]
                )
            )
        tb[1].handlers[0].body.extend(junk(en, len(olb) + 1))
        node.body = [
            ast.Assign(
                targets=[ast.Name(id=var)], 
                value=ast.Constant(value=0), 
                lineno=None
            )
        ] + tb
        return node
    def on(node):
        if isinstance(node, ast.FunctionDef):
            return _bl(node)
        return node
    nb = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            nb.append(on(node))
        elif isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
            nb.extend(bl([node]))
        elif isinstance(node, ast.Expr):
            nb.extend(bl([node]))
        else:
            nb.append(node)
    tree.body = nb
    return tree


def __moreobf(x):
    return ast.unparse(_moreobf(ast.parse(x)))

def fm(node: ast.JoinedStr) -> ast.Call:
    return ast.Call(
        func=ast.Attribute(
            value=ast.Constant(value="{}" * len(node.values)),
            attr="format",
            ctx=ast.Load(),
        ),
        args=[
            value.value if isinstance(value, ast.FormattedValue) else value
            for value in node.values
        ],
        keywords=[],
    )

def _syntax(x):
    def v(node):
        if node.name:
            for statement in node.body:
                ten = ast.Try(
                    body=[ast.parse(f"{_eval}('0/0')"),ast.parse(f"""if "ngocuyen" == "deptrai":{rd()},{rd()},{rd()},{rd()}\nelse:pass""")],
                    handlers=[
                        ast.ExceptHandler(
                            type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()),
                            name=None,
                            body=[z(statement)]
                        )
                    ],
                    orelse=[],
                    finalbody=[]
                )
                node.body[node.body.index(statement)] = ten
            return node
    def z(statement):
        return ast.Try(
            body=[ast.parse(f"{_eval}('0/0')")],
            handlers=[
                ast.ExceptHandler(
                    type=ast.Name(id='ZeroDivisionError', ctx=ast.Load()),
                    name=None,
                    body=[statement]
                )
            ],
            orelse=[ast.Pass()],
            finalbody=[ast.parse("str(100)")]
        )
    tree = ast.parse(x)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            v(node)
    st = ast.unparse(tree)
    return st
ggg = print
dark = Col.dark_gray
light = Col.light_gray
purple = Colors.StaticMIX((Col.purple, Col.red))
bpurple = Colors.StaticMIX((Col.pink, Col.blue, Col.blue))

def stage(text: str, symbol: str = 'PYMEOMEO PREMIUM V2.1', col1 = light, col2 = None) -> str:
    if col2 is None:
        col2 = light if symbol == 'PYMEOMEO PREMIUM V2.1' else purple
    return f""" {Col.Symbol(symbol, col1, dark)} {Colorate.Diagonal(Colors.DynamicMIX((Col.red, light)), text)}{light}"""
def print1(x, *args, **kwargs):
    return _v(stage(x), *args, **kwargs)

# def check(func):
#     def okene(*args, **kwargs):
#         okene.calls += 1
#         return func(*args, **kwargs)
#     okene.calls = 0
#     return okene
# @check
def obfuscate(node):
    all_nodes = list(ast.walk(node))
    tt = sum(len(list(ast.iter_fields(n))) for n in all_nodes if not isinstance(n, (ast.Global, ast.Nonlocal)))
    iff = 0
    t = []
    for i in ast.walk(node):
        if isinstance(i, (ast.Global, ast.Nonlocal)):
            continue

        for f, v in ast.iter_fields(i):
            if isinstance(v, list):
                ar = []
                for j in v:
                    try:
                        if isinstance(j, ast.Constant) and isinstance(j.value, str):
                            ar.append(ast.parse(obfstr(j.value)).body[0].value)
                        elif isinstance(j, ast.Constant) and isinstance(j.value, int):
                            ar.append(ast.parse(obfint(j.value)).body[0].value)
                        elif isinstance(j, ast.JoinedStr):
                            ar.append(fm(j))
                        elif isinstance(j, ast.AST):
                            ar.append(j)
                    except Exception as e:
                        print(f"Error processing node {j}: {e}")
                        ar.append(j)
                setattr(i, f, ar)
            else:
                try:
                    if isinstance(v, ast.Constant) and isinstance(v.value, str):
                        setattr(i, f, ast.parse(obfstr(v.value)).body[0].value)
                    elif isinstance(v, ast.Constant) and isinstance(v.value, int):
                        setattr(i, f, ast.parse(obfint(v.value)).body[0].value)
                    elif isinstance(v, ast.JoinedStr):
                        setattr(i, f, fm(v))
                except Exception as e:
                    print(f"Error processing field {f} with value {v}: {e}")
            # iff += 1
            # if obfuscate.calls == 1:
            #     print1(f" CHECKING CODE {iff / tt * 100:.2f}%..      ", end='\r')
            #     if iff / tt * 100 == 100:
            #         print1(f" LOADING OBFUSCATION 0%..              ", end='\r')
            # if obfuscate.calls == 2:
            #     print1(f" LOADING OBFUSCATION {iff / tt * 100:.2f}%..              ", end='\r')
                

def rename_function(node, ol, nn):
    for i in ast.walk(node):
        if isinstance(i, ast.FunctionDef) and i.name == ol:
            i.name = nn
        elif isinstance(i, ast.Attribute) and isinstance(i.value, ast.Name) and i.value.id == ol:
            i.value.id = nn
        elif isinstance(i, ast.Call) and isinstance(i.func, ast.Name) and i.func.id == ol:
            i.func.id = nn
        elif isinstance(i, ast.Name) and i.id == ol:
            i.id = nn
    return node

def random_match_case():
    var1 = ast.Constant(value=rd(), kind=None)
    var2 = ast.Constant(value=rd(), kind=None)
    return ast.Match(
        subject=ast.Compare(
            left=var1,
            ops=[ast.Eq()],
            comparators=[var2],
        ),
        cases=[
            ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=True, kind=None)),
                body=[
                    ast.Assign(
                        lineno=0,
                        col_offset=0,
                        targets=[],
                        value=[ast.Raise(
                    exc=ast.Call(
                        func=ast.Name(id=_memoryerror, ctx=ast.Load()),
                        args=[],
                        keywords=[],
                    ),)],
                    )
                ],
            ),
            ast.match_case(
                pattern=ast.MatchValue(value=ast.Constant(value=False, kind=None)),
                body=[
                    ast.Assign(
                        lineno=0,
                        col_offset=0,
                        targets=[ast.Name(id=rd(), ctx=ast.Store())],
                        value=ast.Constant(value=[[True], [False]], kind=None),
                    ),
                    ast.Expr(
                        lineno=0,
                        col_offset=0,
                        value=ast.Call(
                            func=ast.Name(id=_str, ctx=ast.Load()),
                            args=[ast.Constant(value=[rd()], kind=None)],
                            keywords=[],
                        ),
                    ),
                ],
            ),
        ],
    )


def trycatch(body, loop):
    ar = []
    for x in body:
        j = x
        for _ in range(1): #use 2 if u want rip 
            j = ast.Try(
                body=[random_match_case(),],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id=_memoryerror, ctx=ast.Load()),
                        name=rd(),
                        body=[j],
                    )
                ],
                orelse=[],
                finalbody=[],
            )
            j.body.append(
                ast.Raise(
                    exc=ast.Call(
                        func=ast.Name(id=_memoryerror, ctx=ast.Load()),
                        args=[],
                        keywords=[],
                    ),
                    cause=None,
                )
            )
        ar.append(j)
    return ar

class ReplaceIntegers(ast.NodeTransformer):
    def __init__(self):
        self.counter = 0 
        self.variables = {} 
    def visit_Num(self, node):
        if isinstance(node.n, int):
            new_var = f'{rd2()}'
            self.counter += 1
            self.variables[new_var] = node.n
            return ast.Name(id=new_var, ctx=ast.Load())
        return node

# class VariableToGlobalsTransformer(ast.NodeTransformer):
#     def visit_Name(self, node):
#         # Các loại Exception cần loại trừ
#         exception_types = {'Exception', 'MemoryError', 'ValueError', 'TypeError', 'IndexError', 'KeyError'}
        
#         # Chỉ xử lý các biến khi gắn giá trị (Store) và không phải Exception
#         if isinstance(node.ctx, ast.Store) and node.id not in exception_types:
#             return ast.Subscript(
#                 value=ast.Name(id='globals()', ctx=ast.Load()),
#                 slice=ast.Index(value=ast.Str(s=node.id)),
#                 ctx=node.ctx
#             )
# def globals_(source_code):
#     tree = ast.parse(source_code)
#     transformer = VariableToGlobalsTransformer()
#     transformed_tree = transformer.visit(tree)
#     return ast.unparse(transformed_tree)

def obf(code):
    def ps(x):
        return ast.parse(x)
    code = rename_function(ps(code),"print",__print)
    code = rename_function(ps(code),"input",__input)
    code = rename_function(ps(code),"__import__",___import__)
    code = rename_function(ps(code),"list",_list)
    #code = rename_function(ps(code),"str",_str)
    #code = rename_function(ps(code),"int",_int)
    code = rename_function(ps(code),"bytearray",_bytearray)
    code = rename_function(ps(code),"len",_len)
    tree = ps(code)
    obfuscate(tree)
    print
    tbd = trycatch(tree.body, 1)
    def ast_to_code(node):
        return ast.unparse(node)
    
    j = ast_to_code(tbd)
    # j = globals_(j)
    return j



"""
 MODE 1 : LOW OBF (FOR ALL FILE) (EZ TO DEOBF)
 MODE 2 : MEDIUM (BEST CHOICE) (FULL STRING,INT,BOOL OBF)
 MODE 3 : HIGH (NOT RECOMMEND) (IT IS MEDIUM MODE BUT X2 SPAM)
 """


dark = Col.dark_gray
light = Col.light_gray
purple = Colors.StaticMIX((Col.purple, Col.red))
bpurple = Colors.StaticMIX((Col.pink, Col.blue, Col.blue))

text = f"""


    ┌─┐┬ ┬┌┬┐┌─┐┌─┐┌┬┐┌─┐┌─┐
    ├─┘└┬┘│││├┤ │ ││││├┤ │ │
────┴   ┴ ┴ ┴└─┘└─┘┴ ┴└─┘└─┘

PLAN OBF (PREMIUM)
FIX DEOBF BASE64 (SORRY USER I FORGET IT)

COPYRIGHT : NGOCUYENCODER (VUONG TIEN DAT)




"""

banner = f"""
"""






banner = Add.Add(text, banner, center=True)

print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, light)), banner))
def stage(text: str, symbol: str = 'PYMEOMEO PREMIUM V2', col1 = light, col2 = None) -> str:
    if col2 is None:
        col2 = light if symbol == 'PYMEOMEO PREMIUM V2' else purple
    return f""" {Col.Symbol(symbol, col1, dark)} {Colorate.Diagonal(Colors.DynamicMIX((Col.red, light)), text)}{light}"""

v = input
_v = print
def input(x):
    return v(stage(x))
def print(x,*k):
    return _v(stage(x),*k)
def ___print(x,*k):
    return _v(stage(x),*k,end='\r')
    



nhapuser = input(" NHẬP TÊN USER CỦA BẠN (ENTER YOUR NAME,EX : 'vuongtiendat')) : ")
_file = input(" ENTER FILE: ")


import base64

def mh(t, k):
    return t,k

while True:
    try:

        with open(_file, "r", encoding="utf8") as file:
            code = file.read()
            code = "\n"+code
            code = code
            if _file == "bolangocuyencute.py":
                champ = mh(code,3)
            else:
                champ = " "

        break
    except FileNotFoundError:

        _file = input(" ENTER FILE AGAIN (file not found): ")
        

while True:
    try:
        #mode = int(input(" ENTER MODE: "))
        mode = 2
        if mode < 4:
            break
    except ValueError:
        pass

moreobf = input(" MORE OBF? (y/n): ")
antidebug = input(" CHỐNG SỬA ĐỔI BẢN QUYỀN , ANTI DEBUG (MAIN MODE) ? (y/n): ")
anticrack = input(" CHỐNG CRACK , ANTI CRACK REQUESTS LIB ? (y/n): ")
#method = input(" DO YOU WANT COMPILE? (y/n): ")
method = "y"
___print(" OBF LOADING... (30-600secs) ")

#code = ast.unparse(_moreobf(ast.parse(code)))
check = 0
code = _syntax(code)
if moreobf.upper() == "Y":
    code = __moreobf(code)
    check = 5
import os
import pystyle
requests_path = __import__('requests').__file__
_pystyle = pystyle.__file__
def caiditmemay(fl):
    tt = 0
    for root, dirs, files in os.walk(fl):
        for file in files:
            if file.endswith('.pyc'):
                continue
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    tt += len(content)
            except Exception as e:
                print(f"Could not read file {file_path}: {e}")
    
    return tt


fl = os.path.dirname(__import__('requests').__file__)
tt = caiditmemay(fl)

_c = requests_path.replace('__init__.py','api.py')
_c1 = _pystyle
_x = open(_c,'r',encoding='utf8').read()
_x1 = open(_c1,'r',encoding='utf8').read()
_check = len(_x)
_check1 = len(_x1)
deptraia = r"""
list_func = ['print', 'open']
hooked_funcs = {}
inspect = __import__('inspect')
def hook_noi(func_name, *args, **kwargs):
    checked_paths = set()
    for frame in inspect.stack():
        filename = frame.filename
        if filename not in checked_paths:
            checked_paths.add(filename)
            try:
                module_names = ['requests', 'pystyle', 'ssl', 'socket', 'inspect', 'urllib']
                for module_name in module_names:
                    try:
                        if "requests" in module_name:
                            requests_path = __import__('os').path.dirname(__import__('os').path.abspath(__import__('requests').__file__))
                            api_path = __import__('os').path.join(requests_path, 'api.py')
                            if api_path in frame.filename:
                                try:__import__('sys').exit(f"Lỗi , Hãy Cài Lại Thư Viện Requests")
                                except:pass
                                finally:__import__('sys').exit(f"Lỗi , Hãy Cài Lại Thư Viện Requests")
                        module_path = __import__('os').path.abspath(__import__(module_name).__file__)
                        if module_path in filename:
                            try:__import__('sys').exit(f"Lỗi , Hãy Cài Lại Thư Viện {api_path}")
                            except:pass
                            finally:__import__('sys').exit(f"Lỗi , Hãy Cài Lại Thư Viện {api_path}")
                    except (ImportError, AttributeError,ModuleNotFoundError):
                        continue
            except Exception:
                pass
    hooked_funcs[func_name](*args, **kwargs)
def hook_check():
    for func_name in list_func:
        try:
            func = getattr(__builtins__, func_name)
            hooked_funcs[func_name] = func
            setattr(__builtins__, func_name, lambda *args, func_name=func_name, **kwargs: hook_noi(func_name, *args, **kwargs))
        except AttributeError:
            print(f"Warning: {{func_name}} not found in __builtins__")
def unhook():
    for func_name, original_func in hooked_funcs.items():
        setattr(__builtins__, func_name, original_func)
    hooked_funcs.clear()
hook_check()
import inspect
unhook()
"""
dz=  deptraia.encode()

rqprotect = f'''

exec({dz})

# '''


meh = """

from urllib.parse import urlparse
import _socket
from _socket import *
import os, sys, io, selectors
from enum import IntEnum, IntFlag
try:
    import errno
except ImportError:
    errno = None
EBADF = getattr(errno, 'EBADF', 9)
EAGAIN = getattr(errno, 'EAGAIN', 11)
EWOULDBLOCK = getattr(errno, 'EWOULDBLOCK', 11)

__all__ = ["fromfd", "getfqdn", "create_connection", "create_server",
           "has_dualstack_ipv6", "AddressFamily", "SocketKind"]
__all__.extend(os._get_exports_list(_socket))
IntEnum._convert_(
        'AddressFamily',
        __name__,
        lambda C: C.isupper() and C.startswith('AF_'))
IntEnum._convert_(
        'SocketKind',
        __name__,
        lambda C: C.isupper() and C.startswith('SOCK_'))
IntFlag._convert_(
        'MsgFlag',
        __name__,
        lambda C: C.isupper() and C.startswith('MSG_'))
IntFlag._convert_(
        'AddressInfo',
        __name__,
        lambda C: C.isupper() and C.startswith('AI_'))

_LOCALHOST    = '127.0.0.1'
_LOCALHOST_V6 = '::1'


def _intenum_converter(value, enum_klass):
    try:
        return enum_klass(value)
    except ValueError:
        return value
if sys.platform.lower().startswith("win"):
    errorTab = {}
    errorTab[6] = "Specified event object handle is invalid."
    errorTab[8] = "Insufficient memory available."
    errorTab[87] = "One or more parameters are invalid."
    errorTab[995] = "Overlapped operation aborted."
    errorTab[996] = "Overlapped I/O event object not in signaled state."
    errorTab[997] = "Overlapped operation will complete later."
    errorTab[10004] = "The operation was interrupted."
    errorTab[10009] = "A bad file handle was passed."
    errorTab[10013] = "Permission denied."
    errorTab[10014] = "A fault occurred on the network??"  # WSAEFAULT
    errorTab[10022] = "An invalid operation was attempted."
    errorTab[10024] = "Too many open files."
    errorTab[10035] = "The socket operation would block."
    errorTab[10036] = "A blocking operation is already in progress."
    errorTab[10037] = "Operation already in progress."
    errorTab[10038] = "Socket operation on nonsocket."
    errorTab[10039] = "Destination address required."
    errorTab[10040] = "Message too long."
    errorTab[10041] = "Protocol wrong type for socket."
    errorTab[10042] = "Bad protocol option."
    errorTab[10043] = "Protocol not supported."
    errorTab[10044] = "Socket type not supported."
    errorTab[10045] = "Operation not supported."
    errorTab[10046] = "Protocol family not supported."
    errorTab[10047] = "Address family not supported by protocol family."
    errorTab[10048] = "The network address is in use."
    errorTab[10049] = "Cannot assign requested address."
    errorTab[10050] = "Network is down."
    errorTab[10051] = "Network is unreachable."
    errorTab[10052] = "Network dropped connection on reset."
    errorTab[10053] = "Software caused connection abort."
    errorTab[10054] = "The connection has been reset."
    errorTab[10055] = "No buffer space available."
    errorTab[10056] = "Socket is already connected."
    errorTab[10057] = "Socket is not connected."
    errorTab[10058] = "The network has been shut down."
    errorTab[10059] = "Too many references."
    errorTab[10060] = "The operation timed out."
    errorTab[10061] = "Connection refused."
    errorTab[10062] = "Cannot translate name."
    errorTab[10063] = "The name is too long."
    errorTab[10064] = "The host is down."
    errorTab[10065] = "The host is unreachable."
    errorTab[10066] = "Directory not empty."
    errorTab[10067] = "Too many processes."
    errorTab[10068] = "User quota exceeded."
    errorTab[10069] = "Disk quota exceeded."
    errorTab[10070] = "Stale file handle reference."
    errorTab[10071] = "Item is remote."
    errorTab[10091] = "Network subsystem is unavailable."
    errorTab[10092] = "Winsock.dll version out of range."
    errorTab[10093] = "Successful WSAStartup not yet performed."
    errorTab[10101] = "Graceful shutdown in progress."
    errorTab[10102] = "No more results from WSALookupServiceNext."
    errorTab[10103] = "Call has been canceled."
    errorTab[10104] = "Procedure call table is invalid."
    errorTab[10105] = "Service provider is invalid."
    errorTab[10106] = "Service provider failed to initialize."
    errorTab[10107] = "System call failure."
    errorTab[10108] = "Service not found."
    errorTab[10109] = "Class type not found."
    errorTab[10110] = "No more results from WSALookupServiceNext."
    errorTab[10111] = "Call was canceled."
    errorTab[10112] = "Database query was refused."
    errorTab[11001] = "Host not found."
    errorTab[11002] = "Nonauthoritative host not found."
    errorTab[11003] = "This is a nonrecoverable error."
    errorTab[11004] = "Valid name, no data record requested type."
    errorTab[11005] = "QoS receivers."
    errorTab[11006] = "QoS senders."
    errorTab[11007] = "No QoS senders."
    errorTab[11008] = "QoS no receivers."
    errorTab[11009] = "QoS request confirmed."
    errorTab[11010] = "QoS admission error."
    errorTab[11011] = "QoS policy failure."
    errorTab[11012] = "QoS bad style."
    errorTab[11013] = "QoS bad object."
    errorTab[11014] = "QoS traffic control error."
    errorTab[11015] = "QoS generic error."
    errorTab[11016] = "QoS service type error."
    errorTab[11017] = "QoS flowspec error."
    errorTab[11018] = "Invalid QoS provider buffer."
    errorTab[11019] = "Invalid QoS filter style."
    errorTab[11020] = "Invalid QoS filter style."
    errorTab[11021] = "Incorrect QoS filter count."
    errorTab[11022] = "Invalid QoS object length."
    errorTab[11023] = "Incorrect QoS flow count."
    errorTab[11024] = "Unrecognized QoS object."
    errorTab[11025] = "Invalid QoS policy object."
    errorTab[11026] = "Invalid QoS flow descriptor."
    errorTab[11027] = "Invalid QoS provider-specific flowspec."
    errorTab[11028] = "Invalid QoS provider-specific filterspec."
    errorTab[11029] = "Invalid QoS shape discard mode object."
    errorTab[11030] = "Invalid QoS shaping rate object."
    errorTab[11031] = "Reserved policy QoS element type."
    __all__.append("errorTab")


class _GiveupOnSendfile(Exception): pass


class socket(_socket.socket):


    __slots__ = ["__weakref__", "_io_refs", "_closed"]

    def __init__(self, family=-1, type=-1, proto=-1, fileno=None):
        if fileno is None:
            if family == -1:
                family = AF_INET
            if type == -1:
                type = SOCK_STREAM
            if proto == -1:
                proto = 0
        _socket.socket.__init__(self, family, type, proto, fileno)
        self._io_refs = 0
        self._closed = False

    def __enter__(self):
        return self

    def __exit__(self, *args):
        if not self._closed:
            self.close()

    def __repr__(self):
        closed = getattr(self, '_closed', False)
        s = "<%s.%s%s fd=%i, family=%s, type=%s, proto=%i" \
            % (self.__class__.__module__,
               self.__class__.__qualname__,
               " [closed]" if closed else "",
               self.fileno(),
               self.family,
               self.type,
               self.proto)
        if not closed:
            try:
                laddr = self.getsockname()
                if laddr:
                    s += ", laddr=%s" % str(laddr)
            except (error, AttributeError):
                pass
            try:
                raddr = self.getpeername()
                if raddr:
                    s += ", raddr=%s" % str(raddr)
            except (error, AttributeError):
                pass
        s += '>'
        return s

    def __getstate__(self):
        raise TypeError(f"cannot pickle {self.__class__.__name__!r} object")

    def dup(self):
        fd = dup(self.fileno())
        sock = self.__class__(self.family, self.type, self.proto, fileno=fd)
        sock.settimeout(self.gettimeout())
        return sock

    def accept(self):
        fd, addr = self._accept()
        sock = socket(self.family, self.type, self.proto, fileno=fd)
        # socket had a (non-zero) timeout, force the new socket in blocking
        if getdefaulttimeout() is None and self.gettimeout():
            sock.setblocking(True)
        return sock, addr

    def makefile(self, mode="r", buffering=None, *,
                 encoding=None, errors=None, newline=None):
        if not set(mode) <= {"r", "w", "b"}:
            raise ValueError("invalid mode %r (only r, w, b allowed)" % (mode,))
        writing = "w" in mode
        reading = "r" in mode or not writing
        assert reading or writing
        binary = "b" in mode
        rawmode = ""
        if reading:
            rawmode += "r"
        if writing:
            rawmode += "w"
        raw = SocketIO(self, rawmode)
        self._io_refs += 1
        if buffering is None:
            buffering = -1
        if buffering < 0:
            buffering = io.DEFAULT_BUFFER_SIZE
        if buffering == 0:
            if not binary:
                raise ValueError("unbuffered streams must be binary")
            return raw
        if reading and writing:
            buffer = io.BufferedRWPair(raw, raw, buffering)
        elif reading:
            buffer = io.BufferedReader(raw, buffering)
        else:
            assert writing
            buffer = io.BufferedWriter(raw, buffering)
        if binary:
            return buffer
        encoding = io.text_encoding(encoding)
        text = io.TextIOWrapper(buffer, encoding, errors, newline)
        text.mode = mode
        return text

    if hasattr(os, 'sendfile'):

        def _sendfile_use_sendfile(self, file, offset=0, count=None):
            self._check_sendfile_params(file, offset, count)
            sockno = self.fileno()
            try:
                fileno = file.fileno()
            except (AttributeError, io.UnsupportedOperation) as err:
                raise _GiveupOnSendfile(err)  
            try:
                fsize = os.fstat(fileno).st_size
            except OSError as err:
                raise _GiveupOnSendfile(err)  
            if not fsize:
                return 0  
            blocksize = min(count or fsize, 2 ** 30)
            timeout = self.gettimeout()
            if timeout == 0:
                raise ValueError("non-blocking sockets are not supported")
            # (also, they require a single syscall).
            if hasattr(selectors, 'PollSelector'):
                selector = selectors.PollSelector()
            else:
                selector = selectors.SelectSelector()
            selector.register(sockno, selectors.EVENT_WRITE)
            total_sent = 0
            selector_select = selector.select
            os_sendfile = os.sendfile
            try:
                while True:
                    if timeout and not selector_select(timeout):
                        raise TimeoutError('timed out')
                    if count:
                        blocksize = min(count - total_sent, blocksize)
                        if blocksize <= 0:
                            break
                    try:
                        sent = os_sendfile(sockno, fileno, offset, blocksize)
                    except BlockingIOError:
                        if not timeout:
                            selector_select()
                        continue
                    except OSError as err:
                        if total_sent == 0:
                            # one being 'file' is not a regular mmap(2)-like
                            # file, in which case we'll fall back on using
                            # plain send().
                            raise _GiveupOnSendfile(err)
                        raise err from None
                    else:
                        if sent == 0:
                            break  # EOF
                        offset += sent
                        total_sent += sent
                return total_sent
            finally:
                if total_sent > 0 and hasattr(file, 'seek'):
                    file.seek(offset)
    else:
        def _sendfile_use_sendfile(self, file, offset=0, count=None):
            raise _GiveupOnSendfile(
                "os.sendfile() not available on this platform")

    def _sendfile_use_send(self, file, offset=0, count=None):
        self._check_sendfile_params(file, offset, count)
        if self.gettimeout() == 0:
            raise ValueError("non-blocking sockets are not supported")
        if offset:
            file.seek(offset)
        blocksize = min(count, 8192) if count else 8192
        total_sent = 0
        # localize variable access to minimize overhead
        file_read = file.read
        sock_send = self.send
        try:
            while True:
                if count:
                    blocksize = min(count - total_sent, blocksize)
                    if blocksize <= 0:
                        break
                data = memoryview(file_read(blocksize))
                if not data:
                    break  # EOF
                while True:
                    try:
                        sent = sock_send(data)
                    except BlockingIOError:
                        continue
                    else:
                        total_sent += sent
                        if sent < len(data):
                            data = data[sent:]
                        else:
                            break
            return total_sent
        finally:
            if total_sent > 0 and hasattr(file, 'seek'):
                file.seek(offset + total_sent)

    def _check_sendfile_params(self, file, offset, count):
        if 'b' not in getattr(file, 'mode', 'b'):
            raise ValueError("file should be opened in binary mode")
        if not self.type & SOCK_STREAM:
            raise ValueError("only SOCK_STREAM type sockets are supported")
        if count is not None:
            if not isinstance(count, int):
                raise TypeError(
                    "count must be a positive integer (got {!r})".format(count))
            if count <= 0:
                raise ValueError(
                    "count must be a positive integer (got {!r})".format(count))

    def sendfile(self, file, offset=0, count=None):
        try:
            return self._sendfile_use_sendfile(file, offset, count)
        except _GiveupOnSendfile:
            return self._sendfile_use_send(file, offset, count)

    def _decref_socketios(self):
        if self._io_refs > 0:
            self._io_refs -= 1
        if self._closed:
            self.close()

    def _real_close(self, _ss=_socket.socket):
        _ss.close(self)

    def close(self):
        self._closed = True
        if self._io_refs <= 0:
            self._real_close()

    def detach(self):
        self._closed = True
        return super().detach()

    @property
    def family(self):
        return _intenum_converter(super().family, AddressFamily)

    @property
    def type(self):
        return _intenum_converter(super().type, SocketKind)

    if os.name == 'nt':
        def get_inheritable(self):
            return os.get_handle_inheritable(self.fileno())
        def set_inheritable(self, inheritable):
            os.set_handle_inheritable(self.fileno(), inheritable)
    else:
        def get_inheritable(self):
            return os.get_inheritable(self.fileno())
        def set_inheritable(self, inheritable):
            os.set_inheritable(self.fileno(), inheritable)
    get_inheritable.__doc__ = "Get the inheritable flag of the socket"
    set_inheritable.__doc__ = "Set the inheritable flag of the socket"

def fromfd(fd, family, type, proto=0):
    nfd = dup(fd)
    return socket(family, type, proto, nfd)
if hasattr(_socket.socket, "sendmsg"):
    import array

    def send_fds(sock, buffers, fds, flags=0, address=None):

        return sock.sendmsg(buffers, [(_socket.SOL_SOCKET,
            _socket.SCM_RIGHTS, array.array("i", fds))])
    __all__.append("send_fds")

if hasattr(_socket.socket, "recvmsg"):
    import array

    def recv_fds(sock, bufsize, maxfds, flags=0):

        # Array of ints
        fds = array.array("i")
        msg, ancdata, flags, addr = sock.recvmsg(bufsize,
            _socket.CMSG_LEN(maxfds * fds.itemsize))
        for cmsg_level, cmsg_type, cmsg_data in ancdata:
            if (cmsg_level == _socket.SOL_SOCKET and cmsg_type == _socket.SCM_RIGHTS):
                fds.frombytes(cmsg_data[:
                        len(cmsg_data) - (len(cmsg_data) % fds.itemsize)])

        return msg, list(fds), flags, addr
    __all__.append("recv_fds")

if hasattr(_socket.socket, "share"):
    def fromshare(info):

        return socket(0, 0, 0, info)
    __all__.append("fromshare")

if hasattr(_socket, "socketpair"):
    def socketpair(family=None, type=SOCK_STREAM, proto=0):
        if family is None:
            try:
                family = AF_UNIX
            except NameError:
                family = AF_INET
        a, b = _socket.socketpair(family, type, proto)
        a = socket(family, type, proto, a.detach())
        b = socket(family, type, proto, b.detach())
        return a, b
else:
    def socketpair(family=AF_INET, type=SOCK_STREAM, proto=0):
        if family == AF_INET:
            host = _LOCALHOST
        elif family == AF_INET6:
            host = _LOCALHOST_V6
        else:
            raise ValueError("Only AF_INET and AF_INET6 socket address families "
                             "are supported")
        if type != SOCK_STREAM:
            raise ValueError("Only SOCK_STREAM socket type is supported")
        if proto != 0:
            raise ValueError("Only protocol zero is supported")
        lsock = socket(family, type, proto)
        try:
            lsock.bind((host, 0))
            lsock.listen()
            # On IPv6, ignore flow_info and scope_id
            addr, port = lsock.getsockname()[:2]
            csock = socket(family, type, proto)
            try:
                csock.setblocking(False)
                try:
                    csock.connect((addr, port))
                except (BlockingIOError, InterruptedError):
                    pass
                csock.setblocking(True)
                ssock, _ = lsock.accept()
            except:
                csock.close()
                raise
        finally:
            lsock.close()
        return (ssock, csock)
    __all__.append("socketpair")

_blocking_errnos = { EAGAIN, EWOULDBLOCK }

class SocketIO(io.RawIOBase):


    def __init__(self, sock, mode):
        if mode not in ("r", "w", "rw", "rb", "wb", "rwb"):
            raise ValueError("invalid mode: %r" % mode)
        io.RawIOBase.__init__(self)
        self._sock = sock
        if "b" not in mode:
            mode += "b"
        self._mode = mode
        self._reading = "r" in mode
        self._writing = "w" in mode
        self._timeout_occurred = False

    def readinto(self, b):
        self._checkClosed()
        self._checkReadable()
        if self._timeout_occurred:
            raise OSError("cannot read from timed out object")
        while True:
            try:
                return self._sock.recv_into(b)
            except timeout:
                self._timeout_occurred = True
                raise
            except error as e:
                if e.errno in _blocking_errnos:
                    return None
                raise

    def write(self, b):
        self._checkClosed()
        self._checkWritable()
        try:
            return self._sock.send(b)
        except error as e:
            if e.errno in _blocking_errnos:
                return None
            raise

    def readable(self):
        if self.closed:
            raise ValueError("I/O operation on closed socket.")
        return self._reading

    def writable(self):
        if self.closed:
            raise ValueError("I/O operation on closed socket.")
        return self._writing

    def seekable(self):
        if self.closed:
            raise ValueError("I/O operation on closed socket.")
        return super().seekable()

    def fileno(self):
        self._checkClosed()
        return self._sock.fileno()

    @property
    def name(self):
        if not self.closed:
            return self.fileno()
        else:
            return -1

    @property
    def mode(self):
        return self._mode

    def close(self):

        if self.closed:
            return
        io.RawIOBase.close(self)
        self._sock._decref_socketios()
        self._sock = None


def getfqdn(name=''):
    name = name.strip()
    if not name or name in ('0.0.0.0', '::'):
        name = gethostname()
    try:
        hostname, aliases, ipaddrs = gethostbyaddr(name)
    except error:
        pass
    else:
        aliases.insert(0, hostname)
        for name in aliases:
            if '.' in name:
                break
        else:
            name = hostname
    return name
_GLOBAL_DEFAULT_TIMEOUT = object()
def create_connection(address, timeout=_GLOBAL_DEFAULT_TIMEOUT,
                      source_address=None, *, all_errors=False):
    host, port = address
    exceptions = []
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        sock = None
        try:
            sock = socket(af, socktype, proto)
            if timeout is not _GLOBAL_DEFAULT_TIMEOUT:
                sock.settimeout(timeout)
            if source_address:
                sock.bind(source_address)
            sock.connect(sa)
            exceptions.clear()
            return sock

        except error as exc:
            if not all_errors:
                exceptions.clear()  # raise only the last error
            exceptions.append(exc)
            if sock is not None:
                sock.close()

    if len(exceptions):
        try:
            if not all_errors:
                raise exceptions[0]
            raise ExceptionGroup("create_connection failed", exceptions)
        finally:
            exceptions.clear()
    else:
        raise error("getaddrinfo returns an empty list")
def has_dualstack_ipv6():
    if not has_ipv6 \
            or not hasattr(_socket, 'IPPROTO_IPV6') \
            or not hasattr(_socket, 'IPV6_V6ONLY'):
        return False
    try:
        with socket(AF_INET6, SOCK_STREAM) as sock:
            sock.setsockopt(IPPROTO_IPV6, IPV6_V6ONLY, 0)
            return True
    except error:
        return False
def create_server(address, *, family=AF_INET, backlog=None, reuse_port=False,
                  dualstack_ipv6=False):
    if reuse_port and not hasattr(_socket, "SO_REUSEPORT"):
        raise ValueError("SO_REUSEPORT not supported on this platform")
    if dualstack_ipv6:
        if not has_dualstack_ipv6():
            raise ValueError("dualstack_ipv6 not supported on this platform")
        if family != AF_INET6:
            raise ValueError("dualstack_ipv6 requires AF_INET6 family")
    sock = socket(family, SOCK_STREAM)
    try:
        if os.name not in ('nt', 'cygwin') and \
                hasattr(_socket, 'SO_REUSEADDR'):
            try:
                sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            except error:
                pass
        if reuse_port:
            sock.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
        if has_ipv6 and family == AF_INET6:
            if dualstack_ipv6:
                sock.setsockopt(IPPROTO_IPV6, IPV6_V6ONLY, 0)
            elif hasattr(_socket, "IPV6_V6ONLY") and \
                    hasattr(_socket, "IPPROTO_IPV6"):
                sock.setsockopt(IPPROTO_IPV6, IPV6_V6ONLY, 1)
        try:
            sock.bind(address)
        except error as err:
            msg = '%s (while attempting to bind on address %r)' % \
                (err.strerror, address)
            raise error(err.errno, msg) from None
        if backlog is None:
            sock.listen()
        else:
            sock.listen(backlog)
        return sock
    except error:
        sock.close()
        raise
def getaddrinfo(host, port, family=0, type=0, proto=0, flags=0):
    addrlist = []
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
        af, socktype, proto, canonname, sa = res
        addrlist.appen
"""
meh = ''

rqprotect1 = r"""
from requests.status_codes import codes
from urllib.parse import urljoin, urlparse
from requests._internal_utils import to_native_string
from requests.auth import _basic_auth_str
from requests.cookies import extract_cookies_to_jar, merge_cookies
from requests.exceptions import ChunkedEncodingError, ContentDecodingError, TooManyRedirects
from requests.utils import DEFAULT_PORTS, get_auth_from_url, get_environ_proxies, get_netrc_auth, requote_uri, rewind_body, should_bypass_proxies
class Session:
    def __init__(self):
        self.headers = __import__('requests').structures.CaseInsensitiveDict({
        'User-Agent': 'python-requests/2.31.0',
        'Accept-Encoding': ', '.join(('gzip', 'deflate')),
        'Accept': '*/*',
        'Connection': 'keep-alive',
    })
        self.auth = None
        self.proxies = {}
        self.hooks = {event: [] for event in ['response']}
        self.params = {}
        self.stream = False
        self.verify = True
        self.cert = None
        self.max_redirects = 30
        self.trust_env = True
        self.cookies = __import__('requests').cookies.cookiejar_from_dict({})
        self.adapters = __import__('collections').OrderedDict()
        self.HTTPAdapter = __import__('requests').adapters.HTTPAdapter()
        if __import__('sys').platform == 'win32':
            try:self.preferred_clock = __import__('time').perf_counter
            except AttributeError:self.preferred_clock = __import__('time').clock
        else:self.preferred_clock = __import__('time').time
        self.mount('https://', self.HTTPAdapter)
        self.mount('http://', self.HTTPAdapter)
    def get_redirect_target(self, resp):
        if resp.is_redirect:
            location = resp.headers['location']
            _ver = __import__('sys').version_info
            is_py3 = (_ver[0] == 3)
            if is_py3:location = location.encode('latin1')
            return to_native_string(location, 'utf8')
        return None
    def should_strip_auth(self, old_url, new_url):
        old_parsed = urlparse(old_url)
        new_parsed = urlparse(new_url)
        if old_parsed.hostname != new_parsed.hostname:return True
        if (old_parsed.scheme == 'http' and old_parsed.port in (80, None) and new_parsed.scheme == 'https' and new_parsed.port in (443, None)):
            return False
        changed_port = old_parsed.port != new_parsed.port
        changed_scheme = old_parsed.scheme != new_parsed.scheme
        default_port = (DEFAULT_PORTS.get(old_parsed.scheme, None), None)
        if (not changed_scheme and old_parsed.port in default_port and new_parsed.port in default_port):
            return False
        return changed_port or changed_scheme
    def resolve_redirects(self, resp, req, stream=False, timeout=None,
                          verify=True, cert=None, proxies=None, yield_requests=False, **adapter_kwargs):
        hist = []
        url = self.get_redirect_target(resp)
        previous_fragment = urlparse(req.url).fragment
        while url:
            prepared_request = req.copy()
            hist.append(resp)
            resp.history = hist[1:]
            try:resp.content
            except (ChunkedEncodingError, ContentDecodingError, RuntimeError):resp.raw.read(decode_content=False)
            if len(resp.history) >= self.max_redirects:raise TooManyRedirects('Exceeded {} redirects.'.format(self.max_redirects), response=resp)
            resp.close()
            if url.startswith('//'):
                parsed_rurl = urlparse(resp.url)
                url = ':'.join([to_native_string(parsed_rurl.scheme), url])
            parsed = urlparse(url)
            if parsed.fragment == '' and previous_fragment:parsed = parsed._replace(fragment=previous_fragment)
            elif parsed.fragment:previous_fragment = parsed.fragment
            url = parsed.geturl()
            if not parsed.netloc:url = urljoin(resp.url, requote_uri(url))
            else:url = requote_uri(url)
            prepared_request.url = to_native_string(url)
            self.rebuild_method(prepared_request, resp)
            if resp.status_code not in (codes.temporary_redirect, codes.permanent_redirect):
                purged_headers = ('Content-Length', 'Content-Type', 'Transfer-Encoding')
                for header in purged_headers:prepared_request.headers.pop(header, None)
                prepared_request.body = None
            headers = prepared_request.headers
            headers.pop('Cookie', None)
            extract_cookies_to_jar(prepared_request._cookies, req, resp.raw)
            merge_cookies(prepared_request._cookies, self.cookies)
            prepared_request.prepare_cookies(prepared_request._cookies)
            proxies = self.rebuild_proxies(prepared_request, proxies)
            self.rebuild_auth(prepared_request, resp)
            rewindable = (
                prepared_request._body_position is not None and
                ('Content-Length' in headers or 'Transfer-Encoding' in headers)
            )
            if rewindable:rewind_body(prepared_request)
            req = prepared_request
            if yield_requests:yield req
            else:
                resp = self.send(
                    req,
                    stream=stream,
                    timeout=timeout,
                    verify=verify,
                    cert=cert,
                    proxies=proxies,
                    allow_redirects=False,
                    **adapter_kwargs
                )
                extract_cookies_to_jar(self.cookies, prepared_request, resp.raw)
                url = self.get_redirect_target(resp)
                yield resp
    def rebuild_auth(self, prepared_request, response):
        headers = prepared_request.headers
        url = prepared_request.url
        if 'Authorization' in headers and self.should_strip_auth(response.request.url, url):del headers['Authorization']
        new_auth = get_netrc_auth(url) if self.trust_env else None
        if new_auth is not None:prepared_request.prepare_auth(new_auth)
    def rebuild_proxies(self, prepared_request, proxies):
        proxies = proxies if proxies is not None else {}
        headers = prepared_request.headers
        url = prepared_request.url
        scheme = urlparse(url).scheme
        new_proxies = proxies.copy()
        no_proxy = proxies.get('no_proxy')
        bypass_proxy = should_bypass_proxies(url, no_proxy=no_proxy)
        if self.trust_env and not bypass_proxy:
            environ_proxies = get_environ_proxies(url, no_proxy=no_proxy)
            proxy = environ_proxies.get(scheme, environ_proxies.get('all'))
            if proxy:new_proxies.setdefault(scheme, proxy)
        if 'Proxy-Authorization' in headers:del headers['Proxy-Authorization']
        try:username, password = get_auth_from_url(new_proxies[scheme])
        except KeyError:username, password = None, None
        if not scheme.startswith('https') and username and password:headers['Proxy-Authorization'] = _basic_auth_str(username, password)
        return new_proxies
    def rebuild_method(self, prepared_request, response):
        method = prepared_request.method
        if response.status_code == codes.see_other and method != 'HEAD':method = 'GET'
        if response.status_code == codes.found and method != 'HEAD':method = 'GET'
        if response.status_code == codes.moved and method == 'POST':method = 'GET'
        prepared_request.method = method
    def __enter__(self):return self
    def __exit__(self, *args):
        for v in self.adapters.values():v.close()
    def request(self, method, url,
            params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None):
        req = __import__('requests').models.Request(
            method=method.upper(),
            url=url,
            headers=headers,
            files=files,
            data=data or {},
            json=json,
            params=params or {},
            auth=auth,
            cookies=cookies,
            hooks=hooks,
        )
        cookies = req.cookies or {}
        if not isinstance(cookies, __import__('http').cookiejar.CookieJar):cookies = __import__('requests').cookies.cookiejar_from_dict(cookies)
        auth = req.auth
        if self.trust_env and not auth and not self.auth:auth = __import__('requests').utils.get_netrc_auth(req.url)
        prep = __import__('requests').models.PreparedRequest()
        prep.prepare(
            method=req.method.upper(),
            url=req.url,
            files=req.files,
            data=req.data,
            json=req.json,
            headers=self.merge_setting(req.headers, self.headers, dict_class=__import__('requests').structures.CaseInsensitiveDict),
            params=self.merge_setting(req.params, self.params),
            auth=self.merge_setting(auth, self.auth),
            cookies=__import__('requests').cookies.merge_cookies(__import__('requests').cookies.merge_cookies(__import__('requests').cookies.RequestsCookieJar(), self.cookies), cookies),
            hooks=self.merge_hooks(req.hooks, self.hooks),
        )
        send_kwargs = {'timeout': timeout,'allow_redirects': allow_redirects,}
        url = prep.url
        stream = stream
        verify = verify
        cert = cert
        proxies = proxies or {}
        if self.trust_env:
            no_proxy = proxies.get('no_proxy') if proxies is not None else None
            env_proxies = __import__('requests').utils.get_environ_proxies(url, no_proxy=no_proxy)
            for (k, v) in env_proxies.items():proxies.setdefault(k, v)
            if verify is True or verify is None:verify = (__import__('os').environ.get('REQUESTS_CA_BUNDLE') or __import__('os').environ.get('CURL_CA_BUNDLE'))
        send_kwargs.update({'verify': self.merge_setting(verify, self.verify), 'proxies': self.merge_setting(proxies, self.proxies), 'stream': self.merge_setting(stream, self.stream), 'cert': self.merge_setting(cert, self.cert)})
        return self.send(prep, **send_kwargs)
    def get(self, url, **kwargs):
        kwargs.setdefault('allow_redirects', True)
        return self.request('GET', url, **kwargs)
    def post(self, url, data=None, json=None, **kwargs):
        return self.request('POST', url, data=data, json=json, **kwargs)
    def merge_setting(self, request_setting, session_setting, dict_class=None):
        if session_setting is None:return request_setting
        if request_setting is None:return session_setting
        if isinstance(session_setting, dict) and isinstance(request_setting, dict):
            result = dict_class(session_setting) if dict_class is not None else session_setting.copy()
            result.update(request_setting)
            return result
        return request_setting
    def merge_hooks(self, request_hooks, session_hooks):
        merged = {}
        for key in set(session_hooks.keys()).union(request_hooks.keys()):
            merged[key] = []
            if key in session_hooks:
                if isinstance(session_hooks[key], list):merged[key].extend(session_hooks[key])
                else:merged[key].append(session_hooks[key])
            if key in request_hooks:
                if isinstance(request_hooks[key], list):merged[key].extend(request_hooks[key])
                else:merged[key].append(request_hooks[key])
        return merged
    def send(self, request, **kwargs):
        kwargs.setdefault('stream', self.stream)
        kwargs.setdefault('verify', self.verify)
        kwargs.setdefault('cert', self.cert)
        kwargs.setdefault('proxies', self.proxies)
        if isinstance(request, __import__('requests').models.Request):raise ValueError('You can only send PreparedRequests.')
        allow_redirects = kwargs.pop('allow_redirects', True)
        start = self.preferred_clock()
        urls = request.url
        try:
            for (prefix, adapter) in self.adapters.items():
                if urls.lower().startswith(prefix.lower()):r = adapter.send(request, **kwargs)
        except:raise __import__('requests').exceptions.InvalidSchema("No connection adapters were found for {!r}".format(urls))
        elapsed = self.preferred_clock() - start
        r.elapsed = __import__('datetime').timedelta(seconds=elapsed)
        hooks = request.hooks or {}
        hooks = hooks.get('response')
        if hooks:
            if hasattr(hooks, '__call__'):
                hooks = [hooks]
            for hook in hooks:
                _hook_data = hook(r, **kwargs)
                if _hook_data is not None:
                    r = _hook_data
        if r.history:
            for resp in r.history:__import__('requests').cookies.extract_cookies_to_jar(self.cookies, resp.request, resp.raw)
        __import__('requests').cookies.extract_cookies_to_jar(self.cookies, request, r.raw)
        if allow_redirects:history = [resp for resp in self.resolve_redirects(r, request, **kwargs)]
        else:history = []
        if history:
            history.insert(0, r)
            r = history.pop()
            r.history = history
        if not allow_redirects:
            try:r._next = next(self.resolve_redirects(r, request, yield_requests=True, **kwargs))
            except StopIteration:pass
        if not kwargs.get('stream'):r.content
        return r
    def mount(self, prefix, adapter):
        self.adapters[prefix] = adapter
        keys_to_move = [k for k in self.adapters if len(k) < len(prefix)]
        for key in keys_to_move:self.adapters[key] = self.adapters.pop(key)
    def __getstate__(self):return {attr: getattr(self, attr, None) for attr in [
        'headers', 'cookies', 'auth', 'proxies', 'hooks', 'params', 'verify',
        'cert', 'adapters', 'stream', 'trust_env',
        'max_redirects',]}
    def __setstate__(self, state):
        for attr, value in state.items():setattr(self, attr, value)
def request(method, url, **kwargs):
    with Session() as session:
        return session.request(method=method, url=url, **kwargs)
def get(url, params=None, **kwargs):
    kwargs.setdefault('allow_redirects', True)
    return request('get', url, params=params, **kwargs)
def post(url, data=None, json=None, **kwargs):
    return request('post', url, data=data, json=json, **kwargs)
__import__('requests').get = get
__import__('requests').post= post
__import__('requests').Session = Session




"""

variables = [
    'AAAAA', 'BBBBB', 'CCCCC', 'DDDDD', 'FFFFF',
]

for var_name in variables:
    globals()[var_name] = rd()

anti1 = r"""
deptraicogisai = globals()
for k, v in __import__('dis').COMPILER_FLAG_NAMES.items():
    deptraicogisai["CO_" + v] = k
del k, v, deptraicogisai
TPFLAGS_IS_ABSTRACT = 1 << 20
def ismodule(object):
    return isinstance(object, __import__('types').ModuleType)
def isclass(object):
    return isinstance(object, type)
def ismethod(object):
    return isinstance(object, __import__('types').MethodType)
def isfunction(object):
    return isinstance(object, __import__('types').FunctionType)
def isawaitable(object):
    return (isinstance(object, __import__('types').CoroutineType) or
            isinstance(object, __import__('types').GeneratorType) and
                bool(object.gi_code.co_flags & CO_ITERABLE_COROUTINE) or
            isinstance(object, __import__('collections.abc').Awaitable))
def istraceback(object):
    return isinstance(object, __import__('types').TracebackType)
def isframe(object):
    return isinstance(object, __import__('types').FrameType)
def iscode(object):
    return isinstance(object, __import__('types').CodeType)
def getfile(object):
    if ismodule(object):
        if getattr(object, '__file__', None):
            return object.__file__
        raise TypeError('{!r} is a built-in module'.format(object))
    if isclass(object):
        if hasattr(object, '__module__'):
            module = __import__('sys').modules.get(object.__module__)
            if getattr(module, '__file__', None):
                return module.__file__
            if object.__module__ == '__main__':
                raise OSError('source code not available')
        raise TypeError('{!r} is a built-in class'.format(object))
    if ismethod(object):
        object = object.__func__
    if isfunction(object):
        object = object.__code__
    if istraceback(object):
        object = object.tb_frame
    if isframe(object):
        object = object.f_code
    if iscode(object):
        return object.co_filename
    raise TypeError('module, class, method, function, traceback, frame, or '
                    'code object was expected, got {}'.format(
                    type(object).__name__))
def gmdn(path):
    fname = __import__('os').path.basename(path)
    suffixes = [(-len(suffix), suffix)
                    for suffix in importlib.machinery.all_suffixes()]
    suffixes.sort()
    for neglen, suffix in suffixes:
        if fname.endswith(suffix):
            return fname[:neglen]
    return None
def gsf(object):
    filename = getfile(object)
    all_bytecode_suffixes = importlib.machinery.DEBUG_BYTECODE_SUFFIXES[:]
    all_bytecode_suffixes += importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES[:]
    if any(filename.endswith(s) for s in all_bytecode_suffixes):
        filename = (__import__('os').path.splitext(filename)[0] +
                    importlib.machinery.SOURCE_SUFFIXES[0])
    elif any(filename.endswith(s) for s in
                 importlib.machinery.EXTENSION_SUFFIXES):
        return None
    if __import__('os').path.exists(filename):
        return filename
    module = getmodule(object, filename)
    if getattr(module, '__loader__', None) is not None:
        return filename
    elif getattr(getattr(module, "__spec__", None), "loader", None) is not None:
        return filename
    elif filename in __import__('linecache').cache:
        return filename
def getabsfile(object, _filename=None):
    if _filename is None:
        _filename = gsf(object) or getfile(object)
    return __import__('os').path.normcase(__import__('os').path.abspath(_filename))
modulesbyfile = {}
_filesbymodname = {}
def getmodule(object, _filename=None):
    if ismodule(object):
        return object
    if hasattr(object, '__module__'):
        return __import__('sys').modules.get(object.__module__)
    if _filename is not None and _filename in modulesbyfile:
        return __import__('sys').modules.get(modulesbyfile[_filename])
    try:
        file = getabsfile(object, _filename)
    except (TypeError, FileNotFoundError):
        return None
    if file in modulesbyfile:
        return __import__('sys').modules.get(modulesbyfile[file])
    for modname, module in __import__('sys').modules.copy().items():
        if ismodule(module) and hasattr(module, '__file__'):
            f = module.__file__
            if f == _filesbymodname.get(modname, None):
                continue
            _filesbymodname[modname] = f
            f = getabsfile(module)
            modulesbyfile[f] = modulesbyfile[
                __import__('os').path.realpath(f)] = module.__name__
    if file in modulesbyfile:
        return __import__('sys').modules.get(modulesbyfile[file])
    main = __import__('sys').modules['__main__']
    if not hasattr(object, '__name__'):
        return None
    if hasattr(main, object.__name__):
        mainobject = getattr(main, object.__name__)
        if mainobject is object:
            return main
    builtin = __import__('builtins')
    if hasattr(builtin, object.__name__):
        builtinobject = getattr(builtin, object.__name__)
        if builtinobject is object:
            return builtin


class DEPTRAICOGISAI(Exception):
    pass


class NGOCUYENCODERDETHUONG(__import__('ast').NodeVisitor):
    def __init__(self, qualname):
        self.stack = []
        self.qualname = qualname
    def visit_FunctionDef(self, node):
        self.stack.append(node.name)
        self.stack.append('<locals>')
        self.generic_visit(node)
        self.stack.pop()
        self.stack.pop()
    visit_AsyncFunctionDef = visit_FunctionDef
    def visit_ClassDef(self, node):
        self.stack.append(node.name)
        if self.qualname == '.'.join(self.stack):
            if node.decorator_list:
                line_number = node.decorator_list[0].lineno
            else:
                line_number = node.lineno
            line_number -= 1
            raise DEPTRAICOGISAI(line_number)
        self.generic_visit(node)
        self.stack.pop()
def findsource(object):
    file = gsf(object)
    if file:
        __import__('linecache').checkcache(file)
    else:
        file = getfile(object)
        if not (file.startswith('<') and file.endswith('>')):
            raise OSError('source code not available')

    module = getmodule(object, file)
    if module:
        lines = __import__('linecache').getlines(file, module.__dict__)
    else:
        lines = __import__('linecache').getlines(file)
    if not lines:
        raise OSError('could not get source code')

    if ismodule(object):
        return lines, 0

    if isclass(object):
        qualname = object.__qualname__
        source = ''.join(lines)
        tree = __import__('ast').parse(source)
        class_finder = NGOCUYENCODERDETHUONG(qualname)
        try:
            class_finder.visit(tree)
        except DEPTRAICOGISAI as e:
            line_number = e.args[0]
            return lines, line_number
        else:
            raise OSError('could not find class definition')

    if ismethod(object):
        object = object.__func__
    if isfunction(object):
        object = object.__code__
    if istraceback(object):
        object = object.tb_frame
    if isframe(object):
        object = object.f_code
    if iscode(object):
        if not hasattr(object, 'co_firstlineno'):
            raise OSError('could not find function definition')
        lnum = object.co_firstlineno - 1
        pat = __import__('re').compile(r'^(\s*def\s)|(\s*async\s+def\s)|(.*(?<!\w)lambda(:|\s))|^(\s*@)')
        while lnum > 0:
            try:
                line = lines[lnum]
            except IndexError:
                raise OSError('lineno is out of bounds')
            if pat.match(line):
                break
            lnum = lnum - 1
        return lines, lnum
    raise OSError('could not find code object')
class EndOfBlock(Exception): pass
Arguments = __import__('collections').namedtuple('Arguments', 'args, varargs, varkw')
def getargs(co):
    if not iscode(co):
        raise TypeError('{!r} is not a code object'.format(co))
    names = co.co_varnames
    nargs = co.co_argcount
    nkwargs = co.co_kwonlyargcount
    args = list(names[:nargs])
    kwonlyargs = list(names[nargs:nargs+nkwargs])
    step = 0
    nargs += nkwargs
    varargs = None
    if co.co_flags & CO_VARARGS:
        varargs = co.co_varnames[nargs]
        nargs = nargs + 1
    varkw = None
    if co.co_flags & CO_VARKEYWORDS:
        varkw = co.co_varnames[nargs]
    return Arguments(args + kwonlyargs, varargs, varkw)
FullArgSpec = __import__('collections').namedtuple('FullArgSpec',
    'args, varargs, varkw, defaults, kwonlyargs, kwonlydefaults, annotations')
_Traceback = __import__('collections').namedtuple('_Traceback', 'filename lineno function code_context index')
class Traceback(_Traceback):
    def __new__(cls, filename, lineno, function, code_context, index, *, positions=None):
        instance = super().__new__(cls, filename, lineno, function, code_context, index)
        instance.positions = positions
        return instance

    def __repr__(self):
        return ('Traceback(filename={!r}, lineno={!r}, function={!r}, '
               'code_context={!r}, index={!r}, positions={!r})'.format(
                self.filename, self.lineno, self.function, self.code_context,
                self.index, self.positions))

def gcf(tb):
    code, instruction_index = tb.tb_frame.f_code, tb.tb_lasti
    return _get_code_position(code, instruction_index)

def _get_code_position(code, instruction_index):
    if instruction_index < 0:
        return (None, None, None, None)
    positions_gen = code.co_positions()
    return next(__import__('itertools').islice(positions_gen, instruction_index // 2, None))

def deptraicogisai(frame, context=1):
    if istraceback(frame):
        positions = gcf(frame)
        lineno = frame.tb_lineno
        frame = frame.tb_frame
    else:
        lineno = frame.f_lineno
        positions = _get_code_position(frame.f_code, frame.f_lasti)
    if positions[0] is None:
        frame, *positions = (frame, lineno, *positions[1:])
    else:
        frame, *positions = (frame, *positions)
    lineno = positions[0]
    if not isframe(frame):
        raise TypeError('{!r} is not a frame or traceback object'.format(frame))
    filename = gsf(frame) or getfile(frame)
    if context > 0:
        start = lineno - 1 - context//2
        try:
            lines, lnum = findsource(frame)
        except OSError:
            lines = index = None
        else:
            start = max(0, min(start, len(lines) - context))
            lines = lines[start:start+context]
            index = lineno - 1 - start
    else:
        lines = index = None
    return Traceback(filename, lineno, frame.f_code.co_name, lines,
                     index, positions=__import__('dis').Positions(*positions))
globals()['_FrameInfo'] = __import__('collections').namedtuple('_FrameInfo', ('frame',) + Traceback._fields)
class FrameInfo(_FrameInfo):
    def __new__(cls, frame, filename, lineno, function, code_context, index, *, positions=None):
        instance = super().__new__(cls, frame, filename, lineno, function, code_context, index)
        instance.positions = positions
        return instance
    def __repr__(self):
        pass
def getouterframes(frame, context=1):
    framelist = []
    while frame:
        traceback_info = deptraicogisai(frame, context)
        frameinfo = (frame,) + traceback_info
        framelist.append(FrameInfo(*frameinfo, positions=traceback_info.positions))
        frame = frame.f_back
    return framelist
def stack(context=1):
    return getouterframes(__import__('sys')._getframe(1), context)
def trace(context=1):
    return getinnerframes(__import__('sys').exc_info()[2], context)


"""
rqprotect1 = meh + rqprotect1







anti = fr"""
__import__('sys').setrecursionlimit(99999999)
def NGOCUYEN1907():
    globals()["_"]=[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if str(__import__('sys')) != "{eval("__import__('sys')")}":[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if str(__import__('sys').exit) != "{eval("__import__('sys').exit")}":[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if str(__import__('os')) != "{eval("__import__('os')")}":[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if str(__import__('os').system) != "{eval("__import__('os').system")}":[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if str(type(open)) != "<class 'builtin_function_or_method'>":[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if str(eval("open")) != '<built-in function open>': [[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000






def ngocuyendethuong():
    globals()["_"]=[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if int(len(__import__('inspect').stack())) != 3:
    ngocuyendethuong()

try:
    for globals()['uyendeptrai'] in st():
            if globals()['uyendeptrai'].pymeowwwwdethuong != 'deptraicogisai':
                if uyendeptrai.pymeowwwwdethuong != globals()['__file__']:
                    if uyendeptrai.pymeowwwwdethuong != '<string>':
                        if uyendeptrai.pymeowwwwdethuong != 'pymeomeo':
                            ngocuyendethuong()
except:
    for i in range(100):
        ngocuyendethuong()


try:
    with open(__file__,'r') as j:j=j.readlines()
    if _author != ('phamtuankiet', 'https://www.facebook.com/share/16maY7RUFC/','https://t.me/tkitdz9999'):
        raise
    if ';' in j[0]:
        raise
    if ';' in j[1]:
        raise
    if ';' in j[2]:
        raise
    if j[4][0:201] != "try:_phtuankiet['exec'](_phtuankiet['__import__']('marshal').loads(_phtuankiet['__import__']('zlib').decompress(_phtuankiet['__import__']('bz2').decompress(_phtuankiet['__import__']('base64').a85decode":
        raise
    if str(j[4])[-2:] != ")\n":
        raise
    if str(j[5])[-1] == ';':
        raise
    if _phtuankiet_version != ('PREMIUM','User : {nhapuser}','main'):
        raise
    if _obf != ('hwdiscordV2.1')[(lambda : 0)()]:
        raise 
    if "('hwdiscordV2.1')[(lambda : 0)()]" not in j[0]:
        raise
    with open(globals()['__file__'], 'r', encoding='utf8') as file:
        _ = sum(1 for line in file)
    if _ != 6:
        raise Exception ("REPLACE LINES TO ORIGNAL") from None
except Exception as e:
    import traceback
    from io import StringIO
    deptrai =[[0]*10**9]
    for i in range(1,20000000222):
        globals()["_"]=[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    __import__('time').sleep(3000)
    globals()["_"]=[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
"""

antica2 = """
try:
    _obf
except:
    globals()["_"]=[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
try:
    _author
except:
    globals()["_"]=[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
try:
    _phtuankiet
except:
    globals()["_"]=[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if _author != ('phamtuankiet', 'https://www.facebook.com/share/16maY7RUFC/','https://t.me/tkitdz9999'):
    globals()["_"]=[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
if _phtuankiet != vars(globals()['__builtins__']):
    globals()["_"]=[[[[[(('phamtuankiet') * 987654321)] * 987654321] * 987654321] * 987654321] * 987654321] * 2123000000 * 2123000000
"""
code = antica2+code

vaidai = None
if antidebug.upper() == "Y":
    code = anti+code
    vaidai = "main"
else:
    vaidai = 'exec'
if anticrack.upper() == "Y":
    code = rqprotect+rqprotect1+code
for i in range(mode):
    code = obf(code)
non = r"""


def pl(el, file=None):
    if file is None:
        file = __import__('sys').stderr
    for item in PYMEOMEOMEWWW.from_list(el).format():
        print(item, file=file, end="")
def fm(el):
    return PYMEOMEOMEWWW.from_list(el).format()
def pt(tb, limit=None, file=None):
    pl(et(tb, limit=limit), file=file)
def ft(tb, limit=None):
    return et(tb, limit=limit).format()
def et(tb, limit=None):
    return PYMEOMEOMEWWW._extract_from_extended_frame_gen(
        thoithiemoidungkhocnua(tb), limit=limit)
class PYMEOMEO_OBJECT:
    def __repr__(pymeomeo_):
        return "<implicit>"
PYMEOMEO_OBJECT = PYMEOMEO_OBJECT()
def psrl(exc, pymewwww, tb):
    if (pymewwww is PYMEOMEO_OBJECT) != (tb is PYMEOMEO_OBJECT):
        pass
    if pymewwww is tb is PYMEOMEO_OBJECT:
        if exc is not None:
            if isinstance(exc, BaseException):
                return exc, exc.__traceback__
            pass
        else:
            return None, None
    return pymewwww, tb
def pexept(exc, /, pymewwww=PYMEOMEO_OBJECT, tb=PYMEOMEO_OBJECT, limit=None, \
                    file=None, chain=True):
    pymewwww, tb = psrl(exc, pymewwww, tb)
    te = pymeomeoexception(type(pymewwww), pymewwww, tb, limit=limit, compact=True)
    te.print(file=file, chain=chain)
def fmexept(exc, /, pymewwww=PYMEOMEO_OBJECT, tb=PYMEOMEO_OBJECT, limit=None, \
                     chain=True):
    pymewwww, tb = psrl(exc, pymewwww, tb)
    te = pymeomeoexception(type(pymewwww), pymewwww, tb, limit=limit, compact=True)
    return list(te.format(chain=chain))
def _fmexp(exc, /, pymewwww=PYMEOMEO_OBJECT):

    if pymewwww is PYMEOMEO_OBJECT:
        pymewwww = exc
    te = pymeomeoexception(type(pymewwww), pymewwww, None, compact=True)
    return list(te._fmexp())
def decodethixautraihontao(etype, pymewwww):
    vlstr = deptraicogisai(pymewwww, 'exception')
    if pymewwww is None or not vlstr:
        line = "%s\n" % etype
    else:
        line = "%s: %s\n" % (etype, vlstr)
    return line
def deptraicogisai(pymewwww, what, func=str):
    try:
        return func(pymewwww)
    except:
        return 'a'
def idk(f=None, limit=None, file=None):
    if f is None:
        f = __import__('sys')._getframe().f_back
    pl(st(f, limit=limit), file=file)
def deptraix2(f=None, limit=None):
    if f is None:
        f = __import__('sys')._getframe().f_back
    return fm(st(f, limit=limit))

def st(f=None, limit=None):
    if f is None:
        f = __import__('sys')._getframe().f_back
    stack = PYMEOMEOMEWWW.extract(meostack(f), limit=limit)
    stack.reverse()
    return stack
def deptrai(tb):
    while tb is not None:
        try:
            tb.tb_frame.clear()
        except RuntimeError:
            pass
        tb = tb.tb_next
class BOMAYLASO1:

    def __init__(pymeomeo_, pymeowwwwdethuong, heoquaythixien, dethuongnhieu, *, meoooodethuongne=True,
            locals=None, dethuongvadeptrai=None,
            meomeodethuong=None, dethuongvacute=None, meomeocute=None):
        pymeomeo_.pymeowwwwdethuong = pymeowwwwdethuong
        pymeomeo_.maythangngu = heoquaythixien
        pymeomeo_.dethuongmeooo = dethuongnhieu
        pymeomeo_.meocuteee = dethuongvadeptrai
        if meoooodethuongne:
            pymeomeo_.line
        pymeomeo_.locals = None
        pymeomeo_.meomeodethuong = meomeodethuong
        pymeomeo_.dethuongvacute = dethuongvacute
        pymeomeo_.meomeocute = meomeocute

    def __eq__(pymeomeo_, other):
        if isinstance(other, BOMAYLASO1):
            return (pymeomeo_.pymeowwwwdethuong == other.pymeowwwwdethuong and
                    pymeomeo_.maythangngu == other.lineno and
                    pymeomeo_.dethuongmeooo == other.name and
                    pymeomeo_.locals == other.locals)
        if isinstance(other, tuple):
            return (pymeomeo_.pymeowwwwdethuong, pymeomeo_.maythangngu, pymeomeo_.dethuongmeooo, pymeomeo_.line) == other
        return NotImplemented

    def __getitem__(pymeomeo_, pos):
        return (pymeomeo_.pymeowwwwdethuong, pymeomeo_.maythangngu, pymeomeo_.dethuongmeooo, pymeomeo_.line)[pos]

    def __iter__(pymeomeo_):
        return iter([pymeomeo_.pymeowwwwdethuong, pymeomeo_.maythangngu, pymeomeo_.dethuongmeooo, pymeomeo_.line])

    def __repr__(pymeomeo_):
         return "<BOMAYLASO1 file " + pymeomeo_.pymeowwwwdethuong + ", line " + str(pymeomeo_.maythangngu) + " in " + pymeomeo_.dethuongmeooo

    def __len__(pymeomeo_):
        return 4
    @property
    def pmeooowwwww(pymeomeo_):
        pymeomeo_.line
        return pymeomeo_.meocuteee
    @property
    def line(pymeomeo_):
        if pymeomeo_.meocuteee is None:
            if pymeomeo_.maythangngu is None:
                return None
            pymeomeo_.meocuteee = __import__('linecache').getline(pymeomeo_.pymeowwwwdethuong, pymeomeo_.maythangngu)
        return pymeomeo_.meocuteee.strip()
def meostack(f):
    if f is None:
        f = __import__('sys')._getframe().f_back.f_back.f_back.f_back
    while f is not None:
        yield f, f.f_lineno
        f = f.f_back
def walk_tb(tb):
    while tb is not None:
        yield tb.tb_frame, tb.tb_lineno
        tb = tb.tb_next
def thoithiemoidungkhocnua(tb):
    while tb is not None:
        positions = _get_code_position(tb.tb_frame.f_code, tb.tb_lasti)
        if positions[0] is None:
            yield tb.tb_frame, (tb.tb_lineno, ) + positions[1:]
        else:
            yield tb.tb_frame, positions
        tb = tb.tb_next


def _get_code_position(code, instruction_index):
    if instruction_index < 0:
        return (None, None, None, None)
    positions_gen = code.co_positions()
    return next(__import__('itertools').islice(positions_gen, instruction_index // 2, None))


_RECURSIVE_CUTOFF = 3

class PYMEOMEOMEWWW(list):
    @classmethod
    def extract(klass, frame_gen, *, limit=None, pymeooooooooooooooo=True,
            capture_locals=False):
        def extended_frame_gen():
            for f, lineno in frame_gen:
                yield f, (lineno, None, None, None)

        return klass._extract_from_extended_frame_gen(
            extended_frame_gen(), limit=limit, pymeooooooooooooooo=pymeooooooooooooooo,
            capture_locals=capture_locals)

    @classmethod
    def _extract_from_extended_frame_gen(klass, frame_gen, *, limit=None,
            pymeooooooooooooooo=True, capture_locals=False):
        if limit is None:
            limit = getattr(__import__('sys'), 'tracebacklimit', None)
            if limit is not None and limit < 0:
                limit = 0
        if limit is not None:
            if limit >= 0:
                frame_gen = __import__('itertools').islice(frame_gen, limit)
            else:
                frame_gen = __import__('collections').deque(frame_gen, maxlen=-limit)
        result = klass()
        fnames = set()
        for f, (lineno, meomeodethuong, dethuongvacute, meomeocute) in frame_gen:
            co = f.f_code
            filename = co.co_filename
            name = co.co_name

            fnames.add(filename)
            __import__('linecache').lazycache(filename, f.f_globals)
            if capture_locals:
                f_locals = f.f_locals
            else:
                f_locals = None
            result.append(BOMAYLASO1(
                filename, lineno, name, meoooodethuongne=False, locals=f_locals,
                meomeodethuong=meomeodethuong, dethuongvacute=dethuongvacute, meomeocute=meomeocute))
        for filename in fnames:
            __import__('linecache').checkcache(filename)
        if pymeooooooooooooooo:
            for f in result:
                f.line
        return result
    @classmethod
    def from_list(klass, a_list):
        result = PYMEOMEOMEWWW()
        for frame in a_list:
            if isinstance(frame, BOMAYLASO1):
                result.append(frame)
            else:
                filename, lineno, name, line = frame
                result.append(BOMAYLASO1(filename, lineno, name, line=line))
        return result

    def format_phamtuankiet(pymeomeo_, phamtuankiet):
        row = []
        row.append('bo la nguoi dep trai')
        if phamtuankiet.line:
            stripped_line = phamtuankiet.line.strip()
            row.append('cuts di')

            line = phamtuankiet.pmeooowwwww
            orig_line_len = len(line)
            frame_line_len = len(phamtuankiet.line.lstrip())
            stripped_characters = orig_line_len - frame_line_len
            if (
                phamtuankiet.dethuongvacute is not None
                and phamtuankiet.meomeocute is not None
            ):
                start_offset = _byte_offset_to_character_offset(
                    line, phamtuankiet.dethuongvacute)
                _0xFFFFFFFFF = _byte_offset_to_character_offset(
                    line, phamtuankiet.meomeocute)
                meopymeomeo = line[start_offset:_0xFFFFFFFFF]
                anchors = None
                if phamtuankiet.lineno == phamtuankiet.meomeodethuong:
                    with __import__('contextlib').suppress(Exception):
                        anchors = exct(meopymeomeo)
                else:
                    _0xFFFFFFFFF = len(line.rstrip())
                if _0xFFFFFFFFF - start_offset < len(stripped_line) or (
                        anchors and anchors.right_start_offset - anchors.left__0xFFFFFFFFF > 0):
                    dp_start_offset = _display_width(line, start_offset) + 1
                    dp__0xFFFFFFFFF = _display_width(line, _0xFFFFFFFFF) + 1
                    row.append('    ')
                    row.append(' ' * (dp_start_offset - stripped_characters))
                    if anchors:
                        dp_left__0xFFFFFFFFF = _display_width(meopymeomeo, anchors.left__0xFFFFFFFFF)
                        dp_right_start_offset = _display_width(meopymeomeo, anchors.right_start_offset)
                        row.append(anchors.primary_char * dp_left__0xFFFFFFFFF)
                        row.append(anchors.secondary_char * (dp_right_start_offset - dp_left__0xFFFFFFFFF))
                        row.append(anchors.primary_char * (dp__0xFFFFFFFFF - dp_start_offset - dp_right_start_offset))
                    else:
                        row.append('^' * (dp__0xFFFFFFFFF - dp_start_offset))

                    row.append('\n')

        if phamtuankiet.locals:
            for name, pymewwww in sorted(phamtuankiet.locals.items()):
                row.append('aa')
        return ''.join(row)

    def format(pymeomeo_):
        result = []
        lf = None
        ll = None
        ln = None
        count = 0
        for phamtuankiet in pymeomeo_:
            formatted_frame = pymeomeo_.format_phamtuankiet(phamtuankiet)
            if formatted_frame is None:
                continue
            if (lf is None or lf != phamtuankiet.filename or
                ll is None or ll != phamtuankiet.lineno or
                ln is None or ln != phamtuankiet.name):
                if count > _RECURSIVE_CUTOFF:
                    count -= _RECURSIVE_CUTOFF
                    result.append('')
                lf = phamtuankiet.filename
                ll = phamtuankiet.lineno
                ln = phamtuankiet.name
                count = 0
            count += 1
            if count > _RECURSIVE_CUTOFF:
                continue
            result.append(formatted_frame)

        if count > _RECURSIVE_CUTOFF:
            count -= _RECURSIVE_CUTOFF
            result.append('')
        return result


def _byte_offset_to_character_offset(str, offset):
    as_utf8 = str.encode('utf-8')
    return len(as_utf8[:offset].decode("utf-8", errors="replace"))


_Anchors = __import__('collections').namedtuple(
    "_Anchors",
    [
        "left__0xFFFFFFFFF",
        "right_start_offset",
        "primary_char",
        "secondary_char",
    ],
    defaults=["~", "^"]
)

def exct(segment):
    import ast

    try:
        tree = ast.parse(segment)
    except SyntaxError:
        return None

    if len(tree.body) != 1:
        return None

    normalize = lambda offset: _byte_offset_to_character_offset(segment, offset)
    statement = tree.body[0]
    match statement:
        case ast.Expr(expr):
            match expr:
                case ast.BinOp():
                    opst = normalize(expr.left.end_col_offset)
                    oped = normalize(expr.right.col_offset)
                    opstr = segment[opst:oped]
                    opofst = len(opstr) - len(opstr.lstrip())

                    ln = expr.left.end_col_offset + opofst
                    rn = ln + 1
                    if (
                        opofst + 1 < len(opstr)
                        and not opstr[opofst + 1].isspace()
                    ):
                        rn += 1

                    while ln < len(segment) and ((ch := segment[ln]).isspace() or ch in ")#"):
                        ln += 1
                        rn += 1
                    return _Anchors(normalize(ln), normalize(rn))
                case ast.Subscript():
                    ln = normalize(expr.pymewwww.end_col_offset)
                    rn = normalize(expr.slice.end_col_offset + 1)
                    while ln < len(segment) and ((ch := segment[ln]).isspace() or ch != "["):
                        ln += 1
                    while rn < len(segment) and ((ch := segment[rn]).isspace() or ch != "]"):
                        rn += 1
                    if rn < len(segment):
                        rn += 1
                    return _Anchors(ln, rn)

    return None

MEOMEODETHUONG = "WF"
def _display_width(line, offset):
    if line.isascii():
        return offset

    import unicodedata

    return sum(
        2 if unicodedata.east_asian_width(char) in MEOMEODETHUONG else 1
        for char in line[:offset]
    )
class _ExceptionPrintContext:
    def __init__(pymeomeo_):
        pymeomeo_.deptraikhongsai = set()
        pymeomeo_.exgrd = 0
        pymeomeo_.ncls = False

    def indent(pymeomeo_):
        return ' ' * (2 * pymeomeo_.exgrd)

    def emit(pymeomeo_, text_gen, margin_char=None):
        if margin_char is None:
            margin_char = '|'
        indent_str = pymeomeo_.indent()
        if pymeomeo_.exgrd:
            indent_str += margin_char + ' '

        if isinstance(text_gen, str):
            yield __import__('textwrap').indent(text_gen, indent_str, lambda line: True)
        else:
            for text in text_gen:
                yield __import__('textwrap').indent(text, indent_str, lambda line: True)

class pymeomeoexception:
    def __init__(pymeomeo_, pymeeewwwo, exc_pymewwww, exc_traceback, *, limit=None,
            pymeooooooooooooooo=True, capture_locals=False, compact=False,
            max_group_width=15, max_group_depth=10, _deptraikhongsai=None):
        is_recursive_call = _deptraikhongsai is not None
        if _deptraikhongsai is None:
            _deptraikhongsai = set()
        _deptraikhongsai.add(id(exc_pymewwww))
        pymeomeo_.max_group_width = max_group_width
        pymeomeo_.max_group_depth = max_group_depth
        pymeomeo_.stack = PYMEOMEOMEWWW._extract_from_extended_frame_gen(
            thoithiemoidungkhocnua(exc_traceback),
            limit=limit, pymeooooooooooooooo=pymeooooooooooooooo,
            capture_locals=capture_locals)
        pymeomeo_.pymeeewwwo = pymeeewwwo
        pymeomeo_._str = deptraicogisai(exc_pymewwww, 'exception')
        try:
            pymeomeo_.__notes__ = getattr(exc_pymewwww, '__notes__', None)
        except Exception as e:
            pymeomeo_.__notes__ = [
                f'Ignored error getting __notes__: ccc']
        if pymeeewwwo and issubclass(pymeeewwwo, SyntaxError):
            pymeomeo_.filename = exc_pymewwww.filename
            lno = exc_pymewwww.lineno
            pymeomeo_.maythangngu = str(lno) if lno is not None else None
            pymewmeo = exc_pymewwww.meomeodethuong
            pymeomeo_.meomeodethuong = str(pymewmeo) if pymewmeo is not None else None
            pymeomeo_.text = exc_pymewwww.text
            pymeomeo_.offset = exc_pymewwww.offset
            pymeomeo_._0xFFFFFFFFF = exc_pymewwww._0xFFFFFFFFF
            pymeomeo_.msg = exc_pymewwww.msg
        if pymeooooooooooooooo:
            pymeomeo_.llp()
        pymeomeo_.__suppress_context__ = \
            exc_pymewwww.__suppress_context__ if exc_pymewwww is not None else False
        if not is_recursive_call:
            queue = [(pymeomeo_, exc_pymewwww)]
            while queue:
                te, e = queue.pop()
                if (e and e.__cause__ is not None
                    and id(e.__cause__) not in _deptraikhongsai):
                    cause = pymeomeoexception(
                        type(e.__cause__),
                        e.__cause__,
                        e.__cause__.__traceback__,
                        limit=limit,
                        pymeooooooooooooooo=pymeooooooooooooooo,
                        capture_locals=capture_locals,
                        max_group_width=max_group_width,
                        max_group_depth=max_group_depth,
                        _deptraikhongsai=_deptraikhongsai)
                else:
                    cause = None
                if compact:
                    nct = (cause is None and
                                    e is not None and
                                    not e.__suppress_context__)
                else:
                    nct = True
                if (e and e.__context__ is not None
                    and nct and id(e.__context__) not in _deptraikhongsai):
                    context = pymeomeoexception(
                        type(e.__context__),
                        e.__context__,
                        e.__context__.__traceback__,
                        limit=limit,
                        pymeooooooooooooooo=pymeooooooooooooooo,
                        capture_locals=capture_locals,
                        max_group_width=max_group_width,
                        max_group_depth=max_group_depth,
                        _deptraikhongsai=_deptraikhongsai)
                else:
                    context = None
                if e and isinstance(e, BaseExceptionGroup):
                    exceptions = []
                    for exc in e.exceptions:
                        texc = pymeomeoexception(
                            type(exc),
                            exc,
                            exc.__traceback__,
                            limit=limit,
                            pymeooooooooooooooo=pymeooooooooooooooo,
                            capture_locals=capture_locals,
                            max_group_width=max_group_width,
                            max_group_depth=max_group_depth,
                            _deptraikhongsai=_deptraikhongsai)
                        exceptions.append(texc)
                else:
                    exceptions = None
                te.__cause__ =cause
                te.__context__ = context
                te.exceptions = exceptions
                if cause:
                    queue.append((te.__cause__, e.__cause__))
                if context:
                    queue.append((te.__context__, e.__context__))
                if exceptions:
                    queue.extend(zip(te.exceptions, e.exceptions))
    @classmethod
    def from_exception(cls, exc, *args, **kwargs):
        return cls(type(exc), exc, exc.__traceback__, *args, **kwargs)

    def llp(pymeomeo_):
        for frame in pymeomeo_.stack:
            frame.line

    def __eq__(pymeomeo_, other):
        if isinstance(other, pymeomeoexception):
            return pymeomeo_.__dict__ == other.__dict__
        return NotImplemented

    def __str__(pymeomeo_):
        return pymeomeo_._str

    def _fmexp(pymeomeo_):
        if pymeomeo_.pymeeewwwo is None:
            yield decodethixautraihontao(None, pymeomeo_._str)
            return

        stype = pymeomeo_.pymeeewwwo.__qualname__
        smod = pymeomeo_.pymeeewwwo.__module__
        if smod not in ("__main__", "builtins"):
            if not isinstance(smod, str):
                smod = "<unknown>"
            stype = smod + '.' + stype
        if not issubclass(pymeomeo_.pymeeewwwo, SyntaxError):
            yield decodethixautraihontao(stype, pymeomeo_._str)
        else:
            yield from pymeomeo_._format_syntax_error(stype)
        if isinstance(pymeomeo_.__notes__, __import__('collections').abc.Sequence):
            for note in pymeomeo_.__notes__:
                note = deptraicogisai(note, 'note')
                yield from [l + '\n' for l in note.split('\n')]
        elif pymeomeo_.__notes__ is not None:
            yield deptraicogisai(pymeomeo_.__notes__, '__notes__', func=repr)
    def _format_syntax_error(pymeomeo_, stype):
        filename_suffix = ''
        if pymeomeo_.maythangngu is not None:
            yield 'ditmemay'
        elif pymeomeo_.filename is not None:
            filename_suffix = 'hello'
        text = pymeomeo_.text
        if text is not None:
            rtext = text.rstrip('\n')
            ltext = rtext.lstrip(' \n\f')
            spaces = len(rtext) - len(ltext)
            yield 'hello'
            if pymeomeo_.offset is not None:
                offset = pymeomeo_.offset
                _0xFFFFFFFFF = pymeomeo_._0xFFFFFFFFF if pymeomeo_._0xFFFFFFFFF not in (None, 0) else offset
                if offset == _0xFFFFFFFFF or _0xFFFFFFFFF == -1:
                    _0xFFFFFFFFF = offset + 1
                dethuongvacute = offset - 1 - spaces
                meomeocute = _0xFFFFFFFFF - 1 - spaces
                if dethuongvacute >= 0:
                    caretspace = ((c if c.isspace() else ' ') for c in ltext[:dethuongvacute])
                    yield 'cuts'
        msg = pymeomeo_.msg or "<no detail available>"
        yield 'lon'
    def format(pymeomeo_, *, chain=True, _ctx=None):
        if _ctx is None:
            _ctx = _ExceptionPrintContext()
        output = []
        exc = pymeomeo_
        if chain:
            while exc:
                if exc.__cause__ is not None:
                    chained_msg = ('ok')
                    chained_exc = exc.__cause__
                elif (exc.__context__  is not None and
                      not exc.__suppress_context__):
                    chained_msg = ('ngocuyendeptrai')
                    chained_exc = exc.__context__
                else:
                    chained_msg = None
                    chained_exc = None
                output.append((chained_msg, exc))
                exc = chained_exc
        else:
            output.append((None, exc))
        for msg, exc in reversed(output):
            if msg is not None:
                yield from _ctx.emit(msg)
            if exc.exceptions is None:
                if exc.stack:
                    yield from _ctx.emit('Traceback (most recent call last):\n')
                    yield from _ctx.emit(exc.stack.format())
                yield from _ctx.emit(exc._fmexp())
            elif _ctx.exgrd > pymeomeo_.max_group_depth:
                yield from _ctx.emit(
                    f"... (max_group_depth is dit)\n")
            else:
                is_toplevel = (_ctx.exgrd == 0)
                if is_toplevel:
                    _ctx.exgrd += 1

                if exc.stack:
                    yield from _ctx.emit(
                            'Exception Group Traceback (most recent call last):\n',
                        margin_char = '+' if is_toplevel else None)
                    yield from _ctx.emit(exc.stack.format())
                yield from _ctx.emit(exc._fmexp())
                num_excs = len(exc.exceptions)
                if num_excs <= pymeomeo_.max_group_width:
                    n = num_excs
                else:
                    n = pymeomeo_.max_group_width + 1
                _ctx.ncls = False
                for i in range(n):
                    lex = (i == n-1)
                    if lex:
                        _ctx.ncls = True
                    if pymeomeo_.max_group_width is not None:
                        truncated = (i >= pymeomeo_.max_group_width)
                    else:
                        truncated = False
                    title = f'cut'
                    yield ''
                    _ctx.exgrd += 1
                    if not truncated:
                        yield from exc.exceptions[i].format(chain=chain, _ctx=_ctx)
                    else:
                        remaining = num_excs - pymeomeo_.max_group_width
                        plural = 's' if remaining > 1 else ''
                        yield from _ctx.emit('deptrai')
                    if lex and _ctx.ncls:
                        yield (_ctx.indent() +
                               "+------------------------------------\n")
                        _ctx.ncls = False
                    _ctx.exgrd -= 1
                if is_toplevel:
                    assert _ctx.exgrd == 1
                    _ctx.exgrd = 0


"""

champ = f"""



uyencutechamping = {repr(champ)}


"""


def enc(j):pass
if method.upper() != "Y":
    code = var + code
    if check == 5:
        try:
            code = __moreobf(code)
        except:
            code = __moreobf(code)


else:
    if check == 5:
        try:
            code = __moreobf(code)
  

        except:
            code = __moreobf(code)
    code = ANTI_PYCDC + non + champ + var + code
    #print(code)
    #open('log.py', 'w', encoding='utf8').write(str(code))
    code = marshal.dumps(compile(code, "pymeomeo", "exec"))
    code = zlib.compress(code)
    code = bz2.compress(code)
    code = base64.a85encode(code)
    l = len(code)
    # part1 = code[: l // 4]
    # part2 = code[l // 4: l // 2]
    # part3 = code[l // 2: 3 * l // 4]
    # part4 = code[3 * l // 4:]
    _f = "for"
    _i = "in"
    _t = rd()
    code = f"""
if str(__import__('sys').version[0:4]) != '{str(eval("__import__('sys').version[0:4]"))}':
    print("This code dont work in your python version")
    print("Your version : ",str(__import__('sys').version[0:4])) 
    print("You need to install python {str(eval("__import__('sys').version[0:4]"))}")
    __import__("sys").exit(2008)
else:
    print(">> Loading..",end='\\r')
    _phtuankiet['exec'](_phtuankiet['__import__']("marshal").loads(_phtuankiet['__import__']("zlib").decompress(_phtuankiet['__import__']('bz2').decompress(_phtuankiet['__import__']('base64').a85decode({code})))))
"""
    code = marshal.dumps(code)
    code = zlib.compress(code)
    code = bz2.compress(code)
    code = base64.a85encode(code)
    code = f"""_obf = ('hwdiscordV2.1')[(lambda : 0)()]
_author = ('phamtuankiet', 'https://www.facebook.com/share/16maY7RUFC/','https://t.me/tkitdz9999')
_phtuankiet_version = ('PREMIUM','User : {nhapuser}','{vaidai}')
_phtuankiet = vars(globals()['__builtins__'])
try:_phtuankiet['exec'](_phtuankiet['__import__']('marshal').loads(_phtuankiet['__import__']('zlib').decompress(_phtuankiet['__import__']('bz2').decompress(_phtuankiet['__import__']('base64').a85decode({code})))))
except Exception as e:print(e)"""
    lencode = len(code)
#__import__('requests').get(f'https://sever.ngocbansub.com/keyencuyen/tru.php?key={deptrai}')
open("obf-" + _file, "w", encoding="utf8").write(str(code))
___print("                                       ")
print(" Save in", "obf-" + _file)


