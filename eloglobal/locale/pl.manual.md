=== 1. Witaj
# Witaj w EloGlobal

EloGlobal to tłumacz w czasie rzeczywistym dla Discorda i każdego innego czatu głosowego. Wszystko działa na twoim
własnym komputerze: rozpoznawanie mowy, tłumaczenie i głosy. Nic, co ktoś mówi lub pisze, nie jest wysyłane do
internetu.

- **Słyszysz innych w swoim języku.** Aplikacja słucha, co mówią ludzie na Discordzie, zapisuje to, tłumaczy,
  pokazuje napisy i może przeczytać ci tłumaczenie naturalnym głosem.
- **Oni słyszą cię w swoim języku.** Mówisz do mikrofonu. Aplikacja tłumaczy to, co powiedziałeś, i wypowiada to na
  Discordzie przez wirtualny kabel audio.
- **Tekst też.** Tłumaczy wiadomości Discorda na serwerach, w wiadomościach prywatnych i wątkach, każdy tekst
  zaznaczony myszą oraz tekst na ekranie za pomocą OCR. Możesz też pisać w ich języku.
- **Za darmo i prywatnie.** Bez konta, bez subskrypcji i bez usług online. Modele pobiera się raz, a potem działają
  bez internetu.

Ta instrukcja ma dwanaście rozdziałów. Używaj przycisków Dalej i Poprzedni albo kliknij rozdział na liście. Przy
każdej zmianie rozdziału lektor przerywa stary i czyta nowy. Lektor to głos, który działa na twoim komputerze.

=== 2. Pierwsze uruchomienie
# Pierwsze uruchomienie

**Krok 1. Otwórz aplikację.** Uruchom EloGlobal z menu Start albo ze Steama. Za pierwszym razem wybierasz język
aplikacji. Wszystko jest pokazywane w tym języku, a przewodnik i ta instrukcja są w nim czytane na głos. Potem
aplikacja wyjaśnia, co robi z głosami i wiadomościami innych osób: wszystko zostaje na twoim komputerze. Następnie
krótki przewodnik pokazuje pierwsze kroki. Otwiera się tylko za pierwszym razem; możesz go powtórzyć na tej karcie.

**Krok 2. Zainstaluj wirtualny kabel audio.** Zainstaluj VB-Audio Virtual Cable ze strony producenta i uruchom
komputer ponownie. Robi go VB-Audio, a nie EloGlobal, i jest darmowy do użytku osobistego. Windows potrzebuje go, aby
utworzyć wirtualny mikrofon.

**Krok 3. Ustaw Discorda.** Otwórz Discorda, potem Ustawienia użytkownika, potem Głos i wideo.

- Urządzenie wejściowe: CABLE Output z VB-Audio Virtual Cable.
- Urządzenie wyjściowe: twoje słuchawki.
- Wyłącz Redukcję szumów, Redukcję echa i Automatyczną regulację wzmocnienia.

**Krok 4. Ustaw aplikację.** Zostaw profil Standard, wszystko na tym komputerze. Na karcie Wyjście wysyłaj
przetłumaczony głos do CABLE Input. Na karcie Wejście zostaw metodę Tylko aplikacja Discord i wybierz swój prawdziwy
mikrofon. Na karcie Na żywo wybierz języki. Potem naciśnij Start albo klawisz F5.

**Gdy pierwszy raz naciśniesz Start**, aplikacja jednorazowo pobiera to, czego potrzebuje: model rozpoznawania mowy,
od 75 do 1600 megabajtów zależnie od komputera, model tłumaczenia około 280 megabajtów na każdą parę językową oraz
głosy twoich języków. Potem działa bez internetu.

**Powiedz osobom w rozmowie**, że używasz tłumacza, na przykład: Używam aplikacji do tłumaczenia, działa tylko na moim
komputerze i nic nie zapisuje.

=== 3. Główne okno
# Główne okno

Na górze jest pole profilu. Profil przechowuje wszystkie twoje ustawienia silników, języków i urządzeń. Profile
można zapisywać, zapisywać jako, usuwać, importować i eksportować. Profile startowe to: Standard, wszystko na tym
komputerze. Najszybszy, dla wolniejszych komputerów. Najlepsza jakość, dla komputera z kartą graficzną NVIDIA. Oraz
Tłumaczenie AI z Ollamą.

Zmiany zapisują się automatycznie mniej więcej sekundę później. Możesz to wyłączyć na karcie Ustawienia.

