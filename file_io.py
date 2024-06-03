def save_list_to_file(file_name, l):
    with open(file_name, 'w') as f:
       f.write('')
    for i in l:
      with open(file_name, 'a') as f:
        s = ' '.join(i)
        f.write(s + '\n')

def read_list_from_file(file_name, is_numlist=False):
    s = []
    with open(file_name, 'r') as f:
          for line in f:
            s_l = line.strip().split()
            if is_numlist:
               if s_l[0] == '#':
                  continue
               else:
                  s_l = [int(s_l[0]), ' '.join(s_l[1:])]
            s.append(s_l)
    return s

def get_webhook():
    with open("webhook.txt", 'r') as f:
        line = f.readline()
    return line.strip()

#save_list_to_file("test.txt", [["a", "b", "c"]])
#print(read_list_from_file("data_numlist.txt", is_numlist=True))