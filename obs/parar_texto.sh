#!/usr/bin/env bash
# Desliga o servidor do "Texto ao vivo".
pkill -f servidor_texto.py 2>/dev/null
notify-send -i process-stop "Texto ao vivo" "Servidor desligado." 2>/dev/null
exit 0
