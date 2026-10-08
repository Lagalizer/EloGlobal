=== 1. Willkommen
# Willkommen bei EloGlobal

EloGlobal ist ein Echtzeit-Übersetzer für Discord und jeden anderen Sprachchat. Alles läuft auf deinem eigenen PC:
Spracherkennung, Übersetzung und Stimmen. Nichts, was jemand sagt oder schreibt, wird ins Internet gesendet.

- **Du hörst die anderen in deiner Sprache.** Die App hört, was die Leute in Discord sagen, schreibt es auf,
  übersetzt es, zeigt Untertitel und kann dir die Übersetzung mit einer natürlichen Stimme vorlesen.
- **Sie hören dich in ihrer Sprache.** Du sprichst in dein Mikrofon. Die App übersetzt, was du gesagt hast, und
  spricht es über ein virtuelles Audiokabel in Discord.
- **Auch Text.** Sie übersetzt Discord-Nachrichten auf Servern, in Direktnachrichten und Threads, jeden Text, den du
  mit der Maus markierst, und Text auf dem Bildschirm per OCR. Du kannst auch in ihrer Sprache schreiben.
- **Kostenlos und privat.** Kein Konto, kein Abo und kein Online-Dienst. Die Modelle werden einmal heruntergeladen
  und laufen danach ohne Internet.

Dieses Handbuch hat zwölf Kapitel. Nutze die Knöpfe Weiter und Zurück oder klicke auf ein Kapitel in der Liste.
Bei jedem Kapitelwechsel hört der Sprecher mit dem alten auf und liest das neue. Der Sprecher ist eine Stimme, die
auf deinem PC läuft.

=== 2. Erster Start
# Erster Start

**Schritt 1. Öffne die App.** Starte EloGlobal über das Startmenü oder über Steam. Beim ersten Mal wählst du die
Sprache der App. Alles wird in dieser Sprache gezeigt, und die Einführung und dieses Handbuch werden darin
vorgelesen. Dann erklärt die App, was sie mit den Stimmen und Nachrichten anderer macht: Alles bleibt auf deinem PC.
Danach zeigt dir eine kurze geführte Tour die ersten Schritte. Sie öffnet sich nur beim ersten Mal; du kannst sie
in diesem Tab wiederholen.

**Schritt 2. Installiere ein virtuelles Audiokabel.** Installiere VB-Audio Virtual Cable von der Website des
Herstellers und starte den PC neu. Es stammt von VB-Audio, nicht von EloGlobal, und ist für den privaten Gebrauch
kostenlos. Windows braucht es, um ein virtuelles Mikrofon zu erzeugen.

**Schritt 3. Richte Discord ein.** Öffne Discord, dann Benutzereinstellungen, dann Sprache und Video.

- Eingabegerät: CABLE Output, von VB-Audio Virtual Cable.
- Ausgabegerät: dein Headset.
- Schalte Rauschunterdrückung, Echounterdrückung und Automatische Verstärkungsregelung aus.

**Schritt 4. Richte die App ein.** Behalte das Profil Standard, alles auf diesem PC. Im Tab Ausgang sendest du deine
übersetzte Stimme an CABLE Input. Im Tab Eingang behältst du die Methode Nur die Discord-App und wählst dein echtes
Mikrofon. Im Tab Live wählst du die Sprachen. Drücke dann Start oder die Taste F5.

**Wenn du zum ersten Mal Start drückst**, lädt die App einmalig herunter, was sie braucht: das
Spracherkennungsmodell, je nach PC zwischen 75 und 1600 Megabyte, ein Übersetzungsmodell von etwa 280 Megabyte pro
Sprachpaar und die Stimmen deiner Sprachen. Danach läuft sie ohne Internet.

**Sag den Leuten in deinem Anruf**, dass du einen Übersetzer benutzt, zum Beispiel: Ich nutze eine Übersetzer-App,
sie läuft nur auf meinem PC und speichert nichts.

=== 3. Das Hauptfenster
# Das Hauptfenster

Oben findest du das Profilfeld. Ein Profil speichert alle deine Einstellungen für Engines, Sprachen und Geräte. Du
kannst Profile speichern, speichern unter, löschen, importieren und exportieren. Die Startprofile sind: Standard,
alles auf diesem PC. Am schnellsten, für langsamere PCs. Beste Qualität, für einen PC mit NVIDIA-Grafikkarte. Und
KI-Übersetzung mit Ollama.

Deine Änderungen werden etwa eine Sekunde danach automatisch gespeichert. Du kannst das im Tab Einstellungen
ausschalten.

