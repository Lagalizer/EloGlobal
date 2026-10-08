=== 1. Benvenuto
# Benvenuto in EloGlobal

EloGlobal è un traduttore in tempo reale per Discord e qualsiasi altra chat vocale. Tutto funziona sul tuo PC: il
riconoscimento vocale, la traduzione e le voci. Niente di ciò che qualcuno dice o scrive viene inviato su Internet.

- **Senti gli altri nella tua lingua.** L'app ascolta ciò che le persone dicono su Discord, lo scrive, lo traduce,
  mostra i sottotitoli e può leggerti la traduzione con una voce naturale.
- **Loro sentono te nella loro lingua.** Parli nel microfono. L'app traduce ciò che hai detto e lo pronuncia su
  Discord tramite un cavo audio virtuale.
- **Anche il testo.** Traduce i messaggi di Discord nei server, nei messaggi diretti e nei thread, qualsiasi testo
  che evidenzi con il mouse e il testo sullo schermo con l'OCR. Puoi anche scrivere nella loro lingua.
- **Gratis e privato.** Nessun account, nessun abbonamento e nessun servizio online. I modelli si scaricano una volta
  e poi funzionano senza Internet.

Questo manuale ha dodici capitoli. Usa i pulsanti Avanti e Precedente, oppure clicca un capitolo nell'elenco. Ogni
volta che cambi capitolo, il narratore interrompe il vecchio e legge il nuovo. Il narratore è una voce che funziona
sul tuo PC.

=== 2. Primo avvio
# Primo avvio

**Passo 1. Apri l'app.** Avvia EloGlobal dal menu Start o da Steam. La prima volta scegli la lingua dell'app. Tutto
è mostrato in quella lingua, e la guida e questo manuale vengono letti ad alta voce in quella lingua. Poi l'app
spiega cosa fa con le voci e i messaggi degli altri: tutto resta sul tuo PC. Dopo, un breve tour guidato ti mostra i
primi passi. Si apre solo questa prima volta; puoi rivederlo da questa scheda.

**Passo 2. Installa un cavo audio virtuale.** Installa VB-Audio Virtual Cable dal sito del produttore e riavvia il
PC. È di VB-Audio, non di EloGlobal, ed è gratis per uso personale. Windows ne ha bisogno per creare un microfono
virtuale.

**Passo 3. Configura Discord.** Apri Discord, poi Impostazioni utente, poi Voce e video.

- Dispositivo di input: CABLE Output, di VB-Audio Virtual Cable.
- Dispositivo di output: le tue cuffie.
- Disattiva Soppressione del rumore, Cancellazione dell'eco e Controllo automatico del guadagno.

**Passo 4. Configura l'app.** Tieni il profilo Standard, tutto su questo PC. Nella scheda Uscita, invia la tua voce
tradotta a CABLE Input. Nella scheda Ingresso, tieni il metodo Solo l'app Discord e scegli il tuo vero microfono.
Nella scheda Dal vivo, scegli le lingue. Poi premi Avvia, o il tasto F5.

**La prima volta che premi Avvia**, l'app scarica ciò che le serve, una sola volta: il modello di riconoscimento
vocale, tra 75 e 1600 megabyte secondo il tuo PC, un modello di traduzione di circa 280 megabyte per ogni coppia di
lingue e le voci delle tue lingue. Dopo funziona senza Internet.

**Avvisa le persone nella tua chiamata** che usi un traduttore, per esempio: Uso un'app di traduzione, funziona solo
sul mio PC e non salva niente.

=== 3. La finestra principale
# La finestra principale

In alto trovi la casella del profilo. Un profilo conserva tutte le tue impostazioni di motori, lingue e dispositivi.
Puoi salvare, salvare con nome, eliminare, importare ed esportare i profili. I profili iniziali sono: Standard,
tutto su questo PC. Il più veloce, per PC più lenti. Massima qualità, per un PC con scheda grafica NVIDIA. E
Traduzione con IA con Ollama.

Le modifiche si salvano automaticamente circa un secondo dopo. Puoi disattivarlo nella scheda Impostazioni.

