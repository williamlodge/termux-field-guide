from pathlib import Path
import re, shutil
root=Path(__file__).resolve().parents[1]; out=root/'_site'
if out.exists(): shutil.rmtree(out)
out.mkdir()
for p in root.iterdir():
    if p.name in {'.git','_site'}: continue
    dst=out/p.name
    if p.is_dir(): shutil.copytree(p,dst,ignore=shutil.ignore_patterns('_site'))
    else: shutil.copy2(p,dst)
idx=out/'index.html'; s=idx.read_text(encoding='utf-8')
s=re.sub(r'<meta name="version" content="[^"]*">','<meta name="version" content="1.1.0">',s)
if 'name="last-updated"' not in s: s=s.replace('</head>','<meta name="last-updated" content="2026-08-30">\n<link rel="manifest" href="./manifest.webmanifest">\n<link rel="stylesheet" href="./pwa.css">\n<link rel="apple-touch-icon" href="./icons/apple-touch-icon.png">\n</head>')
if './pwa-enhance.js' not in s: s=s.replace('</body>','<script src="./pwa-enhance.js" defer></script>\n</body>')
idx.write_text(s,encoding='utf-8')
