=== 1. Bienvenida
# Bienvenido a EloGlobal

EloGlobal es un traductor en tiempo real para Discord y cualquier otro chat de voz. Todo funciona en tu propio PC:
el reconocimiento de voz, la traducción y las voces. Nada de lo que alguien dice o escribe se envía a internet.

- **Oyes a los demás en tu idioma.** La app escucha lo que la gente dice en Discord, lo escribe, lo traduce,
  muestra subtítulos y puede leerte la traducción con una voz natural.
- **Ellos te oyen en su idioma.** Hablas al micrófono. La app traduce lo que dijiste y lo dice en Discord a través
  de un cable de audio virtual.
- **También texto.** Traduce mensajes de Discord en servidores, mensajes directos e hilos, cualquier texto que
  selecciones con el ratón y texto de la pantalla con OCR. También puedes escribir en su idioma.
- **Gratis y privado.** Sin cuenta, sin suscripción y sin servicios en línea. Los modelos se descargan una vez y
  luego funcionan sin internet.

Este manual tiene doce capítulos. Usa los botones Siguiente y Anterior, o haz clic en un capítulo de la lista. Cada
vez que cambias de capítulo, el narrador deja el anterior y lee el nuevo. El narrador es una voz que funciona en tu
PC.

=== 2. Primer inicio
# Primer inicio

**Paso 1. Abre la app.** Abre EloGlobal desde el menú Inicio o desde Steam. La primera vez eliges el idioma de la
app. Todo se muestra en ese idioma, y la guía y este manual se leen en voz alta en él. Después la app explica qué
hace con las voces y los mensajes de los demás: todo se queda en tu PC. Luego una breve visita guiada te muestra
los primeros pasos. Solo se abre esta primera vez; puedes repetirla desde esta pestaña.

**Paso 2. Instala un cable de audio virtual.** Instala VB-Audio Virtual Cable desde su propia web y reinicia el
PC. Lo hace VB-Audio, no EloGlobal, y es gratis para uso personal. Windows lo necesita para crear un micrófono
virtual.

**Paso 3. Configura Discord.** Abre Discord, luego Ajustes de usuario y luego Voz y vídeo.

- Dispositivo de entrada: CABLE Output, de VB-Audio Virtual Cable.
- Dispositivo de salida: tus auriculares.
- Desactiva la Supresión de ruido, la Cancelación de eco y el Control automático de ganancia.

**Paso 4. Configura la app.** Mantén el perfil Estándar, todo en este PC. En la pestaña Salida, envía tu voz
traducida a CABLE Input. En la pestaña Entrada, mantén el método Solo la app de Discord y elige tu micrófono real.
En la pestaña En directo, elige los idiomas. Después pulsa Iniciar, o la tecla F5.

**La primera vez que pulsas Iniciar**, la app descarga lo que necesita, una sola vez: el modelo de reconocimiento de
voz, entre 75 y 1600 megabytes según tu PC, un modelo de traducción de unos 280 megabytes por cada par de idiomas, y
las voces de tus idiomas. Después funciona sin internet.

**Avisa a las personas de tu llamada** de que usas un traductor, por ejemplo: Uso una app de traducción, funciona
solo en mi PC y no guarda nada.

=== 3. La ventana principal
# La ventana principal

Arriba está el cuadro de perfil. Un perfil guarda todos tus ajustes de motores, idiomas y dispositivos. Puedes
guardar, guardar como, eliminar, importar y exportar perfiles. Los perfiles iniciales son: Estándar, todo en este
PC. Más rápido, para PC más lentos. Máxima calidad, para un PC con tarjeta gráfica NVIDIA. Y Traducción con IA con
Ollama.

Tus cambios se guardan automáticamente un segundo después de hacerlos. Puedes desactivarlo en la pestaña Ajustes.

Junto al cuadro de perfil hay tres botones:

- **Subtítulos** muestra una ventana flotante de subtítulos que puedes arrastrar, redimensionar con la rueda del
  ratón y configurar con el botón derecho.
- **Chat** activa la traducción de los mensajes de texto de Discord.
- **Iniciar** pone en marcha el traductor de voz. La tecla F5 hace lo mismo.

Las pestañas son: Panel, En directo, Texto, Entrada, Salida, Voz a texto, Traducción, Modelo de IA, Voz,
Configuración, Ajustes, Manual y Registro. Los siguientes capítulos explican las que más usarás.

=== 4. Panel
# Panel

El Panel es tu centro de control. Es la primera pestaña y lo muestra todo de un vistazo.

- La **tarjeta del traductor de voz** inicia y detiene la traducción de voz en directo, y muestra lo que está
  haciendo: reconociendo, traduciendo o hablando.
