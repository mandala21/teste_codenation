import cript


c = cript.CriptJulio(3)

original_text = 'a ligeira raposa marrom saltou sobre o cachorro cansado'

rs_cript = c.cript(original_text)

hash_sha1 = c.generate_sha1(rs_cript)

print(original_text)

print(rs_cript)

print(hash_sha1)
