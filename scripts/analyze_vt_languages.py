import zipfile, os, re, json
p=r'C:\Users\Mateus\Desktop\vistrailss\exemplos'
summary=[]
for f in sorted(os.listdir(p)):
    if not f.lower().endswith('.vt'):
        continue
    path=os.path.join(p,f)
    info={'file':f,'filesize':os.path.getsize(path),'packages':[], 'hints':[]}
    try:
        with zipfile.ZipFile(path) as z:
            # find the vistrail xml member
            candidate=None
            for m in z.namelist():
                if 'vistrail' in m.lower():
                    candidate=m
                    break
            if candidate is None:
                candidate=z.namelist()[0]
            data=z.read(candidate).decode('utf-8','replace')
            # search for package="..."
            pkgs=re.findall(r'package\s*=\s*"([^"]+)"',data)
            info['packages']=sorted(set(pkgs))
            # search common keywords
            hints=[]
            for kw in ['python','matplotlib','vtk','sklearn','scikit','mongo','mongodb','http','webservice','julia','basic','numpy','pandas']:
                if kw.lower() in data.lower():
                    hints.append(kw)
            info['hints']=sorted(set(hints))
    except Exception as e:
        info['error']=str(e)
    summary.append(info)
print(json.dumps(summary,ensure_ascii=False,indent=2))
