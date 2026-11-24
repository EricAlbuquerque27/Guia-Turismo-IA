# app.py
from llm import gerar_roteiro
import json

def main():
    print("=" * 50)
    print("🌴 Bem-vindo ao Guia Turismo IA 🌴")
    print("=" * 50)
    
    # Pede as preferências ao usuário
    preferencias = input("\nDescreva seu dia perfeito (ex: tenho 1 dia livre, R$ 100, gosto de praia e quero comer bem): ")
    
    # Chama a IA
    roteiro_json = gerar_roteiro(preferencias)
    
    # Mostra o resultado formatado na tela
    print("\n--- SEU ROTEIRO PERSONALIZADO ---")
    if "erro" in roteiro_json:
        print("Desculpe, houve um erro.")
    else:
        print(json.dumps(roteiro_json, indent=4, ensure_ascii=False))
    
    print("\n--- FIM ---")

if __name__ == "__main__":
    main()