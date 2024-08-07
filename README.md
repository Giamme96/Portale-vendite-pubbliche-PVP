# Portale-vendite-pubbliche-PVP

Il progetto PVP ha l'obiettivo di far conoscere al pubblico il portale gestito dal Ministero della Giustizia relativo alle aste pubbliche. 

## Introduzione

Nel 2024, il portale è stato ammodernato con significative integrazioni al back-end. Precedentemente, il portale era interamente basato su HTML statico, ma con il nuovo aggiornamento, è in grado di restituire risposte in formato JSON quando interrogato correttamente. Questo cambiamento facilita l'accesso e l'integrazione delle informazioni sulle aste pubbliche in applicazioni e sistemi esterni.

Questo repository contiene il codice e la documentazione necessari per interagire con il nuovo portale, permettendo agli sviluppatori di accedere ai dati delle aste in modo programmatico e di integrare tali dati nelle proprie applicazioni.

Tramite il codice proposto è possibile scaricare tutto il database del PVP. Il portale è così composto:
- Home page con possibilità di scegliere diversi tipi di asset (nel codice verrà preso in considerazione solo il Real Estate)
- Ogni annuncio è identificato come lotto, quindi può avere al suo interno più assets
- Il portale restituisce anche le righe di storico (esperimenti di vendita) questi non sono stati appositamente integrati nel codice per due motivi principali:
    - Non tutti gli esperimenti di vendita su un bene registrano tutti gli altri esperimenti di vendita, oltretutto gli stessi beni cambiano di ID
    - Tutti gli esperimenti di vendita sono comunque censiti come annunci (se si scarica tutto il db, avrai lo storico completo)
- La "size" della pagina degli annunci non sembra essere limitata, (eg. ho testato 1k annunci e restituiva il risultato correttamente). A vostra discrezione l'ammontare che inserite.

## Indice

- [Introduzione](#introduzione)
- [Installazione](#installazione)
- [Licenza](#licenza)
- [Disclaimer](#disclaimer)

## Installazione

### Istruzioni

Passaggi per installare il progetto:

- Clone del repo
- Install delle dependencies

```bash
pip install -r requirements.txt
```

## Disclaimer

Il codice e la documentazione presenti in questo repository sono forniti esclusivamente a scopo informativo e documentale. Questo progetto non è destinato all'uso commerciale, né garantiamo che sia adatto per qualsiasi specifico utilizzo commerciale. Gli autori non si assumono alcuna responsabilità per eventuali danni diretti o indiretti derivanti dall'uso di questo codice.

Utilizzando il codice presente in questo repository, accetti che:

1. **Nessuna Garanzia**: Il codice è fornito "così com'è", senza garanzia di alcun tipo, espressa o implicita, incluse, ma non limitate a, le garanzie di commerciabilità, idoneità per un particolare scopo e non violazione. Gli autori non garantiscono che il codice sia privo di errori o che funzionerà in modo ininterrotto.

2. **Uso a Proprio Rischio**: L'uso del codice è interamente a tuo rischio. Gli autori non saranno responsabili per eventuali reclami, danni, perdite o altre responsabilità, sia in un'azione di contratto, torto o altro, derivanti da, o in connessione con il codice o l'uso o altri rapporti nel codice.

3. **Scopo Informativo**: Questo progetto è inteso solo per fini educativi e di documentazione. Non è stato sottoposto a controlli rigorosi di sicurezza, quindi non dovrebbe essere utilizzato in ambienti di produzione o per scopi sensibili. Gli autori non garantiscono che il codice sia adatto per qualsiasi specifico utilizzo, né che rispetti normative o requisiti legali applicabili.

4. **Nessun Supporto Ufficiale**: Gli autori non sono obbligati a fornire supporto, aggiornamenti, correzioni di bug o nuove funzionalità per questo progetto. Qualsiasi supporto fornito sarà a totale discrezione degli autori.

Si prega di leggere e comprendere completamente questi termini prima di utilizzare il codice. Se non si è d'accordo con questi termini, si prega di non utilizzare il codice.

Per ulteriori domande, contatta [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/tuo-profilo-linkedin)

