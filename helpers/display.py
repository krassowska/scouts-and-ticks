from IPython.display import display, HTML


def pokaz_zestawienie(**kwargs):
    output = '<table>'
    output += '<th><tr>'
    for name in kwargs:
        output += f'<td>{name}</td>'
    output += '</tr></th>'
    output += '<tr>'
    for values in kwargs.values():
        values_list = ''.join(f'<li>{v}' for v in values)
        output += f'<td><ol>{values_list}</ol></td>'
    output += '</tr>'
    output += '</table>'
    display(HTML(output))
