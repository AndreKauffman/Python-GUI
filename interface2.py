import PySimpleGUI as pg


def window_login():
    pg.theme('Reddit')
    layout = [
        [pg.Text('Nome: ', key='nome')],
        [pg.Input()],
        [pg.Button('Continuar ')]
    ]
    return pg.Window('Login', layout=layout, finalize=True)


def window_pedido():
    pg.theme('Reddit')
    layout = [
        [pg.Text('Fazer pedido: ')],
        [pg.Checkbox('Peperoni', key='pizza'), pg.Checkbox('Frango C/ Catupiri', key='pizza1')],
        [pg.Button('Voltar'), pg.Button('Fazer pedido')]
    ]
    return pg.Window('Montar Pedido', layout=layout, finalize=True)


def window_fim():
    pg.theme('Reddit')
    if values['pizza1'] == True:
        layout = [
            [pg.Text('Foi solicitado uma pizza de Frango C/ Catupiri para {}')]]
    if values['pizza'] == True:
        layout = [
            [pg.Text('Foi solicitado uma pizza de Peperoni ')]]
    if values['pizza'] and values['pizza1'] == True:
        layout = [
            [pg.Text('Foram solicitadas ambas as pizzas ')]]

    return pg.Window('Pedido', layout=layout, finalize=True)


janela1, janela2, janela3 = window_login(), None, None
while True:
    janela, event, values = pg.read_all_windows()
    if janela == janela1 and event == pg.WINDOW_CLOSED or janela == janela2 and event == pg.WINDOW_CLOSED or janela == janela3 and event == pg.WINDOW_CLOSED:
        break
    if janela == janela1 and event == 'Continuar ':
        janela2 = window_pedido()
        janela1.hide()
    if janela == janela2 and event == 'Voltar':
        janela1 = window_login()
        janela2.hide()
    if janela == janela2 and event == 'Fazer pedido':
        janela3 = window_fim()
        janela2.hide()
