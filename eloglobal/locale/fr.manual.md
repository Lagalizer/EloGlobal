=== 1. Bienvenue
# Bienvenue dans EloGlobal

EloGlobal est un traducteur en temps réel pour Discord et toute autre discussion vocale. Tout fonctionne sur votre
propre PC : la reconnaissance vocale, la traduction et les voix. Rien de ce que quelqu'un dit ou écrit n'est envoyé
sur Internet.

- **Vous les entendez dans votre langue.** L'application écoute ce que disent les gens dans Discord, l'écrit, le
  traduit, affiche des sous-titres et peut vous lire la traduction avec une voix naturelle.
- **Ils vous entendent dans leur langue.** Vous parlez dans votre micro. L'application traduit ce que vous avez dit
  et le prononce dans Discord par un câble audio virtuel.
- **Le texte aussi.** Elle traduit les messages Discord des serveurs, des messages privés et des fils, tout texte
  que vous surlignez à la souris, et le texte de l'écran grâce à l'OCR. Vous pouvez aussi écrire dans leur langue.
- **Gratuit et privé.** Pas de compte, pas d'abonnement, pas de service en ligne. Les modèles sont téléchargés une
  fois, puis fonctionnent sans Internet.

Ce manuel compte douze chapitres. Utilisez les boutons Suivant et Précédent, ou cliquez sur un chapitre de la
liste. À chaque changement de chapitre, le narrateur arrête l'ancien et lit le nouveau. Le narrateur est une voix
qui fonctionne sur votre PC.

=== 2. Premier démarrage
# Premier démarrage

**Étape 1. Ouvrez l'application.** Lancez EloGlobal depuis le menu Démarrer ou depuis Steam. La première fois, vous
choisissez la langue de l'application. Tout s'affiche dans cette langue, et le guide et ce manuel sont lus à voix
haute dans cette langue. Ensuite, l'application explique ce qu'elle fait des voix et des messages des autres : tout
reste sur votre PC. Puis une courte visite guidée vous montre les premiers pas. Elle ne s'ouvre que cette première
fois ; vous pouvez la revoir depuis cet onglet.

**Étape 2. Installez un câble audio virtuel.** Installez VB-Audio Virtual Cable depuis son propre site, puis
redémarrez le PC. Il est édité par VB-Audio, pas par EloGlobal, et il est gratuit pour un usage personnel. Windows en
a besoin pour créer un micro virtuel.

**Étape 3. Réglez Discord.** Ouvrez Discord, puis Paramètres utilisateur, puis Voix et vidéo.

- Périphérique d'entrée : CABLE Output, de VB-Audio Virtual Cable.
- Périphérique de sortie : votre casque.
- Désactivez la Suppression du bruit, la Suppression de l'écho et le Contrôle automatique du gain.

**Étape 4. Réglez l'application.** Gardez le profil Standard, tout sur ce PC. Dans l'onglet Sortie, envoyez votre voix
traduite vers CABLE Input. Dans l'onglet Entrée, gardez la méthode Uniquement l'application Discord et choisissez
votre vrai micro. Dans l'onglet Direct, choisissez les langues. Appuyez ensuite sur Démarrer, ou sur la touche F5.

**La première fois que vous appuyez sur Démarrer**, l'application télécharge ce dont elle a besoin, une seule fois :
le modèle de reconnaissance vocale, entre 75 et 1600 mégaoctets selon votre PC, un modèle de traduction d'environ
280 mégaoctets par paire de langues, et les voix de vos langues. Ensuite, elle fonctionne sans Internet.

**Prévenez les personnes de votre appel** que vous utilisez un traducteur, par exemple : J'utilise une appli de
traduction, elle fonctionne uniquement sur mon PC et n'enregistre rien.

=== 3. La fenêtre principale
# La fenêtre principale

En haut se trouve la zone de profil. Un profil enregistre tous vos réglages de moteurs, de langues et de
périphériques. Vous pouvez enregistrer, enregistrer sous, supprimer, importer et exporter des profils. Les profils
de départ sont : Standard, tout sur ce PC. Le plus rapide, pour les PC plus lents. Meilleure qualité, pour un PC
avec une carte graphique NVIDIA. Et Traduction par IA avec Ollama.

