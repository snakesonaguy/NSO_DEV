import requests
import json

# Global variables for the devNet sandbox instance of NSO
NSO_HOST = 'https://sandbox-nso-1.cisco.com'
USERNAME = 'developer'
PASSWORD =  'Services4Ever'
AUTH = (USERNAME, PASSWORD)
VERIFY = False
HEADERS = {'Content-type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}

def get_verify_restconf():
    path = NSO_HOST + '/restconf'
    r = requests.get(path, auth=AUTH,headers=HEADERS, params=None, verify=VERIFY)
    if r.status_code == 200:
        ret = (json.loads(r.text))
        print(json.dumps(ret, indent=4))
    else:
        print('Error Code: {}'.format(r.status_code))

def get_device_groups():
    path = NSO_HOST + '/restconf/data/tailf-ncs:devices/device-group'
    r = requests.get(path, auth=AUTH, headers=HEADERS, params=None, verify=False)
    if r.status_code == 200:
        ret = (json.loads(r.text))
        # print(json.dumps(ret, indent=4))
        groups = ret['tailf-ncs:device-group']
        for g in groups:
            print('Group Name: {}'.format(g['name']))
            print('\tMembers: ')
            for m in g['member']:
                print('\t\t{}'.format(m))
    else:
        print('Error Code: {}'.format(r.status_code))


def main():
    # get_verify_restconf()
    get_device_groups()



if __name__ == '__main__':
    main()