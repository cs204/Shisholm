def tchk(a):
    b=""
    a = a[::-1]
    for i in range(0,len(a),):
        if a[i]!='.':
            b+=a[i]
        else:
            return(b[::-1])
            break
    return(b[::-1])

def opr_type(v):
    if v=='gif': return 'image/gif'
    if v=='jpg': return 'image/jpeg'
    if v=='jpeg': return 'image/jpeg'
    if v=='png': return 'image/png'
    if v=='pdf': return 'application/pdf'
    if v=='txt': return 'text/txt'
    if v=='zip': return 'application/zip'


a = str(input("File name: "))

form = tchk(a)
print(opr_type(form))
