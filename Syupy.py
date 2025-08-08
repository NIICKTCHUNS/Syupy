# Syupy, Instalador de pacotes que eu acho útil.

import os

print("Programa para instalação de pacotes que eu acho útil.\nVersão: 1.1\nPor: NIICKTCHUNS\n")
print("Iniciando instalação de pacotes...\n")

while True:
    resposta = input("Deseja instalar os drivers de qual fabricante? AMD, Intel ou Nenhuma (A/I/N): ").strip().lower()
    if resposta in ("a", "amd"):
        print("Instalando drivers da AMD...\n")
        os.system("sudo pacman -S --needed --noconfirm mesa lib32-mesa xf86-video-amdgpu vulkan-radeon lib32-vulkan-radeon")
        
        break
    elif resposta in ("i", "intel"):
        print("Instalando drivers da Intel...\n")
        os.system("sudo pacman -S --needed intel-media-driver libvpl vpl-gpu-rt vulkan-intel lib32-vulkan-intel")
        break
    elif resposta in ("n", "nao", "não"):
        print("Pulando...\n")
        break
    else:
        print("Responda com as opções disponíveis.")

while True:
    resposta = input("Agora o instalador irá proseguir para a instalação dos demais pacotes (FFmpeg, Gstreamer e etc).\nDeseja continuar? (S/N): ").strip().lower()
    if resposta in ("s", "sim"):
        print("Iniciando instalação...")
        os.system("sudo pacman -Syu --needed ffmpeg gst-plugins-ugly gst-plugins-good gst-plugins-base gst-plugins-bad gst-libav gstreamer git fastfetch gufw fwupd ntfs-3g fuse2 fuse2fs svt-av1 flatpak wine-staging wine-gecko lutris steam fish gparted gamemode lib32-gamemode kimageformats mediainfo noise-suppression-for-voice qt6-imageformats system-config-printer mangohud gamescope alsa-utils")
        break
    elif resposta in ("n", "nao", "não"):
        print("Cancelado...\n")
        break
    else:
        print("Responda com 's' ou 'n'.")
