import ollama 
from datetime import datetime
import os 
import PyPDF2

 
def ler_pdf(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'rb') as arquivo_pdf:
            leitor = PyPDF2.PdfReader(arquivo_pdf)
            
            conteudo_pdf = ''
            
            for pagina in range(len(leitor.pages)):
                pagina_atual = leitor.pages[pagina]
                texto_pagina = pagina_atual.extract_text()  
                conteudo_pdf += f"\n--- Página {pagina+1} ---\n{texto_pagina}\n"
            
            return conteudo_pdf
    
    except Exception as e:
        return f"Ocorreu um erro ao ler o PDF: {e}"


os.system('cls')
prompt= ''
nome = input('Digite seu nome: ')
nome =nome.capitalize()

while prompt != 'PararPrograma':
    hj = datetime.today() 
    model = "phi3"
    prompt = input("Digite sua mensagem:")

    if prompt =='PararPrograma': break
    
    elif "pdf" in prompt or "PDF" in prompt: 
        conteudo = ler_pdf(r'C:\Users\lucas\Desktop\LnGpt\Atividade 1.pdf')
        prompt = prompt + "\n\n" + conteudo


    os.system('cls')
    print(nome, ':')
    print(prompt)


    stream = ollama.chat(
        model = model,
        messages = [{"role": "user", "content" :prompt}],
        stream = True
    )

    print(f'{hj.hour}: {hj.minute}: {hj.second}')
    
    print('')

    print('Chat:')

    for chunk in stream:
        
        print( chunk["message"]["content"],end="")

    print('')
    hj = datetime.today()    
    print(f'{hj.hour}: {hj.minute}: {hj.second}')