Accanto alla casella del profilo ci sono tre pulsanti:

- **Sottotitoli** mostra una finestra di sottotitoli mobile che puoi trascinare, ridimensionare con la rotellina del
  mouse e configurare con il tasto destro.
- **Chat** attiva la traduzione dei messaggi di testo di Discord.
- **Avvia** avvia il traduttore vocale. Il tasto F5 fa lo stesso.

Le schede sono: Pannello, Dal vivo, Testo, Ingresso, Uscita, Parlato, Traduzione, Modello IA, Voce, Configurazione,
Impostazioni, Manuale e Log. I prossimi capitoli spiegano quelle che userai di più.

=== 4. Pannello
# Pannello

Il Pannello è la tua centrale di controllo. È la prima scheda e mostra tutto a colpo d'occhio.

- La **scheda del traduttore vocale** avvia e ferma la traduzione vocale dal vivo, e mostra cosa sta facendo:
  riconoscimento, traduzione o pronuncia.
- La **scheda della traduzione della chat** avvia e ferma la traduzione dei messaggi di Discord. Ha anche l'opzione
  di leggere ad alta voce i messaggi tradotti, uno dopo l'altro, oppure lasciando che un nuovo messaggio
  interrompa quello in lettura.
- La **scheda Tu** è dove inserisci il tuo nome su Discord e la lingua in cui scrivi.
- La **scheda degli strumenti** ha scorciatoie per evidenzia per tradurre, l'OCR e la finestra dei sottotitoli.
- La **scheda delle scorciatoie** ti ricorda le scorciatoie da tastiera.
- In basso, Ultime traduzioni mostra le ultime frasi tradotte.

Le impostazioni che compaiono in due posti, per esempio nel Pannello e nella scheda Testo, restano sempre
sincronizzate.

=== 5. Traduzione vocale dal vivo
# Traduzione vocale dal vivo

È la funzione principale. Funziona in due direzioni, e ognuna si può attivare separatamente.

**In entrata: loro parlano, tu senti.** L'app ascolta solo l'app Discord, quindi non sente mai la propria voce, il
tuo gioco o la tua musica, e continua ad ascoltare mentre parla. Riconosce il parlato, lo traduce, mostra i
sottotitoli e, se vuoi, pronuncia la traduzione. Scegli la lingua che parlano, o Rilevamento automatico. Scegliere
la lingua rende il riconoscimento sul tuo PC circa due volte più veloce.

**In uscita: tu parli, loro sentono.** L'app ascolta il tuo microfono, traduce ciò che dici e lo pronuncia su
Discord tramite il cavo virtuale. La tua voce non viene inviata a Discord, solo la traduzione. L'app ti avvisa se
Discord usa il tuo vero microfono invece del cavo.

**Senti le persone, il tasto F9.** Di base senti solo le traduzioni. Mentre il traduttore è attivo, l'app abbassa
Discord nel mixer del volume di Windows e gli ridà il volume quando premi Ferma. Premi F9, o il pulsante Senti le
persone, per sentire anche le loro voci. Puoi cambiare il tasto nella scheda Ingresso.

**Una sola voce, in ordine.** Le traduzioni della chiamata e i messaggi della chat letti ad alta voce condividono
una sola voce, quindi non parlano mai uno sopra l'altro. Tutto viene detto nell'ordine in cui è stato pronunciato e
niente viene saltato: la frase successiva viene preparata mentre suona quella attuale, e quando le frasi si
accumulano la voce parla un po' più veloce.

**Chi sta parlando.** La voce dell'app può dire chi ha parlato, per esempio le prime due lettere del nome, o il
nome completo. Sceglilo nella scheda Uscita, sotto La voce dell'app. Nelle chiamate i nomi arrivano dall'app
Discord stessa: nella scheda Uscita, sotto Chi sta parlando, aggiungi una volta la tua applicazione Discord. I
messaggi della chat hanno sempre il nome dell'autore.

