# Считать с клавиатуры отдельными операторами:
# - заголовок страницы (например, Hello);
# - цвет заголовка первого уровня (например, blue);
# - цвет текста абзаца (например, red);
# - текст заголовка первого уровня (например, Title 1);
# - текст статьи (например, Article text).
#
# Использовать только латинские символы.
# Используя декораторы, сформировать текст html-страницы для публикации статьи.
#
# Пример входных данных:
# Hello
# blue
# red
# Title 1
# Article text
#
# Пример выходных данных:
# <html>
# <head>
# <title>Hello</title>
# <style>h1{color:blue}p{color:red}</style>
# </head>
# <body>
# <h1>Title 1</h1>
# <p>Article text</p>
# </body>
# </html>

def mytag(func):
    def decor(*args, **kwargs):
        return f'<{func.__name__}>\n{func(*args, **kwargs)}\n</{func.__name__}>'

    return decor


def mytag2(func):
    def decor(*args, **kwargs):
        return f'<{func.__name__}>{func(*args, **kwargs)}</{func.__name__}>'

    return decor


@mytag2
def title(content):
    return f'{content}'


@mytag2
def style(col1, col2):
    return f'h1{{color:{col1}}}p{{color:{col2}}}'


@mytag2
def p(content):
    return content


@mytag2
def h1(content):
    return content


@mytag
def body(*args):
    return '\n'.join(args)


@mytag
def head(*args):
    return '\n'.join(args)


@mytag
def html(head, body):
    return f'{head}\n{body}'


us_tytle = input()
us_col1 = input()
us_col2 = input()
us_h1 = input()
us_p = input()
print(html(head(title(us_tytle), style(us_col1, us_col2)),
           body(h1(us_h1), p(us_p))))
