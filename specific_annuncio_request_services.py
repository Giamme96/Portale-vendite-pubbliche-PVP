import requests
import pandas as pd

from pandas import json_normalize

#TODO -> aggiugnere vendite precedenti se presenti

def request_specific_annuncio_from_pvp(id_annuncio : int) -> requests.Request:
    
    '''
    Request single annuncio from PVP

    '''
    annuncio_request_response = session.get(f"https://pvp.giustizia.it/ve-3f723b85-986a1b71/ve-ms/vendite/{id_annuncio}")

    return annuncio_request_response

def request_esperimento_for_annuncio(idLotto_annuncio : int) -> requests.Request:
    '''
    Looking for esperimenti d'asta for idLotto in annuncio

    '''
    esperimento_request_response = session.get(f"https://pvp.giustizia.it/ve-3f723b85-986a1b71/ve-ms/vendite/lotti/{idLotto_annuncio}/vendite-precedenti")

    return esperimento_request_response

def parse_info_from_annuncio(annuncio_response : requests.Request) -> int:

    '''
    Parse request response and normalize json to extract all infos about annuncio
    '''

    response_body = annuncio_response.json()["body"]

    df_annuncio = json_normalize(response_body)
    dfs_annunci_annuncio_list.append(df_annuncio)

    source_key = df_annuncio["idVendita"].item()

    if "allegati" in df_annuncio.columns:
        df_allegati = json_normalize(df_annuncio["allegati"].explode())
        df_allegati["source_id"] = source_key
        dfs_annunci_allegati_list.append(df_allegati)
    
    if "eventiSignificativiEstesi" in df_annuncio.columns:
        df_eventi_significativi = json_normalize(df_annuncio["eventiSignificativiEstesi"].explode())
        df_eventi_significativi["source_id"] = source_key
        dfs_annunci_eventi_significativi_list.append(df_eventi_significativi)

    if "siti" in df_annuncio.columns:
        df_pubblicità = json_normalize(df_annuncio["siti"].explode())
        df_pubblicità["source_id"] = source_key
        dfs_annunci_pubblicità_list.append(df_pubblicità)
    
    if "soggetti" in df_annuncio.columns:
        df_soggetti = json_normalize(df_annuncio["soggetti"].explode())
        df_soggetti["source_id"] = source_key
        dfs_annunci_soggetti_list.append(df_soggetti)
    
    if "beni" in df_annuncio.columns:
        df_beni = json_normalize(df_annuncio["beni"].explode())
        df_beni["source_id"] = source_key
        dfs_annunci_beni_list.append(df_beni)

        if "allegati" in df_beni.columns:
            df_allegati_bene = json_normalize(df_beni["allegati"].explode())
            df_allegati_bene["id_bene"] = df_beni["idBene"].item()
            dfs_annunci_allegati_bene_list.append(df_allegati_bene)
        
        if "datiCatastali" in df_beni.columns:
            df_dati_catastali = json_normalize(df_beni["datiCatastali"].explode())
            df_dati_catastali["id_bene"] = df_beni["idBene"].item()
            dfs_annunci_dati_catastali_list.append(df_dati_catastali)

    return df_annuncio["lotto.idLotto"].item()

def cycle_esperimento(df_esperimento : pd.DataFrame) -> None:

        for esperimento in df_esperimento:

            source_key = df_esperimento["idVendita"].item()

            if "allegati" in df_esperimento.columns:
                df_allegati = json_normalize(df_esperimento["allegati"].explode())
                df_allegati["source_id"] = source_key
                dfs_esperimenti_allegati_list.append(df_allegati)
            
            if "altriSiti" in df_esperimento.columns:
                df_altri_siti = json_normalize(df_esperimento["altriSiti"].explode())
                df_altri_siti["source_id"] = source_key
                dfs_esperimenti_altri_siti_list.append(df_altri_siti)
            
            if "siti" in df_esperimento.columns:
                df_pubblicità = json_normalize(df_esperimento["siti"].explode())
                df_pubblicità["source_id"] = source_key
                dfs_esperimenti_pubblicità_list.append(df_pubblicità)
            
            if "soggetti" in df_esperimento.columns:
                df_soggetti = json_normalize(df_esperimento["soggetti"].explode())
                df_soggetti["source_id"] = source_key
                dfs_esperimenti_soggetti_list.append(df_soggetti)
            
            if "beni" in df_esperimento.columns:
                df_beni = json_normalize(df_esperimento["beni"].explode())
                df_beni["source_id"] = source_key
                dfs_esperimenti_beni_list.append(df_beni)
                
                if "allegati" in df_beni.columns:
                    df_allegati_bene = json_normalize(df_beni["allegati"].explode())
                    df_allegati_bene["id_bene"] = df_beni["idBene"].item()
                    dfs_esperimenti_allegati_bene_list.append(df_allegati_bene)
                
                if "datiCatastali" in df_beni.columns:
                    df_dati_catastali = json_normalize(df_beni["datiCatastali"].explode())
                    df_dati_catastali["id_bene"] = df_beni["idBene"].item()
                    dfs_esperimenti_dati_catastali_list.append(df_dati_catastali)

