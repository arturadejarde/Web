import streamlit as st
from nltk.chat.util import Chat, reflections
import time

def quebrar_linha(texto, tamanho=29):
    """
    Função para quebrar uma linha de texto a cada 'tamanho' caracteres.
    
    Parâmetros:
    texto (str): O texto a ser quebrado em linhas.
    tamanho (int): O número máximo de caracteres por linha. O padrão é 29.
    
    Retorna:
    str: O texto com quebras de linha a cada 'tamanho' caracteres.
    """
    palavras = texto.split()
    linhas = []
    linha_atual = palavras[0]

    for palavra in palavras[1:]:
        if len(linha_atual) + len(palavra) < tamanho:
            linha_atual += ' ' + palavra
        else:
            linhas.append(linha_atual)
            linha_atual = palavra

    linhas.append(linha_atual)
    return '\n'.join(linhas)


def tempo ():
    with st.empty():
        for seconds in range(3):
            st.write(f"Falta ⏳ {seconds} segundos")
            time.sleep(1)
        st.write("✔️ Pronto !")



def main():

    # Definindo o CSS personalizado
    # Definindo o CSS personalizado
    disabled_text_css = """
    <style>
    .st-c0 {
        -webkit-text-fill-color: rgb(49, 51, 63);
    }
    .st-c4 {
        -webkit-text-fill-color: rgb(0, 0, 0);
    }
    .st-emotion-cache-up131x {
        font-size: 14px;
        color: rgb(49, 51, 63);
        visibility: visible;
    }
    .st-bv {
        -webkit-text-fill-color: rgb(0, 0, 0);
        }
    </style>
    """



    st.write(disabled_text_css, unsafe_allow_html=True)
    
    st.title("Chatbot de Emergência")

    # Inicializar o chatbot
    Contato = [
        ['SAMU', ['192']],
        ['Defesa civil', ['199']],
        ['Corpo de bombeiros', ['193']],
        ['Polícia civil', ['197']],
        ['Polícia Militar', ['190']],
        ['Guarda municipal', ['153']],
    ]
    chatbot = Chat(Contato, reflections)

    st.write("Olá! Sou o Chatbot de Emergência. Como posso ajudar você hoje?")

    def chat(text):
        container = st.container(border=True)
        tempo ()
        container.text_input("🤖**BOT:**",value=quebrar_linha(text,tamanho=10),disabled=True,max_chars=500)

    def chat_r(text):
        container = st.container(border=True)
        
        container.text_input("👤**EU:**",value=quebrar_linha(text,tamanho=10)+" ✔️",disabled=True,max_chars=500)


       
        # chat("Por favor, faça uma pergunta sobre os números de emergência.")
    with st.sidebar:
        pergunta_usuario = st.text_input("Digite sua pergunta aqui:")
        bot = st.button("Enviar")
        chat("Por favor, faça uma pergunta sobre os números de emergência.")
        if pergunta_usuario!="":
            chat_r(pergunta_usuario)
    
        if bot:
            resposta_chatbot = chatbot.respond(pergunta_usuario)
            if resposta_chatbot:
                tempo ()
                chat(resposta_chatbot)
                # chat(resposta_chatbot)
                # Campo de entrada e botão são exibidos após a resposta do bot
                # pergunta_usuario = st.text_input("Digite sua pergunta aqui:")
                # bot = st.button("Enviar")
            else:
                chat("Desculpe, não consegui entender a pergunta. Por favor, tente novamente.")
                chat("Qual é o número do **SAMU**?")
                chat("Qual é o número da **Defesa Civil**?")
                chat("Qual é o número do **Corpo de Bombeiros**?")
                chat("Qual é o número da **Polícia Civil**?")
                chat("Qual é o número da **Polícia Militar**?")
                chat("Qual é o número da **Guarda Municipal**?")



    

if __name__ == "__main__":
    main()

 



