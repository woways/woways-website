# -*- coding: utf-8 -*-
# Woways site generator — consistent multi-page site, real content, mascot, illustrations, animations.
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

LOGO = 'logo-woways.png'  # lightweight file reference (kept beside the pages)

HEAD = '''<!DOCTYPE html>
<html class="scroll-smooth" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>__TITLE__</title>
<link rel="icon" href="favicon.ico" sizes="any"/>
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png"/>
<link rel="icon" type="image/png" sizes="16x16" href="favicon-16.png"/>
<link rel="apple-touch-icon" href="apple-touch-icon.png"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Syne:wght@500;600;700;800&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="styles.css"/>
<style>
 .material-symbols-outlined{font-variation-settings:'FILL' 0,'wght' 400,'GRAD' 0,'opsz' 24;display:inline-block;vertical-align:middle;line-height:1}
 body{font-family:"Hanken Grotesk",sans-serif;overflow-x:hidden}
 img{max-width:100%;height:auto}
 header img,footer img{max-height:2.5rem;width:auto}
 h1,h2,h3,h4,.font-display{font-family:"Syne",sans-serif;letter-spacing:-0.02em}
 .hd1{font-size:clamp(32px,4.6vw,48px);line-height:1.05;font-weight:700}
 .hd2{font-size:clamp(26px,3.6vw,40px);line-height:1.1;font-weight:700}
 .hd3{font-size:22px;line-height:1.2;font-weight:600}
 .lead{font-size:clamp(17px,2.2vw,20px);line-height:1.6}
 .cap{font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase}
 :focus-visible{outline:2.5px solid #00A9A9;outline-offset:3px}
 .skip{position:absolute;left:-9999px;top:0;background:#00A9A9;color:#02201E;padding:10px 16px;font-weight:600;z-index:200}
 .skip:focus{left:0}
 /* page transition */
 @keyframes pageIn{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
 main#main{animation:pageIn .55s cubic-bezier(.2,.7,.2,1) both}
 body.is-leaving{opacity:0;transform:translateY(-8px);transition:opacity .26s ease,transform .26s ease}
 @media (prefers-reduced-motion:reduce){main#main{animation:none}body.is-leaving{opacity:1!important;transform:none!important;transition:none}}
 /* animations */
 .js-anim .reveal{opacity:0;transform:translateY(22px);transition:opacity .7s cubic-bezier(.2,.7,.2,1),transform .7s cubic-bezier(.2,.7,.2,1)}
 .js-anim .reveal.in{opacity:1;transform:none}
 .js-anim .stagger.in>*{opacity:0;transform:translateY(18px);animation:rise .6s cubic-bezier(.2,.7,.2,1) forwards}
 .js-anim .stagger.in>*:nth-child(2){animation-delay:.08s}.js-anim .stagger.in>*:nth-child(3){animation-delay:.16s}
 .js-anim .stagger.in>*:nth-child(4){animation-delay:.24s}.js-anim .stagger.in>*:nth-child(5){animation-delay:.32s}
 @keyframes rise{to{opacity:1;transform:none}}
 .herofade{opacity:0;transform:translateY(16px);animation:rise .8s cubic-bezier(.2,.7,.2,1) .05s forwards}
 .card-lift{transition:transform .2s ease,box-shadow .2s ease,border-color .2s ease}
 .card-lift:hover{transform:translateY(-4px);box-shadow:0 24px 50px -30px rgba(0,15,36,.5)}
 .arrow-move{transition:transform .16s ease}
 .grp:hover .arrow-move{transform:translateX(4px)}
 @media (prefers-reduced-motion:reduce){.reveal,.stagger>*,.herofade{opacity:1!important;transform:none!important;animation:none!important}.mascot-float{animation:none!important}}
 .mascot-float{animation:bob 4.2s ease-in-out infinite}
 @keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
 @keyframes floaty{0%,100%{transform:translateY(0)}50%{transform:translateY(-14px)}}
 .floaty{animation:floaty 6s ease-in-out infinite}
 @media (prefers-reduced-motion:reduce){.floaty{animation:none!important}}
 .glow{background:radial-gradient(46% 60% at 85% 0%,rgba(0,169,169,.28),transparent 60%),radial-gradient(40% 55% at 0% 100%,rgba(232,163,61,.14),transparent 60%)}
 .gridlines{background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:64px 64px;-webkit-mask:radial-gradient(120% 90% at 50% 0%,#000 30%,transparent 78%);mask:radial-gradient(120% 90% at 50% 0%,#000 30%,transparent 78%)}
</style>
</head>'''

def mascot(size, cls=''):
    h = round(size*1.25)
    return ('<svg viewBox="0 0 120 150" width="%d" height="%d" role="img" aria-label="Wow, the Woways mascot" class="%s">' % (size,h,cls) +
      '<rect x="45" y="16" width="13" height="36" rx="6" fill="#00A9A9"/>'
      '<rect x="62" y="4" width="13" height="48" rx="6" fill="#E8A33D"/>'
      '<rect x="22" y="44" width="76" height="82" rx="30" fill="#00A9A9"/>'
      '<circle cx="47" cy="82" r="8" fill="#fff"/><circle cx="73" cy="82" r="8" fill="#fff"/>'
      '<circle cx="48" cy="83" r="3.6" fill="#000F24"/><circle cx="74" cy="83" r="3.6" fill="#000F24"/>'
      '<circle cx="38" cy="94" r="4" fill="#E8A33D" opacity=".5"/><circle cx="82" cy="94" r="4" fill="#E8A33D" opacity=".5"/>'
      '<path d="M49 99 Q60 108 71 99" fill="none" stroke="#000F24" stroke-width="3.4" stroke-linecap="round"/>'
      '<rect x="37" y="124" width="15" height="11" rx="5.5" fill="#00807F"/><rect x="68" y="124" width="15" height="11" rx="5.5" fill="#00807F"/>'
      '</svg>')

def illo_growth():
    return ('<svg viewBox="0 0 320 260" class="w-full h-auto max-w-[380px]" role="img" aria-label="Rising growth bars">'
      '<rect x="16" y="16" width="288" height="228" rx="16" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.14)"/>'
      '<line x1="44" y1="196" x2="276" y2="196" stroke="rgba(255,255,255,.25)"/>'
      '<rect x="64" y="150" width="36" height="46" rx="7" fill="#00A9A9"/><rect x="118" y="116" width="36" height="80" rx="7" fill="#00A9A9"/>'
      '<rect x="172" y="82" width="36" height="114" rx="7" fill="#3EC9C4"/><rect x="226" y="50" width="36" height="146" rx="7" fill="#E8A33D"/>'
      '<path d="M66 158 L136 122 L190 92 L244 60" fill="none" stroke="#66DCD9" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
      '<circle cx="244" cy="60" r="6" fill="#66DCD9"/></svg>')

def illo_connect():
    return ('<svg viewBox="0 0 320 260" class="w-full h-auto max-w-[380px]" role="img" aria-label="Companies and talent connected through Woways">'
      '<line x1="70" y1="70" x2="160" y2="130" stroke="rgba(255,255,255,.25)" stroke-width="2"/><line x1="250" y1="70" x2="160" y2="130" stroke="rgba(255,255,255,.25)" stroke-width="2"/>'
      '<line x1="70" y1="190" x2="160" y2="130" stroke="rgba(255,255,255,.25)" stroke-width="2"/><line x1="250" y1="190" x2="160" y2="130" stroke="rgba(255,255,255,.25)" stroke-width="2"/>'
      '<circle cx="70" cy="70" r="22" fill="#0A1830" stroke="#00A9A9" stroke-width="2"/><circle cx="250" cy="70" r="22" fill="#0A1830" stroke="#00A9A9" stroke-width="2"/>'
      '<circle cx="70" cy="190" r="22" fill="#0A1830" stroke="#E8A33D" stroke-width="2"/><circle cx="250" cy="190" r="22" fill="#0A1830" stroke="#E8A33D" stroke-width="2"/>'
      '<circle cx="160" cy="130" r="32" fill="#00A9A9"/><text x="160" y="135" text-anchor="middle" font-family="Syne" font-weight="700" font-size="13" fill="#02201E">WOW</text></svg>')

def illo_target():
    return ('<svg viewBox="0 0 320 260" class="w-full h-auto max-w-[380px]" role="img" aria-label="Pipeline funneling to a target">'
      '<rect x="16" y="16" width="288" height="228" rx="16" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.14)"/>'
      '<path d="M56 70 H264 L200 130 V196 L120 196 V130 Z" fill="none" stroke="#66DCD9" stroke-width="2.5" stroke-linejoin="round"/>'
      '<circle cx="160" cy="150" r="26" fill="none" stroke="#E8A33D" stroke-width="3"/><circle cx="160" cy="150" r="13" fill="none" stroke="#E8A33D" stroke-width="3"/><circle cx="160" cy="150" r="3" fill="#E8A33D"/>'
      '<circle cx="86" cy="70" r="5" fill="#00A9A9"/><circle cx="160" cy="70" r="5" fill="#00A9A9"/><circle cx="234" cy="70" r="5" fill="#00A9A9"/></svg>')

def illo_pathway():
    labels=[("Learn",120,"#0A1830"),("Execute",92,"#00807F"),("Perform",64,"#00A9A9"),("Grow",40,"#E8A33D")]
    bars=''; x=30
    for i,(lab,y,c) in enumerate(labels):
        bh=196-y
        bars+='<rect x="%d" y="%d" width="52" height="%d" rx="8" fill="%s"><animate attributeName="height" from="0" to="%d" dur="0.8s" begin="%.2fs" fill="freeze"/><animate attributeName="y" from="196" to="%d" dur="0.8s" begin="%.2fs" fill="freeze"/></rect>'%(x,y,bh,c,bh,i*0.15,y,i*0.15)
        bars+='<text x="%d" y="214" text-anchor="middle" font-family="Hanken Grotesk" font-size="11" fill="rgba(255,255,255,.75)">%s</text>'%(x+26,lab)
        x+=66
    return ('<svg viewBox="0 0 320 230" class="w-full h-auto max-w-[420px]" role="img" aria-label="The Wower pathway: Learn, Execute, Perform, Grow">'
      '<rect x="8" y="8" width="304" height="214" rx="16" fill="rgba(255,255,255,.04)" stroke="rgba(255,255,255,.14)"/>'
      '<line x1="22" y1="196" x2="298" y2="196" stroke="rgba(255,255,255,.25)"/>'
      '<path d="M56 150 L122 118 L188 90 L254 60" fill="none" stroke="#66DCD9" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.6s" begin="0.7s" fill="freeze"/></path>'
      '<circle cx="254" cy="60" r="5" fill="#E8A33D" opacity="0"><animate attributeName="opacity" from="0" to="1" dur="0.4s" begin="1.1s" fill="freeze"/></circle>'+bars+'</svg>')

NAV = [("index.html","Home"),("companies.html","For Companies"),("wowers.html","For Wowers"),
       ("products.html","Products"),("about.html","About")]
FOOTER_NAV = NAV + [("contact.html","Contact")]

def header(active):
    links = ''
    for href,label in NAV:
        if href==active:
            links += '<a class="cap text-white transition-colors relative" href="%s" aria-current="page">%s<span class="absolute -bottom-1.5 left-1/2 -translate-x-1/2 w-1 h-1 rounded-full bg-brandTeal"></span></a>' % (href,label)
        else:
            links += '<a class="cap text-slate-300 hover:text-white transition-colors" href="%s">%s</a>' % (href,label)
    mob=''
    for h,l in NAV:
        mob += '<a class="block px-6 py-3 text-slate-200 border-t border-white/10 font-display font-semibold" href="%s">%s</a>'%(h,l)
    mob += '<div class="p-4 border-t border-white/10"><a class="block text-center bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold px-6 py-3 transition-colors" href="contact.html">Talk to us</a></div>'
    return ('<a href="#main" class="skip">Skip to content</a>'
      '<header class="sticky top-0 z-50 bg-brandNavy/95 backdrop-blur border-b border-white/10">'
      '<div class="max-w-[1440px] mx-auto px-6 lg:px-12 h-16 flex items-center justify-between">'
      '<a href="index.html" aria-label="Woways — Execute, Grow, Transform" class="flex items-center gap-1 shrink-0">'
      '<img src="logo-icon.png" alt="" class="h-5 w-auto"/>'
      '<img src="logo-word.png" alt="Woways" class="h-5 w-auto"/></a>'
      '<div class="flex items-center gap-5">'
      '<nav class="hidden md:flex items-center gap-5 lg:gap-7" aria-label="Primary">%s</nav>'
      '<a class="hidden sm:inline-flex items-center bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold px-5 py-2.5 transition-colors" href="contact.html">Talk to us</a>'
      '<button id="mbtn" class="md:hidden text-white p-2" aria-label="Open menu" aria-expanded="false"><span class="material-symbols-outlined">menu</span></button>'
      '</div></div>'
      '<div id="mmenu" class="hidden md:hidden bg-brandNavy border-t border-white/10">%s</div>'
      '</header>') % (links, mob)

