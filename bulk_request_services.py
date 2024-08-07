import requests
import pandas as pd
import numpy as np

from pandas import json_normalize

def request_annunci_from_pvp(size : int, page : int) -> requests.Request:

    '''
    Bulk request to PVP (only RE assets), size(n° annunci seems not be capped, CAREFUL, could be limited/cause problems if size -> high number)

    '''

    global bulk_iterations

    annunci_request_response = session.post("https://pvp.giustizia.it/ric-496b258c-986a1b71/ric-ms/ricerca/vendite", 
                                            json={"language" : "it", "tipoLotto" : "IMMOBILI"}, 
                                            params={"size" : size, "page" : page})
    
    #Compute numbers of iterations
    if page == 0:

        #Max elements
        # max_elements_in_pvp = annunci_request_response.json()["body"]["totalElements"]
        # bulk_iterations = int(np.ceil(max_elements_in_pvp / size))

        #Bypass max elements
        bulk_iterations = 5

    return annunci_request_response

def parse_annunci_from_request_response(annunci_request_response : requests.Request) -> pd.DataFrame:
    
    '''
    Parse request response and normalize json for cumulative annunci
    '''

    response_body = annunci_request_response.json()["body"]["content"]
    df_annunci = json_normalize(response_body)

    return df_annunci

def run_bulk_request(size : int) -> pd.DataFrame:

    global session
    global bulk_iterations

    session = requests.session()
    dfs_annunci_list = []

    bulk_iterations = 1
    annunci_page = 0

    while annunci_page < bulk_iterations:
        
        print(f"Annunci page: ({annunci_page} / {bulk_iterations}) x {size} specific annuncio")
              
        bulk_request_response = request_annunci_from_pvp(size, annunci_page)
        dfs_annunci_list.append(parse_annunci_from_request_response(bulk_request_response))

        annunci_page += 1

    df_annunci = pd.concat(dfs_annunci_list, axis=0)
    
    return df_annunci

if __name__ == "__main__":
    run_bulk_request()