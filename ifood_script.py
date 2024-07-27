import sys
import time

from selenium import webdriver
from selenium.webdriver.support import wait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
from pynput.keyboard import Key, Controller
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

df = pd.read_csv('pratos.csv', on_bad_lines='skip', sep=";", header=0)
df_complemento_1 = pd.read_csv('complemento_grupo_1.csv', on_bad_lines='skip', sep=";", header=0)
df_complemento_2 = pd.read_csv('complemento_grupo_2.csv', on_bad_lines='skip', sep=";", header=0)
df_complemento_3 = pd.read_csv('complemento_grupo_3.csv', on_bad_lines='skip', sep=";", header=0)
df_complemento_4 = pd.read_csv('complemento_grupo_4.csv', on_bad_lines='skip', sep=";", header=0)

servico = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\tamor\AppData\Local\Google\Chrome\User Data")
options.add_argument(r'--profile-directory=Profile 6')
navegador = uc.Chrome(service=servico, options=options)
navegador.implicitly_wait(35)
wait = WebDriverWait(navegador, 10)

navegador.get('https://portal.ifood.com.br/home')

# clicando em menu
navegador.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[3]/div[1]/div/div/div/div/div/div[2]/div[4]/div[2]/a/div/div[1]/div/div[1]/span').click()

# clicando em adicionar categoria
navegador.find_element(By.XPATH, '//*[@id="micro-frontend-catalog"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/div/div[4]/div/div[1]/div/button').click()

# selecionando a opção 'itens principais'
navegador.find_element(By.XPATH, '//*[@id="micro-frontend-catalog"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/div/div/a[1]').click()

# definindo o titulo da categoria
navegador.find_element(By.XPATH, '//*[@id="name"]').send_keys('Categoria - teste de automação')

# clicando em criar categoria
navegador.find_element(By.XPATH, '//*[@id="micro-frontend-catalog"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/div/form/div[2]/button[2]').click()


time.sleep(2)
navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
# PAUSANDO A CATEGORIA
input_button = navegador.find_element(By.XPATH, "(//input[@type='checkbox' and contains(@class, 'Input-sc-1of0msz-2')])[last()]")
input_button.click()

#CLICANDO

# É AQUI ONDE VAI INCIAR O LOOP
contador_imagem = 1
total_variacao = 0

