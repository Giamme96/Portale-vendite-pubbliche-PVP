import requests
import pandas as pd

from pandas import json_normalize

def request_annunci_from_pvp(size : int) -> requests.Request:

    '''
    Bulk request to PVP (only RE assets), size(n° annunci seems not be capped, CAREFUL, could be limited/cause problems if size -> high number)

    '''

    url = "https://pvp.giustizia.it/ric-496b258c-986a1b71/ric-ms/ricerca/vendite"
    payload = {
        "language": "it",
        "codTipoLotto" : "IMMOBILI",
        # "size": "100",
        # "page": 0,
        # "sort" : "dataOraVendita,asc",
        # "sort" : "citta,asc",
    }
    params = {
        "size": size,
        "page": 0,
        # "sort": "dataOraVendita,asc"  # o "citta,asc"
    }

    annunci_request_response = session.post(url, json=payload, params=params)

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

    session = requests.session()

    bulk_request_response = request_annunci_from_pvp(size)
    df_annunci = parse_annunci_from_request_response(bulk_request_response)
    # df_annunci.to_excel("Output/Export_df_annunci.xlsx", index=False)
    return df_annunci

# Questo permette di eseguire il codice solo quando script1.py è eseguito direttamente
if __name__ == "__main__":
    run_bulk_request()