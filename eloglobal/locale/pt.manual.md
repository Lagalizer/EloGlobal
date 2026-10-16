=== 1. Bem-vindo
# Bem-vindo ao EloGlobal

O EloGlobal é um tradutor em tempo real para o Discord e qualquer outro chat de voz. Tudo roda no seu próprio PC:
o reconhecimento de fala, a tradução e as vozes. Nada do que alguém diz ou escreve é enviado para a internet.

- **Você ouve os outros no seu idioma.** O app escuta o que as pessoas dizem no Discord, escreve, traduz, mostra
  legendas e pode ler a tradução para você com uma voz natural.
- **Eles ouvem você no idioma deles.** Você fala no microfone. O app traduz o que você disse e fala no Discord
  por meio de um cabo de áudio virtual.
- **Texto também.** Ele traduz mensagens do Discord em servidores, mensagens diretas e tópicos, qualquer texto que
  você selecionar com o mouse, e texto da tela usando OCR. Você também pode escrever no idioma deles.
- **Grátis e privado.** Sem conta, sem assinatura e sem serviço online. Os modelos são baixados uma vez e depois
  funcionam sem internet.

Este manual tem doze capítulos. Use os botões Próximo e Anterior, ou clique num capítulo da lista. Toda vez que
você muda de capítulo, o narrador para o antigo e lê o novo. O narrador é uma voz que roda no seu PC.

=== 2. Primeiro início
# Primeiro início

**Passo 1. Abra o app.** Abra o EloGlobal pelo menu Iniciar ou pela Steam. Na primeira vez, você escolhe o idioma do
app. Tudo aparece nesse idioma, e o guia e este manual são lidos em voz alta nele. Depois o app explica o que faz
com as vozes e mensagens das outras pessoas: tudo fica no seu PC. Em seguida, um tour guiado curto mostra os
primeiros passos. Ele só abre nessa primeira vez; você pode vê-lo de novo nesta aba.

**Passo 2. Instale um cabo de áudio virtual.** Instale o VB-Audio Virtual Cable pelo site do próprio fabricante e
reinicie o PC. Ele é feito pela VB-Audio, não pelo EloGlobal, e é grátis para uso pessoal. O Windows precisa dele
para criar um microfone virtual.

**Passo 3. Configure o Discord.** Abra o Discord, depois Configurações de usuário, depois Voz e vídeo.

- Dispositivo de entrada: CABLE Output, do VB-Audio Virtual Cable.
- Dispositivo de saída: seus fones.
- Desligue a Supressão de ruído, o Cancelamento de eco e o Controle automático de ganho.

**Passo 4. Configure o app.** Mantenha o perfil Padrão, tudo neste PC. Na aba Saída, envie sua voz traduzida para o
CABLE Input. Na aba Entrada, mantenha o método Só o app do Discord e escolha seu microfone de verdade. Na aba Ao
vivo, escolha os idiomas. Depois aperte Iniciar, ou a tecla F5.

**Na primeira vez que você aperta Iniciar**, o app baixa o que precisa, uma vez só: o modelo de reconhecimento de
fala, entre 75 e 1600 megabytes conforme o seu PC, um modelo de tradução de cerca de 280 megabytes para cada par
de idiomas, e as vozes dos seus idiomas. Depois disso, ele funciona sem internet.

**Avise as pessoas da sua chamada** que você usa um tradutor, por exemplo: Eu uso um app de tradução, ele roda só no
meu PC e não salva nada.

=== 3. A janela principal
# A janela principal

No topo fica a caixa de perfil. Um perfil guarda todas as suas configurações de mecanismos, idiomas e
dispositivos. Você pode salvar, salvar como, excluir, importar e exportar perfis. Os perfis iniciais são: Padrão,
tudo neste PC. Mais rápido, para PCs mais lentos. Melhor qualidade, para um PC com placa de vídeo NVIDIA. E
Tradução por IA com o Ollama.