Nella scheda **Dal vivo** imposti le lingue delle due direzioni, guardi gli indicatori di livello e leggi la
trascrizione. Puoi usare un pulsante push-to-talk, e la casella Scrivi per parlare, dove scrivi una frase che viene
tradotta e pronunciata su Discord. L'opzione Rispondi nella lingua che parlano fa seguire alla tua lingua di uscita
l'ultima lingua rilevata dall'altra persona.

Nella scheda **Ingresso** scegli cosa ascoltare e come parte il tuo microfono: rilevamento vocale, push-to-talk o
alternanza. C'è anche un controllo della sensibilità. L'app riconosce la propria voce quando il tuo microfono la
sente, e la ignora.

Nella scheda **Uscita** scegli dove suonano le traduzioni, il cavo virtuale per la tua voce, la voce dell'app e chi
sta parlando.

Tutti i dispositivi audio sono anche riuniti in un unico posto, nella scheda Impostazioni, sotto Dispositivi audio.

=== 6. Motori: parlato, traduzione, IA e voce
# Motori

Ogni fase della traduzione funziona sul tuo PC, e puoi cambiare le impostazioni quando vuoi. Sono salvate nel tuo
profilo.

- **Scheda Parlato.** Trasforma la voce in testo con Whisper. La dimensione del modello auto è scelta per il tuo PC:
  un modello piccolo sul processore, uno grande e preciso su una scheda grafica NVIDIA. Un modello più grande è più
  preciso ma più lento. In questa scheda c'è una prova del microfono.
- **Scheda Traduzione.** Il motore OPUS-MT, dell'Università di Helsinki, traduce in circa un decimo di secondo per
  frase. Ogni coppia di lingue si scarica una volta; le lingue senza modello diretto passano dall'inglese. Il
  pulsante Scarica ora i modelli delle mie lingue li prende prima della tua chiamata. Puoi scegliere il tono, e un
  glossario fissa come si traducono nomi e termini di gioco.
- **Scheda Modello IA.** Facoltativa. Se installi Ollama o LM Studio e un modello sul tuo PC, il motore Modello IA su
  questo PC traduce con quello. Capisce meglio slang e contesto, ma serve un PC veloce o una scheda grafica. L'app
  parla solo con server IA sul tuo computer o nella rete locale.
- **Scheda Voce.** Le voci di questo PC: voci naturali Piper e Kokoro, e le voci integrate in Windows. Auto sceglie
  una voce per ogni lingua. Una voce si scarica una volta, la prima volta che si usa. Le voci Kokoro sono molto
  naturali ma richiedono un PC veloce. Per altre voci di Windows, apri Impostazioni di Windows, Data/ora e lingua,
  Voce, Aggiungi voci. Per ogni direzione puoi regolare velocità, tonalità e volume.

Ogni scheda ha un pulsante Prova per controllare un motore prima di usarlo.

=== 7. Privacy e i tuoi dati
# Privacy e i tuoi dati

EloGlobal funziona solo sul tuo PC. Ciò che le persone dicono nella chiamata, il tuo microfono, i messaggi della
chat e il testo che traduci non lasciano mai il tuo computer. L'app non ha account, statistiche d'uso né pubblicità.

**Le voci degli altri.** Mentre il traduttore è attivo, l'app sente ciò che dicono le persone nella tua chiamata,
per tradurlo per te. Di' loro che usi un traduttore. In alcuni paesi serve il loro consenso.

**Cosa viene salvato.** Le tue impostazioni e i profili, e file di log con messaggi tecnici, non con ciò che dicono
le persone. Le trascrizioni delle chiamate si salvano solo se le attivi, nella scheda Impostazioni, in Privacy e
informazioni.

**Dove.** Tutto ciò che l'app salva è nella tua cartella utente, in App Data, Local, EloGlobal: profili, log,
trascrizioni e i modelli scaricati. La scheda Impostazioni ha pulsanti per aprire la cartella dei dati e quella dei
modelli.

**Internet.** L'app scarica solo file di modelli, una volta. La funzione facoltativa Chi sta parlando accede a
Discord con la tua applicazione Discord. Gli aggiornamenti arrivano dallo store.

