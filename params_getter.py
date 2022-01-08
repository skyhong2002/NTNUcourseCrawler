

def enter():
  print("Enter/Paste your content. Ctrl-Z to save it. strings:")
  contents = []
  while True:
    try:
      line = input()
    except EOFError:
      break
    contents.append(line)
  return contents
  


  
  

head = 's.headers.update({'  
tail = '})'


cont = enter()
body = ''

for c in cont:
  tmp = '\'' + c.replace(': ', '\':\'') + '\',\n'
  pat = len(head)*' '
  tmp += pat
  body += tmp
  
header = head + body[:-(2+len(head))] + tail

print(header)
  