Obok pola profilu są trzy przyciski:

- **Napisy** pokazuje pływające okno napisów, które możesz przeciągać, zmieniać jego rozmiar kółkiem myszy i
  ustawiać prawym przyciskiem.
- **Czat** włącza tłumaczenie wiadomości tekstowych Discorda.
- **Start** uruchamia tłumacza głosu. Klawisz F5 robi to samo.

Karty to: Pulpit, Na żywo, Tekst, Wejście, Wyjście, Mowa, Tłumaczenie, Model AI, Głos, Konfiguracja, Ustawienia,
Instrukcja i Log. Następne rozdziały wyjaśniają te, których będziesz używać najczęściej.

=== 4. Pulpit
# Pulpit

Pulpit to twoje centrum sterowania. To pierwsza karta i pokazuje wszystko na jednym ekranie.

- **Karta tłumacza głosu** uruchamia i zatrzymuje tłumaczenie głosu na żywo oraz pokazuje, co właśnie robi:
  rozpoznaje, tłumaczy czy mówi.
- **Karta tłumaczenia czatu** uruchamia i zatrzymuje tłumaczenie wiadomości z Discorda. Ma też opcję czytania
  przetłumaczonych wiadomości na głos, po kolei albo tak, by nowa wiadomość przerywała czytaną.
- **Karta Ty** to miejsce na twoją nazwę na Discordzie i język, w którym piszesz.
- **Karta narzędzi** ma skróty do zaznaczania, by przetłumaczyć, OCR i okna napisów.
- **Karta skrótów** przypomina twoje skróty klawiszowe.
- Na dole Ostatnie tłumaczenia pokazuje ostatnio przetłumaczone zdania.

Ustawienia, które są w dwóch miejscach, na przykład na Pulpicie i na karcie Tekst, zawsze są zsynchronizowane.

=== 5. Tłumaczenie głosu na żywo
# Tłumaczenie głosu na żywo

To główna funkcja. Działa w dwóch kierunkach i każdy można włączyć osobno.

**Przychodzące: oni mówią, ty słyszysz.** Aplikacja słucha tylko aplikacji Discord, więc nigdy nie słyszy własnego
głosu, twojej gry ani muzyki, i słucha dalej, gdy mówi. Rozpoznaje mowę, tłumaczy ją, pokazuje napisy i, jeśli
chcesz, wypowiada tłumaczenie. Wybierasz język, którym mówią, albo automatyczne wykrywanie. Wybranie języka
sprawia, że rozpoznawanie na twoim PC jest mniej więcej dwa razy szybsze.

**Wychodzące: ty mówisz, oni słyszą.** Aplikacja słucha twojego mikrofonu, tłumaczy to, co mówisz, i wypowiada to
na Discordzie przez wirtualny kabel. Twój własny głos nie trafia na Discorda, tylko tłumaczenie. Aplikacja ostrzeże
cię, jeśli Discord używa twojego prawdziwego mikrofonu zamiast kabla.

**Słysz ludzi, klawisz F9.** Domyślnie słyszysz tylko tłumaczenia. Gdy tłumacz działa, aplikacja ścisza Discorda w
mikserze głośności Windows i oddaje mu głośność, gdy naciśniesz Stop. Naciśnij F9 albo przycisk Słysz ludzi, aby
słyszeć też ich własne głosy. Klawisz możesz zmienić na karcie Wejście.

**Jeden głos, po kolei.** Tłumaczenia z rozmowy i czytane na głos wiadomości z czatu mają jeden głos, więc nigdy
nie mówią jednocześnie. Wszystko jest mówione w kolejności, w jakiej zostało powiedziane, i nic nie jest pomijane:
następne zdanie przygotowuje się, gdy gra obecne, a gdy zdania się piętrzą, głos mówi trochę szybciej.

**Kto mówi.** Głos aplikacji może mówić, kto mówił, na przykład pierwsze dwie litery imienia albo pełną nazwę.
Wybierasz to na karcie Wyjście, w sekcji Głos aplikacji. W rozmowach imiona pochodzą z samej aplikacji Discord: na
karcie Wyjście, w sekcji Kto mówi, raz dodaj swoją własną aplikację Discord. Wiadomości z czatu zawsze mają nazwę
autora.

