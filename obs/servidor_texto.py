#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Texto ao vivo para OBS (funciona no Wayland).

Voce digita numa janela de controle (navegador normal, onde o teclado
funciona) e o texto aparece na tela do OBS em tempo real (~80 ms).

COMO USAR
  1. Rode:  python3 obs/servidor_texto.py
  2. No OBS: fonte Navegador (Browser), "Arquivo local" DESMARCADO,
     URL:  http://localhost:4466/
     Largura 1920, Altura 1080.
  3. No Firefox, abra:  http://localhost:4466/controle
     Digite ali e ajuste a formatacao. Aparece no OBS ao vivo.
  Ctrl+C no terminal para parar.
"""
import json, threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = 4466

STATE = {
    "texto": "",
    "formato": {
        "size": 60, "color": "ffffff", "font": "sans", "weight": 800,
        "italic": 0, "pos": "baixo", "align": "center",
        "shadow": 1, "bg": 0, "bgcolor": "140529"
    }
}
LOCK = threading.Lock()

OVERLAY = r"""<!doctype html><html lang="pt-br"><head><meta charset="utf-8">
<title>Texto ao vivo</title><style>
:root{--tam:60px;--cor:#fff;--peso:800;--fonte:Inter,"Open Sans","Segoe UI",Arial,sans-serif;--bgcor:rgba(20,5,45,.72);--sombra:0 2px 10px rgba(0,0,0,.9),0 0 3px rgba(0,0,0,.95)}
*{box-sizing:border-box}html,body{margin:0;width:1920px;height:1080px;background:transparent;overflow:hidden;font-family:var(--fonte)}
.palco{position:absolute;inset:0;display:flex;padding:5vh 6vw}
.palco.baixo{align-items:flex-end}.palco.meio{align-items:center}.palco.top{align-items:flex-start}
.campo{width:100%;font-size:var(--tam);font-weight:var(--peso);font-family:var(--fonte);line-height:1.22;color:var(--cor);text-align:center;white-space:pre-wrap;word-break:break-word;text-shadow:var(--sombra);border-radius:14px;padding:6px 10px}
body.italic .campo{font-style:italic}
body.bg .campo{background:var(--bgcor);text-shadow:none;box-shadow:0 8px 30px rgba(0,0,0,.35);padding:18px 28px}
body.bg .campo:empty{background:transparent;box-shadow:none}
</style></head><body>
<div class="palco baixo" id="palco"><div class="campo" id="campo"></div></div>
<script>
var FONTES={sans:'Inter,"Open Sans","Segoe UI",Arial,sans-serif',serif:'Georgia,"Times New Roman",serif',mono:'"JetBrains Mono","DejaVu Sans Mono",monospace',cond:'"Arial Narrow","Roboto Condensed",sans-serif',round:'"Trebuchet MS","Segoe UI",sans-serif'};
var campo=document.getElementById('campo'),palco=document.getElementById('palco'),root=document.documentElement;
function on(v){return v==1||v==='1'||v===true;}
function aplicar(f){f=f||{};
 root.style.setProperty('--tam',(f.size||60)+'px');
 root.style.setProperty('--cor','#'+(''+(f.color||'ffffff')).replace('#',''));
 root.style.setProperty('--peso',f.weight||800);
 root.style.setProperty('--fonte',FONTES[f.font]||FONTES.sans);
 campo.style.textAlign=f.align||'center';
 document.body.classList.toggle('italic',on(f.italic));
 document.body.classList.toggle('bg',on(f.bg));
 if(f.bgcolor)root.style.setProperty('--bgcor','#'+(''+f.bgcolor).replace('#',''));
 root.style.setProperty('--sombra',(f.shadow===0||f.shadow==='0')?'none':'0 2px 10px rgba(0,0,0,.9),0 0 3px rgba(0,0,0,.95)');
 palco.className='palco '+(['top','meio','baixo'].indexOf(f.pos)>=0?f.pos:'baixo');}
var ut=null,uf=null;
function tick(){fetch('/estado?_='+Date.now(),{cache:'no-store'}).then(function(r){return r.json();}).then(function(s){
 if(s.texto!==ut){ut=s.texto;campo.textContent=s.texto;}
 var j=JSON.stringify(s.formato);if(j!==uf){uf=j;aplicar(s.formato);}}).catch(function(){});}
setInterval(tick,80);tick();
</script></body></html>"""

CONTROLE = r"""<!doctype html><html lang="pt-br"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Controle - Texto ao vivo</title><style>
:root{--roxo:#5213B9;--esc:#1F0646;--txt:#2E3233;--sec:#646C6F;--bg:#F4F2F8;--card:#fff;--chip:#E9E1F5;--linha:#E7E1F1}
*{box-sizing:border-box}html,body{margin:0}body{background:var(--bg);color:var(--txt);font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:1000px;margin:0 auto;padding:20px}
h1{font-size:22px;margin:0 0 2px}.sub{color:var(--sec);font-size:14px;margin:0 0 14px}
textarea{width:100%;min-height:150px;font-size:22px;line-height:1.3;padding:14px 16px;border:2px solid var(--linha);border-radius:12px;resize:vertical;font-family:inherit;outline:none}
textarea:focus{border-color:var(--roxo)}
.fmt{display:flex;flex-wrap:wrap;gap:14px 20px;align-items:center;background:var(--card);border:1px solid var(--linha);border-radius:12px;padding:14px 16px;margin-top:14px}
.fmt .g{display:flex;flex-direction:column;gap:4px}
.fmt label{font-size:11.5px;font-weight:700;color:var(--esc);text-transform:uppercase;letter-spacing:.03em}
select,input[type=range]{font:inherit}select{padding:6px 8px;border:1px solid var(--linha);border-radius:7px;background:#fff}
input[type=color]{width:42px;height:30px;border:1px solid var(--linha);border-radius:6px;padding:2px;cursor:pointer}
.chk{flex-direction:row;align-items:center;gap:6px;font-size:14px}
.status{margin-top:10px;font-size:13px;color:var(--sec)}
.status b{color:#2E8B57}
.nota{background:var(--chip);color:#3d2a63;border-radius:10px;padding:10px 14px;margin-top:12px;font-size:13px}
</style></head><body><div class="wrap">
<h1>Controle do texto ao vivo</h1>
<p class="sub">Digite aqui: aparece na tela do OBS ao vivo. Ajuste o visual nos menus embaixo.</p>
<textarea id="texto" placeholder="Digite... (aparece no OBS enquanto voce digita)"></textarea>
<div class="fmt">
 <div class="g"><label>Fonte</label><select id="font"><option value="sans">Sem serifa</option><option value="serif">Com serifa</option><option value="mono">Monoespacada</option><option value="cond">Condensada</option><option value="round">Arredondada</option></select></div>
 <div class="g"><label>Tamanho</label><input type="range" id="size" min="28" max="120" value="60"><span id="sv" style="font-size:12px;color:var(--sec)">60px</span></div>
 <div class="g"><label>Cor</label><input type="color" id="color" value="#ffffff"></div>
 <div class="g chk"><input type="checkbox" id="bold" checked><label for="bold">Negrito</label></div>
 <div class="g chk"><input type="checkbox" id="italic"><label for="italic">Italico</label></div>
 <div class="g"><label>Posicao</label><select id="pos"><option value="baixo">Embaixo</option><option value="meio">Meio</option><option value="top">Cima</option></select></div>
 <div class="g"><label>Alinhar</label><select id="align"><option value="center">Centro</option><option value="left">Esquerda</option><option value="right">Direita</option></select></div>
 <div class="g chk"><input type="checkbox" id="shadow" checked><label for="shadow">Sombra</label></div>
 <div class="g chk"><input type="checkbox" id="bg"><label for="bg">Faixa</label></div>
 <div class="g"><label>Cor faixa</label><input type="color" id="bgcolor" value="#140529"></div>
</div>
<div class="status">Conexao: <b id="conn">verificando...</b></div>
<div class="nota">Deixe esta janela aberta enquanto grava. No OBS a fonte "Texto ao vivo" deve ser um Navegador com a URL <b>http://localhost:4466/</b> ("Arquivo local" desmarcado).</div>
</div><script>
var el=function(i){return document.getElementById(i);};
function post(url,body){return fetch(url,{method:'POST',body:body,headers:{'Content-Type':'text/plain'}});}
// texto ao vivo
el('texto').addEventListener('input',function(){post('/texto',el('texto').value).then(function(){el('conn').textContent='ok';el('conn').style.color='#2E8B57';}).catch(function(){el('conn').textContent='sem servidor';el('conn').style.color='#c0392b';});});
// formatacao
function fmt(){return{size:+el('size').value,color:el('color').value.replace('#',''),font:el('font').value,weight:el('bold').checked?800:400,italic:el('italic').checked?1:0,pos:el('pos').value,align:el('align').value,shadow:el('shadow').checked?1:0,bg:el('bg').checked?1:0,bgcolor:el('bgcolor').value.replace('#','')};}
function enviaFmt(){el('sv').textContent=el('size').value+'px';post('/formato',JSON.stringify(fmt()));}
Array.prototype.forEach.call(document.querySelectorAll('.fmt input,.fmt select'),function(c){c.addEventListener('input',enviaFmt);c.addEventListener('change',enviaFmt);});
// carrega estado atual
fetch('/estado').then(function(r){return r.json();}).then(function(s){el('texto').value=s.texto||'';el('conn').textContent='ok';el('conn').style.color='#2E8B57';
 var f=s.formato||{};if(f.size){el('size').value=f.size;el('sv').textContent=f.size+'px';}if(f.color)el('color').value='#'+f.color;if(f.font)el('font').value=f.font;el('bold').checked=(f.weight!=400);el('italic').checked=(f.italic==1);if(f.pos)el('pos').value=f.pos;if(f.align)el('align').value=f.align;el('shadow').checked=(f.shadow!=0);el('bg').checked=(f.bg==1);if(f.bgcolor)el('bgcolor').value='#'+f.bgcolor;
}).catch(function(){el('conn').textContent='sem servidor';el('conn').style.color='#c0392b';});
</script></body></html>"""

class H(BaseHTTPRequestHandler):
    def _send(self, code, ctype, body):
        if isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        p = self.path.split("?")[0]
        if p == "/":
            self._send(200, "text/html; charset=utf-8", OVERLAY)
        elif p == "/controle":
            self._send(200, "text/html; charset=utf-8", CONTROLE)
        elif p == "/estado":
            with LOCK:
                self._send(200, "application/json", json.dumps(STATE))
        else:
            self._send(404, "text/plain", "nao encontrado")

    def do_POST(self):
        p = self.path.split("?")[0]
        n = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(n).decode("utf-8") if n else ""
        if p == "/texto":
            with LOCK:
                STATE["texto"] = body
            self._send(200, "text/plain", "ok")
        elif p == "/formato":
            try:
                f = json.loads(body)
                with LOCK:
                    STATE["formato"] = f
                self._send(200, "text/plain", "ok")
            except Exception:
                self._send(400, "text/plain", "formato invalido")
        else:
            self._send(404, "text/plain", "nao")

    def log_message(self, *a):
        pass  # silencia o log de requests

if __name__ == "__main__":
    srv = ThreadingHTTPServer(("127.0.0.1", PORT), H)
    print("=" * 54)
    print(" Texto ao vivo para OBS  (Ctrl+C para parar)")
    print("=" * 54)
    print(" OBS  -> Browser Source, URL: http://localhost:%d/" % PORT)
    print(" Voce -> abra no navegador:   http://localhost:%d/controle" % PORT)
    print("=" * 54)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nparado.")