def footer():
    prod = [("https://studentmentor.co.in","Student Mentor"),("https://collegemacha.com","College Macha"),("https://talentignition.in","Talent Ignition"),("https://bispun.com","Bispun"),("https://woways-site.vercel.app","Perfoin")]
    plinks = ''.join('<li><a class="hover:text-white transition-colors" href="%s" target="_blank" rel="noopener noreferrer">%s</a></li>'%(u,n) for u,n in prod)
    exp = ''.join('<li><a class="hover:text-white transition-colors" href="%s">%s</a></li>'%(h,l) for h,l in FOOTER_NAV)
    return ('<footer class="bg-brandNavy text-slate-400 py-16 border-t border-white/10">'
      '<div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
      '<div class="grid grid-cols-2 md:grid-cols-4 gap-x-8 lg:gap-x-16 gap-y-10 pb-12 border-b border-white/10">'
      '<div class="col-span-2 md:col-span-1">'
      '<div class="flex items-center gap-1 mb-3"><img src="logo-icon.png" alt="" class="h-6 w-auto"/><img src="logo-word.png" alt="Woways" class="h-6 w-auto"/></div>'
      '<p class="cap text-brandTeal mb-2">Execute. Grow. Transform.</p>'
      '<p class="text-sm max-w-[30ch]">An execution partner and product studio for growing companies.</p></div>'
      '<div><h4 class="cap text-white mb-4">Explore</h4><ul class="space-y-2.5 text-sm">%s</ul></div>'
      '<div><h4 class="cap text-white mb-4">Products</h4><ul class="space-y-2.5 text-sm">%s</ul></div>'
      '<div><h4 class="cap text-white mb-4">Contact</h4><p class="text-sm mb-1"><a class="hover:text-white transition-colors" href="mailto:tech@woways.in">tech@woways.in</a></p>'
      '<p class="text-sm mb-1"><a class="hover:text-white transition-colors" href="tel:+919390188553">+91 93901 88553</a></p>'
      '<p class="text-sm">2nd floor, LorVen Smart Spaces,<br/>Gachibowli, Hyderabad, 500032</p></div>'
      '</div><div class="pt-6 text-sm text-slate-500 flex flex-wrap justify-between gap-3">'
      '<span>&copy; 2026 Woways Private Limited. All rights reserved.</span>'
      '<span class="flex flex-wrap gap-x-4 gap-y-1"><a class="hover:text-white transition-colors" href="privacy.html">Privacy Policy</a><a class="hover:text-white transition-colors" href="terms.html">Terms of Use</a><a class="hover:text-white transition-colors" href="cookies.html">Cookie Policy</a></span></div>'
      '</div></footer>') % (exp, plinks)

SCRIPT = ('<script>'
 '(function(){var b=document.getElementById("mbtn"),m=document.getElementById("mmenu");if(b)b.addEventListener("click",function(){var o=m.classList.toggle("hidden");b.setAttribute("aria-expanded",String(!o));});})();'
 '(function(){var els=document.querySelectorAll(".reveal,.stagger");'
 'if(matchMedia("(prefers-reduced-motion: reduce)").matches||!("IntersectionObserver" in window))return;'
 'document.documentElement.classList.add("js-anim");'
 'var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target);}});},{threshold:.12,rootMargin:"0px 0px -6% 0px"});'
 'els.forEach(function(e){io.observe(e);});'
 'setTimeout(function(){els.forEach(function(e){e.classList.add("in");});},1600);})();'
 '(function(){var els=document.querySelectorAll(".countup");if(!els.length)return;var fmt=function(n){return n.toLocaleString("en-IN");};var run=function(el){var to=parseInt(el.getAttribute("data-to"),10)||0,st=null,d=1400;setTimeout(function(){el.textContent=fmt(to);},d+500);if(matchMedia("(prefers-reduced-motion: reduce)").matches||!window.requestAnimationFrame){el.textContent=fmt(to);return;}el.textContent="0";function step(t){if(!st)st=t;var p=Math.min((t-st)/d,1);el.textContent=fmt(Math.floor((1-Math.pow(1-p,3))*to));if(p<1)requestAnimationFrame(step);}requestAnimationFrame(step);};if("IntersectionObserver" in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){run(e.target);io.unobserve(e.target);}});},{threshold:.4});els.forEach(function(e){io.observe(e);});}else{els.forEach(run);}})();'
 '(function(){document.querySelectorAll("form.w3form").forEach(function(f){f.addEventListener("submit",function(e){e.preventDefault();'
 'var ok=f.querySelector(".form-ok"),err=f.querySelector(".form-err"),btn=f.querySelector("button[type=submit]"),lbl=btn?btn.textContent:"";'
 'if(err)err.classList.add("hidden");if(ok)ok.classList.add("hidden");'
 'var obj={};new FormData(f).forEach(function(v,k){obj[k]=v;});'
 'if(btn){btn.disabled=true;btn.textContent="Sending\\u2026";}'
 'fetch("/api/submit",{method:"POST",headers:{"Content-Type":"application/json",Accept:"application/json"},body:JSON.stringify(obj)})'
 '.then(function(r){return r.json();}).then(function(j){if(j.success){f.reset();if(ok){ok.classList.remove("hidden");ok.scrollIntoView({block:"center",behavior:"smooth"});}}else{if(err){err.textContent=(j&&j.message)||"Something went wrong. Please email tech@woways.in.";err.classList.remove("hidden");}}})'
 '.catch(function(){if(err){err.textContent="Network error. Please email tech@woways.in.";err.classList.remove("hidden");}})'
 '.finally(function(){if(btn){btn.disabled=false;btn.textContent=lbl;}});});});})();'
 '(function(){if(matchMedia("(prefers-reduced-motion: reduce)").matches)return;'
 'document.addEventListener("click",function(e){if(e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey)return;'
 'var a=e.target.closest&&e.target.closest("a");if(!a)return;'
 'if(a.target==="_blank"||a.hasAttribute("download"))return;'
 'var href=a.getAttribute("href")||"";if(!href||href.charAt(0)==="#"||/^(mailto:|tel:)/.test(href))return;'
 'var url;try{url=new URL(a.href,location.href);}catch(_){return;}'
 'if(url.origin!==location.origin)return;'
 'if(url.pathname===location.pathname){return;}'
 'e.preventDefault();document.body.classList.add("is-leaving");'
 'setTimeout(function(){location.href=a.href;},230);'
 'setTimeout(function(){document.body.classList.remove("is-leaving");},2500);});'
 'window.addEventListener("pageshow",function(ev){if(ev.persisted)document.body.classList.remove("is-leaving");});})();'
 '</script>')

def page(title, active, body):
    return HEAD.replace('__TITLE__', title) + '<body class="bg-paperBg text-brandNavy antialiased">' + header(active) + '<main id="main" tabindex="-1">' + body + '</main>' + footer() + SCRIPT + '</body></html>'

# ---------- shared content bits ----------
CHECK = '<span class="material-symbols-outlined text-brandTeal text-[20px] shrink-0" aria-hidden="true">check</span>'

def eyebrow(t): return '<span class="cap text-brandTeal block mb-2">%s</span>' % t

def sec_head(eb, h, p, dark=False):
    tc = 'text-white' if dark else 'text-brandNavy'
    pc = 'text-slate-300' if dark else 'text-slate-600'
    return ('<div class="max-w-3xl mb-12 reveal">%s<h2 class="hd2 %s mb-3">%s</h2><p class="lead %s">%s</p></div>'
            % (eyebrow(eb), tc, h, pc, p))

CAPS = [("show_chart","Sales","Pipeline execution, outreach and closing support that plugs into your existing targets."),
        ("campaign","Marketing","Campaigns, content and channel work run end to end, reporting back into your team."),
        ("account_tree","Operations","Process execution and coordination that keeps daily operations moving without gaps."),
        ("groups","HR","Hiring, onboarding and people operations handled with your standards, on your timeline."),
        ("terminal","Technology","Product, platform and tooling work — including the products we build ourselves.")]

def caps_grid():
    cards=''
    for ic,n,d in CAPS:
        cards += ('<div class="bg-white border border-borderLine p-6 card-lift group">'
          '<span class="material-symbols-outlined text-[26px] text-brandNavy group-hover:text-brandTeal transition-colors mb-6 block" aria-hidden="true">%s</span>'
          '<h3 class="hd3 text-brandNavy mb-2">%s</h3><p class="text-[15px] leading-relaxed text-slate-600 leading-relaxed">%s</p></div>' % (ic,n,d))
    return '<div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-6 stagger reveal">%s</div>' % cards

def egt():
    rows=[("STAGE 01","Execute","We take on the work that's already defined — running it well, on schedule, inside your existing systems.","brandNavy"),
          ("STAGE 02","Grow","Once the work is stable, we look for where it can scale — more reach, more output, more coverage.","brandTeal"),
          ("STAGE 03","Transform","We bring in the data, tooling and process changes that shift how the function runs going forward.","brandOrange")]
    cards=''
    for i,(idx,h,p,c) in enumerate(rows):
        lb = ''
        cards += ('<div class="border border-borderLine%s p-8 bg-white card-lift"><div class="w-full h-1 bg-%s mb-6"></div>'
          '<span class="cap text-%s font-bold">%s</span><h3 class="hd3 text-brandNavy mt-2 mb-4" style="font-size:24px">%s</h3>'
          '<p class="text-slate-600 leading-relaxed">%s</p></div>' % (lb,c,c,idx,h,p))
    return '<div class="grid grid-cols-1 md:grid-cols-3 gap-8 stagger reveal">%s</div>' % cards

SERVICES=[("filter_alt","Lead Generation","DM outreach, prospecting and targeted campaigns to fill your pipeline."),
          ("call","Sales Support","Telecalling, demo booking and follow-ups to close deals faster."),
          ("bolt","Growth Operations","Marketing execution, CRM management and process optimization."),
          ("hub","Talent Ecosystem","Wower internships, project work and performance-based growth.")]

def services_grid():
    cards=''
    for ic,n,d in SERVICES:
        cards += ('<div class="bg-white border border-borderLine p-8 card-lift flex gap-5 items-start">'
          '<span class="w-12 h-12 shrink-0 bg-brandTealTint text-brandTealDark grid place-items-center"><span class="material-symbols-outlined" aria-hidden="true">%s</span></span>'
          '<div><h3 class="hd3 text-brandNavy mb-2" style="font-size:19px">%s</h3><p class="text-slate-600">%s</p></div></div>' % (ic,n,d))
    return '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 stagger reveal">%s</div>' % cards

def product_cards(group):
    edu=[("Career guidance · Class 10 to PG","Student Mentor","Career guidance and mentoring for students from Class 10 through postgraduate study.","https://studentmentor.co.in","Explore the product"),
         ("College discovery","College Macha","A clearer way for students and families to explore college options and make informed choices.","https://collegemacha.com","Explore the product"),
         ("Future-readiness · School","Talent Ignition","Future-readiness learning programs for school students.","https://talentignition.in","Explore the product")]
    biz=[("CRM · consultants & institutions","Bispun","A CRM for education-focused consultants and institutions.","https://bispun.com","Explore the product"),
         ("Performance management · SaaS","Perfoin","A performance-management platform for teams that want better visibility, accountability and growth.","https://woways-site.vercel.app","Explore the product")]
    IMG={"Student Mentor":"shot-studentmentor.jpg","College Macha":"shot-collegemacha.jpg","Talent Ignition":"shot-talentignition.jpg","Bispun":"shot-bispun.jpg","Perfoin":"shot-performance.jpg"}
    def preview_html(name):
        shot=IMG.get(name)
        if shot:
            return '<div class="aspect-[16/10] overflow-hidden -mx-8 -mt-8 mb-6 border-b border-borderLine"><img src="%s" alt="%s preview" loading="lazy" class="w-full h-full object-cover object-top"/></div>'%(shot,name)
        return '<div class="aspect-[16/10] -mx-8 -mt-8 mb-6 border-b border-borderLine bg-gradient-to-br from-brandNavy to-brandInk grid place-items-center"><span class="font-display font-semibold text-white/85" style="font-size:18px">%s</span></div>'%name
    def card(tag,name,desc,url,cta):
        preview=preview_html(name)
        if url:
            return ('<a class="bg-white border border-borderLine p-8 card-lift grp flex flex-col justify-between hover:border-brandNavy overflow-hidden" href="%s" target="_blank" rel="noopener noreferrer">'
              '<div>%s<span class="cap text-brandTeal bg-brandTealTint px-2.5 py-1">%s</span>'
              '<h3 class="hd3 text-brandNavy mt-4 mb-3" style="font-size:20px">%s</h3><p class="text-[15px] leading-relaxed text-slate-600 leading-relaxed mb-8">%s</p></div>'
              '<span class="inline-flex items-center gap-2 text-sm font-semibold text-brandNavy">%s <span class="material-symbols-outlined text-[16px] arrow-move" aria-hidden="true">open_in_new</span></span></a>' % (url,preview,tag,name,desc,cta))
        # coming soon (no link)
        return ('<div class="bg-white border border-borderLine p-8 flex flex-col justify-between overflow-hidden">'
          '<div>%s<span class="cap text-orange-700 bg-orange-50 px-2.5 py-1" style="color:#C6842A;background:#FDF3E3">%s</span>'
          '<h3 class="hd3 text-brandNavy mt-4 mb-3" style="font-size:20px">%s</h3><p class="text-[15px] leading-relaxed text-slate-600 leading-relaxed mb-8">%s</p></div>'
          '<span class="inline-flex items-center gap-2 text-sm font-semibold text-slate-400">%s <span class="material-symbols-outlined text-[16px]" aria-hidden="true">schedule</span></span></div>' % (preview,tag,name,desc,cta))
    if group=='edu':
        return '<div class="grid grid-cols-1 md:grid-cols-3 gap-6 stagger reveal">%s</div>' % ''.join(card(*e) for e in edu)
    return '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 stagger reveal">%s</div>' % ''.join(card(*b) for b in biz)