Vos modifications sont enregistrées automatiquement environ une seconde après. Vous pouvez désactiver cela dans
l'onglet Paramètres.

À côté de la zone de profil se trouvent trois boutons :

- **Sous-titres** affiche une fenêtre de sous-titres flottante que vous pouvez déplacer, redimensionner avec la
  molette de la souris et configurer d'un clic droit.
- **Chat** active la traduction des messages texte de Discord.
- **Démarrer** lance le traducteur vocal. La touche F5 fait la même chose.

Les onglets sont : Tableau de bord, Direct, Texte, Entrée, Sortie, Parole, Traduction, Modèle d'IA, Voix,
Installation, Paramètres, Manuel et Journal. Les chapitres suivants expliquent ceux que vous utiliserez le plus.

=== 4. Tableau de bord
# Tableau de bord

Le Tableau de bord est votre poste de commande. C'est le premier onglet, et il montre tout d'un coup d'œil.

- La **carte du traducteur vocal** lance et arrête la traduction vocale en direct, et montre ce qu'il fait :
  reconnaissance, traduction ou parole.
- La **carte de la traduction du chat** lance et arrête la traduction des messages Discord. Elle permet aussi de
  lire à voix haute les messages traduits, l'un après l'autre, ou en laissant un nouveau message interrompre celui
  qui est lu.
- La **carte Vous** sert à indiquer votre nom sur Discord et la langue dans laquelle vous écrivez.
- La **carte des outils** donne accès au surlignage pour traduire, à l'OCR et à la fenêtre des sous-titres.
- La **carte des raccourcis** rappelle vos raccourcis clavier.
- En bas, Dernières traductions montre les dernières phrases traduites.

Les réglages présents à deux endroits, par exemple dans le Tableau de bord et dans l'onglet Texte, restent
toujours synchronisés.

=== 5. Traduction vocale en direct
# Traduction vocale en direct

C'est la fonction principale. Elle marche dans les deux sens, et chaque sens peut être activé séparément.

**Entrant : ils parlent, vous entendez.** L'application écoute seulement l'application Discord : elle n'entend donc
jamais sa propre voix, votre jeu ni votre musique, et elle continue d'écouter pendant qu'elle parle. Elle reconnaît
la parole, la traduit, affiche des sous-titres et, si vous le voulez, prononce la traduction. Vous choisissez la
langue qu'ils parlent, ou Détection automatique. Choisir la langue rend la reconnaissance sur votre PC environ deux
fois plus rapide.

**Sortant : vous parlez, ils entendent.** L'application écoute votre micro, traduit ce que vous dites et le
prononce dans Discord par le câble virtuel. Votre propre voix n'est pas envoyée à Discord, seulement la traduction.
L'application vous prévient si Discord utilise votre vrai micro au lieu du câble.

**Entendre les personnes, la touche F9.** Par défaut, vous n'entendez que les traductions. Pendant que le
traducteur tourne, l'application baisse Discord dans le mélangeur de volume de Windows, et lui rend son volume
quand vous appuyez sur Arrêter. Appuyez sur F9, ou sur le bouton Entendre les personnes, pour entendre aussi leurs
propres voix. Vous pouvez changer la touche dans l'onglet Entrée.

**Vous avez raté quelque chose ? Ctrl+Alt+R** redit la dernière traduction, dans votre casque. **Ctrl+Alt+L** fixe
la langue qu'ils parlent sur celle que l'application vient d'entendre : la reconnaissance est plus rapide, et vos
réponses vont dans cette langue. Appuyez à nouveau pour revenir à Détection automatique quand vous rejoignez un
autre groupe. Vous pouvez changer les deux touches dans l'onglet Entrée, et l'onglet Direct a aussi des boutons
pour elles.

**Une seule voix, dans l'ordre.** Les traductions de l'appel et les messages du chat lus à voix haute partagent une
seule voix : elles ne parlent jamais en même temps. Tout est dit dans l'ordre où cela a été prononcé, et rien n'est
sauté : la phrase suivante est préparée pendant que l'actuelle joue, et quand les phrases s'accumulent, la voix
parle un peu plus vite.