- La **tarjeta de la traducción del chat** inicia y detiene la traducción de los mensajes de Discord. También
  tiene la opción de leer en voz alta los mensajes traducidos, uno tras otro, o dejando que un mensaje nuevo
  interrumpa al que se está leyendo.
- La **tarjeta Tú** es donde pones tu nombre de Discord y el idioma en el que escribes.
- La **tarjeta de herramientas** tiene accesos a seleccionar para traducir, el OCR y la ventana de subtítulos.
- La **tarjeta de atajos** te recuerda tus atajos de teclado.
- Abajo, Últimas traducciones muestra las últimas frases traducidas.

Los ajustes que aparecen en dos sitios, por ejemplo en el Panel y en la pestaña Texto, siempre están sincronizados.

=== 5. Traducción de voz en directo
# Traducción de voz en directo

Es la función principal. Funciona en dos direcciones, y cada una se puede activar por separado.

**Entrada: ellos hablan, tú oyes.** La app escucha solo la app de Discord, así que nunca oye su propia voz, tu
juego ni tu música, y sigue escuchando mientras habla. Reconoce la voz, la traduce, muestra subtítulos y, si
quieres, dice la traducción. Eliges el idioma que hablan, o Detectar automáticamente. Elegir el idioma hace que el
reconocimiento en tu PC sea casi el doble de rápido.

**Saliente: tú hablas, ellos oyen.** La app escucha tu micrófono, traduce lo que dices y lo dice en Discord a
través del cable virtual. Tu propia voz no se envía a Discord, solo la traducción. La app te avisa si Discord usa
tu micrófono real en lugar del cable.

**Oír a las personas, la tecla F9.** Por defecto oyes solo las traducciones. Mientras el traductor funciona, la app
baja Discord en el mezclador de volumen de Windows y le devuelve el volumen cuando pulsas Detener. Pulsa F9, o el
botón Oír a las personas, para oír también sus propias voces. Puedes cambiar la tecla en la pestaña Entrada.

**Una sola voz, en orden.** Las traducciones de la llamada y los mensajes del chat leídos en voz alta comparten una
sola voz, así que nunca se pisan. Todo se dice en el orden en que se habló y no se salta nada: la siguiente frase
se prepara mientras suena la actual, y cuando se acumulan frases la voz habla un poco más rápido.

**Quién habla.** La voz de la app puede decir quién habló, por ejemplo las dos primeras letras del nombre, o el
nombre completo. Elígelo en la pestaña Salida, en La voz de la app. En las llamadas los nombres vienen de la propia
app de Discord: en la pestaña Salida, en Quién habla, añade una vez tu propia aplicación de Discord. Los mensajes
del chat siempre llevan el nombre del autor.

En la pestaña **En directo** defines los idiomas de las dos direcciones, ves los medidores de nivel y lees la
transcripción. Puedes usar un botón de pulsar para hablar, y el cuadro Escribe para hablar, donde escribes una
frase, se traduce y se dice en Discord. La opción Responder en el idioma que hablan hace que tu idioma de salida
siga el último idioma detectado de la otra persona.

En la pestaña **Entrada** eliges qué escuchar y cómo empieza tu micrófono: actividad de voz, pulsar para hablar o
alternar. También hay un control de sensibilidad. La app reconoce su propia voz cuando tu micrófono la oye, y la
ignora.

En la pestaña **Salida** eliges dónde suenan las traducciones, el cable virtual para tu voz, la voz de la app y
quién habla.

Todos los dispositivos de sonido están también juntos en un solo sitio, en la pestaña Ajustes, en Dispositivos de
sonido.

=== 6. Motores: voz a texto, traducción, IA y voz
# Motores

Cada paso de la traducción funciona en tu PC, y puedes cambiar los ajustes cuando quieras. Se guardan en tu perfil.

- **Pestaña Voz a texto.** Convierte la voz en texto con Whisper. El tamaño de modelo auto se elige para tu PC: un
  modelo pequeño en el procesador, uno grande y preciso en una tarjeta gráfica NVIDIA. Un modelo más grande es más
  preciso pero más lento. En esta pestaña hay una prueba de micrófono.
- **Pestaña Traducción.** El motor OPUS-MT, de la Universidad de Helsinki, traduce en una décima de segundo por
  frase. Cada par de idiomas se descarga una vez; los idiomas sin modelo directo pasan por el inglés. El botón
  Descargar ahora los modelos de mis idiomas los trae antes de tu llamada. Puedes elegir el tono, y un glosario
  fija cómo se traducen los nombres y los términos de juego.
- **Pestaña Modelo de IA.** Opcional. Si instalas Ollama o LM Studio y un modelo en tu PC, el motor Modelo de IA en
  este PC traduce con él. Entiende mejor la jerga y el contexto, pero necesita un PC rápido o una tarjeta gráfica.
  La app solo habla con servidores de IA de tu propio ordenador o de tu red local.