Neben dem Profilfeld gibt es drei Knöpfe:

- **Untertitel** zeigt ein schwebendes Untertitelfenster, das du ziehen, mit dem Mausrad vergrößern und mit einem
  Rechtsklick einstellen kannst.
- **Chat** schaltet die Übersetzung der Discord-Textnachrichten ein.
- **Start** startet den Sprachübersetzer. Die Taste F5 macht dasselbe.

Die Tabs sind: Übersicht, Live, Text, Eingang, Ausgang, Spracherkennung, Übersetzung, KI-Modell, Stimme,
Einrichtung, Einstellungen, Handbuch und Log. Die nächsten Kapitel erklären die, die du am häufigsten brauchst.

=== 4. Übersicht
# Übersicht

Die Übersicht ist deine Schaltzentrale. Sie ist der erste Tab und zeigt alles auf einen Blick.

- Die **Karte des Sprachübersetzers** startet und stoppt die Live-Sprachübersetzung und zeigt, was er gerade tut:
  erkennen, übersetzen oder sprechen.
- Die **Karte der Chat-Übersetzung** startet und stoppt die Übersetzung der Discord-Nachrichten. Sie kann
  übersetzte Nachrichten auch vorlesen, eine nach der anderen, oder so, dass eine neue Nachricht die gerade
  gelesene unterbricht.
- In der **Karte Du** trägst du deinen Discord-Namen und die Sprache ein, in der du schreibst.
- Die **Werkzeug-Karte** hat Abkürzungen zu Markieren zum Übersetzen, OCR und dem Untertitelfenster.
- Die **Tastenkürzel-Karte** erinnert dich an deine Tastenkürzel.
- Unten zeigt Letzte Übersetzungen die zuletzt übersetzten Zeilen.

Einstellungen, die an zwei Stellen vorkommen, zum Beispiel in der Übersicht und im Tab Text, bleiben immer
synchron.

=== 5. Live-Sprachübersetzung
# Live-Sprachübersetzung

Das ist die Hauptfunktion. Sie arbeitet in zwei Richtungen, und jede kann einzeln eingeschaltet werden.

**Eingehend: Sie sprechen, du hörst.** Die App hört nur die Discord-App, also hört sie nie ihre eigene Stimme, dein
Spiel oder deine Musik, und sie hört weiter zu, während sie spricht. Sie erkennt die Sprache, übersetzt sie, zeigt
Untertitel und spricht, wenn du willst, die Übersetzung. Du wählst die Sprache, die sie sprechen, oder Automatisch
erkennen. Wenn du die Sprache wählst, ist die Erkennung auf deinem PC etwa doppelt so schnell.

**Ausgehend: du sprichst, sie hören.** Die App hört dein Mikrofon, übersetzt, was du sagst, und spricht es über das
virtuelle Kabel in Discord. Deine eigene Stimme wird nicht an Discord geschickt, nur die Übersetzung. Die App warnt
dich, wenn Discord dein echtes Mikrofon statt des Kabels nutzt.

**Leute hören, die Taste F9.** Standardmäßig hörst du nur die Übersetzungen. Solange der Übersetzer läuft, macht
die App Discord im Windows-Lautstärkemixer leise und gibt ihm seine Lautstärke zurück, wenn du Stopp drückst. Drück
F9 oder die Schaltfläche Leute hören, um auch ihre eigenen Stimmen zu hören. Die Taste kannst du im Tab Eingang
ändern.

**Eine Stimme, der Reihe nach.** Die Übersetzungen aus dem Anruf und die vorgelesenen Chatnachrichten teilen sich
eine Stimme, sie reden also nie durcheinander. Alles wird in der Reihenfolge gesagt, in der es gesprochen wurde,
und nichts wird ausgelassen: Der nächste Satz wird vorbereitet, während der aktuelle läuft, und wenn sich Sätze
stauen, spricht die Stimme etwas schneller.

**Wer spricht.** Die Stimme der App kann sagen, wer gesprochen hat, zum Beispiel die ersten zwei Buchstaben des
Namens oder den ganzen Namen. Das wählst du im Tab Ausgang unter Die Stimme der App. In Anrufen kommen die Namen
aus der Discord-App selbst: Im Tab Ausgang trägst du unter Wer spricht einmal deine eigene Discord-Anwendung ein.
Chatnachrichten haben immer den Namen des Autors.