def cta_band(kind='general'):
    conf={
      'company':("Ready to move the work forward?","Share your requirement and we'll come back with the right execution scope within 48 hours.","Discuss your requirement","partnerships.html#partner-form"),
      'wower':("Ready to do real work?","Apply for a project and start building evidence of what you can do.","Apply for opportunities","internships.html#apply-form"),
      'product':("Want to see a product in action?","Tell us what you're looking for and we'll point you to the right one.","Talk to us","contact.html"),
      'general':("Let's talk about what you need.","Whether you're a company or an emerging professional, we'll point you to the right place — within 48 hours.","Talk to us","contact.html"),
    }
    h,p,cta,href=conf.get(kind,conf['general'])
    return ('<section class="bg-brandNavy text-white py-20"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 text-center reveal">'
      '<h2 class="hd2 text-white mb-4">%s</h2>'
      '<p class="lead text-slate-300 max-w-2xl mx-auto mb-8">%s</p>'
      '<a class="inline-flex items-center gap-2 bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold px-8 py-4 transition-colors" href="%s">%s <span class="material-symbols-outlined text-[18px]" aria-hidden="true">arrow_forward</span></a>'
      '</div></section>')%(h,p,href,cta)

def industries():
    inds=["Manufacturing","SaaS","Education","Professional Services","Growing Businesses"]
    pills=''.join('<span class="px-4 py-2 bg-white border border-borderLine text-sm font-display font-medium text-brandNavy card-lift">%s</span>'%i for i in inds)
    return ('<section class="bg-paperBg py-16 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
      '<p class="cap text-slate-500 mb-5 reveal">Industries we serve</p><div class="flex flex-wrap gap-3 stagger reveal">%s</div></div></section>') % pills

def hero_big(eb, h, sub, ctas):
    btns=''
    for label,href,prim in ctas:
        if prim: btns+='<a class="bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold px-7 py-3.5 transition-colors inline-flex items-center gap-2" href="%s">%s <span class="material-symbols-outlined text-[18px]" aria-hidden="true">arrow_forward</span></a>'%(href,label)
        else: btns+='<a class="border border-white/30 hover:border-white hover:bg-white/5 text-white text-sm font-semibold px-7 py-3.5 transition-colors" href="%s">%s</a>'%(href,label)
    return ('<section class="relative bg-brandNavy text-white overflow-hidden"><div class="absolute inset-0 glow pointer-events-none"></div>'
      '<div class="absolute inset-0 gridlines opacity-60 pointer-events-none"></div>'
      '<div class="relative max-w-[1440px] mx-auto px-6 lg:px-12 pt-16 lg:pt-28 pb-16 lg:pb-24 herofade">'
      '<span class="cap text-brandTeal block mb-5">%s</span>'
      '<h1 class="font-display font-bold text-white tracking-[-0.02em] max-w-[16ch]" style="font-size:clamp(40px,7vw,84px);line-height:1.02">%s</h1>'
      '<p class="lead text-slate-300 max-w-2xl mt-8">%s</p>'
      '<div class="flex flex-wrap gap-4 mt-9">%s</div>'
      '</div></section>') % (eb,h,sub,btns)

def hero_chips(eb, h, sub, ctas, chips):
    btns=''
    for label,href,prim in ctas:
        if prim: btns+='<a class="bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold px-7 py-3.5 transition-colors inline-flex items-center gap-2" href="%s">%s <span class="material-symbols-outlined text-[18px]" aria-hidden="true">arrow_forward</span></a>'%(href,label)
        else: btns+='<a class="border border-white/30 hover:border-white hover:bg-white/5 text-white text-sm font-semibold px-7 py-3.5 transition-colors" href="%s">%s</a>'%(href,label)
    chiprow=''.join('<div class="flex items-center gap-2.5"><span class="w-9 h-9 rounded-lg bg-white/5 border border-white/10 grid place-items-center text-brandTeal shrink-0"><span class="material-symbols-outlined text-[18px]" aria-hidden="true">%s</span></span><span class="text-sm font-display font-semibold text-white">%s</span></div>'%(ic,label) for ic,label in chips)
    return ('<section class="relative bg-brandNavy text-white overflow-hidden"><div class="absolute inset-0 glow pointer-events-none"></div>'
      '<div class="absolute inset-0 gridlines opacity-60 pointer-events-none"></div>'
      '<div class="relative max-w-[1000px] mx-auto px-6 lg:px-12 pt-14 lg:pt-20 pb-14 lg:pb-16 text-center herofade">'
      '<span class="cap text-brandTeal block mb-4">%s</span>'
      '<h1 class="hd1 text-white mb-6">%s</h1>'
      '<p class="lead text-slate-300 max-w-2xl mx-auto mb-8">%s</p>'
      '<div class="flex flex-wrap gap-4 justify-center">%s</div>'
      '<div class="mt-12 flex flex-wrap justify-center gap-x-8 gap-y-4 reveal">%s</div>'
      '</div></section>') % (eb,h,sub,btns,chiprow)

def hero(eb, h, sub, ctas, illo=None, funcs=False):
    fn=''
    if funcs:
        pills=''.join('<span class="px-3 py-1 bg-white/5 border border-white/10 text-slate-300 cap text-[11px]">%s</span>'%x for x in ["Sales","Marketing","Operations","HR","Technology"])
        fn=('<div class="pt-6 border-t border-white/10 mt-10"><span class="cap text-slate-400 block mb-3">We execute across</span>'
            '<div class="flex flex-wrap gap-2">%s</div></div>'%pills)
    btns=''
    for i,(label,href,prim) in enumerate(ctas):
        if prim: btns+='<a class="bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold px-7 py-3.5 transition-colors inline-flex items-center gap-2" href="%s">%s <span class="material-symbols-outlined text-[18px]" aria-hidden="true">arrow_forward</span></a>'%(href,label)
        else: btns+='<a class="border border-white/30 hover:border-white hover:bg-white/5 text-white text-sm font-semibold px-7 py-3.5 transition-colors" href="%s">%s</a>'%(href,label)
    if illo:
        col='<div class="hidden lg:flex items-center justify-center herofade" style="animation-delay:.18s">%s</div>'%illo
        grid='<div class="relative max-w-[1440px] mx-auto px-6 lg:px-12 pt-12 lg:pt-16 pb-14 lg:pb-20 grid lg:grid-cols-2 gap-12 items-center"><div class="max-w-2xl herofade">%s</div>%s</div>'
        inner=('<div class="inline-flex items-center gap-2 px-3 py-1 bg-white/5 border border-white/15 text-brandTeal cap mb-6"><span class="w-1.5 h-1.5 bg-brandTeal inline-block"></span> %s</div>'
          '<h1 class="hd1 text-white mb-6">%s</h1><p class="lead text-slate-300 mb-8">%s</p><div class="flex flex-wrap gap-4">%s</div>%s'%(eb,h,sub,btns,fn))
        return ('<section class="relative bg-brandNavy text-white overflow-hidden"><div class="absolute inset-0 glow pointer-events-none"></div>'
          '<div class="absolute inset-0 gridlines opacity-60 pointer-events-none"></div>'+(grid%(inner,col))+'</section>')
    return ('<section class="relative bg-brandNavy text-white overflow-hidden"><div class="absolute inset-0 glow pointer-events-none"></div>'
      '<div class="absolute inset-0 gridlines opacity-60 pointer-events-none"></div>'
      '<div class="relative max-w-[1440px] mx-auto px-6 lg:px-12 pt-12 lg:pt-16 pb-14 lg:pb-16"><div class="max-w-3xl herofade">'
      '<div class="inline-flex items-center gap-2 px-3 py-1 bg-white/5 border border-white/15 text-brandTeal cap mb-6">'
      '<span class="w-1.5 h-1.5 bg-brandTeal inline-block"></span> %s</div>'
      '<h1 class="hd1 text-white mb-6">%s</h1><p class="lead text-slate-300 max-w-2xl mb-8">%s</p>'
      '<div class="flex flex-wrap gap-4">%s</div>%s</div></div></section>' % (eb,h,sub,btns,fn))

def caps_detailed():
    data=[("show_chart","Sales","Prospecting, outreach cadences, demo booking, deal follow-up and CRM hygiene — aligned to your existing targets."),
          ("campaign","Marketing","Campaign execution, content production, channel management and reporting straight into your team."),
          ("account_tree","Operations","Daily coordination, process running, vendor and task management — keeping work moving without gaps."),
          ("groups","HR","Sourcing, screening, onboarding and people-ops support, on your standards and your timeline."),
          ("terminal","Technology","Websites, internal tools, integrations and product work — including the platforms we build ourselves.")]
    cards=''
    for ic,n,d in data:
        cards+=('<div class="bg-white border border-borderLine p-7 card-lift flex gap-5 items-start">'
          '<span class="w-11 h-11 shrink-0 bg-brandTealTint text-brandTealDark grid place-items-center"><span class="material-symbols-outlined" aria-hidden="true">%s</span></span>'
          '<div><h3 class="hd3 text-brandNavy mb-1.5" style="font-size:19px">%s</h3><p class="text-[15px] leading-relaxed text-slate-600 leading-relaxed">%s</p></div></div>'%(ic,n,d))
    return '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 stagger reveal">%s</div>'%cards

def journey():
    steps=[("Tell us the work","A single capability or a combined requirement — in your words."),
      ("We capture the essentials","Company, role, the core problem, team size and timeline, with consent."),
      ("We classify the need","Execution support, one of our products, or both."),
      ("Discovery conversation","We define scope, dependencies, the commercial path and success measures."),
      ("A matched plan","An Execute, Grow or Transform engagement, sized to the outcome."),
      ("Kick off","Access, data handling and a working cadence — set after a formal agreement.")]
    items=''
    for i,(h,p) in enumerate(steps):
        items+=('<div class="flex gap-5 group"><div class="shrink-0 w-10 h-10 bg-brandNavy group-hover:bg-brandTeal transition-colors text-white grid place-items-center font-display font-bold text-sm">%02d</div>'
          '<div class="pb-5 border-b border-borderLine flex-1"><h3 class="hd3 text-brandNavy mb-1" style="font-size:18px">%s</h3><p class="text-slate-600">%s</p></div></div>'%(i+1,h,p))
    return '<div class="max-w-3xl space-y-5 stagger reveal">%s</div>'%items

def why_cards():
    data=[("bolt","Delivery, not slideware","We run the work and report back — you get outcomes, not a deck."),
      ("dashboard","Embedded like your team","We work inside your systems, tools and standards, not from the outside."),
      ("hub","One partner, five functions","Sales, Marketing, Operations, HR and Technology from a single team."),
      ("terminal","We build our own products","Real technical capability, shipped — Bispun, Perfoin and more."),
      ("verified","Honest scope","We state intended value and stand behind what we actually deliver."),
      ("schedule","No long ramp","We embed fast and start moving work, not onboarding for months.")]
    cards=''
    for ic,h,p in data:
        cards+=('<div class="bg-white border border-borderLine p-6 card-lift"><span class="material-symbols-outlined text-brandTeal mb-4 block" aria-hidden="true">%s</span>'
          '<h3 class="hd3 text-brandNavy mb-2" style="font-size:18px">%s</h3><p class="text-[15px] leading-relaxed text-slate-600 leading-relaxed">%s</p></div>'%(ic,h,p))
    return '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 stagger reveal">%s</div>'%cards

def services_detailed():
    data=[("filter_alt","Lead Generation","Build a relevant prospect pipeline through research, outreach and campaign execution.","A qualified pipeline you can sell to."),
      ("call","Sales Support","Improve follow-up, qualification, demo coordination and CRM discipline.","Booked meetings and follow-through to close."),
      ("campaign","Marketing Execution","Keep campaigns, content and channels moving consistently.","Consistent presence and inbound interest."),
      ("account_tree","Operations Systems","Create smoother processes, cleaner workflows and better execution visibility.","Processes that run without gaps."),
      ("rocket_launch","Business Scaling","Turn early traction into a repeatable operating rhythm.","Momentum that compounds.")]
    cards=''
    for i,(ic,n,d,out) in enumerate(data):
        cards+=('<div class="group bg-white border border-borderLine p-7 card-lift hover:border-brandTeal transition-colors">'
          '<div class="flex items-center justify-between mb-5"><span class="w-11 h-11 bg-brandTealTint text-brandTealDark group-hover:bg-brandTeal group-hover:text-white transition-colors grid place-items-center"><span class="material-symbols-outlined" aria-hidden="true">%s</span></span>'
          '<span class="font-display font-bold" style="font-size:22px;color:#DCE3EA">%02d</span></div>'
          '<h3 class="hd3 text-brandNavy mb-2" style="font-size:19px">%s</h3><p class="text-slate-600 mb-4">%s</p>'
          '<div class="pt-4 border-t border-borderLine flex items-start gap-2"><span class="material-symbols-outlined text-brandTeal text-[18px] mt-0.5" aria-hidden="true">arrow_outward</span><span class="text-sm font-display font-semibold text-brandNavy">%s</span></div></div>'%(ic,i+1,n,d,out))
    return '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 stagger reveal">%s</div>'%cards

