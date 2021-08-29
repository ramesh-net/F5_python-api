import requests,json,os,argparse
from openpyxl import Workbook
from tqdm import tqdm

#Arguments
parser = argparse.ArgumentParser(description='Host info')
parser.add_argument('--host', dest='host', type=str, help='Hostname')
parser.add_argument('--token', dest='token', type=str, help='Token')
args = parser.parse_args()

# REST API Paramaters
base_url = "https://{}/mgmt/tm/ltm/".format(args.host)
payload={}
headers = {
    'Authorization': 'Basic {}'.format(args.token)
    }

#main fuction
def main():
    # Virtual server URI
    vs_url=base_url+'virtual/'
    response = requests.request("GET", vs_url, headers=headers, data=payload, verify=False)
    # If response code is not 200, fuction will return error code
    if response.status_code==200:
        vs_list=(json.loads(response.text))['items']
    else:
        print("Error code (VS): {}".format(response.status_code))
        return None
    #Create a new workbook to save output in excel
    wb = Workbook()
    vip_details = wb.active
    vip_details.title = "Virtual server & Pool member info."
    f5_headers=['VirtualServer Name','Virtual IP','Pool Name','IP Address','State']
    vip_details.append(f5_headers)
    #List all virtual server in f5 Host
    for vs in tqdm(vs_list):
        try:
            pool_mem_url=base_url+'pool/{}/members/'.format(vs['pool'][8:])
            pool_mem_response = requests.request("GET", pool_mem_url, headers=headers, verify=False)
            if pool_mem_response.status_code==200:
                pool_members=(json.loads(pool_mem_response.text))['items']
                #Append all members in pool to excel file 
                for member in pool_members:
                    line = [vs['name'],vs['destination'][8:],vs['pool'][8:],member['address'],member['state']]
                    vip_details.append(line)
            else:
                member['address']=member['state']='Member unavailable' 
                line = [vs['name'],vs['destination'][8:],vs['pool'][8:],member['address'],member['state']]
                vip_details.append(line)
                
        #if pool is not attached to VS, exception will be raised
        except KeyError:
            try:
                line = [vs['name'],vs['destination'][8:],'','','']
                vip_details.append(line)
            except Exception as e:
                print ("Error: ", e)

    filename=args.host+"_vip_info.xlsx"
    wb.save(filename)
    print("Completed")
    print("File Location: ", os.path.abspath(filename))


if __name__ == "__main__":
    main()