Im Tab **Live** stellst du die Sprachen beider Richtungen ein, siehst die Pegelanzeigen und liest das Transkript.
Du kannst einen Push-to-Talk-Knopf nutzen und das Feld Tippen zum Sprechen, in das du eine Zeile tippst, die
übersetzt und in Discord gesprochen wird. Die Option In der Sprache antworten, die sie sprechen, lässt deine
Ausgabesprache der zuletzt bei der anderen Person erkannten Sprache folgen.

Im Tab **Eingang** wählst du, was die App hört und wie dein Mikrofon startet: Sprachaktivierung, Push-to-Talk oder
Umschalten. Es gibt auch eine Empfindlichkeitsregelung. Die App erkennt ihre eigene Stimme, wenn dein Mikrofon sie
hört, und ignoriert sie.

Im Tab **Ausgang** wählst du, wo die Übersetzungen laufen, das virtuelle Kabel für deine Stimme, die Stimme der App
und wer spricht.

Alle Audiogeräte findest du außerdem gesammelt an einem Ort, im Tab Einstellungen unter Audiogeräte.

=== 6. Engines: Sprache, Übersetzung, KI und Stimme
# Engines

Jeder Schritt der Übersetzung läuft auf deinem PC, und du kannst die Einstellungen jederzeit ändern. Sie werden in
deinem Profil gespeichert.

- **Tab Spracherkennung.** Macht aus Sprache Text mit Whisper. Die Modellgröße auto wird für deinen PC gewählt: ein
  kleines Modell auf dem Prozessor, ein großes, genaues auf einer NVIDIA-Grafikkarte. Ein größeres Modell ist
  genauer, aber langsamer. In diesem Tab gibt es einen Mikrofontest.
- **Tab Übersetzung.** Die Engine OPUS-MT der Universität Helsinki übersetzt in etwa einer Zehntelsekunde pro Satz.
  Jedes Sprachpaar wird einmal geladen; Sprachen ohne direktes Modell laufen über Englisch. Der Knopf Modelle für
  meine Sprachen jetzt herunterladen holt sie schon vor deinem Anruf. Du kannst den Ton wählen, und ein Glossar legt
  fest, wie Namen und Spielbegriffe übersetzt werden.
- **Tab KI-Modell.** Optional. Wenn du Ollama oder LM Studio und ein Modell auf deinem PC installierst, übersetzt die
  Engine KI-Modell auf diesem PC damit. Sie versteht Slang und Kontext besser, braucht aber einen schnellen PC oder
  eine Grafikkarte. Die App spricht nur mit KI-Servern auf deinem eigenen Computer oder im lokalen Netz.
- **Tab Stimme.** Die Stimmen auf diesem PC: natürliche Piper- und Kokoro-Stimmen und die in Windows eingebauten
  Stimmen. Auto wählt eine Stimme für jede Sprache. Eine Stimme wird bei der ersten Nutzung einmal geladen.
  Kokoro-Stimmen klingen sehr natürlich, brauchen aber einen schnellen PC. Für mehr Windows-Stimmen öffne
  Windows-Einstellungen, Zeit und Sprache, Sprache, Stimmen hinzufügen. Für jede Richtung kannst du Tempo, Tonhöhe
  und Lautstärke einstellen.

Jeder Tab hat einen Test-Knopf, damit du eine Engine prüfen kannst, bevor du sie nutzt.

=== 7. Datenschutz und deine Daten
# Datenschutz und deine Daten

EloGlobal arbeitet nur auf deinem PC. Was die Leute im Anruf sagen, dein Mikrofon, die Chatnachrichten und der Text,
den du übersetzt, verlassen nie deinen Computer. Die App hat kein Konto, keine Nutzungsstatistik und keine Werbung.

**Die Stimmen der anderen.** Während der Übersetzer läuft, hört die App, was die Leute in deinem Anruf sagen, um es
für dich zu übersetzen. Sag ihnen, dass du einen Übersetzer benutzt. In manchen Ländern brauchst du ihre Zustimmung.

**Was gespeichert wird.** Deine Einstellungen und Profile sowie Log-Dateien mit technischen Meldungen, nicht mit dem,
was Leute sagen. Transkripte der Anrufe werden nur gespeichert, wenn du es einschaltest, im Tab Einstellungen unter
Datenschutz und Info.

**Wo.** Alles, was die App speichert, liegt in deinem Benutzerordner unter App Data, Local, EloGlobal: Profile, Logs,
Transkripte und die heruntergeladenen Modelle. Der Tab Einstellungen hat Knöpfe, um den Datenordner und den
Modellordner zu öffnen.

