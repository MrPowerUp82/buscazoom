# buscazoom
Esse script vai fazer uma busca no https://www.zoom.com.br e vai salvar os nomes dos produtos e dos preços, numa tabela no formato xlsx. Com dados do seu email preenchidos em “email_user=’ ‘ “, ele vai enviar para um email desejado (“email_send=’ ’ ”).

# Campos a serem preenchidos:
email_user = ''
email_send = ''
email_password = ''
subject = ''
body = ""
filename = ''
search=""

# Bibliotecas usadas:
requests
lxml
openpyxl
smtplib
email

# Erro de Auth:
https://www.google.com/settings/security/lesssecureapps

Acesso a app menos seguro.

# 2.0:
Pega de todas as paginas do site.