def how_engagement():
    steps=[("01","Start with one service","Pick the service that unblocks you now. We scope it and embed fast."),
      ("02","We run it and report","We execute inside your tools and report results into your team."),
      ("03","Expand as it works","Grow across functions, or bring in our products where they help — no long lock-ins.")]
    sc=''.join('<div class="border border-borderLine p-8 bg-white card-lift"><div class="w-full h-1 bg-brandTeal mb-6"></div><span class="cap text-brandTeal font-bold">STEP %s</span><h3 class="hd3 text-brandNavy mt-2 mb-3" style="font-size:20px">%s</h3><p class="text-slate-600">%s</p></div>'%(i,h,p) for i,h,p in steps)
    return '<div class="grid grid-cols-1 md:grid-cols-3 gap-8 stagger reveal">%s</div>'%sc

def wowers_work():
    data=[("trending_up","Lead generation & outreach","Real prospecting and campaigns for partner companies."),
      ("call","Sales & growth support","Telecalling, follow-ups, CRM and demo coordination."),
      ("campaign","Marketing & operations","Content, campaigns and process work that actually ships."),
      ("terminal","Product & tech projects","Hands-on work on real tools and platforms.")]
    cards=''
    for ic,h,p in data:
        cards+=('<div class="bg-white border border-borderLine p-6 card-lift"><span class="material-symbols-outlined text-brandTeal mb-4 block" aria-hidden="true">%s</span><h3 class="hd3 text-brandNavy mb-2" style="font-size:17px">%s</h3><p class="text-[15px] leading-relaxed text-slate-600">%s</p></div>'%(ic,h,p))
    return '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 stagger reveal">%s</div>'%cards

def faq(items):
    rows=''.join('<details class="border border-borderLine bg-white group"><summary class="cursor-pointer list-none flex justify-between items-center gap-4 p-5 font-display font-semibold text-brandNavy">%s<span class="material-symbols-outlined text-brandTeal transition-transform group-open:rotate-45" aria-hidden="true">add</span></summary><div class="px-5 pb-5 text-slate-600">%s</div></details>'%(q,a) for q,a in items)
    return '<div class="max-w-3xl mx-auto space-y-3 reveal">%s</div>'%rows

def testimonials():
    data=[("Siri","Working on real projects helped me understand how professional software teams plan, build and improve products."),
      ("Abhigna","Woways gave me the opportunity to learn through execution—not only through theory. I became more confident in building practical solutions."),
      ("Santoshi","Every task came with ownership and learning. The experience helped me understand how technology supports real business work."),
      ("Shreelakshmi","I learned how collaboration, consistency and attention to detail turn an idea into a product people can use.")]
    cards=''
    for n,q in data:
        cards+=('<div class="bg-white border border-borderLine p-7 card-lift flex flex-col">'
          '<span class="text-brandTeal font-display font-bold leading-none mb-2" style="font-size:44px" aria-hidden="true">“</span>'
          '<p class="text-slate-700 leading-relaxed flex-1">%s</p>'
          '<div class="flex items-center gap-3 mt-6 pt-5 border-t border-borderLine">'
          '<span class="w-10 h-10 rounded-full bg-brandNavy text-white grid place-items-center font-display font-bold text-sm">%s</span>'
          '<div><div class="font-display font-semibold text-brandNavy text-sm">%s</div><div class="text-xs text-slate-500">Software Developer Intern</div></div></div></div>'%(q,n[0],n))
    return '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 stagger reveal">%s</div>'%cards

def impact_stats(dark=False):
    stats=[("300","+","Wowers trained"),("25","+","Companies partnered"),("59675","+","Leads generated"),("125","+","Projects executed")]
    num='text-white' if dark else 'text-brandNavy'
    lab='text-slate-400' if dark else 'text-slate-500'
    div='md:border-l md:border-white/10' if dark else 'md:border-l md:border-borderLine'
    st=''
    for i,(v,suf,l) in enumerate(stats):
        edge='' if i==0 else div
        disp='{:,}'.format(int(v))
        st+=('<div class="text-center px-2 %s"><div class="font-display font-bold %s" style="font-size:clamp(30px,4.6vw,46px);letter-spacing:-0.02em">'
          '<span class="countup" data-to="%s">%s</span>%s</div><div class="cap %s mt-2">%s</div></div>'%(edge,num,v,disp,suf,lab,l))
    return '<div class="grid grid-cols-2 md:grid-cols-4 gap-y-8 reveal">%s</div>'%st

def credibility_strip():
    faces=[("jagadishwar-reddy.jpg","Jagadishwar Reddy"),("vihang.jpg","Vihang Gunnam"),
      ("bhargav-chowdary.jpg","Durga Bhargav Chowdary Kotha"),("rohit-karre.jpg","Rohit Karre"),
      ("omkareshwar-boda.jpg","Omkareshwar Boda")]
    av=''.join('<img src="m/%s" alt="%s" loading="lazy" class="w-10 h-10 rounded-full object-cover border-2 border-brandNavy ring-1 ring-white/25 -ml-3 first:ml-0"/>'%(f,n) for f,n in faces)
    return ('<section class="bg-brandNavy py-6 border-b border-white/10"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 flex flex-col sm:flex-row items-center sm:items-center gap-4 sm:gap-6 reveal">'
      '<div class="flex items-center shrink-0" aria-hidden="true">%s</div>'
      '<div class="text-center sm:text-left"><div class="text-white text-sm md:text-base font-display font-semibold">Built by IIT alumni and industry operators</div>'
      '<div class="text-slate-300 text-sm md:text-base">Mentors from Microsoft, Deloitte, PwC, KPMG and Accenture</div></div>'
      '</div></section>') % av

MENTOR_DATA=[("Nambi Diwakar","Microsoft, USA","nambi-diwakar.jpg","org-microsoft.png","Microsoft"),
  ("Beldari Lakshmi Sree","Structural Design Engineer, Dar Al-Handasah","lakshmi-sree.jpg","org-dar-al-handasah.svg","Dar Al-Handasah"),
  ("Udaya Sri Kumari Pamugari","Consultant, Workday Integrations, Deloitte","udaya-sri.jpg","org-deloitte.png","Deloitte"),
  ("Madhuvanthi Sankalkar","Software Engineer, Rakuten India","madhuvanthi.jpg","org-rakuten.svg","Rakuten"),
  ("Punugu Jayanth Reddy","Consultant, KPMG","jayanth-reddy.jpg","org-kpmg.svg","KPMG"),
  ("Rishitha Reddy Guddeti","Quality Engineering Analyst, Accenture","rishitha-reddy.jpg","org-accenture.svg","Accenture"),
  ("Bhargav Reddy Perugu","AML Analyst, PwC","bhargav-reddy.jpg","org-pwc.svg","PwC"),
  ("Jagadishwar Reddy","Curriculum Coordinator & Educator","jagadishwar-reddy.jpg",None,None),
  ("Sarath Chandra Reddy Yemma","Verizon Data Services","sarath-yemma.jpg","org-verizon.svg","Verizon"),
  ("Wilson Teja","FWAI, India","wilson-teja.jpg","org-fwai.png","FWAI"),
  ("Vihang Gunnam","Founder & Director, Prakara Learning","vihang.jpg","org-prakara-learning.png","Prakara Learning"),
  ("Durga Bhargav Chowdary Kotha","Founder & Community Builder","bhargav-chowdary.jpg","org-bhargav-community.png","Community"),
  ("Rohit Karre","General Manager, DocTutorials","rohit-karre.jpg","org-doctutorials.png","DocTutorials"),
  ("Gouse Lazam Shaik","Managing Director, AG Elevators & Zyrolifts","gouse-lazam-shaik.jpg","org-zyrolifts.png","Zyrolifts"),
  ("Magdumbi Shaik","Chief Sales Officer, Zyrolifts","magdumbi-shaik.jpg","org-zyrolifts.png","Zyrolifts"),
  ("Omkareshwar Boda","Regional Head, AP & TS, NxtWave","omkareshwar-boda.jpg","org-nxtwave.png","NxtWave"),
  ("C. Latha Prakash","Educator, CBSE National Awardee","latha-prakash.jpg","org-cbse.png","CBSE"),
  ("Peddamale Chetan","Educator & Associate NCC Officer","chetan.jpg","org-ncc.png","NCC")]

def mentors():
    cards=''
    for n,r,a,logo,org in MENTOR_DATA:
        if logo:
            logo_html='<div class="mt-4 pt-4 border-t border-borderLine flex items-center justify-center h-10"><img src="m/%s" alt="%s" loading="lazy" class="max-h-6 max-w-[110px] w-auto object-contain"/></div>'%(logo,org)
        else:
            logo_html='<div class="mt-4 pt-4 border-t border-borderLine flex items-center justify-center h-10"><span class="cap text-slate-400">Educator</span></div>'
        cards+=('<div class="snap-start shrink-0 w-[240px] bg-white border border-borderLine card-lift overflow-hidden flex flex-col">'
          '<div class="aspect-[4/3] overflow-hidden bg-paperDim"><img src="m/%s" alt="%s" loading="lazy" class="w-full h-full object-cover object-top"/></div>'
          '<div class="p-5 text-center flex-1 flex flex-col"><div class="font-display font-semibold text-brandNavy text-[15px] leading-tight">%s</div>'
          '<div class="text-xs text-slate-500 mt-2 leading-snug flex-1">%s</div>%s</div></div>'%(a,n,n,r,logo_html))
    arrow=('<button type="button" aria-label="%s" onclick="document.getElementById(\'mscroll\').scrollBy({left:%d,behavior:\'smooth\'})" '
      'class="absolute %s top-1/2 -translate-y-1/2 z-10 w-10 h-10 rounded-full bg-white border border-borderLine shadow-md grid place-items-center text-brandNavy hover:bg-brandNavy hover:text-white transition-colors">'
      '<span class="material-symbols-outlined" aria-hidden="true">%s</span></button>')
    left=arrow%("Previous mentors",-520,"left-0 lg:-left-2","chevron_left")
    right=arrow%("Next mentors",520,"right-0 lg:-right-2","chevron_right")
    return ('<div class="relative reveal">%s%s'
      '<div id="mscroll" class="flex gap-5 overflow-x-auto snap-x scroll-smooth pb-4 px-1 [scrollbar-width:none] [-ms-overflow-style:none]" style="scrollbar-width:none">%s</div></div>'
      '<style>#mscroll::-webkit-scrollbar{display:none}</style>'
      '<p class="mt-6 reveal text-center" style="font-style:italic;color:#6B7C93;font-size:12px">Company names indicate where our mentors work and are trademarks of their respective owners.</p>'%(left,right,cards))

def problem_solve():
    comp=["Generating qualified leads","Building sales pipelines","Scaling operations cost-effectively"]
    wow=["Lack of real experience","Difficulty getting internships","Limited job opportunities"]
    def col(title,items,color):
        li=''.join('<div class="flex gap-4 items-start"><span class="font-display font-bold text-%s shrink-0" style="font-size:15px">%02d</span><span class="text-slate-700">%s</span></div>'%(color,i+1,x) for i,x in enumerate(items))
        return '<div class="bg-white border border-borderLine p-8"><h3 class="hd3 text-brandNavy mb-6" style="font-size:20px">%s</h3><div class="space-y-4">%s</div></div>'%(title,li)
    return '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 reveal">%s%s</div>'%(col("Companies struggle with",comp,"brandTealDark"),col("Wowers struggle with",wow,"brandOrangeDark"))

def wower_pathway():
    steps=[("Join","Become part of the Woways talent ecosystem and begin your professional journey."),
      ("Learn","Go through structured induction, training and practical learning aligned with business requirements."),
      ("Execute","Work on real projects across functions such as Sales, Marketing, Operations, HR, Technology and Digital Business."),
      ("Perform","Demonstrate your skills, ownership, commitment, professionalism and ability to deliver measurable outcomes."),
      ("Grow","Your performance can open pathways to PPO opportunities, jobs with potential packages, extended internships and other career opportunities.")]
    sc=''.join('<div class="border border-borderLine p-6 bg-white card-lift text-left"><div class="flex items-center gap-3 mb-4"><div class="w-10 h-10 bg-brandTeal text-white grid place-items-center font-display font-bold shrink-0">%02d</div><h3 class="hd3 text-brandNavy" style="font-size:17px">%s</h3></div><p class="text-[15px] leading-relaxed text-slate-600 leading-relaxed">%s</p></div>'%(i+1,h,p) for i,(h,p) in enumerate(steps))
    return '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 stagger reveal">%s</div>'%sc