Na karcie **Na żywo** ustawiasz języki obu kierunków, patrzysz na wskaźniki poziomu i czytasz transkrypcję. Możesz
używać przycisku „naciśnij, aby mówić” i pola Wpisz, aby powiedzieć, w którym wpisujesz zdanie, a ono jest
tłumaczone i wypowiadane na Discordzie. Opcja Odpowiadaj w języku, którym mówią sprawia, że twój język wyjściowy
podąża za ostatnim językiem wykrytym u drugiej osoby.

Na karcie **Wejście** wybierasz, czego słuchać i jak startuje twój mikrofon: aktywacja głosowa, naciśnij, aby
mówić, albo przełączanie. Jest też regulacja czułości. Aplikacja rozpoznaje własny głos, gdy słyszy go twój
mikrofon, i go ignoruje.

Na karcie **Wyjście** wybierasz, gdzie grają tłumaczenia, wirtualny kabel dla twojego głosu, głos aplikacji i kto
mówi.

Wszystkie urządzenia dźwiękowe są też zebrane w jednym miejscu, na karcie Ustawienia, w sekcji Urządzenia
dźwiękowe.

=== 6. Silniki: mowa, tłumaczenie, AI i głos
# Silniki

Każdy krok tłumaczenia działa na twoim komputerze, a ustawienia możesz zmieniać w każdej chwili. Zapisują się w
profilu.

- **Karta Mowa.** Zamienia mowę na tekst za pomocą Whispera. Rozmiar modelu auto jest dobierany do komputera: mały
  model na procesorze, duży i dokładny na karcie graficznej NVIDIA. Większy model jest dokładniejszy, ale wolniejszy.
  Na tej karcie jest test mikrofonu.
- **Karta Tłumaczenie.** Silnik OPUS-MT Uniwersytetu Helsińskiego tłumaczy w około jedną dziesiątą sekundy na
  zdanie. Każdą parę językową pobiera się raz; języki bez bezpośredniego modelu idą przez angielski. Przycisk Pobierz
  teraz modele dla moich języków pobiera je przed rozmową. Możesz wybrać ton, a słowniczek ustala tłumaczenie imion
  i terminów z gier.
- **Karta Model AI.** Opcjonalna. Jeśli zainstalujesz na komputerze Ollamę lub LM Studio i model, silnik Model AI na
  tym komputerze tłumaczy z jego pomocą. Lepiej rozumie slang i kontekst, ale wymaga szybkiego komputera lub karty
  graficznej. Aplikacja łączy się tylko z serwerami AI na twoim komputerze lub w sieci lokalnej.
- **Karta Głos.** Głosy tego komputera: naturalne głosy Piper i Kokoro oraz głosy wbudowane w Windows. Auto wybiera
  głos dla każdego języka. Głos pobiera się raz, przy pierwszym użyciu. Głosy Kokoro brzmią bardzo naturalnie, ale
  wymagają szybkiego komputera. Aby dodać głosy Windows, otwórz Ustawienia systemu Windows, Czas i język, Mowa, Dodaj
  głosy. Dla każdego kierunku możesz ustawić szybkość, wysokość i głośność.

Każda karta ma przycisk Test, aby sprawdzić silnik przed użyciem.

=== 7. Prywatność i twoje dane
# Prywatność i twoje dane

EloGlobal działa tylko na twoim komputerze. To, co mówią ludzie w rozmowie, twój mikrofon, wiadomości czatu i
tłumaczony tekst nigdy nie opuszczają komputera. Aplikacja nie ma konta, statystyk użycia ani reklam.

**Głosy innych osób.** Gdy tłumacz działa, aplikacja słyszy, co mówią osoby w twojej rozmowie, aby to dla ciebie
przetłumaczyć. Powiedz im, że używasz tłumacza. W niektórych krajach potrzebna jest ich zgoda.

**Co jest zapisywane.** Twoje ustawienia i profile oraz pliki logów z komunikatami technicznymi, a nie z tym, co
mówią ludzie. Transkrypcje rozmów są zapisywane tylko wtedy, gdy to włączysz: karta Ustawienia, sekcja Prywatność i
informacje.

**Gdzie.** Wszystko, co zapisuje aplikacja, jest w twoim folderze użytkownika, w App Data, Local, EloGlobal:
profile, logi, transkrypcje i pobrane modele. Karta Ustawienia ma przyciski do otwierania folderu danych i folderu
modeli.

