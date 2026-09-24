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
<link rel="icon" href="favicon.ico"/>
<link rel="apple-touch-icon" href="apple-touch-icon.png"/>
<link href="https://fonts.googleapis.com" rel="preconnect"/>
<link crossorigin="" href="https://fonts.gstatic.com" rel="preconnect"/>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Syne:wght@500;600;700;800&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<script>
tailwind.config={theme:{extend:{
 colors:{brandNavy:"#000F24",brandNavy2:"#0A1830",brandInk:"#122238",brandTeal:"#00A9A9",brandTealDark:"#00807F",brandTealTint:"#E3F4F3",brandOrange:"#E8A33D",brandOrangeDark:"#C6842A",paperBg:"#F5F7FA",paperDim:"#EAEEF3",borderLine:"#DCE3EA"},
 fontFamily:{display:["Syne","sans-serif"],body:["Hanken Grotesk","sans-serif"]},
}}};
</script>
<style>
 .material-symbols-outlined{font-variation-settings:'FILL' 0,'wght' 400,'GRAD' 0,'opsz' 24;display:inline-block;vertical-align:middle;line-height:1}
 body{font-family:"Hanken Grotesk",sans-serif}
 h1,h2,h3,h4,.font-display{font-family:"Syne",sans-serif;letter-spacing:-0.02em}
 .hd1{font-size:clamp(36px,6vw,58px);line-height:1.03;font-weight:700}
 .hd2{font-size:clamp(28px,4vw,42px);line-height:1.08;font-weight:700}
 .hd3{font-size:22px;line-height:1.2;font-weight:600}
 .lead{font-size:clamp(17px,2.2vw,20px);line-height:1.6}
 .cap{font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase}
 :focus-visible{outline:2.5px solid #00A9A9;outline-offset:3px}
 .skip{position:absolute;left:-9999px;top:0;background:#00A9A9;color:#02201E;padding:10px 16px;font-weight:600;z-index:200}
 .skip:focus{left:0}
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

NAV = [("companies.html","For Companies"),("wowers.html","For Wowers"),("services.html","Services"),("about.html","About")]

def header(active):
    links = ''
    for href,label in NAV:
        cur = ' aria-current="page"' if href==active else ''
        cls = 'text-white' if href==active else 'text-slate-300 hover:text-white'
        links += '<a class="cap %s transition-colors" href="%s"%s>%s</a>' % (cls,href,cur,label)
    mob = ''.join('<a class="block px-6 py-3 text-slate-200 border-t border-white/10 font-display font-semibold" href="%s">%s</a>'%(h,l) for h,l in NAV)
    mob += '<a class="block px-6 py-3 text-slate-200 border-t border-white/10 font-display font-semibold" href="contact.html">Talk to us</a>'
    return ('<a href="#main" class="skip">Skip to content</a>'
      '<header class="sticky top-0 z-50 bg-brandNavy/95 backdrop-blur border-b border-white/10">'
      '<div class="max-w-[1440px] mx-auto px-6 lg:px-12 h-16 flex items-center justify-between">'
      '<a href="index.html" aria-label="Woways — Execute, Grow, Transform" class="flex items-center gap-1 shrink-0">'
      '<img src="logo-icon.png" alt="" class="h-5 w-auto"/>'
      '<img src="logo-word.png" alt="Woways" class="h-5 w-auto"/></a>'
      '<div class="flex items-center gap-8">'
      '<nav class="hidden md:flex items-center gap-8" aria-label="Primary">%s</nav>'
      '<a class="hidden sm:inline-flex items-center bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold px-6 py-2.5 transition-colors" href="contact.html">Talk to us</a>'
      '<button id="mbtn" class="md:hidden text-white p-2" aria-label="Open menu" aria-expanded="false"><span class="material-symbols-outlined">menu</span></button>'
      '</div></div>'
      '<div id="mmenu" class="hidden md:hidden bg-brandNavy border-t border-white/10">%s</div>'
      '</header>') % (links, mob)

def footer():
    prod = [("https://talentignition.in","Talent Ignition"),("https://studentmentor.co.in","Student Mentor"),("https://collegemacha.com","College Macha"),("https://bispun.com","Bispun"),("https://woways-performance.vercel.app","Performance Portal")]
    plinks = ''.join('<li><a class="hover:text-white transition-colors" href="%s" target="_blank" rel="noopener noreferrer">%s</a></li>'%(u,n) for u,n in prod)
    exp = ''.join('<li><a class="hover:text-white transition-colors" href="%s">%s</a></li>'%(h,l) for h,l in NAV)
    return ('<footer class="bg-brandNavy text-slate-400 py-16 border-t border-white/10">'
      '<div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
      '<div class="grid grid-cols-2 md:grid-cols-4 gap-8 pb-10 border-b border-white/10">'
      '<div class="col-span-2 md:col-span-1">'
      '<div class="flex items-center gap-1 mb-3"><img src="logo-icon.png" alt="" class="h-6 w-auto"/><img src="logo-word.png" alt="Woways" class="h-6 w-auto"/></div>'
      '<p class="cap text-brandTeal mb-2">Execute. Grow. Transform.</p>'
      '<p class="text-sm max-w-[30ch]">An additional executive partner and product studio.</p></div>'
      '<div><h4 class="cap text-white mb-4">Explore</h4><ul class="space-y-2.5 text-sm">%s<li><a class="hover:text-white transition-colors" href="contact.html">Talk to us</a></li></ul></div>'
      '<div><h4 class="cap text-white mb-4">Products</h4><ul class="space-y-2.5 text-sm">%s</ul></div>'
      '<div><h4 class="cap text-white mb-4">Contact</h4><p class="text-sm mb-1"><a class="hover:text-white transition-colors" href="mailto:info@woways.in">info@woways.in</a></p>'
      '<p class="text-sm">2nd floor, LorVen Smart Spaces,<br/>Gachibowli, Hyderabad, 500032</p></div>'
      '</div><div class="pt-6 text-sm text-slate-500 flex flex-wrap justify-between gap-3">'
      '<span>&copy; 2026 Woways Private Limited. All rights reserved.</span><span>Privacy · Terms · Cookie policy</span></div>'
      '</div></footer>') % (exp, plinks)

SCRIPT = ('<script>'
 '(function(){var b=document.getElementById("mbtn"),m=document.getElementById("mmenu");if(b)b.addEventListener("click",function(){var o=m.classList.toggle("hidden");b.setAttribute("aria-expanded",String(!o));});})();'
 '(function(){var els=document.querySelectorAll(".reveal,.stagger");'
 'if(matchMedia("(prefers-reduced-motion: reduce)").matches||!("IntersectionObserver" in window))return;'
 'document.documentElement.classList.add("js-anim");'
 'var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target);}});},{threshold:.12,rootMargin:"0px 0px -6% 0px"});'
 'els.forEach(function(e){io.observe(e);});'
 'setTimeout(function(){els.forEach(function(e){e.classList.add("in");});},1600);})();'
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
          '<h3 class="hd3 text-brandNavy mb-2">%s</h3><p class="text-sm text-slate-600 leading-relaxed">%s</p></div>' % (ic,n,d))
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
    edu=[("Grades 4–12","Talent Ignition","Closes the gap between what students are taught and what industry expects — assessment, daily learning, guidance and AI literacy.","https://talentignition.in","Visit Talent Ignition"),
         ("After Class 10 / 12","Student Mentor","Counselling for students after 12th, helping them choose the right course, college and career with clarity instead of guesswork.","https://studentmentor.co.in","Visit Student Mentor"),
         ("College discovery","College Macha","Explore, compare and decide on colleges that fit the student and the parent — estimates for guidance, not admission guarantees.","https://collegemacha.com","Visit College Macha")]
    biz=[("CRM & entity management","Bispun","A business control centre for leads, admissions, revenue and team activity — with AI surfacing corrections and plans from your data.","https://bispun.com","Visit Bispun"),
         ("Company & employee performance","Performance Portal","Accountable work, goals, KPIs and attendance — management visibility across every department, without surveillance.","https://woways-performance.vercel.app","Open Performance Portal")]
    def card(tag,name,desc,url,cta,wide=False):
        return ('<a class="bg-white border border-borderLine p-8 card-lift grp flex flex-col justify-between hover:border-brandNavy" href="%s" target="_blank" rel="noopener noreferrer">'
          '<div><span class="cap text-brandTeal bg-brandTealTint px-2.5 py-1">%s</span>'
          '<h3 class="hd3 text-brandNavy mt-4 mb-3" style="font-size:20px">%s</h3><p class="text-sm text-slate-600 leading-relaxed mb-8">%s</p></div>'
          '<span class="inline-flex items-center gap-2 text-sm font-semibold text-brandNavy">%s <span class="material-symbols-outlined text-[16px] arrow-move" aria-hidden="true">open_in_new</span></span></a>' % (url,tag,name,desc,cta))
    if group=='edu':
        return '<div class="grid grid-cols-1 md:grid-cols-3 gap-6 stagger reveal">%s</div>' % ''.join(card(*e) for e in edu)
    return '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 stagger reveal">%s</div>' % ''.join(card(*b) for b in biz)

def cta_band():
    return ('<section class="bg-brandNavy text-white py-20"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 text-center reveal">'
      '<h2 class="hd2 text-white mb-4">Let\'s find where Woways fits.</h2>'
      '<p class="lead text-slate-300 max-w-2xl mx-auto mb-8">One short form. We reply within one business day, from a real person on the Woways team.</p>'
      '<a class="inline-flex items-center gap-2 bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold px-8 py-4 transition-colors" href="contact.html">Bring us in <span class="material-symbols-outlined text-[18px]" aria-hidden="true">arrow_forward</span></a>'
      '</div></section>')

def industries():
    inds=["Manufacturing","SaaS","Education","Professional Services","Growing Businesses"]
    pills=''.join('<span class="px-4 py-2 bg-white border border-borderLine text-sm font-display font-medium text-brandNavy">%s</span>'%i for i in inds)
    return ('<section class="bg-paperBg py-16 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 reveal">'
      '<p class="cap text-slate-500 mb-5">Industries we serve</p><div class="flex flex-wrap gap-3">%s</div></div></section>') % pills

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
    return ('<section class="relative bg-brandNavy text-white overflow-hidden"><div class="absolute inset-0 glow pointer-events-none"></div>'
      '<div class="absolute inset-0 gridlines opacity-60 pointer-events-none"></div>'
      '<div class="relative max-w-[1440px] mx-auto px-6 lg:px-12 py-20 lg:py-28"><div class="max-w-3xl herofade">'
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
          '<div><h3 class="hd3 text-brandNavy mb-1.5" style="font-size:19px">%s</h3><p class="text-sm text-slate-600 leading-relaxed">%s</p></div></div>'%(ic,n,d))
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
        items+=('<div class="flex gap-5 reveal"><div class="shrink-0 w-10 h-10 bg-brandNavy text-white grid place-items-center font-display font-bold text-sm">%02d</div>'
          '<div class="pb-5 border-b border-borderLine flex-1"><h3 class="hd3 text-brandNavy mb-1" style="font-size:18px">%s</h3><p class="text-slate-600">%s</p></div></div>'%(i+1,h,p))
    return '<div class="max-w-3xl space-y-5">%s</div>'%items

def why_cards():
    data=[("bolt","Delivery, not slideware","We run the work and report back — you get outcomes, not a deck."),
      ("dashboard","Embedded like your team","We work inside your systems, tools and standards, not from the outside."),
      ("hub","One partner, five functions","Sales, Marketing, Operations, HR and Technology from a single team."),
      ("terminal","We build our own products","Real technical capability, shipped — Bispun, the Performance Portal and more."),
      ("verified","Honest scope","We state intended value and stand behind what we actually deliver."),
      ("schedule","No long ramp","We embed fast and start moving work, not onboarding for months.")]
    cards=''
    for ic,h,p in data:
        cards+=('<div class="bg-white border border-borderLine p-6 card-lift"><span class="material-symbols-outlined text-brandTeal mb-4 block" aria-hidden="true">%s</span>'
          '<h3 class="hd3 text-brandNavy mb-2" style="font-size:18px">%s</h3><p class="text-sm text-slate-600 leading-relaxed">%s</p></div>'%(ic,h,p))
    return '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 stagger reveal">%s</div>'%cards

def services_detailed():
    data=[("filter_alt","Lead Generation","DM outreach, prospecting and targeted campaigns to fill your pipeline.",["ICP definition and verified target lists","Multichannel outreach — email, DM and calls","Qualified meeting and demo booking"]),
      ("call","Sales Support","Telecalling, demo booking and follow-ups to close deals faster.",["Telecalling and structured follow-up cadences","CRM hygiene and pipeline updates","Proposals and sales collateral support"]),
      ("bolt","Growth Operations","Marketing execution, CRM management and process optimization.",["Campaign and content execution","CRM setup and day-to-day management","Reporting, dashboards and process fixes"]),
      ("hub","Talent Ecosystem","Wower internships, project work and performance-based growth.",["Vetted Wowers embedded on your work","Managed, accountable project delivery","Performance-based scaling as it works"])]
    cards=''
    for ic,n,d,inc in data:
        li=''.join('<li class="flex items-start gap-2.5 text-sm text-slate-600">%s<span>%s</span></li>'%(CHECK,x) for x in inc)
        cards+=('<div class="bg-white border border-borderLine p-8 card-lift">'
          '<span class="w-12 h-12 bg-brandTealTint text-brandTealDark grid place-items-center mb-5"><span class="material-symbols-outlined" aria-hidden="true">%s</span></span>'
          '<h3 class="hd3 text-brandNavy mb-2" style="font-size:20px">%s</h3><p class="text-slate-600 mb-5">%s</p>'
          '<ul class="space-y-2.5 border-t border-borderLine pt-5">%s</ul></div>'%(ic,n,d,li))
    return '<div class="grid grid-cols-1 md:grid-cols-2 gap-6 stagger reveal">%s</div>'%cards

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
        cards+=('<div class="bg-white border border-borderLine p-6 card-lift"><span class="material-symbols-outlined text-brandTeal mb-4 block" aria-hidden="true">%s</span><h3 class="hd3 text-brandNavy mb-2" style="font-size:17px">%s</h3><p class="text-sm text-slate-600">%s</p></div>'%(ic,h,p))
    return '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 stagger reveal">%s</div>'%cards

def faq(items):
    rows=''.join('<details class="border border-borderLine bg-white group"><summary class="cursor-pointer list-none flex justify-between items-center gap-4 p-5 font-display font-semibold text-brandNavy">%s<span class="material-symbols-outlined text-brandTeal transition-transform group-open:rotate-45" aria-hidden="true">add</span></summary><div class="px-5 pb-5 text-slate-600">%s</div></details>'%(q,a) for q,a in items)
    return '<div class="max-w-3xl space-y-3 reveal">%s</div>'%rows

# ================= PAGES =================
def build_index():
    b = hero("Execution capacity, on demand","Your Additional Executive Partner.",
        "Woways gives growing companies accountable execution capacity across Sales, Marketing, Operations, HR and Technology—working inside your systems, alongside your team.<br class=\"hidden sm:block\"/><span class=\"inline-block mt-4 text-white font-semibold\">Not advice. Delivery.</span>",
        [("Bring us in","contact.html",True),("Explore solutions","#products",False)], funcs=True)
    b += '<section class="bg-paperBg py-20 lg:py-24 border-b border-borderLine" id="capabilities"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("What we do","An added execution layer across your core functions.","Woways works alongside partnered companies as an added execution layer — taking on the day-to-day work across five functions, the way an internal team would.")
    b += caps_grid()
    b += '<div class="mt-10 reveal"><a class="inline-flex items-center gap-2 bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold px-7 py-3.5 transition-colors grp" href="companies.html">See the executive partnership <span class="material-symbols-outlined text-[18px] arrow-move" aria-hidden="true">arrow_forward</span></a></div></div></section>'
    b += '<section class="bg-white py-20 lg:py-24 border-b border-borderLine" id="how"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("How we work","Execute. Grow. Transform.","Every engagement moves through the same three stages — it's the reason clients bring us in, and the reason we stay.")
    b += egt() + '</div></section>'
    b += '<section class="bg-paperBg py-20 lg:py-24 border-b border-borderLine" id="products"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Our products","One execution partner. Five focused products.","Woways is the common partner behind the ecosystem. Each product opens in its own live portal.")
    b += '<div class="flex items-center gap-3 mb-6 reveal"><span class="cap text-slate-500">Education &amp; Career</span><div class="h-px bg-borderLine flex-1"></div></div>' + product_cards('edu')
    b += '<div class="flex items-center gap-3 mb-6 mt-12 reveal"><span class="cap text-slate-500">Business Visibility &amp; Execution</span><div class="h-px bg-borderLine flex-1"></div></div>' + product_cards('biz')
    b += '</div></section>'
    # wowers teaser
    b += ('<section class="bg-brandNavy text-white py-20 lg:py-24"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
      '<div class="max-w-3xl reveal">%s<h2 class="hd2 text-white mb-4">Where careers get built.</h2>'
      '<p class="lead text-slate-300 mb-6">We create real project work for Wowers — the talent who help deliver it. Real projects, practical skills, performance-based growth.</p>'
      '<a class="inline-flex items-center gap-2 bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold px-7 py-3.5 transition-colors" href="wowers.html">Join as a Wower <span class="material-symbols-outlined text-[18px]" aria-hidden="true">arrow_forward</span></a></div></div></section>' % eyebrow("For Wowers"))
    b += cta_band()
    return page("Woways — Your Executive Partner","index.html",b)

def build_companies():
    b = hero("For Companies","Add execution capacity without building another internal team.",
        "Bring Woways in as an added execution layer. We embed like an internal team across five functions, run the work on your systems and standards, and report straight back to you.",
        [("Bring us in","contact.html",True),("See our services","services.html",False)])
    b += '<section class="bg-paperBg py-20 lg:py-24 border-b border-borderLine" id="capabilities"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("What we execute","Five functions, one embedded team.","Point to a work area, describe the need, and we take it on — with the scope and standards of an internal team.")
    b += caps_detailed() + '</div></section>'
    b += '<section class="bg-white py-20 lg:py-24 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Bringing us in","How an engagement starts.","A short, clear path from first conversation to work moving — no drawn-out sales cycle.")
    b += journey() + '</div></section>'
    b += '<section class="bg-paperBg py-20 lg:py-24 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Why companies choose Woways","Execution you can hold accountable.","")
    b += why_cards() + '</div></section>'
    b += industries() + cta_band()
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
    b = hero("For Wowers","Real work. Real growth.",
        "A Wower doesn't fetch coffee. You work on live company projects, learn how a business actually grows, and get paid on the results you help deliver.<br class=\"hidden sm:block\"/><span class=\"inline-block mt-4 text-white font-semibold\">Real project work, practical skill-building and performance-based career growth.</span>",
        [("Join as a Wower","contact.html",True)])
    b += '<section class="bg-paperBg py-20 lg:py-24 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Why Woways","What you get as a Wower.","")
    b += ('<div class="grid grid-cols-1 lg:grid-cols-2 gap-6 reveal"><div class="bg-white border border-borderLine p-8"><ul class="space-y-4">%s</ul></div>'
      '<div class="bg-brandTealTint border border-teal-200/60 p-8 flex items-center">'
      '<p class="font-display text-brandNavy" style="font-size:22px;line-height:1.4">\u201CYour career starts with real projects, not just theory.\u201D</p></div></div>' % bl)
    b += '</div></section>'
    b += '<section class="bg-white py-20 lg:py-24 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("What you'll work on","Real work across partner companies.","")
    b += wowers_work() + '</div></section>'
    b += '<section class="bg-paperBg py-20 lg:py-24 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("How it works","Three steps to your first project.","")
    b += '<div class="grid grid-cols-1 md:grid-cols-3 gap-8 stagger reveal">%s</div></div></section>' % sc
    b += '<section class="bg-white py-20 lg:py-24 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Questions","Good to know.","")
    b += faq(faqs) + '</div></section>'
    b += cta_band()
    return page("Woways — For Wowers","wowers.html",b)

def build_services():
    b = hero("Services","The work we run, end to end.",
        "Productized execution you can start with one service and scale as it proves out — from first outreach to closed revenue, plus the talent engine that delivers it.",
        [("Discuss your needs","contact.html",True),("For companies","companies.html",False)], illo=illo_target())
    b += '<section class="bg-paperBg py-20 lg:py-24 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("What we do","Four services, one pipeline.","Each service is run by our team and reports into yours. Pick one, or combine them.")
    b += services_detailed() + '</div></section>'
    b += '<section class="bg-white py-20 lg:py-24 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("How an engagement works","Start small. Scale with results.","")
    b += how_engagement() + '</div></section>'
    b += ('<section class="bg-paperBg py-16 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12 reveal flex flex-col md:flex-row md:items-center justify-between gap-6">'
      '<div><h3 class="hd3 text-brandNavy mb-1" style="font-size:20px">The tools behind the work</h3><p class="text-slate-600">Our services run on the same platforms we ship to customers — Bispun and the Performance Portal.</p></div>'
      '<a class="shrink-0 inline-flex items-center gap-2 border border-borderLine px-6 py-3 text-sm font-semibold text-brandNavy hover:bg-brandNavy hover:text-white transition-colors grp" href="about.html">See our products <span class="material-symbols-outlined text-[16px] arrow-move" aria-hidden="true">arrow_forward</span></a>'
      '</div></section>')
    b += cta_band()
    return page("Woways — Services","services.html",b)

def build_about():
    b = hero("About Woways","A growth ecosystem where companies scale and careers get built.",
        "Woways is an additional executive partner and a product studio. We take on real execution for companies, and turn that work into real opportunities for talent — one connected ecosystem.",
        [("Work with us","contact.html",True),("Meet the products","#products",False)], illo=illo_connect())
    # two-sided
    comp=["Lead generation, sales support and growth operations","Execution across Sales, Marketing, Operations, HR and Technology","Our own products where they help — reporting into your team"]
    wow=["Real company projects, not busywork","Practical business skills and mentoring","Performance incentives and career growth"]
    cl=''.join('<li class="flex items-start gap-3 text-slate-700">%s<span>%s</span></li>'%(CHECK,x) for x in comp)
    wl=''.join('<li class="flex items-start gap-3 text-slate-700">%s<span>%s</span></li>'%(CHECK,x) for x in wow)
    b += '<section class="bg-white py-20 lg:py-24 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Our story","Built to do the opposite of advice.","")
    b += ('<div class="max-w-3xl reveal space-y-5 text-lg text-slate-700 leading-relaxed">'
      '<p>Woways started with a simple observation: companies need execution, and talented people need real experience. Most consultancies sell advice; most internships offer busywork.</p>'
      '<p>We built Woways to do the opposite — run real work for companies, and staff it with talent that grows by doing. Our mission is to be the execution layer that helps companies grow, and the launchpad where careers get built.</p></div>'
      '</div></section>')
    b += '<section class="bg-paperBg py-20 lg:py-24 border-b border-borderLine" id="ecosystem"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("The ecosystem model","One partner. Two engines of growth.","Companies need execution and pipeline. Talent needs real experience. Woways connects the two into a single virtuous cycle.")
    b += ('<div class="grid grid-cols-1 md:grid-cols-2 gap-6 reveal">'
      '<div class="bg-white border border-borderLine p-8"><div class="w-full h-1 bg-brandTeal mb-6"></div>'
      '<span class="cap text-slate-500">For companies</span><h3 class="hd3 text-brandNavy mt-2 mb-4" style="font-size:20px">Scale without adding overhead</h3><ul class="space-y-3.5">%s</ul></div>'
      '<div class="bg-white border border-borderLine p-8"><div class="w-full h-1 bg-brandOrange mb-6"></div>'
      '<span class="cap text-slate-500">For Wowers</span><h3 class="hd3 text-brandNavy mt-2 mb-4" style="font-size:20px">Build a career on real work</h3><ul class="space-y-3.5">%s</ul></div></div>' % (cl,wl))
    b += '</div></section>'
    b += '<section class="bg-white py-20 lg:py-24 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("How we operate","What we stand for.","")
    values=[("bolt","Delivery over decks","We run the work and are measured on outcomes, not slideware."),
      ("verified","Honesty over hype","Intended value, stated plainly — no inflated claims or fake metrics."),
      ("hub","Growth for both sides","Every engagement builds a company and a career at the same time.")]
    vcards=''.join('<div class="bg-paperBg border border-borderLine p-7 card-lift"><span class="material-symbols-outlined text-brandTeal mb-4 block" aria-hidden="true">%s</span><h3 class="hd3 text-brandNavy mb-2" style="font-size:18px">%s</h3><p class="text-sm text-slate-600">%s</p></div>'%(ic,h,p) for ic,h,p in values)
    b += '<div class="grid grid-cols-1 md:grid-cols-3 gap-6 stagger reveal">%s</div></div></section>'%vcards
    b += '<section id="products" class="bg-paperBg py-20 lg:py-24 border-b border-borderLine"><div class="max-w-[1440px] mx-auto px-6 lg:px-12">'
    b += sec_head("Our products","Products we build ourselves.","The technology side of Woways, shipped as live products. Each opens in its own portal.")
    b += '<div class="flex items-center gap-3 mb-6 reveal"><span class="cap text-slate-500">Education &amp; Career</span><div class="h-px bg-borderLine flex-1"></div></div>'+product_cards('edu')
    b += '<div class="flex items-center gap-3 mb-6 mt-12 reveal"><span class="cap text-slate-500">Business Systems</span><div class="h-px bg-borderLine flex-1"></div></div>'+product_cards('biz')
    b += '</div></section>'
    b += cta_band()
    return page("Woways — About","about.html",b)

def build_contact():
    opts=["Execution support (sales, marketing, ops, HR, tech)","Join as a Wower","Talent Ignition","Student Mentor","College Macha","Bispun","Performance Portal","Become a mentor","Not sure yet"]
    os_=''.join('<option>%s</option>'%o for o in opts)
    reassure=["One short form. No sales call unless you ask for one.","We reply from a real person on the Woways team, not an inbox.","We'll get back to you within one business day."]
    rl=''.join('<div class="flex items-start gap-3 text-slate-300">%s<span>%s</span></div>'%(CHECK,x) for x in reassure)
    b = ('<section class="bg-brandNavy text-white"><div class="absolute inset-0"></div>'
      '<div class="max-w-[1440px] mx-auto px-6 lg:px-12 py-20 grid grid-cols-1 lg:grid-cols-2 gap-12 items-start">'
      '<div class="herofade">%s<h1 class="hd1 text-white mb-5" style="font-size:clamp(30px,4.5vw,48px)">Let\'s work out where you need us.</h1>'
      '<p class="lead text-slate-300 mb-8 max-w-xl">Tell us a little about your company and what you\'re trying to get done. We\'ll come back with where Woways fits — execution support, one of our products, or both.</p>'
      '<div class="space-y-4">%s</div></div>'
      '<form class="bg-white p-8 lg:p-10 herofade" novalidate onsubmit="event.preventDefault();document.getElementById(\'ok\').classList.remove(\'hidden\');this.reset();">'
      '<div id="ok" class="hidden mb-5 p-4 bg-brandTealTint text-brandTealDark text-sm border border-teal-200">Thank you. Our team will get back to you within one business day.</div>'
      '<div class="grid grid-cols-1 md:grid-cols-2 gap-5">'
      '<div><label class="cap text-slate-600 block mb-1.5" for="c-name">Your name</label><input id="c-name" required class="w-full h-11 px-3.5 border border-borderLine text-brandNavy" autocomplete="name"/></div>'
      '<div><label class="cap text-slate-600 block mb-1.5" for="c-desig">Designation</label><input id="c-desig" class="w-full h-11 px-3.5 border border-borderLine text-brandNavy" autocomplete="organization-title"/></div></div>'
      '<div class="grid grid-cols-1 md:grid-cols-2 gap-5 mt-5">'
      '<div><label class="cap text-slate-600 block mb-1.5" for="c-email">Email</label><input id="c-email" type="email" required class="w-full h-11 px-3.5 border border-borderLine text-brandNavy" autocomplete="email"/></div>'
      '<div><label class="cap text-slate-600 block mb-1.5" for="c-phone">Phone number</label><input id="c-phone" class="w-full h-11 px-3.5 border border-borderLine text-brandNavy" autocomplete="tel"/></div></div>'
      '<div class="mt-5"><label class="cap text-slate-600 block mb-1.5" for="c-org">Company / entity name</label><input id="c-org" class="w-full h-11 px-3.5 border border-borderLine text-brandNavy" autocomplete="organization"/></div>'
      '<div class="mt-5"><label class="cap text-slate-600 block mb-1.5" for="c-int">What are you looking for?</label><select id="c-int" required class="w-full h-11 px-3.5 border border-borderLine text-brandNavy"><option value="">Select one</option>%s</select></div>'
      '<div class="mt-5"><label class="cap text-slate-600 block mb-1.5" for="c-msg">Tell us briefly what you need</label><textarea id="c-msg" rows="3" class="w-full p-3.5 border border-borderLine text-brandNavy"></textarea></div>'
      '<label class="flex items-start gap-2.5 mt-5 text-sm text-slate-600"><input type="checkbox" required class="mt-1"/> <span>I agree to Woways contacting me about this enquiry and to the privacy policy.</span></label>'
      '<button type="submit" class="mt-6 w-full bg-brandTeal hover:bg-brandTealDark text-white text-sm font-semibold py-4 transition-colors">Send request</button>'
      '</form></div></section>' % (eyebrow("Talk to the Woways team"), rl, os_))
    return page("Woways — Contact","contact.html",b)

pages={'index.html':build_index(),'companies.html':build_companies(),'wowers.html':build_wowers(),
       'services.html':build_services(),'about.html':build_about(),'contact.html':build_contact()}
import os
for fn,html in pages.items():
    open(fn,'w',encoding='utf-8').write(html)
    print('wrote',fn,round(len(html)/1024),'KB')
# remove stale extra pages so nav stays consistent
for extra in ['solutions.html','product.html','wowers2.html']:
    if os.path.exists(extra): os.remove(extra); print('removed',extra)
print('done')