def ecosystem_model():
    steps=[("Companies","brandTeal","Companies partner with us"),("Woways","brandNavy","We build lead pipelines"),
      ("Wowers","brandOrangeDark","Wowers work on real projects"),("Woways","brandNavy","Sales & growth execution"),
      ("Companies","brandTeal","Companies generate revenue"),("Wowers","brandOrangeDark","Wowers gain experience & income")]
    sc=''
    for i,(who,c,txt) in enumerate(steps):
        sc+='<div class="bg-white border border-borderLine p-5 card-lift"><div class="flex items-center gap-3 mb-2"><span class="w-7 h-7 bg-%s text-white grid place-items-center font-display font-bold text-xs shrink-0">%02d</span><span class="cap text-slate-500">%s</span></div><p class="text-slate-700 text-sm">%s</p></div>'%(c,i+1,who,txt)
    return '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 stagger reveal">%s</div>'%sc

def inspiration():
    return ('<section class="bg-brandNavy py-16 lg:py-20"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
      '<div class="max-w-4xl mx-auto grid grid-cols-1 md:grid-cols-[auto_1fr] gap-8 md:gap-10 items-center reveal">'
      '<img src="m/bhaskar-rao.jpg" alt="Dr. B. Bhaskar Rao" loading="lazy" class="w-32 h-32 md:w-40 md:h-40 rounded-full object-cover object-top border-2 border-brandTeal/40 mx-auto"/>'
      '<div class="text-center md:text-left"><span class="cap text-brandTeal block mb-4">Our inspiration</span>'
      '<p class="font-display text-white" style="font-size:clamp(20px,2.8vw,28px);line-height:1.4;letter-spacing:-0.02em">“Inspired by a vision to empower people, bridge the employability gap, and contribute to a stronger, future-ready India.”</p>'
      '<div class="mt-6"><div class="font-display font-semibold text-white">Dr. B. Bhaskar Rao</div>'
      '<div class="text-sm text-slate-400 mt-1">Managing Director &amp; Senior Consultant</div></div></div></div></div></section>')

def core_team():
    data=[("workspace_premium","Significant industry experience","Our core team brings strong experience across key sectors, with deep exposure to real-world business environments."),
      ("bolt","Execution-driven mindset","Built with a practical understanding of how businesses operate and execute — not theory, delivery.")]
    cards=''.join('<div class="bg-paperBg border border-borderLine p-8 card-lift"><span class="material-symbols-outlined text-brandTeal mb-4 block" aria-hidden="true">%s</span><h3 class="hd3 text-brandNavy mb-2" style="font-size:20px">%s</h3><p class="text-slate-600 leading-relaxed">%s</p></div>'%(ic,h,p) for ic,h,p in data)
    return '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 stagger reveal">%s</div>'%cards

def where_today():
    pts=["We are currently working with early-stage and growing companies.",
      "We are building outreach systems that deliver repeatable results.",
      "We focus on measurable outcomes — meetings booked, leads generated, pipelines built."]
    items=''.join('<div class="flex gap-5 reveal"><div class="shrink-0 w-10 h-10 bg-brandNavy text-white grid place-items-center font-display font-bold text-sm">%02d</div><div class="pb-5 border-b border-borderLine flex-1 self-center"><p class="text-slate-700 text-lg">%s</p></div></div>'%(i+1,x) for i,x in enumerate(pts))
    return '<div class="max-w-3xl space-y-5">%s</div>'%items

def hero_cards(items):
    # floating stat cards, scattered and gently animated (reference: Active Theory)
    pos=['top-0 left-0','top-14 right-0','bottom-6 left-8','bottom-0 right-6']
    cards=''
    for i,(ic,label,val,trend) in enumerate(items[:4]):
        sub='<div class="text-xs text-brandTeal mt-1 flex items-center gap-1"><span class="material-symbols-outlined text-[14px]" aria-hidden="true">trending_up</span>%s</div>'%trend if trend else ''
        cards+=('<div class="floaty absolute %s w-[220px] rounded-xl border border-white/12 bg-white/[0.06] backdrop-blur px-4 py-3.5 shadow-[0_26px_55px_-26px_rgba(0,0,0,.8)]" style="animation-delay:%.1fs">'
          '<div class="flex items-center gap-2 mb-1"><span class="material-symbols-outlined text-brandTeal text-[18px]" aria-hidden="true">%s</span><span class="cap text-slate-400">%s</span></div>'
          '<div class="font-display font-bold text-white leading-none" style="font-size:26px">%s</div>%s</div>'%(pos[i],i*0.8,ic,label,val,sub))
    return '<div class="relative w-full max-w-[440px] h-[380px] mx-auto">%s</div>'%cards

_VDEFS=('<defs><filter id="vg" x="-50%" y="-50%" width="200%" height="200%">'
  '<feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
  '<radialGradient id="vc" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#00A9A9" stop-opacity=".9"/><stop offset="100%" stop-color="#00A9A9" stop-opacity="0"/></radialGradient></defs>')

def _svg(inner, label):
    return ('<svg viewBox="0 0 400 400" class="w-full max-w-[460px] mx-auto" role="img" aria-label="%s">%s%s</svg>'%(label,_VDEFS,inner))

def viz_orbit():
    # Home — execution orbit with our five functions as nodes
    import math
    rings='<circle cx="200" cy="200" r="150" fill="none" stroke="rgba(255,255,255,.08)"/><circle cx="200" cy="200" r="95" fill="none" stroke="rgba(0,169,169,.28)"/>'
    funcs=[("Sales",-90),("Marketing",-18),("Operations",54),("Technology",126),("People",198)]
    spokes=''; nodes=''
    for i,(name,ang) in enumerate(funcs):
        a=math.radians(ang); r=150
        x=200+r*math.cos(a); y=200+r*math.sin(a)
        lx=200+(r+2)*math.cos(a); ly=200+(r+2)*math.sin(a)
        anchor='middle'
        if math.cos(a)>0.3: anchor='start'
        elif math.cos(a)<-0.3: anchor='end'
        dy = -12 if math.sin(a)<-0.3 else (20 if math.sin(a)>0.3 else 4)
        spokes+='<line x1="200" y1="200" x2="%.0f" y2="%.0f" stroke="rgba(0,169,169,.20)" stroke-width="1"/>'%(x,y)
        nodes+=('<circle cx="%.0f" cy="%.0f" r="7" fill="#0A1830" stroke="#00A9A9" stroke-width="2"><animate attributeName="r" values="7;9;7" dur="%ss" begin="%ss" repeatCount="indefinite"/></circle>'
          '<text x="%.0f" y="%.0f" text-anchor="%s" font-family="Hanken Grotesk,sans-serif" font-size="12" font-weight="600" fill="rgba(255,255,255,.85)" dy="%d">%s</text>'%(x,y,3+i*0.3,i*0.4,lx,ly,anchor,dy,name))
    orbit='<g><animateTransform attributeName="transform" type="rotate" from="0 200 200" to="360 200 200" dur="46s" repeatCount="indefinite"/><circle cx="295" cy="200" r="4" fill="#E8A33D"/></g>'
    core=('<circle cx="200" cy="200" r="46" fill="url(#vc)" opacity=".45"/>'
      '<circle cx="200" cy="200" r="30" fill="#0A1830" stroke="#00A9A9" stroke-width="1.5"/>'
      '<path d="M186 200 l8 9 18 -20" fill="none" stroke="#00A9A9" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>'
      '<circle cx="200" cy="200" r="30" fill="none" stroke="#00A9A9" stroke-width="1.5"><animate attributeName="r" values="30;150;30" dur="6s" repeatCount="indefinite"/><animate attributeName="opacity" values=".55;0;.55" dur="6s" repeatCount="indefinite"/></circle>')
    return _svg(rings+spokes+orbit+nodes+core,"Woways execution across five functions")

def viz_network():
    # Companies — connected node graph
    nodes=[(80,120),(200,80),(320,140),(120,260),(260,280),(200,180)]
    lines=[(0,1),(1,2),(0,5),(1,5),(2,5),(3,5),(4,5),(3,0),(4,2)]
    ln=''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="rgba(0,169,169,.25)" stroke-width="1"/>'%(nodes[a][0],nodes[a][1],nodes[b][0],nodes[b][1]) for a,b in lines)
    nd=''
    for i,(x,y) in enumerate(nodes):
        r=10 if i==5 else 6
        col='#00A9A9' if i==5 else ('#E8A33D' if i in (1,4) else '#7FD9D6')
        nd+=('<circle cx="%d" cy="%d" r="%d" fill="%s"><animate attributeName="opacity" values=".55;1;.55" dur="%ss" begin="%ss" repeatCount="indefinite"/></circle>'%(x,y,r,col,3+i*0.3,i*0.4))
    pulse='<circle cx="200" cy="180" r="10" fill="none" stroke="#00A9A9"><animate attributeName="r" values="10;70;10" dur="5s" repeatCount="indefinite"/><animate attributeName="opacity" values=".7;0;.7" dur="5s" repeatCount="indefinite"/></circle>'
    return _svg(ln+pulse+nd,"An embedded team, connected")

def viz_growth():
    # Wowers — an ascending path with a travelling marker
    path='M40 320 C 120 300, 150 220, 210 200 S 300 140, 360 70'
    base='<path d="%s" fill="none" stroke="rgba(255,255,255,.12)" stroke-width="2"/>'%path
    prog=('<path d="%s" fill="none" stroke="#00A9A9" stroke-width="3" stroke-linecap="round" stroke-dasharray="520" stroke-dashoffset="520">'
      '<animate attributeName="stroke-dashoffset" values="520;0" dur="3s" fill="freeze"/></path>'%path)
    steps=''.join('<circle cx="%d" cy="%d" r="5" fill="#0A1830" stroke="#00A9A9" stroke-width="2"><animate attributeName="r" values="5;7;5" dur="2.4s" begin="%ss" repeatCount="indefinite"/></circle>'%(x,y,b) for x,y,b in [(40,320,0),(140,262,.4),(210,200,.8),(300,132,1.2),(360,70,1.6)])
    marker=('<circle r="6" fill="#E8A33D" filter="url(#vg)"><animateMotion path="%s" dur="4s" repeatCount="indefinite"/></circle>'%path)
    glow='<circle cx="360" cy="70" r="30" fill="url(#vc)" opacity=".5"/>'
    return _svg(base+prog+glow+steps+marker,"Learn, execute, perform, grow")

def viz_rings():
    # Services — concentric pulse rings
    r=''.join('<circle cx="200" cy="200" r="30" fill="none" stroke="#00A9A9" stroke-width="1.5"><animate attributeName="r" values="30;170" dur="4s" begin="%ss" repeatCount="indefinite"/><animate attributeName="opacity" values=".7;0" dur="4s" begin="%ss" repeatCount="indefinite"/></circle>'%(b,b) for b in [0,1,2,3])
    dots=''.join('<circle cx="%d" cy="%d" r="4" fill="%s"/>'%(200+int(120* (1 if i%2 else -1) * (0.5+0.1*i)),200+int(90*((-1)**i)*(0.4+0.12*i)),'#E8A33D' if i%3==0 else '#7FD9D6') for i in range(5))
    core=('<circle cx="200" cy="200" r="34" fill="#0A1830" stroke="#00A9A9" stroke-width="1.5"/>'
      '<path d="M186 200 l8 9 18 -20" fill="none" stroke="#00A9A9" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>')
    return _svg(r+dots+core,"Services radiating from one team")

def viz_constellation():
    # About — star map with faint links
    pts=[(70,90),(150,60),(250,90),(330,70),(110,180),(210,160),(300,190),(80,290),(180,300),(290,300),(350,240)]
    links=[(0,1),(1,2),(2,3),(0,4),(4,5),(5,6),(6,3),(4,7),(7,8),(8,9),(9,10),(5,8),(6,10)]
    ln=''.join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="rgba(255,255,255,.08)" stroke-width="1"/>'%(pts[a][0],pts[a][1],pts[b][0],pts[b][1]) for a,b in links)
    nd=''.join('<circle cx="%d" cy="%d" r="%s" fill="%s"><animate attributeName="opacity" values=".3;1;.3" dur="%ss" begin="%ss" repeatCount="indefinite"/></circle>'%(x,y,(3 if i in(5,) else 2),'#00A9A9' if i in(5,2,8) else ('#E8A33D' if i in(1,10) else '#cfe'),3+ (i%4),i*0.3) for i,(x,y) in enumerate(pts))
    return _svg(ln+nd,"A connected ecosystem")

