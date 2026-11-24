# interface.py
import streamlit as st
import json
from llm import gerar_roteiro

# Configuração da página
st.set_page_config(page_title="Guia Turismo IA", page_icon="🌴", layout="centered")

# Cabeçalho
st.title("🌴 Guia Turismo IA (Ceará)")
st.markdown("""
**Bem-vindo ao seu planejador de viagem inteligente!** 
Descreva o que você gosta, seu orçamento e quanto tempo tem. A nossa IA cria um roteiro personalizado para você conhecer o melhor do Ceará.
""")

st.divider()

# Campo de entrada do usuário
preferencias = st.text_area(
    "Descreva o seu dia perfeito:", 
    placeholder="Ex: Tenho 1 dia livre em Fortaleza, R$ 150, gosto de cultura e quero comer um bom peixe."
)

# Botão para gerar o roteiro
if st.button("✨ Gerar Roteiro", type="primary"):
    if preferencias.strip() == "":
        st.warning("Por favor, digite as suas preferências antes de gerar o roteiro.")
    else:
        with st.spinner("A IA está pensando no seu roteiro..."):
            # Chama a função do seu motor
            resultado = gerar_roteiro(preferencias)
            
        if "erro" in resultado:
            st.error("Ocorreu um erro ao gerar o roteiro. Tente novamente.")
        else:
            st.success("Roteiro gerado com sucesso!")
            
            # Exibe os dados formatados (Interface Amigável)
            st.subheader("📅 Seu Roteiro Personalizado")
            
            for item in resultado.get("roteiro", []):
                with st.container(border=True):
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        st.markdown(f"**⏰ {item.get('horario')}**")
                    with col2:
                        st.markdown(f"**📍 {item.get('local')}**")
                        st.write(f"*{item.get('atividade')}*")
                        st.caption(f"Custo estimado: {item.get('custo_estimado')}")
            
            # Exibe o resumo financeiro e a dica
            st.info(f"💰 **Custo Total Estimado:** {resultado.get('custo_total_estimado')}")
            st.warning(f"💡 **Dica Local:** {resultado.get('dica_local')}")
            
            # Mostra o JSON puro (Requisito da Rubrica)
            with st.expander("Ver saída em JSON (Requisito Técnico)"):
                st.json(resultado)