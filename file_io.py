import configparser
import os

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

def read_or_create_config(fname='config.cfg'):
    cfg_p = configparser.ConfigParser()

    if os.path.exists(fname):
        cfg_p.read(fname)
        if 'general' in cfg_p and 'threshold_notification' in cfg_p['general']:
            try:
                threshold_notification = int(cfg_p['general']['threshold_notification'])
                notification_level = int(cfg_p['general']['notification_level'])
                extra_notification = int(cfg_p['general']['extra_notification'])

                if 1 <= notification_level <= 3 and 50 <= threshold_notification <= 100:
                  None
                else:
                  print('The value of notification_level is out of the valid range (1-3).')
                  print('The value of threshold_notification is out of the valid range (50-100).')
                  return 
                
                if extra_notification > threshold_notification:
                   print('The value of extra_notification must be less than threshold_notification.')
                   return 
                else:
                   return threshold_notification, notification_level, extra_notification
                   
        
            except ValueError:
                print('The value of threshold_notification is not an integer.')
                return None
        else:
            print('threshold_notification not found in the [general] section.')
            return None
    else:
        cfg_p['general'] = {
            'threshold_notification': '90',
            'notification_level': '1',
            'extra_notification': '85'
        }
        with open(fname, 'w') as f:
            cfg_p.write(f)
        print(f'Config file {fname} created.')
        exit()

