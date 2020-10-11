import urllib.request


url = "https://hwcdn.libsyn.com/p/2/9/3/293daf4be9059198/Star_Trek_Outpost-Episode_1-What_Could_Be_So_Bad.mp3?c_id=4712145&cs_id=4712145&expiration=1602201478&hwt=ebb4668b71c4ed5598531ea63937aa66"

file_name = 'content.mp3'
u = urllib.request.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.get("Content-Length")[0])
print("Downloading: %s Bytes: %s" % (file_name, file_size))

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print(status)

f.close()