Suas alterações são salvas automaticamente cerca de um segundo depois que você as faz. Você pode desligar isso na
aba Configurações.

Ao lado da caixa de perfil há três botões:

- **Legendas** mostra uma janela de legendas flutuante que você pode arrastar, redimensionar com a roda do mouse e
  configurar com o botão direito.
- **Chat** liga a tradução das mensagens de texto do Discord.
- **Iniciar** começa o tradutor de voz. A tecla F5 faz o mesmo.

As abas são: Painel, Ao vivo, Texto, Entrada, Saída, Fala, Tradução, Modelo de IA, Voz, Configuração,
Configurações, Manual e Log. Os próximos capítulos explicam as que você mais vai usar.

=== 4. Painel
# Painel

O Painel é o seu painel de controle. É a primeira aba e mostra tudo de uma vez.

- O **cartão do tradutor de voz** inicia e para a tradução de voz ao vivo, e mostra o que ele está fazendo:
  reconhecendo, traduzindo ou falando.
- O **cartão da tradução do chat** inicia e para a tradução das mensagens do Discord. Ele também tem a opção de
  ler as mensagens traduzidas em voz alta, uma depois da outra, ou deixando uma mensagem nova interromper a que
  está sendo lida.
- O **cartão Você** é onde você coloca seu nome no Discord e o idioma em que escreve.
- O **cartão de ferramentas** tem atalhos para selecionar para traduzir, OCR e a janela de legendas.
- O **cartão de atalhos** lembra os seus atalhos de teclado.
- Embaixo, Últimas traduções mostra as últimas frases traduzidas.

Opções que aparecem em dois lugares, por exemplo no Painel e na aba Texto, ficam sempre sincronizadas.

=== 5. Tradução de voz ao vivo
# Tradução de voz ao vivo

Esta é a função principal. Ela funciona em duas direções, e cada uma pode ser ligada separadamente.

**Entrada: eles falam, você ouve.** O app escuta só o app do Discord, então nunca ouve a própria voz, o seu jogo ou
a sua música, e continua ouvindo enquanto fala. Ele reconhece a fala, traduz, mostra legendas e, se você quiser,
fala a tradução. Você escolhe o idioma que eles falam, ou Detectar automaticamente. Escolher o idioma deixa o
reconhecimento no seu PC cerca de duas vezes mais rápido.

**Saída: você fala, eles ouvem.** O app escuta o seu microfone, traduz o que você diz e fala no Discord pelo cabo
virtual. Sua própria voz não é enviada ao Discord, só a tradução. O app avisa se o Discord usar o seu microfone de
verdade em vez do cabo.

**Ouvir as pessoas, a tecla F9.** Por padrão você ouve só as traduções. Enquanto o tradutor roda, o app abaixa o
Discord no mixer de volume do Windows e devolve o volume quando você aperta Parar. Aperte F9, ou o botão Ouvir as
pessoas, para ouvir também a voz delas. Você pode trocar a tecla na aba Entrada.

**Perdeu alguma coisa? Ctrl+Alt+R** diz a última tradução de novo, nos seus fones. **Ctrl+Alt+L** fixa o idioma
que eles falam no idioma que o app acabou de ouvir: o reconhecimento fica mais rápido, e as suas respostas vão
para esse idioma. Aperte de novo para voltar a Detectar automaticamente quando entrar em outro grupo. Você pode
trocar as duas teclas na aba Entrada, e a aba Ao vivo também tem botões para elas.

**Uma voz, em ordem.** As traduções da chamada e as mensagens do chat lidas em voz alta usam uma só voz, então
nunca falam uma por cima da outra. Tudo é dito na ordem em que foi falado, e nada é pulado: a próxima frase é
preparada enquanto a atual toca, e quando as frases se acumulam a voz fala um pouco mais rápido.