**Internet.** Aplikacja tylko raz pobiera pliki modeli. Opcjonalna funkcja Kto mówi loguje się do Discorda twoją
własną aplikacją Discorda. Aktualizacje przychodzą ze sklepu.

Karta Ustawienia pokazuje też ponownie informację o prywatności, a okno Informacje i licencje wymienia całe
oprogramowanie i wszystkie modele, na których opiera się EloGlobal.

=== 8. Tłumaczenie tekstu z Discorda
# Tłumaczenie tekstu z Discorda

Naciśnij przycisk **Czat** albo użyj karty czatu na Pulpicie. Aplikacja zacznie wtedy czytać wiadomości, które
widzisz w aplikacji Discord, przez ułatwienia dostępu Windows, jak czytnik ekranu. Nie potrzebuje tokenu ani bota i
niczego nie wysyła na Discorda.

Nowe wiadomości są tłumaczone i pokazywane nad oryginalnym tekstem, bezpośrednio w Discordzie, albo w małym oknie
obok. Wybierasz to na karcie Tekst, w Pokazuj tłumaczenia. Działa na serwerach, w wiadomościach prywatnych,
grupach, wątkach i postach na forum, nawet gdy Discord jest w tle. Wiadomości, które już są w twoim języku, i twoje
własne wiadomości są pomijane. Tłumaczenia widać tylko wtedy, gdy Discord jest aktywnym oknem, więc nigdy nie
zasłaniają gry.

**Czytanie na głos.** Na głos czytane są tylko nowe wiadomości. Wiadomości, do których przewijasz wstecz, edytowane
i stare wiadomości są tłumaczone na ekranie, ale nigdy nie są czytane. Wiadomości z czatu dzielą głos aplikacji z
tłumaczeniami z rozmowy, więc nigdy nie mówią naraz.

Karta Tekst ma więcej narzędzi:

- **Zaznacz, aby przetłumaczyć.** Zaznacz tekst albo kliknij dwukrotnie słowo, a obok myszy pojawi się okienko z
  tłumaczeniem.
- **Ctrl+Alt+T** tłumaczy bieżące zaznaczenie w dowolnej aplikacji.
- **Ctrl+Alt+Y** zastępuje to, co wpisałeś w polu wiadomości Discorda, tłumaczeniem na język używany na tym czacie.
- **Pisz w ich języku.** Pisz na karcie Tekst, potem skopiuj, wklej na Discordzie albo wyślij.
- **Ctrl+Alt+O** pozwala przeciągnąć ramkę nad dowolną częścią ekranu. Aplikacja odczytuje tekst przez OCR i
  pokazuje nad nim tłumaczenie. Może to powtarzać co kilka sekund.
- **Skopiowany tekst.** Opcjonalnie tłumaczy wszystko, co kopiujesz.

Każdy skrót możesz zmienić na karcie Tekst. Dla OCR innych alfabetów, na przykład rosyjskiego czy japońskiego,
dodaj ten język w Ustawieniach systemu Windows.

=== 9. Napisy i transkrypcje
# Napisy i transkrypcje

**Okno napisów** unosi się nad grą lub Discordem. Przeciągnij je, aby je przesunąć. Kółkiem myszy zmieniasz rozmiar.
Prawy przycisk otwiera opcje, na przykład ile linii pokazywać, czy pokazywać oryginalny tekst i tło. W Ustawieniach
zmieniasz rozmiar i czcionkę tekstu.

Rozmowę można zapisać jako **transkrypcję**. Domyślnie jest to wyłączone, bo transkrypcje zawierają słowa innych
osób. Włącz to na karcie Wyjście lub w Ustawieniach. Transkrypcje zapisują się w folderze danych, w transcripts.

Karta Log pokazuje, co robi aplikacja w czasie rzeczywistym. Ma też przyciski do otwierania logów, transkrypcji i
folderu danych. Jeśli coś pójdzie nie tak, najpierw zajrzyj do logu.

Pasek stanu na dole pokazuje opóźnienie każdego etapu: rozpoznawania mowy, tłumaczenia i głosu, aby było widać,
który krok jest wolny.

=== 10. Ustawienia i informacje
# Ustawienia i informacje

Karta **Ustawienia** ustala język aplikacji. Po zmianie aplikacja uruchamia się ponownie w nowym języku. Zbiera też
wszystkie urządzenia dźwiękowe w jednym miejscu: czego słucha aplikacja, twój mikrofon, gdzie grają tłumaczenia i
dokąd idzie twój przetłumaczony głos.

