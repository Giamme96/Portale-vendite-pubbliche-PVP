# Portale-vendite-pubbliche-PVP [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/gian-maria-lunghi-24376b163/)

Il progetto PVP ha l'obiettivo di far conoscere al pubblico il portale gestito dal Ministero della Giustizia relativo alle aste pubbliche e un modo per scaricare in locale le informazioni su questo pubblicate.

## Indice

- [Introduzione](#introduzione)
- [Uso](#uso)
- [Installazione](#installazione)
- [Licenza](#licenza)
- [Disclaimer](#disclaimer)

## Introduzione

Nel 2024, il portale è stato ammodernato con significative integrazioni al back-end. Precedentemente, le informazioni "scaricabili" del portale erano interamente basate su HTML statico, ma con il nuovo aggiornamento, è in grado di restituire risposte in formato JSON quando interrogato. Questo cambiamento facilita l'accesso e l'integrazione delle informazioni sulle aste pubbliche in applicazioni e sistemi esterni.

![Panoramica_annunci](https://github.com/user-attachments/assets/f70f7a4b-9186-437f-8066-3d0a11145bb0)

## Uso
Tramite il codice proposto è possibile scaricare tutto il database del PVP. Il portale è così composto:
- Home page con possibilità di scegliere diversi tipi di asset (nel codice verrà preso in considerazione solo il Real Estate)
- Ogni annuncio è identificato come lotto, quindi può avere al suo interno più assets
- Il portale restituisce anche le righe di storico (esperimenti di vendita) questi non sono stati appositamente integrati nel codice per due motivi principali:
    - Non tutti gli esperimenti di vendita su un bene registrano tutti gli altri esperimenti di vendita, oltretutto gli stessi beni cambiano di ID
    - Tutti gli esperimenti di vendita sono comunque censiti come annunci (se si scarica tutto il db, avrai lo storico completo)
- La *size* della pagina degli annunci non sembra essere limitata, (eg. ho testato 1k annunci e restituiva il risultato correttamente). A vostra discrezione l'ammontare che inserite
- Le *bulk_iterations* sono limitate a 5 x *size*. Basta decommentare le righe di codice precedenti per avere il full db

```bash
#Max elements
# max_elements_in_pvp = annunci_request_response.json()["body"]["totalElements"]
# bulk_iterations = int(np.ceil(max_elements_in_pvp / size))

#Bypass max elements
bulk_iterations = 5
```

### Alcune info interessanti estraibili dal PVP
- ID procedure
- Prezzi
- Status annuncio
- Geolocalizzazione
- Dati catastali
- Superficie/vani e piano
- Allegati/documenti



## Installazione

Passaggi per installare il progetto:

- Clone del repo
- Install delle dependencies

```bash
pip install -r requirements.txt
```

## Licenza

Questo progetto è distribuito sotto la licenza MIT. Vedi il file [LICENSE](LICENSE) per ulteriori dettagli.

## Disclaimer

Il codice e la documentazione presenti in questo repository sono forniti esclusivamente a scopo informativo e documentale. Questo progetto non è destinato all'uso commerciale, né garantiamo che sia adatto per qualsiasi specifico utilizzo commerciale. Gli autori non si assumono alcuna responsabilità per eventuali danni diretti o indiretti derivanti dall'uso di questo codice.

Utilizzando il codice presente in questo repository, accetti che:

1. **Nessuna Garanzia**: Il codice è fornito "così com'è", senza garanzia di alcun tipo, espressa o implicita, incluse, ma non limitate a, le garanzie di commerciabilità, idoneità per un particolare scopo e non violazione. Gli autori non garantiscono che il codice sia privo di errori o che funzionerà in modo ininterrotto.

2. **Uso a Proprio Rischio**: L'uso del codice è interamente a tuo rischio. Gli autori non saranno responsabili per eventuali reclami, danni, perdite o altre responsabilità, sia in un'azione di contratto, torto o altro, derivanti da, o in connessione con il codice o l'uso o altri rapporti nel codice.

3. **Scopo Informativo**: Questo progetto è inteso solo per fini educativi e di documentazione. Non è stato sottoposto a controlli rigorosi di sicurezza, quindi non dovrebbe essere utilizzato in ambienti di produzione o per scopi sensibili. Gli autori non garantiscono che il codice sia adatto per qualsiasi specifico utilizzo, né che rispetti normative o requisiti legali applicabili.

4. **Nessun Supporto Ufficiale**: Gli autori non sono obbligati a fornire supporto, aggiornamenti, correzioni di bug o nuove funzionalità per questo progetto. Qualsiasi supporto fornito sarà a totale discrezione degli autori.

Si prega di leggere e comprendere completamente questi termini prima di utilizzare il codice. Se non si è d'accordo con questi termini, si prega di non utilizzare il codice.

Per ulteriori domande, contatta [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/gian-maria-lunghi-24376b163/)