**Quem está falando.** A voz do app pode dizer quem falou, por exemplo as duas primeiras letras do nome, ou o nome
completo. Escolha isso na aba Saída, em A voz do app. Nas chamadas os nomes vêm do próprio app do Discord: na aba
Saída, em Quem está falando, adicione uma vez o seu próprio aplicativo do Discord. As mensagens do chat sempre têm
o nome do autor.

Na aba **Ao vivo** você define os idiomas das duas direções, vê os medidores de nível e lê a transcrição. Você
pode usar um botão de aperte para falar, e a caixa Digite para falar, onde você digita uma frase e ela é
traduzida e falada no Discord. A opção Responder no idioma que eles falam faz o seu idioma de saída seguir o
último idioma detectado da outra pessoa.

Na aba **Entrada** você escolhe o que escutar e como o seu microfone começa: detecção de voz, aperte para falar ou
alternar. Há também um controle de sensibilidade. O app reconhece a própria voz quando o seu microfone a ouve, e a
ignora.

Na aba **Saída** você escolhe onde as traduções tocam, o cabo virtual da sua voz, a voz do app e quem está falando.

Todos os dispositivos de som também ficam juntos num só lugar, na aba Configurações, em Dispositivos de som.

=== 6. Mecanismos: fala, tradução, IA e voz
# Mecanismos

Cada etapa da tradução roda no seu PC, e você pode mudar as configurações a qualquer momento. Elas ficam salvas no
seu perfil.

- **Aba Fala.** Transforma a fala em texto com o Whisper. O tamanho de modelo auto é escolhido para o seu PC: um
  modelo pequeno no processador, um grande e preciso numa placa de vídeo NVIDIA. Um modelo maior é mais preciso,
  porém mais lento. Há um teste de microfone nesta aba.
- **Aba Tradução.** O mecanismo OPUS-MT, da Universidade de Helsinque, traduz em cerca de um décimo de segundo por
  frase. Cada par de idiomas é baixado uma vez; idiomas sem modelo direto passam pelo inglês. O botão Baixar agora
  os modelos dos meus idiomas busca tudo antes da sua chamada. Você pode escolher o tom, e um glossário permite
  fixar como nomes e termos de jogo são traduzidos.
- **Aba Modelo de IA.** Opcional. Se você instalar o Ollama ou o LM Studio e um modelo no seu PC, o mecanismo Modelo
  de IA neste PC traduz com ele. Ele entende melhor gírias e contexto, mas precisa de um PC rápido ou de uma placa
  de vídeo. O app só fala com servidores de IA no seu próprio computador ou na rede local.
- **Aba Voz.** As vozes deste PC: vozes naturais Piper e Kokoro, e as vozes que vêm com o Windows. Auto escolhe uma
  voz para cada idioma. Uma voz é baixada uma vez, na primeira vez que é usada. As vozes Kokoro soam bem naturais,
  mas precisam de um PC rápido. Para ter mais vozes do Windows, abra Configurações do Windows, Hora e idioma, Fala,
  Adicionar vozes. Para cada direção você pode ajustar a velocidade, o tom e o volume.

Cada aba tem um botão de Teste, para você conferir um mecanismo antes de usar.

=== 7. Privacidade e seus dados
# Privacidade e seus dados

O EloGlobal funciona só no seu PC. O que as pessoas dizem na chamada, seu microfone, as mensagens do chat e o texto
que você traduz nunca saem do seu computador. O app não tem conta, nem estatísticas de uso, nem anúncios.

**As vozes das outras pessoas.** Enquanto o tradutor roda, o app ouve o que as pessoas da sua chamada dizem, para
traduzir para você. Conte a elas que você usa um tradutor. Em alguns países é preciso o consentimento delas.

**O que é salvo.** Suas configurações e perfis, e arquivos de log com mensagens técnicas, não com o que as pessoas
dizem. As transcrições das chamadas só são salvas se você ligar essa opção, na aba Configurações, em Privacidade e
sobre.