def parse_info_from_esperimento(esperimento_response : requests.Request) -> None:        #2122200
    
    '''
    Parse request response and normalize json to extract all infos about esperimento (annuncio couln't have esperimento phase yet)
    '''
    
    response_body = esperimento_response.json()["body"]
    
    #Check annuncio w/o esperimenti
    if response_body == []:
        return
    
    df_esperimento = json_normalize(response_body)
    dfs_esperimenti_esperimento_list.append(df_esperimento)

    
def cycle_annnci(df_annunci : pd.DataFrame):

    #Annunci lists
    global dfs_annunci_annuncio_list
    global dfs_annunci_allegati_list
    global dfs_annunci_eventi_significativi_list
    global dfs_annunci_pubblicità_list
    global dfs_annunci_soggetti_list
    global dfs_annunci_beni_list
    global dfs_annunci_allegati_bene_list
    global dfs_annunci_dati_catastali_list

    #Esperimenti lists
    global dfs_esperimenti_esperimento_list
    global dfs_esperimenti_altri_siti_list
    global dfs_esperimenti_allegati_list
    global dfs_esperimenti_eventi_significativi_list
    global dfs_esperimenti_pubblicità_list
    global dfs_esperimenti_soggetti_list
    global dfs_esperimenti_beni_list
    global dfs_esperimenti_allegati_bene_list
    global dfs_esperimenti_dati_catastali_list

    #Annunci lists
    dfs_annunci_annuncio_list = []
    dfs_annunci_allegati_list = []
    dfs_annunci_eventi_significativi_list = []
    dfs_annunci_pubblicità_list = []
    dfs_annunci_soggetti_list = []
    dfs_annunci_beni_list = []
    dfs_annunci_allegati_bene_list = []
    dfs_annunci_dati_catastali_list = []

    #esperimenti lists
    dfs_esperimenti_esperimento_list = []
    dfs_esperimenti_altri_siti_list = []
    dfs_esperimenti_allegati_list = []
    dfs_esperimenti_eventi_significativi_list = []
    dfs_esperimenti_pubblicità_list = []
    dfs_esperimenti_soggetti_list = []
    dfs_esperimenti_beni_list = []
    dfs_esperimenti_allegati_bene_list = []
    dfs_esperimenti_dati_catastali_list = []
    
    #Cycle all annuncio in annunci extraction
    for id_annuncio in df_annunci["id"]:

        annuncio_response = request_specific_annuncio_from_pvp(id_annuncio)
        id_lotto_annuncio = parse_info_from_annuncio(annuncio_response)

        esperimento_response = request_esperimento_for_annuncio(id_lotto_annuncio)
        parse_info_from_esperimento(esperimento_response)

def run_cycle_annuncio_in_annunci(df_annunci : pd.DataFrame) -> list:

    '''
    Cycle annuncio found in annunci with is relative auction esperimento
    '''

    global session

    session = requests.session()

    cycle_annnci(df_annunci)

    dfs_annunci_list =  [dfs_annunci_annuncio_list, dfs_annunci_allegati_list, dfs_annunci_eventi_significativi_list, dfs_annunci_pubblicità_list, dfs_annunci_soggetti_list, dfs_annunci_beni_list, dfs_annunci_allegati_bene_list, dfs_annunci_dati_catastali_list]
    dfs_esperimenti_list=  [dfs_esperimenti_esperimento_list, dfs_esperimenti_altri_siti_list, dfs_esperimenti_allegati_list, dfs_esperimenti_eventi_significativi_list, dfs_esperimenti_pubblicità_list, dfs_esperimenti_soggetti_list, dfs_esperimenti_beni_list, dfs_esperimenti_allegati_bene_list, dfs_esperimenti_dati_catastali_list]

    return dfs_annunci_list, dfs_esperimenti_list

if __name__ == "__main__":
    run_cycle_annuncio_in_annunci()
    

