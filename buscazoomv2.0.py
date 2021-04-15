import requests
from lxml import html
from openpyxl import Workbook
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

email_user = ''
email_send = ''
email_password = ''
subject = ''

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject


body = ""
msg.attach(MIMEText(body, 'plain'))


filename = ''

wb=Workbook()
planilha=wb.worksheets[0]
planilha['A1']='Nome do Produto'
planilha['B1']='Preço'
headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36",
    "Accept" : "*/*"
}
url="https://www.zoom.com.br/search?page="


search="galaxy s9"


if ' ' in search:
    search=search.replace(' ','%20')
k=1
i=1
while True:
    link="{}{}&q={}".format(url,k,search)
    page=requests.get(link, headers=headers)
    if 'Não foram encontrados resultados com o termo buscado :('.encode() in page.content:
        wb.save(filename)
        if email_user == '' or email_password == '' or email_send == '':
            exit()
        else:
            attachment = open(filename, 'rb')

            part = MIMEBase('application', "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(filename))

            msg.attach(part)
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email_user, email_password)


            server.sendmail(email_user, email_send, text)
            server.quit()
            exit()


    tree=html.fromstring(page.content)
    title=tree.xpath('//a[@class="name"]/text()')
    main=tree.xpath('//span[@class="mainValue"]/text()')
    cent=tree.xpath('//span[@class="centsValue"]/text()')
    precos=[]
    r=int(len(main))
    for r in range(r):
        tudo="{}{}".format(main[r],cent[r])
        precos.append(tudo)

    n= int(len(title))
    j=0
    while j < n:
        i+=1
        indexA="A{}".format(i)
        indexB="B{}".format(i)
        planilha[indexA]=title[j]
        planilha[indexB]=precos[j]
        j+=1
    k+=1
