def tag(tag, *args, **kwargs):
    if 'html_class' in kwargs:
        kwargs['class'] = kwargs.pop()


if __name__ == '__main__':
    print(
        tag('p',
            tag('span', 'Curso Python 3, por'),
            tag('strong', 'Juracy Filho', id='jf'),
            tag('span', 'e'),
            tag('strong', 'Leonardo Leitao', id='ll'),
            tag('span', '.'),
            html_class='alert'),
    )