**Internet.** Die App lädt nur einmal Modelldateien herunter. Die optionale Funktion Wer spricht meldet sich mit
deiner eigenen Discord-Anwendung bei Discord an. Updates kommen aus dem Store.

Der Tab Einstellungen zeigt auch den Datenschutzhinweis noch einmal, und das Fenster Info und Lizenzen listet alle
Software und Modelle auf, auf denen EloGlobal aufbaut.

=== 8. Discord-Text übersetzen
# Discord-Text übersetzen

Drücke den Knopf **Chat** oder nutze die Chat-Karte in der Übersicht. Die App liest dann die Nachrichten, die du in
der Discord-App siehst, über die Barrierefreiheitsfunktionen von Windows, wie ein Bildschirmleser. Sie braucht
kein Token und keinen Bot und schickt nichts an Discord.

Neue Nachrichten werden übersetzt und über den Originaltext gezeichnet, direkt in Discord, oder in einem kleinen
Fenster daneben. Das wählst du im Tab Text unter Übersetzungen anzeigen. Es funktioniert in Servern,
Direktnachrichten, Gruppen, Threads und Forenbeiträgen, sogar wenn Discord im Hintergrund ist. Nachrichten, die
schon in deiner Sprache sind, und deine eigenen werden übersprungen. Die Übersetzungen erscheinen nur, solange
Discord das aktive Fenster ist, sie verdecken also nie dein Spiel.

**Vorlesen.** Nur neue Nachrichten werden vorgelesen. Nachrichten, zu denen du zurückscrollst, bearbeitete und alte
Nachrichten werden auf dem Bildschirm übersetzt, aber nie vorgelesen. Chatnachrichten teilen sich die Stimme der
App mit den Übersetzungen aus dem Anruf, also sprechen die beiden nie gleichzeitig.

Der Tab Text hat weitere Werkzeuge:

- **Markieren zum Übersetzen.** Markiere Text oder doppelklicke ein Wort, und ein Popup mit der Übersetzung
  erscheint neben der Maus.
- **Strg+Alt+T** übersetzt die aktuelle Auswahl in jeder App.
- **Strg+Alt+Y** ersetzt, was du in Discords Nachrichtenfeld getippt hast, durch die Übersetzung in die Sprache,
  die in diesem Chat benutzt wird.
- **In ihrer Sprache schreiben.** Tippe im Tab Text, dann kopiere, füge in Discord ein oder sende.
- **Strg+Alt+O** lässt dich einen Rahmen über einen beliebigen Teil des Bildschirms ziehen. Die App liest den Text
  per OCR und zeigt die Übersetzung darüber. Das kann sich alle paar Sekunden wiederholen.
- **Kopierter Text.** Auf Wunsch wird alles übersetzt, was du kopierst.

Du kannst jedes Tastenkürzel im Tab Text ändern. Für OCR in anderen Schriften, etwa Russisch oder Japanisch, füge
die Sprache in den Windows-Einstellungen hinzu.

=== 9. Untertitel und Transkripte
# Untertitel und Transkripte

Das **Untertitelfenster** schwebt über deinem Spiel oder Discord. Zieh es, um es zu verschieben. Mit dem Mausrad
änderst du die Größe. Ein Rechtsklick zeigt Optionen, etwa wie viele Zeilen, ob der Originaltext angezeigt wird und
den Hintergrund. In den Einstellungen änderst du Textgröße und Schrift.

Ein Gespräch kann als **Transkript** gespeichert werden. Das ist standardmäßig aus, weil Transkripte die Worte
anderer Leute enthalten. Schalte es im Tab Ausgang oder in den Einstellungen ein. Transkripte werden im Datenordner
unter transcripts gespeichert.

Der Tab Log zeigt in Echtzeit, was die App tut. Er hat auch Knöpfe, um die Logs, die Transkripte und den Datenordner
zu öffnen. Wenn etwas schiefgeht, schau zuerst ins Log.

Die Statusleiste unten zeigt die Verzögerung jeder Stufe: Spracherkennung, Übersetzung und Stimme, damit du siehst,
welcher Schritt langsam ist.

=== 10. Einstellungen und Info
# Einstellungen und Info

Der Tab **Einstellungen** legt die Sprache der App fest. Nach einer Änderung startet die App in der neuen Sprache neu.
Er bündelt auch alle Audiogeräte an einem Ort: was die App hört, dein Mikrofon, wo die Übersetzungen laufen und wohin
deine übersetzte Stimme geht.