Steruje wyglądem aplikacji: motyw, ciemny lub jasny, czcionka i rozmiar tekstu aplikacji oraz tłumaczeń pokazywanych
w Discordzie, w małym oknie czatu i w okienkach. Są tu też wszystkie skróty, przełącznik trzymający okno nad innymi
oraz przyciski do przywracania położenia okien i otwierania folderów danych, modeli i logów.

Przełącznik Zapisuj zmiany automatycznie zapisuje profil mniej więcej sekundę po każdej zmianie. Domyślnie jest
włączony.

**Prywatność i informacje.** Przełącznik transkrypcji, informacja o prywatności i okno Informacje i licencje z
licencją EloGlobal i listą wszystkich składników, których używa.

**Aktualizacje** przychodzą ze sklepu, w którym zainstalowałeś EloGlobal: Microsoft Store lub Steam. Twoje
ustawienia, profile i pobrane modele zostają zachowane.

=== 11. Rozwiązywanie problemów
# Rozwiązywanie problemów

**Nikt nie słyszy mojego tłumaczenia.** W Discordzie urządzeniem wejściowym musi być CABLE Output. W aplikacji karta
Wyjście musi wysyłać do CABLE Input. Sprawdź, czy Redukcja szumów w Discordzie jest wyłączona.

**Aplikacja nic nie słyszy.** Na karcie Wejście sprawdź metodę. Przy Tylko aplikacja Discord Discord musi być
otwarty. Przy loopbacku urządzeniem musi być to, na którym gra Discord. Spójrz na wskaźniki poziomu na karcie Na
żywo. Jeśli się nie ruszają, ustawienie jest złe.

**Moje tłumaczenie słychać dwa razy albo aplikacja tłumaczy samą siebie.** Użyj metody Tylko aplikacja Discord na
karcie Wejście i załóż słuchawki.

**Discord milczy.** Tak ma być, gdy tłumacz działa: naciśnij F9, aby słyszeć też ludzi. Jeśli EloGlobal został nagle
zamknięty, otwórz go raz, a przywróci głośność Discorda, albo podgłośnij Discorda w mikserze głośności Windows.

**Ludzie słyszą mój prawdziwy głos.** W Discordzie urządzeniem wejściowym musi być CABLE Output, a nie twój mikrofon.
Aplikacja ostrzega, gdy Discord używa twojego prawdziwego mikrofonu.

**Działa wolno.** Na karcie Na żywo wybierz język, którym mówią, zamiast Wykrywaj automatycznie. Na karcie Mowa
wybierz mniejszy model albo użyj karty graficznej NVIDIA. Głosy Kokoro są wolne na wielu procesorach: wybierz głos
Piper lub Windows na karcie Głos.

**Nie ma głosu dla mojego języka.** Dodaj głos Windows: Ustawienia systemu Windows, Czas i język, Mowa, Dodaj głosy.
Potem naciśnij Odśwież listę głosów na karcie Głos.

**Pobieranie się nie udaje.** Sprawdź połączenie z internetem i naciśnij Start ponownie; pobieranie wznowi się tam,
gdzie się zatrzymało.

**Nadal nie działa?** Otwórz kartę Log i folder logów. Log pomoże, gdy zgłosisz problem przez stronę sklepu.

=== 12. O tej instrukcji
# O tej instrukcji

Czytasz instrukcję wbudowaną w EloGlobal. Lektor to głos, który działa na twoim komputerze, w języku aplikacji.
Działa offline i niczego nigdzie nie wysyła.

- **Dalej i Poprzedni** przełączają rozdziały. Lektor przestaje czytać stary rozdział i zaczyna nowy, a nowy tekst
  pojawia się w tym samym momencie.
- **Czytaj na głos** włącza lub wyłącza lektora. Gdy jest wyłączony, instrukcja to tylko tekst.
- **Czytaj ponownie** zaczyna bieżący rozdział od początku.
- **Stop** ucisza lektora.
- **Głos** i **Szybkość** zmieniają jego brzmienie. Możesz wybrać dowolny głos swojego języka na tym komputerze albo
  głos do pobrania.
- **Powtórz przewodnik** pokazuje ponownie pierwsze kroki.

Lektor milknie, gdy opuszczasz tę kartę, i nigdy nie zaczyna sam, gdy używasz tłumacza.

To koniec instrukcji. Miłej zabawy z EloGlobal!