**Onde.** Tudo o que o app salva fica na sua pasta de usuário, em App Data, Local, EloGlobal: perfis, logs,
transcrições e os modelos baixados. A aba Configurações tem botões para abrir a pasta de dados e a pasta de
modelos.

**Internet.** O app só baixa arquivos de modelos, uma vez. O recurso opcional Quem está falando faz login no Discord
com o seu próprio aplicativo do Discord. As atualizações vêm da loja.

A aba Configurações também mostra de novo o aviso de privacidade, e a janela Sobre e licenças lista todos os
softwares e modelos em que o EloGlobal se baseia.

=== 8. Traduzindo texto do Discord
# Traduzindo texto do Discord

Aperte o botão **Chat**, ou use o cartão do chat no Painel. O app então lê as mensagens que você vê no app do
Discord, usando os recursos de acessibilidade do Windows, como um leitor de tela. Ele não precisa de token nem de
bot, e não envia nada ao Discord.

As mensagens novas são traduzidas e desenhadas sobre o texto original, dentro do próprio Discord, ou numa janela
pequena ao lado dele. Você escolhe isso na aba Texto, em Mostrar traduções. Funciona em servidores, mensagens
diretas, grupos, tópicos e posts de fórum, mesmo com o Discord em segundo plano. Mensagens que já estão no seu
idioma, e as suas próprias mensagens, são puladas. As traduções só aparecem enquanto o Discord é a janela ativa,
então elas nunca cobrem o seu jogo.

**Leitura em voz alta.** Só as mensagens novas são lidas em voz alta. As mensagens para as quais você rola de
volta, as mensagens editadas e as antigas são traduzidas na tela, mas nunca lidas. As mensagens do chat usam a
mesma voz do app que as traduções da chamada, então as duas nunca falam ao mesmo tempo.

A aba Texto tem mais ferramentas:

- **Selecionar para traduzir.** Selecione um texto, ou dê clique duplo numa palavra, e aparece um popup com a
  tradução perto do mouse.
- **Ctrl+Alt+T** traduz a seleção atual em qualquer app.
- **Ctrl+Alt+Y** troca o que você digitou na caixa de mensagem do Discord pela tradução no idioma usado naquele
  chat.
- **Escrever no idioma deles.** Digite na aba Texto e depois copie, cole no Discord ou envie.
- **Ctrl+Alt+O** deixa você arrastar uma caixa sobre qualquer parte da tela. O app lê o texto com OCR e mostra a
  tradução por cima. Isso pode se repetir a cada poucos segundos.
- **Texto copiado.** Opcionalmente, traduz tudo o que você copia.

Você pode mudar todos os atalhos na aba Texto. Para OCR em outros alfabetos, como russo ou japonês, adicione esse
idioma nas Configurações do Windows.

=== 9. Legendas e transcrições
# Legendas e transcrições

A **janela de legendas** flutua acima do seu jogo ou do Discord. Arraste para mover. Use a roda do mouse para
redimensionar. Clique com o botão direito para ver opções, como quantas linhas mostrar, se mostra o texto original
e o fundo. Em Configurações você muda o tamanho e a fonte do texto.

Uma conversa pode ser salva como **transcrição**. Isso vem desligado, porque as transcrições contêm as palavras de
outras pessoas. Ligue na aba Saída ou em Configurações. As transcrições ficam na pasta de dados, em transcripts.

A aba Log mostra o que o app está fazendo em tempo real. Ela também tem botões para abrir os logs, as transcrições
e a pasta de dados. Se algo der errado, o log é o primeiro lugar para olhar.

A barra de status embaixo mostra o atraso de cada etapa: reconhecimento de fala, tradução e voz, para você ver qual
etapa está lenta.

=== 10. Configurações e sobre
# Configurações e sobre

A aba **Configurações** define o idioma do app. Depois que você o muda, o app reinicia no novo idioma. Ela também
reúne todos os dispositivos de som num só lugar: o que o app escuta, seu microfone, onde as traduções tocam e para
onde vai sua voz traduzida.

