
caminho_da_imagem_para_testar = 'pasta/img/bola.jpg'


diretorio_de_trabalho_atual = os.getcwd()

caminho_absoluto_do_arquivo = os.path.abspath(os.path.join(diretorio_de_trabalho_atual, caminho_da_imagem_para_testar))

print(f"Executando o teste no diretório: '{diretorio_de_trabalho_atual}'")
print(f"Caminho que está sendo testado (absoluto): '{caminho_absoluto_do_arquivo}'")

# Verifica se o arquivo existe nesse caminho
if os.path.exists(caminho_absoluto_do_arquivo):
    print("\n[SUCESSO] O arquivo existe neste caminho!")
    print("Você pode prosseguir com o 'cv2.imread()' usando o caminho original que você testou.")
else:
    print("\n[FALHA] O arquivo NÃO foi encontrado neste caminho!")
    print("Possíveis razões:")
    print("  1. O caminho relativo está incorreto para onde seu script está.")
    print("  2. O nome do arquivo (incluindo maiúsculas/minúsculas e extensão) está errado.")
    print("  3. O arquivo não está no local esperado.")