Er steuert das Aussehen der App: das Thema, dunkel oder hell, die Schrift und die Textgröße der App und der
Übersetzungen in Discord, im kleinen Chatfenster und in den Popups. Außerdem gibt es dort alle Tastenkürzel, einen
Schalter, der das Fenster über anderen hält, und Knöpfe, um die Fensterpositionen zurückzusetzen und den Daten-,
Modell- und Log-Ordner zu öffnen.

Der Schalter Änderungen automatisch speichern speichert dein Profil etwa eine Sekunde nach jeder Änderung. Er ist
standardmäßig an.

**Datenschutz und Info.** Der Schalter für Transkripte, der Datenschutzhinweis und das Fenster Info und Lizenzen mit
der Lizenz von EloGlobal und der Liste aller Bestandteile, die es nutzt.

**Updates** kommen aus dem Store, in dem du EloGlobal installiert hast, dem Microsoft Store oder Steam. Deine
Einstellungen, Profile und heruntergeladenen Modelle bleiben erhalten.

=== 11. Fehlerbehebung
# Fehlerbehebung

**Niemand hört meine Übersetzung.** In Discord muss das Eingabegerät CABLE Output sein. In der App muss der Tab
Ausgang an CABLE Input senden. Prüfe, dass die Rauschunterdrückung in Discord aus ist.

**Die App hört nichts.** Prüfe im Tab Eingang die Methode. Bei Nur die Discord-App muss Discord offen sein. Bei
Loopback muss das Gerät das sein, auf dem Discord spielt. Sieh dir die Pegelanzeigen im Tab Live an. Bewegen sie
sich nicht, ist die Einstellung falsch.

**Meine Übersetzung ist doppelt zu hören, oder die App übersetzt sich selbst.** Nutze im Tab Eingang die Methode Nur
die Discord-App und trag ein Headset.

**Discord ist stumm.** Das ist Absicht, solange der Übersetzer läuft: Drücke F9, um auch die Leute zu hören. Wurde
EloGlobal abrupt beendet, öffne es einmal, dann gibt es Discord die Lautstärke zurück, oder dreh Discord im
Windows-Lautstärkemixer auf.

**Die Leute hören meine echte Stimme.** In Discord muss das Eingabegerät CABLE Output sein, nicht dein Mikrofon. Die
App warnt dich, wenn Discord dein echtes Mikrofon benutzt.

**Es ist langsam.** Wähle im Tab Live die Sprache, die sie sprechen, statt Automatisch erkennen. Wähle im Tab
Spracherkennung ein kleineres Modell oder nutze eine NVIDIA-Grafikkarte. Kokoro-Stimmen sind auf vielen Prozessoren
langsam: Wähle im Tab Stimme eine Piper- oder Windows-Stimme.

**Keine Stimme für meine Sprache.** Füge eine Windows-Stimme hinzu: Windows-Einstellungen, Zeit und Sprache, Sprache,
Stimmen hinzufügen. Drücke dann im Tab Stimme auf Stimmenliste neu laden.

**Ein Download schlägt fehl.** Prüfe deine Internetverbindung und drücke erneut Start; der Download macht dort weiter,
wo er aufgehört hat.

**Immer noch Probleme?** Öffne den Tab Log und den Log-Ordner. Das Log hilft, wenn du ein Problem über die Store-Seite
meldest.

=== 12. Über dieses Handbuch
# Über dieses Handbuch

Du liest das in EloGlobal eingebaute Handbuch. Der Sprecher ist eine Stimme, die auf deinem PC läuft, in der Sprache
der App. Er funktioniert offline und sendet nichts irgendwohin.

- **Weiter und Zurück** wechseln zwischen den Kapiteln. Der Sprecher hört mit dem alten Kapitel auf und beginnt das
  neue, und der neue Text erscheint gleichzeitig.
- **Vorlesen** schaltet den Sprecher ein oder aus. Ist er aus, ist das Handbuch nur Text.
- **Nochmal lesen** beginnt das aktuelle Kapitel von vorn.
- **Stopp** bringt den Sprecher zum Schweigen.
- **Stimme** und **Tempo** ändern, wie er klingt. Du kannst jede Stimme deiner Sprache auf diesem PC wählen oder eine
  zum Herunterladen.
- **Geführte Tour wiederholen** zeigt die ersten Schritte noch einmal.

Der Sprecher schweigt, wenn du diesen Tab verlässt, und startet nie von selbst, während du den Übersetzer benutzt.

Das ist das Ende des Handbuchs. Viel Spaß mit EloGlobal!