- **Pestaña Voz.** Las voces de este PC: voces naturales Piper y Kokoro, y las voces incluidas en Windows. Auto elige
  una voz para cada idioma. Una voz se descarga una vez, la primera vez que se usa. Las voces Kokoro suenan muy
  naturales pero necesitan un PC rápido. Para tener más voces de Windows, abre Configuración de Windows, Hora e
  idioma, Voz, Agregar voces. Para cada dirección puedes ajustar la velocidad, el tono y el volumen.

Cada pestaña tiene un botón de Prueba para comprobar un motor antes de usarlo.

=== 7. Privacidad y tus datos
# Privacidad y tus datos

EloGlobal funciona solo en tu PC. Lo que dice la gente en la llamada, tu micrófono, los mensajes del chat y el texto
que traduces nunca salen de tu ordenador. La app no tiene cuenta, ni estadísticas de uso, ni publicidad.

**Las voces de los demás.** Mientras el traductor funciona, la app oye lo que dicen las personas de tu llamada, para
traducírtelo. Diles que usas un traductor. En algunos países necesitas su consentimiento.

**Qué se guarda.** Tus ajustes y perfiles, y archivos de registro con mensajes técnicos, no con lo que dice la gente.
Las transcripciones de las llamadas solo se guardan si lo activas, en la pestaña Ajustes, en Privacidad e
información.

**Dónde.** Todo lo que guarda la app está en tu carpeta de usuario, en App Data, Local, EloGlobal: perfiles,
registros, transcripciones y los modelos descargados. La pestaña Ajustes tiene botones para abrir la carpeta de
datos y la de modelos.

**Internet.** La app solo descarga archivos de modelos, una vez. La función opcional Quién habla inicia sesión en
Discord con tu propia aplicación de Discord. Las actualizaciones llegan desde la tienda.

La pestaña Ajustes también vuelve a mostrar el aviso de privacidad, y la ventana Información y licencias enumera
todo el software y los modelos en los que se basa EloGlobal.

=== 8. Traducir texto de Discord
# Traducir texto de Discord

Pulsa el botón **Chat**, o usa la tarjeta del chat en el Panel. La app lee entonces los mensajes que ves en la app
de Discord, usando las funciones de accesibilidad de Windows, como un lector de pantalla. No necesita token ni bot,
y no envía nada a Discord.

Los mensajes nuevos se traducen y se dibujan sobre el texto original, dentro del propio Discord, o en una ventana
pequeña a su lado. Lo eliges en la pestaña Texto, en Mostrar traducciones. Funciona en servidores, mensajes
directos, grupos, hilos y publicaciones de foro, incluso con Discord en segundo plano. Los mensajes que ya están en
tu idioma, y tus propios mensajes, se omiten. Las traducciones solo se ven mientras Discord es la ventana activa,
así que nunca tapan tu juego.

**Lectura en voz alta.** Solo se leen en voz alta los mensajes nuevos. Los mensajes a los que vuelves
desplazándote, los editados y los antiguos se traducen en pantalla, pero nunca se leen. Los mensajes del chat
comparten la voz de la app con las traducciones de la llamada, así que nunca hablan a la vez.

La pestaña Texto tiene más herramientas:

- **Seleccionar para traducir.** Selecciona texto, o haz doble clic en una palabra, y aparece una ventanita con la
  traducción junto al ratón.
- **Ctrl+Alt+T** traduce la selección actual en cualquier app.
- **Ctrl+Alt+Y** sustituye lo que escribiste en el cuadro de mensajes de Discord por su traducción al idioma usado
  en ese chat.
- **Escribir en su idioma.** Escribe en la pestaña Texto y luego copia, pega en Discord o envía.
- **Ctrl+Alt+O** te deja arrastrar un recuadro sobre cualquier parte de la pantalla. La app lee el texto con OCR y
  muestra la traducción encima. Puede repetirse cada pocos segundos.
- **Texto copiado.** Opcionalmente, traduce todo lo que copias.

Puedes cambiar todos los atajos en la pestaña Texto. Para el OCR de otros alfabetos, como el ruso o el japonés,
añade ese idioma en la Configuración de Windows.

=== 9. Subtítulos y transcripciones
# Subtítulos y transcripciones

La **ventana de subtítulos** flota sobre tu juego o Discord. Arrástrala para moverla. Usa la rueda del ratón para
cambiar su tamaño. Haz clic derecho para ver opciones, como cuántas líneas mostrar, si se ve el texto original y el
fondo. En Ajustes puedes cambiar el tamaño y la fuente del texto.

