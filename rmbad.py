


fn = 'allpost.xml'
n_fn = 'allpost-k.xml'
tmp = ''
with open(fn, 'r', encoding='utf-8') as f:
	tmp = f.read()

blk = u'\ufe0f\u3000\u2764\ufe0f\u200d\u00a0\u202c\ufffc\uffef\u2800\u200b\ufeff\u202a'
for b in blk:
	tmp = tmp.replace(b,u' ')

with open(n_fn, 'w', encoding='utf-8') as f:
	f.write(tmp)