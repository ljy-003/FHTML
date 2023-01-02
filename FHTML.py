# 使用递归对HTML代码进行格式化


# 删除HTML注释（不太友好）
def Delete_comments(htmlc : str):
    if '<!--' in htmlc:
        del htmlc[htmlc.find('<!--'):htmlc.find('-->')+3]
    return htmlc

# 删除所有注释
def Delete_all_comments(html_code_lines : list):
    reput = []
    for i in html_code_lines:
        reput.append(Delete_comments(i))
    return reput


def recursion_html(code_h : str):
    
    ''' 处理split('<')后：
    注意，在split('<')后，'<'的左右两边都生成了内容
    所以需要code_h[1:]
    html>
    body>
    a harf='//xx.html'>
    p>
    /p>
    /a>
    /body>
    /html>
    '''
    
    code_h = code_h.split('<')
    code_h = code_h[1:]
    # code_h : 递归内容
    # return digui(code_h)
    # digui(code_h) # 最后递归结果：
    ans = digui(code_h)
    
    ens = []
    for i in ans.splitlines():
        a = i.split('\t') # 补充'<'号
        ens.append('\t'*(len(a)-1) + '<' + a[-1])
    return ens

def digui(code_v : list):
    # code_v : 下一层递归代码;
    # the_index : 递归当前位置;
    the_index_code = code_v[0]
    # the_index_code : 递归当前代码, 如"/body"
    
    if type(code_v) == str: # 如果(输入的)只有一项，则返回递归
            # 因为(输入的)只有一项字符串，
            # 当父递归列表只有2项时，type(code_v[1]) == str
            # 即输入字符串
        return code_v[2:] # [1:]是为了去掉最后的"\t"，因为后面不再递归
    
    code_sp = [] # Tab缩进处理
        # 注意，是“后面的”，所以应为code_v[1:]而不是code_v
        # 如果不指定替换次数，则replace()方法会替换全部指定的字符串
        # 现在已弃用replace()方法，因为此方法必须设置new参数，而我们不希望new内容出现
    if '/' in the_index_code:
        # 若"/", 则递归返回
        for i in code_v: # 每一项都减
            code_sp.append(i[1:]) # 删除"\t"(Tab)  注意："\t"为一位字符
        # 这里是因为特殊情况：
        # 第一次应该是“每一项都减”，后面的递归次数应为“后面的每一项都减”
        return the_index_code[1:]+'\n'+digui(code_v[1]) # 这一行代码有难度
    else:
        # 如果没有，则需要缩进，加入"\t"
        for i in code_v[1:]: # 后面的每一项都加
            code_sp.append('\t'+i)
    
    # 应为code_sp，而不是code_v
    return the_index_code+'\n'+digui(code_sp) # insert方法和append方法，append的效率更高

    ''' 处理append('\t'+i)后
    html>
        body>
        a harf='//xx.html'>
        p>
        /p>
        /a>
        /body>
        /html>
    '''



test_code = "<html><a><p></p></a></html>"
# test_code_lines = Delete_all_comments(test_code)
# print('recursion_html(test_code): ', recursion_html(test_code))



