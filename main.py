from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import PromptTemplate

import streamlit as st
NOMBRE = "Ziko"
# ---------------------------- Configuracion de la pagina ------------------------

st.set_page_config(
    page_title=f"{NOMBRE} AI",
    page_icon="🤖",
)
st.markdown(f"<h1 style='text-align:center'>🤖 Chatea con {NOMBRE}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#555; margin-bottom:30px; margin-top:-5px;'>¡Escribe tu mensaje abajo para comenzar la conversación!</p>", unsafe_allow_html=True)
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# --------------------------- Funciones -----------------------------------------

def mensajeMarkdown(rol, mensaje):
    esAsistente = rol == "assistant"
    color = "transparent" if esAsistente else "#2b2b2b"
    direccion = "flex-start" if esAsistente else "flex-end"
    burbuja = f'<div style="background:{color}; padding:10px 14px; border-radius:12px; max-width:80%;">{mensaje}</div>'

    st.markdown(f"""
        <div style="display:flex; justify-content:{direccion}; align-items:center; gap:10px; margin:8px 0;">
            {burbuja}
        </div>
    """, unsafe_allow_html=True)

def limpiarChat():
    st.session_state.messages = []

@st.cache_resource
def cargar_modelo(nombre, temp):
    return ChatGroq(model=nombre, temperature=temp)

# ---------------------------- Sidebar ------------------------------------------

with st.sidebar:
    st.button(label="Nueva conversación", icon="🗑️", on_click=limpiarChat)
    st.header("Configuración")
    temperature = st.slider("Temperatura", 0.0, 1.0, 0.7, 0.1)
    model_name = st.selectbox("Modelo", ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "gemma2-9b-it"])

model = cargar_modelo(model_name, temperature)

# ---------------------------- Template -----------------------------------------

template = PromptTemplate.from_template(
    """
    Eres un asistente llamado {nombre} que habla en español.
    Responde de forma concisa y directa. Si el usuario corrige algo, adáptate inmediatamente.

    Historial de la conversación:
    {historial}

    Pregunta del usuario: {mensaje}
    """
)

chain = template | model

# ---------------------------- Chat ---------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    if isinstance(msg, SystemMessage):
        continue
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    mensajeMarkdown(role, msg.content)

pregunta = st.chat_input("Escribe tu pregunta aquí...")

try:
    if pregunta:
      mensajeMarkdown("user", pregunta)
      st.session_state.messages.append(HumanMessage(content=pregunta))

      # Crear historial formateado para el prompt
      historial = "\n".join([ 
          f"{'Usuario' if isinstance(m, HumanMessage) else 'Asistente'}: {m.content}"
          for m in st.session_state.messages[:-1]
      ])

      try: 
          # Generar respuesta
          with st.chat_message("assistant"):
              response_placeholder = st.empty() # Placeholder para mostrar la respuesta a medida que se genera
              full_response = "" # Variable para acumular la respuesta completa

              # Streaming de la respuesta
              for chunk in chain.stream({"nombre": NOMBRE, "historial": historial, "mensaje": pregunta}): 
                  full_response += chunk.content
                  response_placeholder.markdown(full_response + "▌")

              response_placeholder.markdown(full_response)

          st.session_state.messages.append(AIMessage(content=full_response))

      except Exception as e:
          mensaje = f"⚠️ {type(e).__name__}: {str(e)}"
          mensajeMarkdown("assistant", mensaje)
          st.session_state.messages.append(AIMessage(content=mensaje))

except Exception as e:
    mensaje= f"Error: {str(e)}"
    mensajeMarkdown("assistant", mensaje)
    st.session_state.messages.append(AIMessage(content=mensaje))