# ================= PAGES =================
def build_index():
    b = hero("Execution partner · Talent ecosystem","Build momentum without building everything alone.",
        "Woways gives growing companies an execution layer across sales, marketing, operations, technology and people functions. At the same time, we prepare emerging professionals through meaningful, real-world work.<br class=\"hidden sm:block\"/><span class=\"inline-block mt-4 text-white font-semibold\">Not advice. Delivery.</span>",
        [("Talk about your business need","partnerships.html#partner-form",True),("Explore the Wower pathway","wowers.html",False)],
        illo=viz_orbit())
    b += credibility_strip()
    b += '<section class="bg-brandNavy py-14 lg:py-16 border-b border-white/10"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += '<p class="cap text-slate-400 mb-8 text-center reveal">Our impact</p>'
    b += impact_stats(dark=True) + '</div></section>'
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("The problem we solve","Two sides of the same gap.","Companies need execution and pipeline. Talent needs real experience. We connect the two.")
    b += problem_solve() + '</div></section>'
    b += '<section class="bg-paperBg py-16 lg:py-20 border-b border-borderLine" id="capabilities"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("What we do","An added execution layer across your core functions.","Woways works alongside partnered companies as an added execution layer — taking on the day-to-day work across five functions, the way an internal team would.")
    b += caps_grid()
    b += '<div class="mt-10 reveal"><a class="inline-flex items-center gap-2 bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold px-7 py-3.5 transition-colors grp" href="companies.html">See the executive partnership <span class="material-symbols-outlined text-[18px] arrow-move" aria-hidden="true">arrow_forward</span></a></div></div></section>'
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine" id="how"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("How we work","Execute. Grow. Transform.","Every engagement moves through the same three stages — it's the reason clients bring us in, and the reason we stay.")
    b += egt() + '</div></section>'
    b += '<section class="bg-paperBg py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("The ecosystem model","How the loop works.","Woways connects industry needs with emerging talent and execution capabilities — a virtuous cycle.")
    b += ecosystem_model() + '</div></section>'
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine" id="products"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Our products","One execution partner. Five focused products.","Software built by Woways — for education and career growth, and for running businesses.")
    b += '<div class="flex items-center gap-3 mb-6 reveal"><span class="cap text-slate-500">Education &amp; Career</span><div class="h-px bg-borderLine flex-1"></div></div>' + product_cards('edu')
    b += '<div class="flex items-center gap-3 mb-6 mt-12 reveal"><span class="cap text-slate-500">Business Visibility &amp; Execution</span><div class="h-px bg-borderLine flex-1"></div></div>' + product_cards('biz')
    b += '</div></section>'
    b += industries()
    # WOWER — full-width text section (For Wowers)
    b += ('<section class="relative bg-brandNavy text-white overflow-hidden"><div class="absolute inset-0 glow pointer-events-none"></div>'
      '<div class="absolute inset-0 gridlines opacity-60 pointer-events-none"></div>'
      '<div class="relative max-w-[1440px] mx-auto px-6 lg:px-12 py-16 lg:py-24">'
      '<div class="max-w-3xl reveal">%s'
      '<h2 class="hd2 text-white mb-3" style="font-size:clamp(28px,4vw,44px)">WOWER — The WOW Maker</h2>'
      '<p class="font-display font-semibold text-brandTeal mb-6" style="font-size:clamp(20px,2.8vw,30px);letter-spacing:-0.01em">Learn. Execute. Perform. Grow.</p>'
      '<p class="lead text-slate-300 mb-8 max-w-2xl">A performance-driven pathway that transforms aspiring talent into work-ready professionals through training, real projects, and meaningful career opportunities.</p>'
      '<div class="flex flex-wrap gap-4"><a class="inline-flex items-center gap-2 bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold px-7 py-3.5 transition-colors" href="internships.html#apply-form">Apply for opportunities <span class="material-symbols-outlined text-[18px]" aria-hidden="true">arrow_forward</span></a>'
      '<a class="inline-flex items-center gap-2 border border-white/30 hover:border-white hover:bg-white/5 text-white text-sm font-semibold px-7 py-3.5 transition-colors" href="wowers.html#pathway">How WOWER works</a></div></div></div></section>' % eyebrow("For Wowers"))
    b += inspiration()
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Our mentors","Guided by people who have done the work.","Mentors from Microsoft, Deloitte, PwC, KPMG, Accenture and more support our Wowers and our execution.")
    b += mentors() + '</div></section>'
    b += cta_band()
    return page("Woways — Your Executive Partner","index.html",b)

def build_companies():
    b = hero_chips("For Companies","Your execution team for the work that cannot wait.",
        "When sales pipelines, campaigns, operations or systems need momentum, Woways works alongside your team to make the work move — inside your tools, standards and reporting rhythm.",
        [("Discuss your requirement","partnerships.html#partner-form",True),("See our services","companies.html#services",False)],
        [("grid_view","Five core functions"),("bolt","End-to-end delivery"),("insights","Measurable outcomes"),("schedule","48-hour reply")])
    b += '<section class="bg-paperBg py-16 lg:py-20 border-b border-borderLine" id="capabilities"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("What we execute","Five functions, one embedded team.","Point to a work area, describe the need, and we take it on — with the scope and standards of an internal team.")
    b += caps_detailed() + '</div></section>'
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine" id="services"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Services","Five services, one execution partner.","Pick the service that unblocks you now, or combine them — each is run by our team and reports into yours.")
    b += services_detailed() + '</div></section>'
    b += '<section class="bg-paperBg py-16 lg:py-20 border-b border-borderLine" id="partnerships"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Partnerships","What you get, and who we partner with.","")
    what=["Access to lead generation infrastructure","Sales pipeline management","Expansion into new markets","Cost-effective talent through the Wower ecosystem"]
    wl=''.join('<div class="flex items-start gap-3 text-slate-700">%s<span>%s</span></div>'%(CHECK,x) for x in what)
    ptypes=["Technology Companies","Manufacturing Companies","Service Companies","Startups"]
    pp=''.join('<span class="px-4 py-2 bg-paperBg border border-borderLine text-sm font-display font-medium text-brandNavy">%s</span>'%t for t in ptypes)
    b += ('<div class="grid grid-cols-1 lg:grid-cols-2 gap-6 reveal">'
      '<div class="bg-white border border-borderLine p-8"><h3 class="hd3 text-brandNavy mb-5" style="font-size:20px">What you get</h3><div class="space-y-4">%s</div></div>'
      '<div class="bg-white border border-borderLine p-8"><h3 class="hd3 text-brandNavy mb-5" style="font-size:20px">Partner types</h3><div class="flex flex-wrap gap-3">%s</div></div></div>' % (wl,pp))
    b += '</div></section>'
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 grid lg:grid-cols-[0.85fr_1.15fr] gap-10 lg:gap-16 items-start">'
    b += ('<div class="reveal"><span class="cap text-brandTeal block mb-2">Bringing us in</span>'
      '<h2 class="hd2 text-brandNavy mb-3">How an engagement starts.</h2>'
      '<p class="lead text-slate-600">A short, clear path from first conversation to work moving — no drawn-out sales cycle.</p></div>')
    b += '<div>'+journey()+'</div></div></section>'
    b += '<section class="bg-paperBg py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Why companies choose Woways","Execution you can hold accountable.","")
    b += why_cards() + '</div></section>'
    b += industries() + cta_band('company')
    return page("Woways — For Companies","companies.html",b)

def build_wowers():
    benes=["Work on real company projects","Learn practical business skills","Earn performance incentives","Build lasting career opportunities"]
    bl=''.join('<li class="flex items-start gap-3 text-slate-700">%s<span>%s</span></li>'%(CHECK,x) for x in benes)
    steps=[("01","Apply","Tell us your interests, skills and availability."),("02","Get matched","We place you on live work on a partner company project."),("03","Deliver & grow","Do real work, learn and earn — with performance-based growth.")]
    sc=''.join('<div class="border border-borderLine p-8 bg-white card-lift"><div class="w-full h-1 bg-brandTeal mb-6"></div><span class="cap text-brandTeal font-bold">STEP %s</span><h3 class="hd3 text-brandNavy mt-2 mb-3" style="font-size:22px">%s</h3><p class="text-slate-600">%s</p></div>'%(i,h,p) for i,h,p in steps)
    faqs=[("Is it paid?","Yes — Wowers earn performance-based incentives tied to the results they help deliver."),
      ("Do I need prior experience?","No. We match you to work at your level and support you as you learn."),
      ("How do I start?","Apply with your interests and availability; we match you to a live project on a partner company."),
      ("What will I gain?","Real project experience, practical business skills and a track record you can actually show.")]
    b = hero_big("For Wowers","Build your career by doing real work.",
        "<span class=\"block text-brandTeal font-display font-semibold mb-4\" style=\"font-size:clamp(20px,2.8vw,30px);letter-spacing:-0.01em\">Learn. Execute. Perform. Grow.</span>A Wower is an emerging professional who learns through live projects, structured guidance and performance-based growth — not classroom theory alone.",
        [("Explore opportunities","internships.html#apply-form",True),("How WOWER works","#pathway",False)])
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine" id="pathway"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("How WOWER works","Five steps, one performance-driven pathway.","From joining the ecosystem to real career growth — here is how a Wower's journey unfolds.")
    b += wower_pathway() + '</div></section>'
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Who is a Wower","Potential, ready to perform.","A Wower is an aspiring professional who is ready to learn, execute, grow, and create a WOW factor through meaningful work.")
    who=[("diversity_3","Every kind of starter","Wowers can be freshers, interns, graduates, pursuing graduates, career starters, or individuals actively looking for meaningful job and growth opportunities."),
      ("rocket_launch","Learning by doing","At Woways, we identify potential, provide structured training, and place Wowers into real-world projects aligned with our partner companies. Instead of waiting for an opportunity, Wowers learn by doing, contribute to real business work, and build their careers through performance.")]
    wc2=''.join('<div class="bg-paperBg border border-borderLine p-8 card-lift"><span class="material-symbols-outlined text-brandTeal mb-4 block" aria-hidden="true">%s</span><h3 class="hd3 text-brandNavy mb-2" style="font-size:19px">%s</h3><p class="text-slate-600 leading-relaxed">%s</p></div>'%(ic,h,p) for ic,h,p in who)
    b += '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 stagger reveal">%s</div></div></section>'%wc2
    b += ('<section class="relative bg-brandNavy text-white overflow-hidden"><div class="absolute inset-0 glow pointer-events-none"></div>'
      '<div class="relative max-w-[1440px] mx-auto px-6 lg:px-12 py-16 lg:py-20 text-center reveal">'
      '<span class="cap text-brandTeal block mb-4">Our objective</span>'
      '<p class="font-display text-white mx-auto max-w-3xl" style="font-size:clamp(20px,2.8vw,30px);line-height:1.4;letter-spacing:-0.02em">To transform aspiring talent into capable professionals by providing real work, structured learning, and performance-driven growth opportunities.</p>'
      '<p class="mt-8 text-brandTeal font-display font-semibold" style="font-size:clamp(18px,2.2vw,24px)">&ldquo;Potential gets the opportunity. Performance creates the growth.&rdquo;</p>'
      '</div></section>')
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 grid lg:grid-cols-2 gap-12 items-center">'
    b += ('<div class="reveal"><span class="cap text-brandTeal block mb-3">More than a job opportunity</span>'
      '<h2 class="hd2 text-brandNavy mb-5" style="font-size:clamp(26px,3.4vw,38px)">Built work-ready, not just placed.</h2>'
      '<p class="text-slate-600 leading-relaxed mb-4">Being a Wower is not just about getting placed into a role. It is about becoming work-ready, gaining practical business exposure, contributing to real organizations, and creating a foundation for long-term professional growth.</p>'
      '<p class="text-slate-600 leading-relaxed">At Woways, every Wower gets the opportunity to learn with purpose, work with responsibility, and grow through performance.</p></div>')
    promise=[("Real Work","work"),("Real Learning","school"),("Real Performance","trending_up"),("Real Growth","rocket_launch")]
    pcards=''.join('<div class="bg-brandNavy text-white p-6 card-lift"><span class="material-symbols-outlined text-brandTeal mb-3 block" aria-hidden="true">%s</span><div class="font-display font-semibold" style="font-size:18px">%s</div></div>'%(ic,t) for t,ic in promise)
    b += '<div class="reveal"><p class="cap text-slate-500 mb-4">The WOWER promise</p><div class="grid grid-cols-2 gap-4 stagger">%s</div></div>'%pcards
    b += '</div></section>'
    b += '<section class="bg-paperBg py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("What you'll work on","Real work across partner companies.","")
    b += wowers_work() + '</div></section>'
    b += '<section class="bg-brandNavy py-16 lg:py-20"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += ('<div class="max-w-3xl mb-12 reveal"><span class="cap text-brandTeal block mb-2">What Wowers say</span>'
      '<h2 class="hd2 text-white">Real work. Real responsibility. Real growth.</h2></div>')
    b += testimonials() + '</div></section>'
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += '<div class="max-w-3xl mx-auto text-center mb-12 reveal"><span class="cap text-brandTeal block mb-2">Questions</span><h2 class="hd2 text-brandNavy">Good to know.</h2></div>'
    b += faq(faqs) + '</div></section>'
    b += cta_band('wower')
    return page("Woways — For Wowers","wowers.html",b)

