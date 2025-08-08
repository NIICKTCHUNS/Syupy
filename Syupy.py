# Teste simples de execução de comandos do shell

import subprocess
import os

print("Programa para instalação de pacotes que eu acho útil.\nVersão: 1.0\nPor: NIICKTCHUNS\n")
print("Iniciando instalação de pacotes...\n")

while True:
    resposta = input("Deseja instalar os drivers de qual fabricante? (S/n): ").strip().lower()
    if resposta in ("s", "sim"):
        print("Instalando drivers da AMD...\n")
        os.system("sudo pacman -S --needed --noconfirm mesa lib32-mesa xf86-video-amdgpu vulkan-radeon lib32-vulkan-radeon")
        
        break
    elif resposta in ("n", "nao", "não"):
        print("Pulando...\n")

        while True:
            resposta2 = input("Deseja instalar os drivers da Intel? (S/N): ").strip().lower()
            if resposta2 in ("s", "sim"):
                print("Instalando drivers da Intel...\n")
                os.system("sudo pacman -S --needed intel-media-driver libvpl vpl-gpu-rt vulkan-intel lib32-vulkan-intel")
                break
            elif resposta2 in ("n", "nao", "não"):
                print("Pulando...\n")
                break
            else:
                print("Responda com 's' ou 'n'.")

        break
    else:
        print("Responda com 's' ou 'n'.")

while True:
    resposta = input("Agora o instalador irá proseguir para a instalação dos demais pacotes (FFmpeg, Gstreamer e etc).\nDeseja continuar? (S/N): ").strip().lower()
    if resposta in ("s", "sim"):
        print("Iniciando instalação...")
        os.system("sudo pacman -Syu --needed ffmpeg gst-plugins-ugly gst-plugins-good gst-plugins-base gst-plugins-bad gst-libav gstreamer git fastfetch gufw fwupd ntfs-3g fuse2 fuse2fs svt-av1 flatpak wine-staging wine-gecko lutris steam fish gparted gamemode lib32-gamemode kimageformats mediainfo noise-suppression-for-voice qt6-imageformats system-config-printer mangohud gamescope alsa-utils")
        break
    elif resposta in ("n", "nao", "não"):
        print("Cancelado...")
        break
    else:
        print("Responda com 's' ou 'n'.")
