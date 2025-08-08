# Teste simples de execução de comandos do shell

import subprocess
import os

print("Programa para instalação de pacotes que eu acho útil.\nVersão: 1.0\nPor: NIICKTCHUNS\n")
print("Iniciando instalação de pacotes...\n")

while True:
    resposta = input("Deseja instalar os drivers da AMD? (S/N): ").strip().lower()
    if resposta in ("s", "sim"):
        print("Instalando drivers da AMD... \n")
        os.system("sudo pacman -S --needed --noconfirm mesa lib32-mesa xf86-video-amdgpu vulkan-radeon lib32-vulkan-radeon")
        
        break
    elif resposta in ("n", "nao", "não"):
        print("Você respondeu NÃO!")

        while True:
            resposta2 = input("Deseja instalar os drivers da NVIDIA? (S/N): ").strip().lower()
            if resposta2 in ("s", "sim"):
                print("Você respondeu SIM!")
                break
            elif resposta2 in ("n", "nao", "não"):
                print("Você respondeu NÃO!")
                break
            else:
                print("Por favor, responda com 's' ou 'n'.")

        break
    else:
        print("Responda com 's' ou 'n'.")

