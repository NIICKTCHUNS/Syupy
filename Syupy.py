# Syupy, Instalador de pacotes que eu acho útil.

import os
import signal
import sys

# Handler de saída
def bela_saida(sig, frame):
    print("\n\nSaindo...\n")
    sys.exit(0)
signal.signal(signal.SIGINT, bela_saida)

# Créditos e aviso
print("Programa para instalação de pacotes que eu acho útil.\nVersão: 1.3\nPor: NIICKTCHUNS\n\n\033[1;31mOs demais pacotes podem instalar outras dependências consigo.\033[0m")
print("Iniciando instalação de pacotes...\n")

# Drivers
while True:
    resposta = input("Deseja instalar os drivers de qual fabricante? AMD, Intel ou Nenhuma (A/I/N): ").strip().lower()
    if resposta in ("a", "amd"):
        print("Instalando drivers da AMD...\n")
        os.system("sudo pacman -S --noconfirm --needed mesa lib32-mesa xf86-video-amdgpu vulkan-radeon lib32-vulkan-radeon")
        while True:
            rocm = input("Deseja instalar os drivers adicionais OpenCL, ROCm e HIP? (S/N): ").strip().lower()
            if rocm in ("s", "sim"):
                os.system("sudo pacman -S --noconfirm --needed rocm-core rocm-cmake rocm-language-runtime rocm-opencl-runtime rocminfo rocm-hip-runtime rocm-llvm")
                break
            elif rocm in ("n", "nao", "não"):
                print("Pulando...\n")
                break
            else:
                print("Responda com as opções disponíveis.")
        break
    elif resposta in ("i", "intel"):
        print("Instalando drivers da Intel...\n")
        os.system("sudo pacman -S --noconfirm --needed intel-media-driver libvpl vpl-gpu-rt vulkan-intel lib32-vulkan-intel intel-compute-runtime")
        break
    elif resposta in ("n", "nao", "não"):
        print("Pulando...\n")
        break
    else:
        print("Responda com as opções disponíveis.")

# Pacotes
while True:
    pacotes = input("Agora o instalador irá proseguir para a instalação dos demais pacotes (FFmpeg, Gstreamer e etc).\nDeseja continuar? (S/N): ").strip().lower()
    if pacotes in ("s", "sim"):
        print("Iniciando instalação...\n")
        os.system("sudo pacman -S --noconfirm --needed ffmpeg gst-plugins-ugly gst-plugins-good gst-plugins-base gst-plugins-bad gst-libav gstreamer git fastfetch gufw fwupd ntfs-3g fuse2 fuse2fs svt-av1 flatpak wine-staging wine-gecko lutris steam fish gparted gamemode lib32-gamemode kimageformats mediainfo noise-suppression-for-voice qt6-imageformats system-config-printer mangohud gamescope alsa-utils")
        # Firewall
        while True:
            firewall = input("Deseja configurar o Firewall UFW? (S/N): ").strip().lower()
            if firewall in ("s", "sim"):
                print("Iniciando configuração do UFW...\n")
                os.system("sudo ufw enable && sudo ufw allow 1714:1764/udp && sudo ufw allow 1714:1764/tcp && sudo ufw reload")
                print(f"\n\033[32mFinalizado...\033[0m\n")
                break
            elif firewall in ("n", "nao", "não"):
                print(f"\n\033[32mFinalizado...\033[0m\n")
                break
        break
    elif pacotes in ("n", "nao", "não"):
        print("Cancelado...\n")
        break
    else:
        print("Responda com as opções disponíveis.")
