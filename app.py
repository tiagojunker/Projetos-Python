import smtplib
import datetime
from email.message import EmailMessage

# Color change date
white =             ['27/12']
orange_and_purple = ['1/2']
purple =            ['20/3']
yellow_and_blue =   ['21/3']
blue =              ['22/3', '1/8', '1/11']
yellow =            ['1/5', '10/5', '1/9', '6/9', '22/9', '28/9']
pink =              ['9/5', '1/10']
green =             ['1/6', '5/9', '21/9', '27/9']
red =               ['11/6', '29/6', '25/11']
red_and_orange =    ['28/6']
cian =              ['1/7']
orange =            ['29/8', '2/12']
green_and_yellow =  ['19/11']
red_and_green =     ['18/12']

# All holidays that disable asco key
year_holidays = ['1/1', '21/4', '1/5', '7/9', '12/10', '2/11', '15/11', '25/12']


get_date = datetime.datetime.now()
current_day = (f"{str(get_date.day)}/{str(get_date.month)}")
weekday = get_date.weekday()


def send_email(title, content):
    """ Function that send email """

    email_address = ''              # Email de saida
    email_password = ''             # Senha
    message = EmailMessage()        # Inicia uma nova mensagem
    message['Subject'] = title      # Titulo do Email
    message['From'] = ''            # Email de saida
    message['To'] = ''              # Email destino
    message.set_content(content)    # Conteúdo do Email

    # Envio do Email
    with smtplib.SMTP('smtp.tvriosul.com.br', 587) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(message)


def verify_date():
    """ function that verify change colors """

    if current_day in white:
        return 'Hoje a cor da torre será Branca'
    if current_day in orange_and_purple:
        return 'NECESSÁRIO TROCAR A COR DA TORRE HOJE -> Laranja e Roxo.'
    if current_day in purple:
        return 'NECESSÁRIO TROCAR A COR DA TORRE HOJE -> Roxo.'
    if current_day in yellow_and_blue:
        return 'NECESSÁRIO TROCAR A COR DA TORRE HOJE -> Amarelo e Azul.'
    if current_day in blue:
        return 'NECESSÁRIO TROCAR A COR DA TORRE HOJE -> Azul.'
    if current_day in yellow:
        return 'NECESSÁRIO TROCAR A COR DA TORRE HOJE -> Amarelo.'
    if current_day in pink:
        return 'NECESSÁRIO TROCAR A COR DA TORRE HOJE -> Rosa.'
    if current_day in green:
        return 'NECESSÁRIO TROCAR A COR DA TORRE HOJE -> Verde.'
    if current_day in red:
        return 'NECESSÁRIO TROCAR A COR DA TORRE HOJE -> Vermelho.'
    if current_day in red_and_orange:
        return 'NECESSÁRIO TROCAR A COR DA TORRE HOJE -> Vermelho e Laranja.'
    if current_day in cian:
        return 'NECESSÁRIO TROCAR A COR DA TORRE HOJE -> Ciano.'
    if current_day in orange:
        return 'NECESSÁRIO TROCAR A COR DA TORRE HOJE -> Laranja.'
    if current_day in green_and_yellow:
        return 'NECESSÁRIO TROCAR A COR DA TORRE HOJE -> Verde e Amarelo.'
    if current_day in red_and_green:
        return 'NECESSÁRIO TROCAR A COR DA TORRE HOJE -> Vermelho e Verde.'
    if current_day:
        return 'false'


VERIFICATION = verify_date()

# sending the emails of tower color, fuel supply diesel and disable asco in holidays
if VERIFICATION != 'false':
    send_email('Troca de cor Torre', VERIFICATION)

if weekday == 3:
    send_email('ABASTECIMENTO GERADOR EMISSORA', 'VERIFICAR PEDIDO DE DIESEL HOJE.')

if current_day in year_holidays:
    send_email('CHAVE ASCO FERIADO', 'DESATIVAR CHAVE ASCO HOJE')


#   Gerar Executavel --> pyinstaller app.py