**Qui parle.** La voix de l'application peut dire qui a parlé, par exemple les deux premières lettres du nom, ou le
nom complet. Choisissez-le dans l'onglet Sortie, sous La voix de l'application. Dans les appels, les noms viennent
de l'application Discord elle-même : dans l'onglet Sortie, sous Qui parle, ajoutez une fois votre propre
application Discord. Les messages du chat ont toujours le nom de l'auteur.

Dans l'onglet **Direct**, vous réglez les langues des deux sens, regardez les vumètres et lisez la transcription.
Vous pouvez utiliser un bouton appuyer pour parler, et la case Tapez pour parler, où vous tapez une phrase qui est
traduite et dite dans Discord. L'option Répondre dans la langue qu'ils parlent fait suivre à votre langue de sortie
la dernière langue détectée chez l'autre personne.

Dans l'onglet **Entrée**, vous choisissez ce qu'il faut écouter et comment votre micro démarre : détection de la
voix, appuyer pour parler, ou bascule. Il y a aussi un réglage de sensibilité. L'application reconnaît sa propre
voix quand votre micro l'entend, et l'ignore.

Dans l'onglet **Sortie**, vous choisissez où jouent les traductions, le câble virtuel pour votre voix, la voix de
l'application et qui parle.

Tous les périphériques audio sont aussi réunis au même endroit, dans l'onglet Paramètres, sous Périphériques audio.

=== 6. Moteurs : parole, traduction, IA et voix
# Moteurs

Chaque étape de la traduction fonctionne sur votre PC, et vous pouvez changer les réglages à tout moment. Ils sont
enregistrés dans votre profil.

- **Onglet Parole.** Transforme la parole en texte avec Whisper. La taille de modèle auto est choisie pour votre PC :
  un petit modèle sur le processeur, un grand modèle précis sur une carte graphique NVIDIA. Un modèle plus grand est
  plus précis mais plus lent. Cet onglet propose un test du micro.
- **Onglet Traduction.** Le moteur OPUS-MT, de l'Université d'Helsinki, traduit en un dixième de seconde environ
  par phrase. Chaque paire de langues est téléchargée une fois ; les langues sans modèle direct passent par
  l'anglais. Le bouton Télécharger maintenant les modèles de mes langues les récupère avant votre appel. Vous
  pouvez choisir le ton, et un glossaire fixe la traduction des noms et des termes de jeu.
- **Onglet Modèle d'IA.** Facultatif. Si vous installez Ollama ou LM Studio et un modèle sur votre PC, le moteur
  Modèle d'IA sur ce PC traduit avec lui. Il comprend mieux l'argot et le contexte, mais demande un PC rapide ou une
  carte graphique. L'application ne parle qu'aux serveurs d'IA de votre ordinateur ou de votre réseau local.
- **Onglet Voix.** Les voix de ce PC : voix naturelles Piper et Kokoro, et voix intégrées à Windows. Auto choisit une
  voix pour chaque langue. Une voix est téléchargée une fois, la première fois qu'elle sert. Les voix Kokoro sont très
  naturelles mais demandent un PC rapide. Pour plus de voix Windows, ouvrez Paramètres Windows, Heure et langue,
  Voix, Ajouter des voix. Pour chaque sens, vous pouvez régler la vitesse, la hauteur et le volume.

Chaque onglet a un bouton Test pour essayer un moteur avant de l'utiliser.

=== 7. Confidentialité et vos données
# Confidentialité et vos données

EloGlobal fonctionne uniquement sur votre PC. Ce que disent les gens dans l'appel, votre micro, les messages du chat
et le texte que vous traduisez ne quittent jamais votre ordinateur. L'application n'a ni compte, ni statistiques
d'utilisation, ni publicité.

**Les voix des autres.** Pendant que le traducteur fonctionne, l'application entend ce que disent les personnes de
votre appel, pour vous le traduire. Dites-leur que vous utilisez un traducteur. Dans certains pays, leur
consentement est nécessaire.

**Ce qui est enregistré.** Vos réglages et profils, et des fichiers journaux avec des messages techniques, pas avec ce
que disent les gens. Les transcriptions des appels ne sont enregistrées que si vous l'activez, dans l'onglet
Paramètres, sous Confidentialité et à propos.

**Où.** Tout ce que l'application enregistre se trouve dans votre dossier utilisateur, dans App Data, Local,
EloGlobal : profils, journaux, transcriptions et modèles téléchargés. L'onglet Paramètres a des boutons pour ouvrir
le dossier des données et celui des modèles.