def build_services():
    b = hero("Services","Practical execution across the functions that drive growth.",
        "Each service is run by our team and reports into yours — practical execution with a clear output, whether you start with one or combine several.",
        [("Discuss your requirement","partnerships.html#partner-form",True),("For companies","companies.html",False)],
        illo=viz_rings())
    b += '<section class="bg-paperBg py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("What we do","Five services, one execution partner.","Each service is run by our team and reports into yours. Pick one, or combine them.")
    b += services_detailed() + '</div></section>'
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("How an engagement works","Start small. Scale with results.","")
    b += how_engagement() + '</div></section>'
    b += ('<section class="bg-paperBg py-16 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 reveal flex flex-col md:flex-row md:items-center justify-between gap-6">'
      '<div><h3 class="hd3 text-brandNavy mb-1" style="font-size:20px">The tools behind the work</h3><p class="text-slate-600">Our services run on the same platforms we ship to customers — Bispun and the Performance Portal.</p></div>'
      '<a class="shrink-0 inline-flex items-center gap-2 border border-borderLine px-6 py-3 text-sm font-semibold text-brandNavy hover:bg-brandNavy hover:text-white transition-colors grp" href="about.html">See our products <span class="material-symbols-outlined text-[16px] arrow-move" aria-hidden="true">arrow_forward</span></a>'
      '</div></section>')
    b += cta_band('company')
    return page("Woways — Services","services.html",b)

def build_about():
    b = hero_chips("About","Built for work that creates visible progress.",
        "Woways was created around a simple belief: growing companies need dependable execution, and emerging professionals need meaningful opportunities to prove themselves. We connect both through real work, clear ownership and measurable progress.",
        [("Work with us","contact.html",True),("How we work","#ecosystem",False)],
        [("bolt","Execution-first"),("query_stats","Evidence of progress"),("handshake","Growth for both sides"),("groups","Emerging talent")])
    b += '<section class="bg-brandNavy py-14 lg:py-16 border-b border-white/10"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += impact_stats(dark=True) + '</div></section>'
    # two-sided
    comp=["Lead generation, sales support and growth operations","Execution across Sales, Marketing, Operations, HR and Technology","Our own products where they help — reporting into your team"]
    wow=["Real company projects, not busywork","Practical business skills and mentoring","Performance incentives and career growth"]
    cl=''.join('<li class="flex items-start gap-3 text-slate-700">%s<span>%s</span></li>'%(CHECK,x) for x in comp)
    wl=''.join('<li class="flex items-start gap-3 text-slate-700">%s<span>%s</span></li>'%(CHECK,x) for x in wow)
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 grid lg:grid-cols-[0.85fr_1.15fr] gap-10 lg:gap-16 items-start">'
    b += ('<div class="reveal"><span class="cap text-brandTeal block mb-2">Our story</span>'
      '<h2 class="hd2 text-brandNavy">Where dependable execution meets real opportunity.</h2></div>')
    b += ('<div class="reveal space-y-5 text-[17px] text-slate-700 leading-relaxed">'
      '<p>Woways began with a simple belief: growing companies need dependable execution, and emerging professionals need meaningful opportunities to prove themselves.</p>'
      '<p>We connect both through real work, clear ownership and measurable progress — an execution layer that helps companies grow, and a launchpad where careers get built.</p></div>'
      '</div></section>')
    b += '<section class="bg-paperBg py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Our core team","Experience that has done the work.","")
    b += core_team() + '</div></section>'
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 grid lg:grid-cols-[0.85fr_1.15fr] gap-10 lg:gap-16 items-start">'
    b += ('<div class="reveal"><span class="cap text-brandTeal block mb-2">Where we are today</span>'
      '<h2 class="hd2 text-brandNavy">Focused on measurable outcomes.</h2></div>')
    b += '<div>'+where_today()+'</div></div></section>'
    b += '<section class="bg-paperBg py-16 lg:py-20 border-b border-borderLine" id="ecosystem"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("The ecosystem model","One partner. Two engines of growth.","Companies need execution and pipeline. Talent needs real experience. Woways connects the two into a single virtuous cycle.")
    b += ('<div class="grid grid-cols-1 md:grid-cols-2 gap-6 reveal">'
      '<div class="bg-white border border-borderLine p-8"><div class="w-full h-1 bg-brandTeal mb-6"></div>'
      '<span class="cap text-slate-500">For companies</span><h3 class="hd3 text-brandNavy mt-2 mb-4" style="font-size:20px">Scale without adding overhead</h3><ul class="space-y-3.5">%s</ul></div>'
      '<div class="bg-white border border-borderLine p-8"><div class="w-full h-1 bg-brandOrange mb-6"></div>'
      '<span class="cap text-slate-500">For Wowers</span><h3 class="hd3 text-brandNavy mt-2 mb-4" style="font-size:20px">Build a career on real work</h3><ul class="space-y-3.5">%s</ul></div></div>' % (cl,wl))
    b += '</div></section>'
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("How we operate","What we stand for.","")
    values=[("bolt","Delivery over decks","We run the work and are measured on outcomes, not slideware."),
      ("verified","Honesty over hype","Intended value, stated plainly — no inflated claims or fake metrics."),
      ("hub","Growth for both sides","Every engagement builds a company and a career at the same time.")]
    vcards=''.join('<div class="bg-paperBg border border-borderLine p-7 card-lift"><span class="material-symbols-outlined text-brandTeal mb-4 block" aria-hidden="true">%s</span><h3 class="hd3 text-brandNavy mb-2" style="font-size:18px">%s</h3><p class="text-[15px] leading-relaxed text-slate-600">%s</p></div>'%(ic,h,p) for ic,h,p in values)
    b += '<div class="grid grid-cols-1 md:grid-cols-3 gap-6 stagger reveal">%s</div></div></section>'%vcards
    # Values — confident, positive
    b += '<section class="relative bg-brandNavy text-white overflow-hidden"><div class="absolute inset-0 glow pointer-events-none"></div><div class="absolute inset-0 gridlines opacity-60 pointer-events-none"></div>'
    b += '<div class="relative max-w-[1440px] mx-auto px-6 lg:px-12 py-16 lg:py-20">'
    b += '<div class="max-w-3xl mb-12 reveal"><span class="cap text-brandTeal block mb-2">What we value</span><h2 class="hd2 text-white mb-3">Progress you can see.</h2><p class="lead text-slate-300">Three principles shape how we work with companies and how Wowers grow.</p></div>'
    vals=[("bolt","Work that moves","We focus on outputs, ownership and momentum."),
      ("query_stats","Growth with evidence","We measure progress through work completed and outcomes created."),
      ("trending_up","Opportunity through performance","Wowers grow by contributing to real business work.")]
    hc=''.join('<div class="border border-white/12 bg-white/5 p-7 card-lift"><span class="material-symbols-outlined text-brandTeal mb-4 block" aria-hidden="true">%s</span><h3 class="hd3 text-white mb-2" style="font-size:18px">%s</h3><p class="text-[15px] leading-relaxed text-slate-300">%s</p></div>'%(ic,h,p) for ic,h,p in vals)
    b += '<div class="grid grid-cols-1 md:grid-cols-3 gap-5 stagger reveal">%s</div></div></section>'%hc
    b += cta_band()
    return page("Woways — About","about.html",b)

PRIVACY_NOTE=('We collect these details only to respond to you and discuss working together. We keep them for up to 24 months after our last contact, then delete them. '
  'To see, correct or delete your details, write to <a class="underline hover:text-brandTeal" href="mailto:tech@woways.in">tech@woways.in</a>. '
  'Woways connects applicants with opportunities at partner companies; Woways is not the employer.')

# Web3Forms access key — the PRIMARY recipient is the address tied to this key (tech@woways.in).
# Get a free key at https://web3forms.com (enter tech@woways.in) and paste it here, then rebuild + deploy.
WEB3FORMS_KEY = "27b6dd29-ea5c-4f5a-9af3-0b3878f94d9b"
# Extra recipients — every submission is also copied to these (comma-separated). Leave "" for none.
CC_EMAILS = "povanapun@woways.in, hr@woways.in"

def render_form(form_id, fields, submit_label, subject, form_type="enquiry", ok_msg="Thank you. Our team will get back to you within 48 hours."):
    ok=form_id+'-ok'; err=form_id+'-err'
    parts=''
    for f in fields:
        fid=form_id+'-'+f['id']; req=' required' if f.get('req') else ''
        full='md:col-span-2' if f.get('full') else ''
        nm=f.get('name') or f['label'].replace('"','')
        if f['t']=='select':
            opts=''.join('<option>%s</option>'%o for o in f['options'])
            ctrl='<select id="%s" name="%s"%s class="w-full h-11 px-3.5 border border-borderLine text-brandNavy bg-white"><option value="">Choose one</option>%s</select>'%(fid,nm,req,opts)
        elif f['t']=='textarea':
            ctrl='<textarea id="%s" name="%s" rows="4"%s class="w-full p-3.5 border border-borderLine text-brandNavy"></textarea>'%(fid,nm,req)
        else:
            auto=' autocomplete="%s"'%f['auto'] if f.get('auto') else ''
            ctrl='<input id="%s" name="%s" type="%s"%s%s class="w-full h-11 px-3.5 border border-borderLine text-brandNavy"/>'%(fid,nm,f['t'],req,auto)
        parts+='<div class="%s"><label class="cap text-slate-600 block mb-1.5" for="%s">%s</label>%s</div>'%(full,fid,f['label'],ctrl)
    return ('<form class="w3form bg-white p-8 lg:p-10 herofade" action="/api/submit" method="POST">'
      '<input type="hidden" name="_form" value="%s"/>'
      '<input type="hidden" name="_subject" value="%s"/>'
      '<input type="checkbox" name="botcheck" tabindex="-1" aria-hidden="true" style="display:none"/>'
      '<div id="%s" class="form-ok hidden mb-5 p-5 bg-brandTealTint border border-teal-200 flex items-start gap-3"><span class="material-symbols-outlined text-brandTeal" aria-hidden="true">check_circle</span><span class="text-brandTealDark text-sm">%s</span></div>'
      '<div id="%s" class="form-err hidden mb-5 p-4 bg-red-50 text-red-700 text-sm border border-red-200" role="alert"></div>'
      '<div class="grid grid-cols-1 md:grid-cols-2 gap-5">%s</div>'
      '<button type="submit" class="mt-6 w-full bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold py-4 transition-colors disabled:opacity-60">%s</button>'
      '<label class="flex items-start gap-2.5 mt-5 text-sm text-slate-600"><input type="checkbox" required class="mt-0.5"/> <span>I agree to be contacted by Woways about my enquiry and accept the <a class="underline hover:text-brandTeal" href="privacy.html">Privacy Policy</a>.</span></label>'
      '<p class="mt-3 text-xs text-slate-400"><a class="hover:text-brandTeal" href="privacy.html">How we use your information</a></p>'
      '</form>')%(form_type,subject,ok,ok_msg,err,parts,submit_label)

def form_section(section_id, eyebrow_t, heading, sub, bullets, form_html, h1=False):
    tag='h1' if h1 else 'h2'
    bl=''.join('<div class="flex items-start gap-3 text-slate-300">%s<span>%s</span></div>'%(CHECK,x) for x in bullets)
    return ('<section id="%s" class="bg-brandNavy text-white"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 py-16 lg:py-20 grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">'
      '<div class="herofade"><span class="cap text-brandTeal block mb-3">%s</span>'
      '<%s class="hd1 text-white mb-5" style="font-size:clamp(26px,3.6vw,42px)">%s</%s>'
      '<p class="lead text-slate-300 mb-8 max-w-xl">%s</p>'
      '<div class="space-y-4">%s</div></div>%s</div></section>')%(section_id,eyebrow_t,tag,heading,tag,sub,bl,form_html)

def build_contact():
    fields=[{'t':'text','id':'name','label':'Your name','req':True,'auto':'name'},
      {'t':'text','id':'org','label':'Company / entity (optional)','auto':'organization'},
      {'t':'email','id':'email','label':'Email','req':True,'auto':'email','name':'email'},
      {'t':'tel','id':'phone','label':'Phone','auto':'tel'},
      {'t':'select','id':'topic','label':'What is this about?','req':True,'options':['Partnership','Internship','Product demo','Become a mentor','General enquiry'],'full':True},
      {'t':'textarea','id':'msg','label':'Tell us briefly what you need','req':True,'full':True}]
    form=render_form('talk',fields,'Send message','New enquiry — Woways website','enquiry')
    bullets=["One short form. No sales call unless you ask for one.","A real person on the Woways team replies, not an inbox.","We reply within 48 hours."]
    b=form_section('talk-form','Talk to the Woways team','Get in touch.',
      "Whether you're a company, a prospective Wower, or just exploring — tell us what you're trying to get done and we'll point you to the right place. For a partnership or an internship, the dedicated forms give us the details faster.",
      bullets, form, h1=True)
    b+=('<section class="bg-white py-14 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 grid grid-cols-1 md:grid-cols-3 gap-6 stagger reveal">'
      '<a class="bg-paperBg border border-borderLine p-6 card-lift block" href="partnerships.html#partner-form"><span class="material-symbols-outlined text-brandTeal mb-3 block" aria-hidden="true">handshake</span><h3 class="hd3 text-brandNavy mb-1" style="font-size:18px">Partnership form</h3><p class="text-[15px] leading-relaxed text-slate-600">For companies who want an execution partner.</p></a>'
      '<a class="bg-paperBg border border-borderLine p-6 card-lift block" href="internships.html#apply-form"><span class="material-symbols-outlined text-brandTeal mb-3 block" aria-hidden="true">school</span><h3 class="hd3 text-brandNavy mb-1" style="font-size:18px">Internship form</h3><p class="text-[15px] leading-relaxed text-slate-600">For Wowers applying for real project work.</p></a>'
      '<div class="bg-paperBg border border-borderLine p-6"><span class="material-symbols-outlined text-brandTeal mb-3 block" aria-hidden="true">call</span><h3 class="hd3 text-brandNavy mb-1" style="font-size:18px">Direct</h3><p class="text-[15px] leading-relaxed text-slate-600"><a class="hover:text-brandTeal" href="mailto:tech@woways.in">tech@woways.in</a><br/><a class="hover:text-brandTeal" href="tel:+919390188553">+91 93901 88553</a></p></div>'
      '</div></section>')
    return page("Woways — Contact","contact.html",b)

