import requests
import pandas as pd

from pandas import json_normalize

def request_specific_annuncio_from_pvp(id_annuncio : int) -> requests.Request:
    
    '''
    Request single annuncio from PVP

    '''
    annuncio_request_response = session.get(f"https://pvp.giustizia.it/ve-3f723b85-986a1b71/ve-ms/vendite/{id_annuncio}")

    return annuncio_request_response

def parse_info_from_annuncio(annuncio_response : requests.Request) -> None:

    '''
    Parse request response and normalize json to extract all infos about annuncio
    '''

    response_body = annuncio_response.json()["body"]

    df_annuncio = json_normalize(response_body)
    dfs_annuncio_list.append(df_annuncio)

    source_key = df_annuncio["idVendita"].item()

    if "allegati" in df_annuncio.columns:
        if df_annuncio["allegati"].notna().any():
            df_allegati = json_normalize(df_annuncio["allegati"].explode())
            df_allegati["source_id"] = source_key
            dfs_allegati_list.append(df_allegati)
    
    if "eventiSignificativiEstesi" in df_annuncio.columns:
        if df_annuncio["eventiSignificativiEstesi"].notna().any():
            df_eventi_significativi = json_normalize(df_annuncio["eventiSignificativiEstesi"].explode())
            df_eventi_significativi["source_id"] = source_key
            dfs_eventi_significativi_list.append(df_eventi_significativi)

    if "siti" in df_annuncio.columns:
        if df_annuncio["siti"].notna().any():
            df_pubblicità = json_normalize(df_annuncio["siti"].explode())
            df_pubblicità["source_id"] = source_key
            dfs_pubblicità_list.append(df_pubblicità)
    
    if "soggetti" in df_annuncio.columns:
        if df_annuncio["soggetti"].notna().any():
            df_soggetti = json_normalize(df_annuncio["soggetti"].explode())
            df_soggetti["source_id"] = source_key
            dfs_soggetti_list.append(df_soggetti)
    
    if "beni" in df_annuncio.columns:
        if df_annuncio["beni"].notna().any():
            df_beni = json_normalize(df_annuncio["beni"].explode())
            df_beni["source_id"] = source_key
            dfs_beni_list.append(df_beni)

            #Gli allegati degli allegati (immagini) sono disponibili al path https://pvp-documenti.apps.pvc-os-caas01-rs.polostrategiconazionale.it/ + allegati.linkAllegato
            if "allegati" in df_beni.columns:
                if df_beni["allegati"].notna().any():
                    df_exploded_allegati = df_beni.explode("allegati")
                    df_allegati_bene = pd.json_normalize(df_exploded_allegati["allegati"].to_list())
                    df_allegati_bene["idBene"] = df_exploded_allegati["idBene"].values
                    dfs_allegati_bene_list.append(df_allegati_bene)

                    #Exploded n:m
                    # df_allegati_bene = pd.json_normalize(df_beni.explode("allegati").to_dict(orient="records"))
            
            if "datiCatastali" in df_beni.columns:  #2131863
                if df_beni["datiCatastali"].notna().any():
                    df_exploded_dati_catastali = df_beni.explode("datiCatastali")
                    # df_dati_catastali = pd.json_normalize(df_exploded_allegati["datiCatastali"].to_list())
                    df_dati_catastali = json_normalize(df_beni["datiCatastali"].explode())  #Ok?
                    df_dati_catastali["idBene"] = df_exploded_dati_catastali["idBene"].values
                    
                    dfs_dati_catastali_list.append(df_dati_catastali)
                    
                    #Exploded n:m
                    # df_dati_catastali = pd.json_normalize(df_beni.explode("datiCatastali").to_dict(orient="records"))
    
def cycle_annnci(df_annunci : pd.DataFrame):

    #Annunci lists
    global dfs_annuncio_list
    global dfs_allegati_list
    global dfs_eventi_significativi_list
    global dfs_pubblicità_list
    global dfs_soggetti_list
    global dfs_beni_list
    global dfs_allegati_bene_list
    global dfs_dati_catastali_list

    #Annunci lists
    dfs_annuncio_list = []
    dfs_allegati_list = []
    dfs_eventi_significativi_list = []
    dfs_pubblicità_list = []
    dfs_soggetti_list = []
    dfs_beni_list = []
    dfs_allegati_bene_list = []
    dfs_dati_catastali_list = []

    #Cycle all annuncio in annunci extraction
    for id_annuncio in df_annunci["id"]:

        annuncio_response = request_specific_annuncio_from_pvp(id_annuncio)
        parse_info_from_annuncio(annuncio_response)

def run_cycle_annuncio_in_annunci(df_annunci : pd.DataFrame) -> list:

    '''
    Cycle annuncio found in annunci bulk request
    '''

    global session

    session = requests.session()

    cycle_annnci(df_annunci)

    dfs_annunci_list =  [dfs_annuncio_list, dfs_allegati_list, dfs_eventi_significativi_list, dfs_pubblicità_list, dfs_soggetti_list, dfs_beni_list, dfs_allegati_bene_list, dfs_dati_catastali_list]

    return dfs_annunci_list

if __name__ == "__main__":
    run_cycle_annuncio_in_annunci()
    

