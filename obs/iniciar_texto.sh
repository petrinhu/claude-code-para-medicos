#!/usr/bin/env bash
# Liga o servidor do "Texto ao vivo" e abre a janela de controle no navegador.
DIR="/home/petrus/IDrive/Vídeos/Dieckmann/aulas_claude_dieckmann/obs"

# Se ainda nao estiver no ar, (re)inicia limpo.
if ! curl -s -m 2 http://localhost:4466/estado >/dev/null 2>&1; then
  pkill -f servidor_texto.py 2>/dev/null
  sleep 1
  setsid python3 "$DIR/servidor_texto.py" >/tmp/srvtexto.log 2>&1 < /dev/null &
  # espera subir (ate ~5s)
  for i in 1 2 3 4 5 6 7 8 9 10; do
    curl -s -m 1 http://localhost:4466/estado >/dev/null 2>&1 && break
    sleep 0.5
  done
fi

# Abre o controle no navegador padrao.
xdg-open "http://localhost:4466/controle" >/dev/null 2>&1 &
notify-send -i input-keyboard "Texto ao vivo" "Servidor ligado. Digite na janela de controle; aparece no OBS." 2>/dev/null
exit 0