La scheda Impostazioni mostra di nuovo anche l'informativa sulla privacy, e la finestra Informazioni e licenze
elenca tutto il software e i modelli su cui si basa EloGlobal.

=== 8. Tradurre il testo di Discord
# Tradurre il testo di Discord

Premi il pulsante **Chat**, o usa la scheda della chat nel Pannello. L'app legge allora i messaggi che vedi
nell'app di Discord, usando le funzioni di accessibilità di Windows, come un lettore di schermo. Non servono token
né bot, e non invia nulla a Discord.

I nuovi messaggi vengono tradotti e mostrati sopra il testo originale, direttamente dentro Discord, o in una
piccola finestra accanto. Lo scegli nella scheda Testo, sotto Mostra le traduzioni. Funziona nei server, nei
messaggi diretti, nei gruppi, nei thread e nei post del forum, anche con Discord in secondo piano. I messaggi già
nella tua lingua, e i tuoi messaggi, vengono saltati. Le traduzioni si vedono solo mentre Discord è la finestra
attiva, quindi non coprono mai il tuo gioco.

**Lettura ad alta voce.** Solo i messaggi nuovi vengono letti ad alta voce. I messaggi a cui torni scorrendo,
quelli modificati e quelli vecchi vengono tradotti sullo schermo, ma mai letti. I messaggi della chat condividono
la voce dell'app con le traduzioni della chiamata, quindi le due non parlano mai insieme.

La scheda Testo ha altri strumenti:

- **Evidenzia per tradurre.** Seleziona del testo, o fai doppio clic su una parola, e accanto al mouse appare un
  popup con la traduzione.
- **Ctrl+Alt+T** traduce la selezione attuale in qualsiasi app.
- **Ctrl+Alt+Y** sostituisce ciò che hai scritto nella casella dei messaggi di Discord con la traduzione nella
  lingua usata in quella chat.
- **Scrivi nella loro lingua.** Scrivi nella scheda Testo, poi copia, incolla su Discord o invia.
- **Ctrl+Alt+O** ti fa trascinare un riquadro su qualsiasi parte dello schermo. L'app legge il testo con l'OCR e
  mostra la traduzione sopra. Può ripetersi ogni pochi secondi.
- **Testo copiato.** Facoltativamente traduce tutto ciò che copi.

Puoi cambiare ogni scorciatoia nella scheda Testo. Per l'OCR di altri alfabeti, come il russo o il giapponese,
aggiungi quella lingua nelle Impostazioni di Windows.

=== 9. Sottotitoli e trascrizioni
# Sottotitoli e trascrizioni

La **finestra dei sottotitoli** fluttua sopra il tuo gioco o Discord. Trascinala per spostarla. Usa la rotellina del
mouse per ridimensionarla. Clic destro per le opzioni, come quante righe mostrare, se mostrare il testo originale e
lo sfondo. Nelle Impostazioni cambi dimensione e carattere del testo.

Una conversazione può essere salvata come **trascrizione**. È disattivato di base, perché le trascrizioni contengono
le parole di altre persone. Attivalo nella scheda Uscita o nelle Impostazioni. Le trascrizioni sono salvate nella
cartella dei dati, in transcripts.

La scheda Log mostra cosa fa l'app in tempo reale. Ha anche pulsanti per aprire i log, le trascrizioni e la cartella
dei dati. Se qualcosa va storto, il log è il primo posto da guardare.

La barra di stato in basso mostra il ritardo di ogni fase: riconoscimento vocale, traduzione e voce, così vedi quale
passaggio è lento.

=== 10. Impostazioni e informazioni
# Impostazioni e informazioni

La scheda **Impostazioni** imposta la lingua dell'app. Dopo un cambio, l'app si riavvia nella nuova lingua. Riunisce
anche tutti i dispositivi audio in un unico posto: cosa ascolta l'app, il tuo microfono, dove suonano le traduzioni
e dove va la tua voce tradotta.