Una conversación se puede guardar como **transcripción**. Viene desactivado, porque las transcripciones contienen
las palabras de otras personas. Actívalo en la pestaña Salida o en Ajustes. Las transcripciones se guardan en la
carpeta de datos, en transcripts.

La pestaña Registro muestra lo que hace la app en tiempo real. También tiene botones para abrir los registros, las
transcripciones y la carpeta de datos. Si algo falla, el registro es lo primero que hay que mirar.

La barra de estado de abajo muestra el retraso de cada etapa: reconocimiento de voz, traducción y voz, para que veas
qué paso va lento.

=== 10. Ajustes e información
# Ajustes e información

La pestaña **Ajustes** define el idioma de la app. Cuando lo cambias, la app se reinicia en el nuevo idioma. También
reúne todos los dispositivos de sonido en un solo lugar: lo que escucha la app, tu micrófono, dónde suenan las
traducciones y adónde va tu voz traducida.

Controla el aspecto de la app: el tema, oscuro o claro, la fuente y el tamaño del texto de la app y de las
traducciones que se muestran dentro de Discord, en la ventanita del chat y en las ventanas emergentes. También
tiene todos los atajos en un solo lugar, una opción para mantener la ventana encima de las demás y botones para
recolocar las ventanas y abrir las carpetas de datos, modelos y registros.

La opción Guardar cambios automáticamente guarda tu perfil un segundo después de cada cambio. Viene activada.

**Privacidad e información.** La opción de las transcripciones, el aviso de privacidad y la ventana Información y
licencias, con la licencia de EloGlobal y la lista de todos los componentes que usa.

**Las actualizaciones** llegan desde la tienda donde instalaste EloGlobal, Microsoft Store o Steam. Se conservan tus
ajustes, perfiles y modelos descargados.

=== 11. Solución de problemas
# Solución de problemas

**Nadie oye mi traducción.** En Discord, el dispositivo de entrada debe ser CABLE Output. En la app, la pestaña
Salida debe enviar a CABLE Input. Comprueba que la Supresión de ruido esté desactivada en Discord.

**La app no oye nada.** En la pestaña Entrada, revisa el método. Con Solo la app de Discord, Discord debe estar
abierto. Con loopback, el dispositivo debe ser el que usa Discord para sonar. Mira los medidores de nivel en la
pestaña En directo. Si no se mueven, el ajuste es incorrecto.

**Mi traducción se oye dos veces, o la app se traduce a sí misma.** Usa el método Solo la app de Discord en la
pestaña Entrada y usa auriculares.

**Discord está en silencio.** Es a propósito mientras el traductor funciona: pulsa F9 para oír también a la gente.
Si EloGlobal se cerró de golpe, ábrelo una vez y devolverá el volumen a Discord, o sube Discord en el mezclador de
volumen de Windows.

**La gente oye mi voz real.** En Discord, el dispositivo de entrada debe ser CABLE Output, no tu micrófono. La app
avisa cuando Discord usa tu micrófono real.

**Va lento.** En la pestaña En directo, elige el idioma que hablan en lugar de Detectar automáticamente. En la
pestaña Voz a texto, elige un modelo más pequeño o usa una tarjeta gráfica NVIDIA. Las voces Kokoro son lentas en
muchos procesadores: elige una voz Piper o de Windows en la pestaña Voz.

**No hay voz para mi idioma.** Añade una voz de Windows: Configuración de Windows, Hora e idioma, Voz, Agregar
voces. Después pulsa Recargar lista de voces en la pestaña Voz.

**Falla una descarga.** Comprueba tu conexión a internet y pulsa Iniciar otra vez; la descarga sigue donde se quedó.

**¿Sigues atascado?** Abre la pestaña Registro y la carpeta de registros. El registro ayuda cuando informas de un
problema desde la página de la tienda.

=== 12. Sobre este manual
# Sobre este manual

Estás leyendo el manual incluido en EloGlobal. El narrador es una voz que funciona en tu PC, en el idioma de la app.
Funciona sin conexión y no envía nada a ninguna parte.

- **Siguiente y Anterior** pasan de un capítulo a otro. El narrador deja de leer el capítulo anterior y empieza el
  nuevo, y el texto nuevo aparece a la vez.
- **Leer en voz alta** activa o desactiva el narrador. Cuando está desactivado, el manual es solo texto.
- **Leer otra vez** empieza el capítulo actual desde el principio.
- **Parar** silencia al narrador.
- **Voz** y **Velocidad** cambian cómo suena. Puedes elegir cualquier voz de tu idioma en este PC, o una para
  descargar.
- **Repetir la visita guiada** vuelve a mostrar los primeros pasos.

El narrador se calla cuando sales de esta pestaña y nunca empieza solo mientras usas el traductor.

Este es el final del manual. ¡Disfruta de EloGlobal!