Ela controla a aparência do app: o tema, escuro ou claro, a fonte e o tamanho do texto do app e das traduções
mostradas dentro do Discord, na janelinha de chat e nos pop-ups. Também tem todos os atalhos num só lugar, uma
opção para manter a janela acima das outras, e botões para reposicionar as janelas e abrir as pastas de dados, de
modelos e de logs.

A opção Salvar alterações automaticamente mantém seu perfil salvo cerca de um segundo depois de cada mudança. Ela
vem ligada.

**Privacidade e sobre.** A opção das transcrições, o aviso de privacidade e a janela Sobre e licenças, com a
licença do EloGlobal e a lista de todos os componentes que ele usa.

**As atualizações** vêm da loja onde você instalou o EloGlobal, a Microsoft Store ou a Steam. Suas configurações,
perfis e modelos baixados são mantidos.

=== 11. Solução de problemas
# Solução de problemas

**Ninguém ouve minha tradução.** No Discord, o dispositivo de entrada deve ser CABLE Output. No app, a aba Saída
deve enviar para CABLE Input. Confira se a Supressão de ruído está desligada no Discord.

**O app não ouve nada.** Na aba Entrada, confira o método. Com Só o app do Discord, o Discord precisa estar aberto.
Com loopback, o dispositivo deve ser aquele onde o Discord toca. Olhe os medidores de nível na aba Ao vivo. Se eles
não se mexem, a configuração está errada.

**Minha tradução aparece duas vezes, ou o app traduz a si mesmo.** Use o método Só o app do Discord na aba Entrada e
use fones.

**O Discord está mudo.** Isso é de propósito enquanto o tradutor roda: aperte F9 para ouvir as pessoas também. Se o
EloGlobal foi fechado de repente, abra-o uma vez e ele devolve o volume do Discord, ou aumente o Discord no mixer de
volume do Windows.

**As pessoas ouvem minha voz de verdade.** No Discord, o dispositivo de entrada deve ser CABLE Output, não seu
microfone. O app mostra um aviso quando o Discord usa seu microfone de verdade.

**Está lento.** Na aba Ao vivo, escolha o idioma que eles falam em vez de Detectar automaticamente. Na aba Fala,
escolha um modelo menor, ou use uma placa de vídeo NVIDIA. As vozes Kokoro são lentas em muitos processadores:
escolha uma voz Piper ou do Windows na aba Voz.

**Não há voz para o meu idioma.** Adicione uma voz do Windows: Configurações do Windows, Hora e idioma, Fala,
Adicionar vozes. Depois aperte Recarregar lista de vozes na aba Voz.

**Um download falha.** Confira sua conexão com a internet e aperte Iniciar de novo; o download continua de onde
parou.

**Ainda com problema?** Abra a aba Log e a pasta de logs. O log ajuda quando você relata um problema pela página da
loja.

=== 12. Sobre este manual
# Sobre este manual

Você está lendo o manual que vem no EloGlobal. O narrador é uma voz que roda no seu PC, no idioma do app. Ele
funciona offline e não envia nada para lugar nenhum.

- **Próximo e Anterior** passam de um capítulo a outro. O narrador para de ler o capítulo antigo e começa o novo,
  e o texto novo aparece ao mesmo tempo.
- **Ler em voz alta** liga ou desliga o narrador. Quando está desligado, o manual é só texto.
- **Ler de novo** recomeça o capítulo atual do início.
- **Parar** silencia o narrador.
- **Voz** e **Velocidade** mudam como ele soa. Você pode escolher qualquer voz do seu idioma neste PC, ou uma para
  baixar.
- **Ver o tour guiado de novo** mostra os primeiros passos outra vez.

O narrador fica em silêncio quando você sai desta aba, e nunca começa sozinho enquanto você usa o tradutor.

Esse é o fim do manual. Aproveite o EloGlobal!