**Internet.** L'application ne télécharge que des fichiers de modèles, une fois. La fonction facultative Qui parle se
connecte à Discord avec votre propre application Discord. Les mises à jour viennent de la boutique.

L'onglet Paramètres affiche aussi à nouveau l'avis de confidentialité, et la fenêtre À propos et licences liste tous
les logiciels et modèles sur lesquels EloGlobal repose.

=== 8. Traduire le texte de Discord
# Traduire le texte de Discord

Appuyez sur le bouton **Chat**, ou utilisez la carte du chat dans le Tableau de bord. L'application lit alors les
messages que vous voyez dans l'application Discord, grâce aux fonctions d'accessibilité de Windows, comme un
lecteur d'écran. Elle n'a besoin ni de jeton ni de bot, et n'envoie rien à Discord.

Les nouveaux messages sont traduits et affichés par-dessus le texte d'origine, directement dans Discord, ou dans
une petite fenêtre à côté. Vous choisissez dans l'onglet Texte, sous Afficher les traductions. Cela marche dans les
serveurs, les messages privés, les groupes, les fils et les posts de forum, même avec Discord en arrière-plan. Les
messages déjà dans votre langue, et vos propres messages, sont ignorés. Les traductions ne s'affichent que lorsque
Discord est la fenêtre active, elles ne cachent donc jamais votre jeu.

**Lecture à voix haute.** Seuls les nouveaux messages sont lus à voix haute. Les messages vers lesquels vous
remontez, les messages modifiés et les anciens messages sont traduits à l'écran, mais jamais lus. Les messages du
chat partagent la voix de l'application avec les traductions de l'appel : les deux ne parlent jamais en même temps.

L'onglet Texte a d'autres outils :

- **Surligner pour traduire.** Sélectionnez du texte, ou double-cliquez sur un mot, et une bulle avec la
  traduction apparaît près de la souris.
- **Ctrl+Alt+T** traduit la sélection en cours dans n'importe quelle application.
- **Ctrl+Alt+Y** remplace ce que vous avez tapé dans la zone de message de Discord par sa traduction dans la langue
  utilisée dans ce chat.
- **Écrire dans leur langue.** Tapez dans l'onglet Texte, puis copiez, collez dans Discord ou envoyez.
- **Ctrl+Alt+O** vous permet de tracer un cadre sur n'importe quelle partie de l'écran. L'application lit le texte
  par OCR et affiche la traduction par-dessus. Cela peut se répéter toutes les quelques secondes.
- **Texte copié.** En option, traduit tout ce que vous copiez.

Vous pouvez modifier tous les raccourcis dans l'onglet Texte. Pour l'OCR d'autres alphabets, comme le russe ou le
japonais, ajoutez cette langue dans les Paramètres de Windows.

=== 9. Sous-titres et transcriptions
# Sous-titres et transcriptions

La **fenêtre de sous-titres** flotte au-dessus de votre jeu ou de Discord. Faites-la glisser pour la déplacer.
Utilisez la molette de la souris pour la redimensionner. Faites un clic droit pour les options, comme le nombre de
lignes, l'affichage du texte original et le fond. Dans Paramètres, vous changez la taille et la police du texte.

Une conversation peut être enregistrée comme **transcription**. C'est désactivé par défaut, car les transcriptions
contiennent les paroles d'autres personnes. Activez-le dans l'onglet Sortie ou dans Paramètres. Les transcriptions
sont enregistrées dans le dossier des données, sous transcripts.

L'onglet Journal montre ce que fait l'application en temps réel. Il a aussi des boutons pour ouvrir les journaux,
les transcriptions et le dossier des données. Si quelque chose ne va pas, le journal est le premier endroit à
consulter.

La barre d'état en bas affiche le délai de chaque étape : reconnaissance vocale, traduction et voix, pour voir quelle
étape est lente.

=== 10. Paramètres et à propos
# Paramètres et à propos

L'onglet **Paramètres** définit la langue de l'application. Après un changement, l'application redémarre dans la
nouvelle langue. Il réunit aussi tous les périphériques audio au même endroit : ce que l'application écoute, votre
micro, où jouent les traductions et où va votre voix traduite.