parou = False
for index, row in df.iterrows():
    if not parou:
        # INICIANDO CADASTRO DE PRODUTOS
        time.sleep(2)
        wait.until(ec.element_to_be_clickable((By.XPATH, "(//button[contains(., 'Adicionar item')])[last()]"))).click()


        # CLICANDO EM PRATO PREPARADO
        navegador.find_element(By.XPATH, "//a[.//p[contains(text(), 'Preparado')]]").click()

        # cadastrando a foto do prato
        navegador.find_element(By.XPATH,"//button[contains(@class, 'DropzoneButton_dropzone-button__hcIht') and contains(@class, 'sc-iUCjyN') and .//div[contains(text(), 'Escolher imagem')]]").click()

        path = f"D:\\Users\\tamor\\PycharmProjects\\AutomacaoIfood\\fotos ordenadas\\pratos\\{index+1}.jpeg"
        input_file = navegador.find_element(By.XPATH, "//input[@type='file']")
        input_file.send_keys(path)

        # navegador.find_element('xpath', '/html/body/div[18]/div/div[1]/div[4]/div/div[2]/button[2]').click()
        navegador.find_element(By.XPATH,"//button[contains(@class, 'BaseButton-sc-odyat6-0') and contains(@class, 'kVbamu') and .//div[contains(text(), 'Salvar')]]").click()

        # nome do prato
        navegador.find_element(By.XPATH, '//*[@id="name"]').click()
        navegador.find_element(By.XPATH, '//*[@id="name"]').send_keys(df['titulo'][index])

        # descricao do prato
        navegador.find_element(By.XPATH, '//*[@id="description"]').click()
        navegador.find_element(By.XPATH, '//*[@id="description"]').send_keys(df['descricao'][index])

        # selecionando prato apenas para uma pessoa
        navegador.find_element(By.XPATH, '//*[@id="micro-frontend-catalog"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/form/div[3]/div[2]/div/div/div[2]/label/div').click()
        navegador.find_element(By.XPATH, '//*[@id="micro-frontend-catalog"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/form/div[3]/div[2]/div/div/div[2]/label/div').click()
        navegador.find_element(By.XPATH, '//*[@id="micro-frontend-catalog"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/form/div[3]/div[2]/div/div/div[2]/label/div').click()

        # selecionando o peso
        navegador.find_element(By.XPATH, '//*[@id="quantity"]').send_keys(400)

        # clicando em continuar
        navegador.find_element(By.XPATH, '//*[@id="micro-frontend-catalog"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/form/div[4]/button[2]').click()

        # digitando o preço sem desconto do prato
        navegador.find_element(By.XPATH, '//*[@id="price.value"]').send_keys(str(df['preco'][index]))

        # clicando no botão de adicionar desconto
        navegador.find_element(By.XPATH, '//*[@id="micro-frontend-catalog"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/button').click()
        navegador.find_element(By.XPATH, '//*[@id="micro-frontend-catalog"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/form/div[3]/div[1]/div/div[2]/button').click()

        # adicionando o valor do prato com o desconto
        navegador.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[3]/div[2]/main/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/form/div[3]/div[1]/div/div[3]/div/div[1]/div/div[1]/input').send_keys(str(df['preco_com_desconto'][index]))

        #caso seja o primeiro item, vou cadastrar os complementos
        if index == 0 or (total_variacao == 0 and df['complemento_variacao'][index] == '14,99'):

            if df['complemento_variacao'][index] == '14,99':
                total_variacao += 1
            # clicando na seção de complementos
            wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(., 'Complementos')]"))).click()


            # clicando na seção de sim, este item tem complementos
            label = navegador.find_element(By.XPATH, "//label[contains(text(), 'Sim, este item tem complementos')]")
            label.find_element(By.XPATH, "preceding-sibling::span").click()
            label.find_element(By.XPATH, "preceding-sibling::span").click()

            # clicando em criar grupo de complemento
            navegador.find_element(By.XPATH, "//button[contains(., 'Criar grupo de complementos')]").click()

            # adicionando o nome do primeiro grupo de complementos
            wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="name"]'))).click()
            wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="name"]'))).send_keys('Leve outra marmitex com desconto')

            # setando o máximos de itens nesse grupo de complemento
            wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="option-group-max"]'))).send_keys('0')
            #clicando em continuar
            wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="micro-frontend-catalog"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/form/div[3]/button[2]'))).click()

            for index_2, row_2 in df_complemento_1.iterrows():
                #seleciona o tipo do item (preparado)
                wait.until(ec.element_to_be_clickable((By.XPATH, "(//button[@type='button' and @data-testid='new-option-type-button']//p[text()='Preparado']/ancestor::button)[last()]"))).click()

                #adicionando foto do item do complemento
                wait.until(ec.element_to_be_clickable(navegador.find_elements(By.CLASS_NAME, 'ImageField_image-field__ZXHsy')[-1])).click()

                path = f"D:\\Users\\tamor\\PycharmProjects\\AutomacaoIfood\\fotos ordenadas\\complemento_grupo_1\\{index_2 + 1}.jpeg"
                input_file = navegador.find_element(By.XPATH, "//input[@type='file']")
                input_file.send_keys(path)

                navegador.find_element(By.XPATH,"//button[contains(@class, 'BaseButton-sc-odyat6-0') and contains(@class, 'kVbamu') and .//div[contains(text(), 'Salvar')]]").click()

                #adicionando titulo
                wait.until(ec.element_to_be_clickable(
                    navegador.find_elements(By.XPATH,
                                            "//input[@label='Nome do complemento']")[-1])).send_keys(df_complemento_1['titulo'][index_2])
                #adicionando descricao
                wait.until(ec.element_to_be_clickable(
                    navegador.find_elements(By.XPATH,
                                            "//textarea[@placeholder='Exemplo: Porção de 150 g.']")[-1])).send_keys(df_complemento_1['descricao'][index_2])

                #adicionando o preco
                if (df['complemento_variacao'][index] == '18,99'):
                    wait.until(ec.element_to_be_clickable(
                        navegador.find_elements(By.XPATH,
                                                "//input[@placeholder='R$' and @label='Preço único']")[-1])).send_keys(
                        df_complemento_1['preco'][index_2])
                else:
                    wait.until(ec.element_to_be_clickable(
                        navegador.find_elements(By.XPATH,
                                                "//input[@placeholder='R$' and @label='Preço único']")[-1])).send_keys(
                        df_complemento_1['preco_2'][index_2])
            #clicando em criar grupo
            wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(., 'Criar grupo')]"))).click()





            # ADICIONANDO O SEGUNDO GRUPO DE COMPLEMENTO
            # criando segundo grupo de complemento
            navegador.find_element(By.XPATH, "//button[contains(., 'Criar grupo de complementos')]").click()

            # digitando o nome do grupo
            wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="name"]'))).send_keys(
                'Acrescente uma bisteca por apenas R$ 9,90')

            # setando o máximos de itens nesse grupo de complemento
            wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="option-group-max"]'))).send_keys('0')
            # clicando em continuar
            wait.until(ec.element_to_be_clickable((By.XPATH,
                                                   '//*[@id="micro-frontend-catalog"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/form/div[3]/button[2]'))).click()
            for index_3, row_3 in df_complemento_2.iterrows():
                #seleciona o tipo do item (preparado)
                wait.until(ec.element_to_be_clickable((By.XPATH, "(//button[@type='button' and @data-testid='new-option-type-button']//p[text()='Preparado']/ancestor::button)[last()]"))).click()

                #adicionando titulo
                wait.until(ec.element_to_be_clickable(
                    navegador.find_elements(By.XPATH,
                                            "//input[@label='Nome do complemento']")[-1])).send_keys(df_complemento_2['titulo'][index_3])

                #adicionando o preco
                preco = float(df_complemento_2['preco'][index_3].replace(',', '.'))

                preco_formatado = f"{preco:.2f}"

                wait.until(ec.element_to_be_clickable(
                    navegador.find_elements(By.XPATH,
                                            "//input[@placeholder='R$' and @label='Preço único']")[-1])).send_keys(preco_formatado)
            # clicando em criar grupo
            wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(., 'Criar grupo')]"))).click()





            # ADICIONANDO O TERCEIRO GRUPO DE COMPLEMENTO
            # criando segundo grupo de complemento
            navegador.find_element(By.XPATH, "//button[contains(., 'Criar grupo de complementos')]").click()

            # digitando o nome do grupo
            wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="name"]'))).send_keys('Aproveite e leve um refri com descontão')

            # setando o máximos de itens nesse grupo de complemento
            wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="option-group-max"]'))).send_keys('0')
            # clicando em continuar
            wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="micro-frontend-catalog"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/form/div[3]/button[2]'))).click()

            for index_4, row_4 in df_complemento_3.iterrows():
                #seleciona o tipo do item (preparado)
                wait.until(ec.element_to_be_clickable((By.XPATH, "(//button[@type='button' and @data-testid='new-option-type-button']//p[text()='Preparado']/ancestor::button)[last()]"))).click()

                # adicionando foto do item do complemento
                wait.until(ec.element_to_be_clickable(
                    navegador.find_elements(By.CLASS_NAME, 'ImageField_image-field__ZXHsy')[-1])).click()

                path = f"D:\\Users\\tamor\\PycharmProjects\\AutomacaoIfood\\fotos ordenadas\\complemento_grupo_3\\{index_4 + 1}.jpeg"
                input_file = navegador.find_element(By.XPATH, "//input[@type='file']")
                input_file.send_keys(path)

                navegador.find_element(By.XPATH, "//button[contains(@class, 'BaseButton-sc-odyat6-0') and contains(@class, 'kVbamu') and .//div[contains(text(), 'Salvar')]]").click()

                # adicionando titulo
                wait.until(ec.element_to_be_clickable(
                    navegador.find_elements(By.XPATH,
                                            "//input[@label='Nome do complemento']")[-1])).send_keys(
                    df_complemento_3['titulo'][index_4])


                # adicionando o preco
                preco = float(df_complemento_3['preco'][index_4].replace(',', '.'))
                preco_formatado = f"{preco:.2f}"

                wait.until(ec.element_to_be_clickable(
                    navegador.find_elements(By.XPATH,
                                            "//input[@placeholder='R$' and @label='Preço único']")[-1])).send_keys(preco_formatado)

            # clicando em criar grupo
            wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(., 'Criar grupo')]"))).click()







            # ADICIONANDO O QUARTO GRUPO DE COMPLEMENTO
            # criando segundo grupo de complemento
            navegador.find_element(By.XPATH, "//button[contains(., 'Criar grupo de complementos')]").click()

            # digitando o nome do grupo
            wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="name"]'))).send_keys('Sobremesa com descontão')

            # setando o máximos de itens nesse grupo de complemento
            wait.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="option-group-max"]'))).send_keys('0')
            # clicando em continuar
            wait.until(ec.element_to_be_clickable((By.XPATH,'//*[@id="micro-frontend-catalog"]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div/div/form/div[3]/button[2]'))).click()

            for index_5, rows_5 in df_complemento_4.iterrows():
                # seleciona o tipo do item (preparado)
                wait.until(ec.element_to_be_clickable((By.XPATH,
                                                       "(//button[@type='button' and @data-testid='new-option-type-button']//p[text()='Preparado']/ancestor::button)[last()]"))).click()

                # adicionando foto do item do complemento
                wait.until(ec.element_to_be_clickable(
                    navegador.find_elements(By.CLASS_NAME, 'ImageField_image-field__ZXHsy')[-1])).click()


                path = f"D:\\Users\\tamor\\PycharmProjects\\AutomacaoIfood\\fotos ordenadas\\complemento_grupo_4\\1.jpeg"
                input_file = navegador.find_element(By.XPATH, "//input[@type='file']")
                input_file.send_keys(path)

                navegador.find_element(By.XPATH, "//button[contains(@class, 'BaseButton-sc-odyat6-0') and contains(@class, 'kVbamu') and .//div[contains(text(), 'Salvar')]]").click()

                # adicionando titulo
                wait.until(ec.element_to_be_clickable(
                    navegador.find_elements(By.XPATH,
                                            "//input[@label='Nome do complemento']")[-1])).send_keys(
                    df_complemento_4['titulo'][index_5])

                # adicionando o preco
                preco = float(df_complemento_4['preco'][index_5].replace(',', '.'))
                preco_formatado = f"{preco:.2f}"

                wait.until(ec.element_to_be_clickable(
                    navegador.find_elements(By.XPATH,
                                            "//input[@placeholder='R$' and @label='Preço único']")[-1])).send_keys(preco_formatado)

            # clicando em criar grupo
            wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(., 'Criar grupo')]"))).click()
        else:

            # clicando na seção de complementos
            wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(., 'Complementos')]"))).click()

            # clicando na seção de sim, este item tem complementos
            label = navegador.find_element(By.XPATH, "//label[contains(text(), 'Sim, este item tem complementos')]")
            label.find_element(By.XPATH, "preceding-sibling::span").click()
            label.find_element(By.XPATH, "preceding-sibling::span").click()

            #clicando copiar de outro item
            button = wait.until(ec.presence_of_element_located(
                (By.XPATH, "//button[.//div[contains(text(), 'Copiar de outro item')]]")))
            navegador.execute_script("arguments[0].click();", button)


            #clicando na droplist da categoria
            time.sleep(2)
            navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            elements = navegador.find_elements(By.XPATH, "//span[@class='Glyph-sc-4ga79h-0 huPCec ifdl-icon-line ifdl-icon-chevron-down']")
            elements[0].click()

            #selecionando a categoria
            wait.until(ec.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Categoria - teste de automação')]"))).click()

            #clicando na droplist do complemento
            time.sleep(2)
            elements[1].click()

            if df['complemento_variacao'][index] == '14,99':
                wait.until(ec.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Feijoada Simples + Lata Coca Normal + R$ 14,99 Leve Outra Marmitex')]"))).click()
            else:
                wait.until(ec.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'Feijoada Simples + R$ 18,99 Leve Outra Marmitex')]"))).click()

            #clicando em confirmar
            wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(., 'Confirmar')]"))).click()

    # clicando no botão de disponibilidade
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(., 'Continuar')]"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(., 'Continuar')]"))).click()

    # clicando no botão de criar item
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(., 'Criar item')]"))).click()

    time.sleep(2)
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")




input('Digite qualquer coisa para encerrar o processo')
navegador.quit()
