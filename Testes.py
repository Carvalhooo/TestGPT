import PyPDF2

def ler_pdf(caminho_arquivo):
    try:
        # Abrir o arquivo PDF
        with open(caminho_arquivo, 'rb') as arquivo_pdf:
            # Criar o leitor de PDF
            leitor = PyPDF2.PdfReader(arquivo_pdf)
            
            # Variável para armazenar o conteúdo do PDF
            conteudo_pdf = ''
            
            # Loop para ler todas as páginas do PDF
            for pagina in range(len(leitor.pages)):
                pagina_atual = leitor.pages[pagina]
                texto_pagina = pagina_atual.extract_text()  # Extrair o texto da página
                conteudo_pdf += f"\n--- Página {pagina+1} ---\n{texto_pagina}\n"
            
            return conteudo_pdf
    
    except Exception as e:
        return f"Ocorreu um erro ao ler o PDF: {e}"

# Exemplo de uso:
caminho_arquivo = r'C:\Users\lucas\Desktop\LnGpt\Atividade 1.pdf'  # Insira o caminho para o arquivo PDF
conteudo = ler_pdf(caminho_arquivo)
print(conteudo)