Il règle l'apparence : le thème, sombre ou clair, la police et la taille du texte de l'application et des
traductions affichées dans Discord, dans la petite fenêtre de chat et dans les fenêtres contextuelles. Il réunit
aussi tous les raccourcis, une option pour garder la fenêtre au-dessus des autres, et des boutons pour replacer les
fenêtres et ouvrir les dossiers des données, des modèles et des journaux.

L'option Enregistrer les changements automatiquement enregistre votre profil environ une seconde après chaque
changement. Elle est activée par défaut.

**Confidentialité et à propos.** L'option des transcriptions, l'avis de confidentialité et la fenêtre À propos et
licences, avec la licence d'EloGlobal et la liste de tous les composants qu'il utilise.

**Les mises à jour** viennent de la boutique où vous avez installé EloGlobal, le Microsoft Store ou Steam. Vos
réglages, profils et modèles téléchargés sont conservés.

=== 11. Dépannage
# Dépannage

**Personne n'entend ma traduction.** Dans Discord, le périphérique d'entrée doit être CABLE Output. Dans
l'application, l'onglet Sortie doit envoyer vers CABLE Input. Vérifiez que la Suppression du bruit est désactivée
dans Discord.

**L'application n'entend rien.** Dans l'onglet Entrée, vérifiez la méthode. Avec Uniquement l'application Discord,
Discord doit être ouvert. Avec le loopback, le périphérique doit être celui où joue Discord. Regardez les vumètres
de l'onglet Direct. S'ils ne bougent pas, le réglage est faux.

**Ma traduction s'entend deux fois, ou l'application se traduit elle-même.** Utilisez la méthode Uniquement
l'application Discord dans l'onglet Entrée, et portez un casque.

**Discord est silencieux.** C'est voulu pendant que le traducteur tourne : appuyez sur F9 pour entendre aussi les
gens. Si EloGlobal a été fermé brutalement, ouvrez-le une fois et il rend son volume à Discord, ou montez Discord
dans le mélangeur de volume de Windows.

**Les gens entendent ma vraie voix.** Dans Discord, le périphérique d'entrée doit être CABLE Output, pas votre
micro. L'application vous avertit quand Discord utilise votre vrai micro.

**C'est lent.** Dans l'onglet Direct, choisissez la langue qu'ils parlent au lieu de Détection automatique. Dans
l'onglet Parole, choisissez un modèle plus petit, ou utilisez une carte graphique NVIDIA. Les voix Kokoro sont
lentes sur beaucoup de processeurs : choisissez une voix Piper ou Windows dans l'onglet Voix.

**Pas de voix pour ma langue.** Ajoutez une voix Windows : Paramètres Windows, Heure et langue, Voix, Ajouter des
voix. Appuyez ensuite sur Recharger la liste des voix dans l'onglet Voix.

**Un téléchargement échoue.** Vérifiez votre connexion Internet et appuyez de nouveau sur Démarrer ; le
téléchargement reprend là où il s'est arrêté.

**Toujours bloqué ?** Ouvrez l'onglet Journal et le dossier des journaux. Le journal aide quand vous signalez un
problème via la page de la boutique.

=== 12. À propos de ce manuel
# À propos de ce manuel

Vous lisez le manuel intégré à EloGlobal. Le narrateur est une voix qui fonctionne sur votre PC, dans la langue de
l'application. Il fonctionne hors ligne et n'envoie rien nulle part.

- **Suivant et Précédent** passent d'un chapitre à l'autre. Le narrateur arrête l'ancien chapitre et commence le
  nouveau, et le nouveau texte s'affiche en même temps.
- **Lire à voix haute** active ou désactive le narrateur. Désactivé, le manuel n'est que du texte.
- **Relire** reprend le chapitre en cours depuis le début.
- **Arrêter** fait taire le narrateur.
- **Voix** et **Vitesse** changent sa façon de parler. Vous pouvez choisir n'importe quelle voix de votre langue sur
  ce PC, ou une à télécharger.
- **Revoir la visite guidée** montre de nouveau les premiers pas.

Le narrateur se tait quand vous quittez cet onglet, et il ne démarre jamais tout seul pendant que vous utilisez le
traducteur.

C'est la fin du manuel. Profitez bien d'EloGlobal !