def legal_page(title, active, eyebrow_t, heading, updated, blocks):
    body=''
    for h,paras in blocks:
        body+='<h2 class="hd3 text-brandNavy mt-10 mb-3" style="font-size:20px">%s</h2>'%h
        for p in paras:
            body+='<p class="text-slate-600 leading-relaxed mb-4">%s</p>'%p
    b=('<section class="bg-brandNavy text-white"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 py-16 lg:py-20 herofade">'
      '<span class="cap text-brandTeal block mb-3">%s</span><h1 class="hd1 text-white" style="font-size:clamp(30px,4.5vw,48px)">%s</h1>'
      '<p class="text-slate-400 mt-4 text-sm">Last updated: %s</p></div></section>'
      '<section class="bg-white py-16 lg:py-20"><div class="max-w-3xl mx-auto px-6 lg:px-12 reveal">%s'
      '<p class="text-slate-600 leading-relaxed mt-10">Questions about this policy? Write to <a class="text-brandTeal underline" href="mailto:tech@woways.in">tech@woways.in</a>.</p>'
      '</div></section>')%(eyebrow_t,heading,updated,body)
    return page(title,active,b)

def build_privacy():
    return legal_page("Woways — Privacy Policy","privacy.html","Legal","Privacy Policy","28 September 2026",[
      ("Who we are",["Woways Private Limited (\"Woways\", \"we\", \"us\") operates this website and provides execution services and talent-ecosystem programmes. This policy explains what personal data we collect, why, and your rights over it."]),
      ("What we collect",["When you submit an enquiry or application, we collect the details you provide — such as your name, email, phone number, company or education details, and the content of your message.","We also collect basic technical data (such as device and usage information) needed to run the site securely."]),
      ("Why we use it",["We use your details only to respond to your enquiry, discuss working together, process an application, and keep you updated where you have asked us to. We do not sell your personal data."]),
      ("How long we keep it",["We keep enquiry and application details for up to 24 months after our last contact with you, then delete them, unless we are required to keep them longer by law."]),
      ("Your rights",["You can ask us to see, correct or delete your details, or withdraw your consent, at any time by writing to tech@woways.in. Where applicable, you may also lodge a complaint with a data-protection authority."]),
      ("A note on opportunities",["Woways connects applicants with opportunities at partner companies; Woways is not the employer. Where we share your application with a partner company, we do so only to progress an opportunity you have applied for."]),
    ])

def build_terms():
    return legal_page("Woways — Terms of Use","terms.html","Legal","Terms of Use","28 September 2026",[
      ("Acceptance",["By using this website you agree to these terms. If you do not agree, please do not use the site."]),
      ("Use of the site",["You may use this site for lawful purposes only. You agree not to misuse it, attempt to disrupt it, or use it to infringe the rights of others."]),
      ("Services and content",["Information on this site is provided for general information about Woways and its services and products. It does not constitute a binding offer or professional advice, and any engagement is subject to a separate written agreement."]),
      ("Intellectual property",["The Woways name, logo, content and design are owned by Woways Private Limited or its licensors. Company names and logos of mentors' employers are trademarks of their respective owners and are shown only to indicate where our mentors work."]),
      ("External links",["Our products and some links open external sites we do not control. We are not responsible for their content or practices."]),
      ("Liability",["To the extent permitted by law, Woways is not liable for any indirect or consequential loss arising from use of this site."]),
      ("Contact",["Questions about these terms can be sent to tech@woways.in."]),
    ])

def build_cookies():
    return legal_page("Woways — Cookie Policy","cookies.html","Legal","Cookie Policy","28 September 2026",[
      ("About cookies",["Cookies are small files stored on your device. We use only what is necessary to run the site reliably and to understand, in aggregate, how it is used."]),
      ("What we use",["Essential cookies keep the site working. Where we use analytics, it is to improve the site — never to build advertising profiles of you."]),
      ("Your choices",["You can control or delete cookies through your browser settings. Blocking essential cookies may affect how the site works."]),
      ("Contact",["Questions about this policy can be sent to tech@woways.in."]),
    ])

def build_partnerships():
    b = hero("Partnerships","Tell us what needs to move.",
        "Share the outcome you want to achieve. We'll review the requirement, identify the right execution scope, and respond within 48 hours.",
        [("Discuss your requirement","#partner-form",True),("See our services","services.html",False)])
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Why companies partner with Woways","Execution you can hold accountable.","")
    b += why_cards() + '</div></section>'
    pfields=[{'t':'text','id':'company','label':'Company name','req':True,'auto':'organization'},
      {'t':'text','id':'name','label':'Your name','req':True,'auto':'name'},
      {'t':'text','id':'desig','label':'Designation','auto':'organization-title'},
      {'t':'email','id':'email','label':'Work email','req':True,'auto':'email','name':'email'},
      {'t':'tel','id':'phone','label':'Phone','auto':'tel'},
      {'t':'select','id':'size','label':'Company size','options':['Startup (1–10)','SME (11–50)','Mid-size (51–200)','Large (201–1,000)','Enterprise (1,000+)']},
      {'t':'select','id':'timeline','label':'Timeline','options':['Immediately','Within 1 month','1–3 months','3–6 months','Just exploring']},
      {'t':'select','id':'need','label':'What do you need?','options':['Lead generation','Sales support','Marketing','Operations','Business scaling','Multiple / not sure']},
      {'t':'select','id':'budget','label':'Monthly budget (optional)','options':['Under ₹50K','₹50K–2 lakh','₹2–5 lakh','₹5 lakh+','Not decided']},
      {'t':'textarea','id':'req','label':'Describe your requirement','req':True,'full':True}]
    pform=render_form('partner',pfields,'Submit requirement','New partnership requirement — Woways website','partnership',ok_msg="Thank you. Our partnerships team will review your requirement and get back within 48 hours.")
    b += form_section('partner-form','Become a partner','Tell us what you need.',
      "Share your requirement and our partnerships team reviews it and gets in touch within 48 hours to explore how we can create value together.",
      ["We review every requirement within 48 hours.","A real person from the partnerships team, not an inbox.","No obligation — a first conversation to see the fit."], pform)
    return page("Woways — Partnerships","partnerships.html",b)

def build_internships():
    b = hero("Internships","Apply for real project experience.",
        "Work on meaningful business projects, learn from structured feedback, and build evidence of what you can do.<br class=\"hidden sm:block\"/><span class=\"inline-block mt-4 text-slate-400 text-sm\">Strong performance can lead to extended projects, referrals and role opportunities. Opportunities depend on project needs and performance; Woways does not guarantee employment.</span>",
        [("Apply for opportunities","#apply-form",True),("How WOWER works","#pathway",False)])
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine" id="pathway"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("How WOWER works","Five steps, one performance-driven pathway.","From joining the ecosystem to real career growth — here is how a Wower's internship journey unfolds.")
    b += wower_pathway() + '</div></section>'
    b += '<section class="bg-paperBg py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("What you'll work on","Real work across partner companies.","")
    b += wowers_work() + '</div></section>'
    who=["Freshers and recent graduates","Pursuing graduates and interns","Career starters changing tracks","Anyone looking for meaningful, real work"]
    wl=''.join('<li class="flex items-start gap-3 text-slate-700">%s<span>%s</span></li>'%(CHECK,x) for x in who)
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 grid lg:grid-cols-2 gap-12 items-center">'
    b += ('<div class="reveal"><span class="cap text-brandTeal block mb-3">Who can apply</span>'
      '<h2 class="hd2 text-brandNavy mb-5" style="font-size:clamp(26px,3.4vw,38px)">Potential, ready to perform.</h2>'
      '<ul class="space-y-4">%s</ul>'
      '<p class="mt-6 text-sm text-slate-500">Woways connects applicants with opportunities at partner companies; Woways is not the employer.</p></div>' % wl)
    b += ('<div class="reveal bg-brandTealTint border border-teal-200/60 p-8">'
      '<p class="font-display text-brandNavy" style="font-size:22px;line-height:1.4">&ldquo;Potential gets the opportunity. Performance creates the growth.&rdquo;</p>'
      '<a class="mt-6 inline-flex items-center gap-2 bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold px-7 py-3.5 transition-colors" href="#apply-form">Apply for opportunities <span class="material-symbols-outlined text-[18px]" aria-hidden="true">arrow_forward</span></a></div>')
    b += '</div></section>'
    ifields=[{'t':'text','id':'name','label':'Full name','req':True,'auto':'name'},
      {'t':'email','id':'email','label':'Email','req':True,'auto':'email','name':'email'},
      {'t':'tel','id':'phone','label':'Phone','req':True,'auto':'tel'},
      {'t':'text','id':'city','label':'City','auto':'address-level2'},
      {'t':'text','id':'college','label':'College / organisation (optional)'},
      {'t':'select','id':'status','label':'Current status','req':True,'options':['College student','Pursuing graduate','Recent graduate','Working professional','Career starter']},
      {'t':'select','id':'interest','label':'Area of interest','req':True,'options':['Sales','Marketing','Operations','HR','Technology','Digital Business','Not sure yet']},
      {'t':'url','id':'link','label':'Resume / LinkedIn / Portfolio link (optional)','auto':'url','full':True},
      {'t':'textarea','id':'msg','label':'Tell us a little about yourself','full':True}]
    iform=render_form('apply',ifields,'Submit application','New internship application — Woways website','internship',ok_msg="Thank you for applying. We review applications and get back within 48 hours.")
    b += form_section('apply-form','Start your internship journey','Apply for an internship.',
      "Tell us about yourself and we'll match you to real project work with a partner company. Woways connects applicants with opportunities; Woways is not the employer.",
      ["We review every application within 48 hours.","No prior experience needed — we match you to your level.","Real projects, mentoring and performance-based growth."], iform)
    return page("Woways — Internships","internships.html",b)

def build_products():
    b = hero("Products","Products built from real execution.",
        "We build focused platforms for education, career growth and business performance — shaped by the work we do with people and companies.",
        [("Talk to us","contact.html",True)],
        illo='<img src="hero-products.png" alt="Woways products across devices" loading="eager" class="w-full" style="-webkit-mask-image:radial-gradient(120% 120% at 62% 40%,#000 46%,rgba(0,0,0,0) 82%);mask-image:radial-gradient(120% 120% at 62% 40%,#000 46%,rgba(0,0,0,0) 82%)"/>')
    b += '<section class="bg-white py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Education &amp; career","For students, families and educators.","Guidance, discovery and future-readiness — from grade 10 through to a career.")
    b += product_cards('edu') + '</div></section>'
    b += '<section class="bg-paperBg py-16 lg:py-20 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Business systems","For running and growing a business.","CRM and performance analytics that power the way we — and our partners — execute.")
    b += product_cards('biz') + '</div></section>'
    b += cta_band('product')
    return page("Woways — Products","products.html",b)

pages={'index.html':build_index(),'companies.html':build_companies(),'wowers.html':build_wowers(),
       'products.html':build_products(),'services.html':build_services(),
       'partnerships.html':build_partnerships(),'internships.html':build_internships(),
       'about.html':build_about(),'contact.html':build_contact(),
       'privacy.html':build_privacy(),'terms.html':build_terms(),'cookies.html':build_cookies()}
import os,re
def clean_hrefs(h):
    for k in ['companies','wowers','products','services','partnerships','internships','about','contact','privacy','terms','cookies']:
        h=h.replace('href="%s.html"'%k,'href="%s"'%k).replace('href="%s.html#'%k,'href="%s#'%k)
    h=h.replace('href="index.html"','href="/"')
    return h
for fn,html in pages.items():
    open(fn,'w',encoding='utf-8').write(clean_hrefs(html))
    print('wrote',fn,round(len(html)/1024),'KB')
# remove stale extra pages so nav stays consistent
for extra in ['solutions.html','product.html','wowers2.html']:
    if os.path.exists(extra): os.remove(extra); print('removed',extra)
# compile Tailwind to a static stylesheet (no runtime CDN)
import subprocess
tw = os.path.abspath('tw.exe' if os.name=='nt' else 'tw')
try:
    r = subprocess.run([tw,'-i','input.css','-o','styles.css','--minify'],
                       capture_output=True, text=True, cwd=os.getcwd())
    if r.returncode==0 and os.path.exists('styles.css'):
        print('compiled styles.css', round(os.path.getsize('styles.css')/1024), 'KB')
    else:
        print('WARN tailwind build failed:', (r.stderr or r.stdout)[:200])
except FileNotFoundError:
    print('WARN tw.exe not found — run tailwind manually')
print('done')
