# 🤖 Ziko AI — Chatbot con LangChain + Groq + Streamlit

Un chatbot conversacional construido con LangChain, Groq y Streamlit. Soporta historial de conversación, streaming de respuestas y configuración dinámica del modelo desde la interfaz.

---

## 🚀 Demo

> Podés hacer el deploy en [Streamlit Community Cloud](https://share.streamlit.io) conectando este repositorio.

---

## 🛠️ Tecnologías

- [LangChain](https://python.langchain.com/) — framework para construir aplicaciones con LLMs
- [Groq](https://console.groq.com/) — inferencia ultrarrápida de modelos open source
- [Streamlit](https://streamlit.io/) — interfaz web interactiva
- [Python 3.11+](https://www.python.org/)

---

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto:

```
GROQ_API_KEY=tu_clave_aqui
```

Podés obtener tu API key gratis en [console.groq.com](https://console.groq.com).

---

## ▶️ Ejecutar la app

```bash
streamlit run main.py
```

La app se abre automáticamente en `http://localhost:8501`.

---

## ✨ Funcionalidades

- 💬 Chat conversacional con historial persistente por sesión
- ⚡ Streaming de respuestas en tiempo real
- 🎛️ Configuración dinámica de temperatura y modelo desde el sidebar
- 🗑️ Botón para limpiar la conversación
- 🛡️ Manejo de errores con mensajes descriptivos

---

## 🤖 Modelos disponibles

| Modelo | Descripción |
|--------|-------------|
| `llama-3.3-70b-versatile` | Más capaz, ideal para respuestas complejas |
| `llama-3.1-8b-instant` | Más rápido y liviano |
| `gemma2-9b-it` | Modelo de Google, buena alternativa |

---

## 🌐 Deploy en Streamlit Community Cloud

1. Subir el proyecto a GitHub
2. Ir a [share.streamlit.io](https://share.streamlit.io) y conectar el repo
3. Seleccionar `main.py` como archivo principal
4. En **Settings → Secrets**, agregar:

```toml
GROQ_API_KEY = "tu_clave_aqui"
```

5. Hacer clic en **Deploy** — en minutos tenés una URL pública

---

## 📁 Estructura del proyecto

```
📦 LangChain-LangGraph
├── main.py          # App principal
├── requirements.txt     # Dependencias
├── .env                 # Variables de entorno (no subir a GitHub)
├── .gitignore           # Ignorar .env y venv
└── README.md
```

---

## ⚠️ Importante

- **No subas el archivo `.env` a GitHub.** Asegurate de tener un `.gitignore` que lo excluya.
- Groq tiene límites de uso en el tier gratuito. Si ves errores `429`, esperá unos segundos y reintentá.

---

## 📝 Licencia

MIT
