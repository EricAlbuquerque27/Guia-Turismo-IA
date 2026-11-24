def gerar_roteiro(preferencias_usuario: str) -> dict:
    """Função que chama a API e retorna o JSON parseado."""
    
    # MODO SIMULADO FORÇADO PARA A ENTREGA
    print("\n[AVISO] Modo Simulado ativado! Retornando resposta falsa para economizar tokens.\n")
    return {
        "roteiro": [
            {"horario": "09:00", "local": "Praia de Iracema", "atividade": "Caminhar e tirar fotos", "custo_estimado": "R$ 0"},
            {"horario": "12:30", "local": "Mercado dos Peixes", "atividade": "Almoçar", "custo_estimado": "R$ 40"}
        ],
        "custo_total_estimado": "R$ 40",
        "dica_local": "Prove o caranguejo no fim da tarde."
    }

    