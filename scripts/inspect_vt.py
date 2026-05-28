import zipfile, os, json
p=r'C:\Users\Mateus\Desktop\vistrailss\exemplos'
out=[]
for f in sorted(os.listdir(p)):
    if f.lower().endswith('.vt'):
        path=os.path.join(p,f)
        try:
            with zipfile.ZipFile(path) as z:
                members=z.namelist()
                total_files=len(members)
                out.append({'file':f,'filesize':os.path.getsize(path),'total_files':total_files,'members_first10':members[:10]})
        except Exception as e:
            out.append({'file':f,'filesize':os.path.getsize(path),'error':str(e)})
print(json.dumps(out,ensure_ascii=False,indent=2))
