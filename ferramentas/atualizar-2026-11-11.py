# Link na bio, 11/11/2026 (pedido do Bruno): logo dele no lugar do @, botão principal pro site novo,
# @novva.business -> @brunocomassettodigital e parceria "Treino e Dieta" (@lorenzoleitef, "fale que veio por mim").
# Edita linkbio/index.html no lugar; cada troca tem que aparecer uma vez só.
import io, re

P = r"C:/Users/bruno/novva/BrunoComassetto/linkbio/index.html"
ICONE = r"C:/Users/bruno/novva/BrunoComassetto/site/assets/icone.svg"
s = io.open(P, encoding="utf-8").read()

def troca(a, b):
    global s
    assert s.count(a) == 1, ("não achei uma vez só", a[:60], s.count(a))
    s = s.replace(a, b)

# fonte do logo
troca("family=Bebas+Neue&family=Manrope:wght@400;500;600;700&display=swap",
      "family=Bebas+Neue&family=Manrope:wght@400;500;600;700&family=JetBrains+Mono:wght@400;800&display=swap")

# logo digitado (o mesmo do topo do site) no lugar do @
troca('<h1 class="handle">@BRUNOCOMASSETTO</h1>',
'''<h1 class="logoDig" aria-label="Bruno Comassetto, desenvolvedor e especialista em IA">
    <span class="ln1" aria-hidden="true"><span class="nome">bruno comassetto</span><span class="cur"></span></span>
    <span class="ln2" aria-hidden="true"><span class="barras">//</span> <span class="frase">desenvolvedor e especialista em IA</span></span>
  </h1>
  <script>
  (function(){
    var logo = document.currentScript.previousElementSibling;
    var nome = logo.querySelector(".nome"), frase = logo.querySelector(".frase"), bar = logo.querySelector(".barras");
    var visto = false;
    try { visto = sessionStorage.getItem("bc-logo") === "1"; sessionStorage.setItem("bc-logo", "1"); } catch (e) {}
    if (visto || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    var tNome = nome.textContent, tFrase = frase.textContent;
    nome.textContent = ""; frase.textContent = ""; bar.style.visibility = "hidden";
    logo.classList.add("digitando");
    function digita(el, texto, rapido, fim){
      var i = 0;
      (function passo(){
        i++; el.textContent = texto.slice(0, i);
        if (i >= texto.length) { fim(); return; }
        var t = rapido ? 16 + Math.random() * 16 : 70 + Math.random() * 70;
        if (texto.charAt(i - 1) === " ") t += rapido ? 25 : 140;
        setTimeout(passo, t);
      })();
    }
    setTimeout(function(){
      digita(nome, tNome, false, function(){
        setTimeout(function(){
          bar.style.visibility = "";
          setTimeout(function(){ digita(frase, tFrase, true, function(){ logo.classList.remove("digitando"); }); }, 120);
        }, 380);
      });
    }, 450);
  })();
  </script>''')

css = """
/* logo (mesmas medidas do logo/final: nome 800, cursor .372em, frase a .39 do tamanho) */
.logoDig{ font-family:'JetBrains Mono',ui-monospace,monospace; font-size:min(27px,7.2vw); width:10.1em; margin:0 auto 16px;
  text-align:left; color:var(--text); line-height:1; font-weight:400; }
.logoDig .ln1{ display:flex; align-items:flex-end; height:.73em; font-weight:800; white-space:pre; }
.logoDig .nome{ display:block; height:.73em; line-height:.73em; }
.logoDig .cur{ flex:none; width:.372em; height:.73em; margin-left:.12em; background:#1F87FF; animation:piscaCur 1.06s steps(1) infinite; }
.logoDig.digitando .cur{ animation:none; }
.logoDig .ln2{ display:block; margin-top:1.25em; font-size:.39em; color:var(--text-soft); white-space:pre; min-height:1.2em; }
.logoDig .barras{ color:#1F87FF; }
@keyframes piscaCur{ 50%{ opacity:0; } }
@media (prefers-reduced-motion: reduce){ .logoDig .cur{ animation:none; } }
.bar .icone-bc{ width:26px; height:26px; flex-shrink:0; display:block; }
.partner-icon.treino{ background:#1F87FF; }
.partner-name small{ display:block; font-size:11.5px; font-weight:500; color:var(--text-soft); margin-top:1px; }
.partner-coupon.indica{ text-align:right; line-height:1.25; font-size:11px; font-weight:600; color:var(--text-soft); }
.partner-coupon.indica b{ display:block; font-size:12.5px; color:#6f9bff; }
"""
troca("\n</style>", css + "</style>")

# botão principal: site novo, com o ícone do logo no lugar do da Novva
icone = io.open(ICONE, encoding="utf-8").read().strip()
icone = icone.replace('width="400" height="400" ', 'class="icone-bc" aria-hidden="true" ')
s, k = re.subn(r'<a class="bar primary" href="https://agencianovva.com" target="_blank" rel="noopener">\s*<svg class="novva-icon".*?</svg>',
               '<a class="bar primary" href="https://brunocomassetto.vercel.app" target="_blank" rel="noopener">\n      ' + icone.replace("\\", "\\\\"),
               s, count=1, flags=re.S)
assert k == 1, "botão principal não encontrado"

# Instagram profissional no lugar do @novva.business
troca('<a class="bar secondary" href="https://www.instagram.com/novva.business/" target="_blank" rel="noopener">',
      '<a class="bar secondary" href="https://www.instagram.com/brunocomassettodigital/" target="_blank" rel="noopener">')
troca("      @novva.business\n", "      @brunocomassettodigital\n")

# parceria: Treino e Dieta com o Lorenzo
treino = '''    <a class="partner" href="https://www.instagram.com/lorenzoleitef/" target="_blank" rel="noopener">
      <span class="partner-icon treino"><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round"><path d="M6.5 6.5v11M17.5 6.5v11M3.5 9.5v5M20.5 9.5v5M6.5 12h11"/></svg></span>
      <span class="partner-name">Treino e Dieta<small>@lorenzoleitef</small></span>
      <span class="partner-coupon indica">Fale que<b>veio por mim</b></span>
    </a>
  </div>

</div>
</body>'''
troca("  </div>\n\n</div>\n</body>", treino)

io.open(P, "w", encoding="utf-8", newline="\n").write(s)
print("ok")