Controlla l'aspetto dell'app: il tema, scuro o chiaro, il carattere e la dimensione del testo dell'app e delle
traduzioni mostrate dentro Discord, nella finestrella della chat e nei popup. Ha anche tutte le scorciatoie in un
unico posto, un'opzione per tenere la finestra sopra le altre e pulsanti per riposizionare le finestre e aprire le
cartelle dei dati, dei modelli e dei log.

L'opzione Salva le modifiche automaticamente salva il tuo profilo circa un secondo dopo ogni modifica. È attiva di
base.

**Privacy e informazioni.** L'opzione delle trascrizioni, l'informativa sulla privacy e la finestra Informazioni e
licenze, con la licenza di EloGlobal e l'elenco di tutti i componenti che usa.

**Gli aggiornamenti** arrivano dallo store da cui hai installato EloGlobal, Microsoft Store o Steam. Impostazioni,
profili e modelli scaricati vengono conservati.

=== 11. Risoluzione dei problemi
# Risoluzione dei problemi

**Nessuno sente la mia traduzione.** In Discord, il dispositivo di input deve essere CABLE Output. Nell'app, la
scheda Uscita deve inviare a CABLE Input. Controlla che la Soppressione del rumore sia disattivata in Discord.

**L'app non sente niente.** Nella scheda Ingresso, controlla il metodo. Con Solo l'app Discord, Discord deve essere
aperto. Con il loopback, il dispositivo deve essere quello su cui suona Discord. Guarda gli indicatori di livello
nella scheda Dal vivo. Se non si muovono, l'impostazione è sbagliata.

**La mia traduzione si sente due volte, o l'app traduce sé stessa.** Usa il metodo Solo l'app Discord nella scheda
Ingresso e usa le cuffie.

**Discord è muto.** È voluto mentre il traduttore è attivo: premi F9 per sentire anche le persone. Se EloGlobal si è
chiuso di colpo, aprilo una volta e restituirà il volume a Discord, oppure alza Discord nel mixer volume di Windows.

**Le persone sentono la mia vera voce.** In Discord, il dispositivo di input deve essere CABLE Output, non il tuo
microfono. L'app ti avvisa quando Discord usa il tuo vero microfono.

**È lento.** Nella scheda Dal vivo, scegli la lingua che parlano invece di Rilevamento automatico. Nella scheda
Parlato, scegli un modello più piccolo o usa una scheda grafica NVIDIA. Le voci Kokoro sono lente su molti
processori: scegli una voce Piper o di Windows nella scheda Voce.

**Non c'è una voce per la mia lingua.** Aggiungi una voce di Windows: Impostazioni di Windows, Data/ora e lingua,
Voce, Aggiungi voci. Poi premi Ricarica l'elenco delle voci nella scheda Voce.

**Un download non riesce.** Controlla la connessione a Internet e premi di nuovo Avvia; il download riprende da dove
si era fermato.

**Ancora bloccato?** Apri la scheda Log e la cartella dei log. Il log aiuta quando segnali un problema dalla pagina
dello store.

=== 12. Su questo manuale
# Su questo manuale

Stai leggendo il manuale integrato in EloGlobal. Il narratore è una voce che funziona sul tuo PC, nella lingua
dell'app. Funziona offline e non invia niente da nessuna parte.

- **Avanti e Precedente** passano da un capitolo all'altro. Il narratore smette di leggere il vecchio capitolo e
  inizia il nuovo, e il nuovo testo appare nello stesso momento.
- **Leggi ad alta voce** attiva o disattiva il narratore. Se è disattivato, il manuale è solo testo.
- **Rileggi** riparte dall'inizio del capitolo attuale.
- **Ferma** zittisce il narratore.
- **Voce** e **Velocità** cambiano come suona. Puoi scegliere qualsiasi voce della tua lingua su questo PC, o una da
  scaricare.
- **Rivedi il tour guidato** mostra di nuovo i primi passi.

Il narratore tace quando lasci questa scheda e non parte mai da solo mentre usi il traduttore.

Questa è la fine del manuale. Buon divertimento con EloGlobal!
