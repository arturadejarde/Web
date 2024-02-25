import streamlit as st
from nltk.chat.util import Chat, reflections

def chat (text):
    a =st.text_input("🤖**BOT:**", value=text,disabled=True)
    return a


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
    

    chat("Por favor, faça uma pergunta sobre os números de emergência.")
    # st.write("Por favor, faça uma pergunta sobre os números de emergência.")

    # Campo de entrada para a pergunta e botão "Enviar"
    pergunta_usuario = st.text_input("Digite sua pergunta aqui:")
    bot = st.button("Enviar")

    if bot:
        resposta_chatbot = chatbot.respond(pergunta_usuario)
        if resposta_chatbot:
            chat(resposta_chatbot)
            # Campo de entrada e botão são exibidos após a resposta do bot
            # pergunta_usuario = st.text_input("Digite sua pergunta aqui:")
            # bot = st.button("Enviar")
        else:
            st.text_input("🤖**BOT:**",value="Desculpe, não consegui entender a pergunta. Por favor, tente novamente.",disabled=True)
            st.text_input("🤖**BOT:**" ,value="Qual é o número do **SAMU**?",disabled=True)
            st.text_input("🤖**BOT:**",value="Qual é o número da **Defesa Civil**?",disabled=True)
            st.text_input("🤖**BOT:**", value="Qual é o número do **Corpo de Bombeiros**?",disabled=True)
            st.text_input("🤖**BOT:**", value="Qual é o número da **Polícia Civil**?",disabled=True)
            st.text_input("🤖**BOT:**", value="Qual é o número da **Polícia Militar**?",disabled=True)
            st.text_input("🤖**BOT:**", value="Qual é o número da **Guarda Municipal**?",disabled=True)

if __name__ == "__main__":
    main()

 