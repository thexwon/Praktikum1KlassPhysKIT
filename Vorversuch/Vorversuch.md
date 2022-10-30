<img src="/home/rwolf/Data/Vorlesungen/2022/2022-WS-P1/AnleitungPendel/Logo_KIT.svg" style="zoom:15%;float:right;" />

# Fakultät für Physik 

## Physikalisches Praktikum P1 für Studierende der Physik



Praktikumsvorversuch

Raum: zu Hause



# Datenverarbeitung am Beispiel des Pendels



## Motivation

Im Mittelpunkt jedes physikalischen Experiments steht die Messung als nachvollziehbare Erfassung und Weiterverarbeitung von Daten unter Laborbedingungen. In diesem Praktikumsvorversuch möchten wir Sie anhand eines einfachen physikalischen Vorgangs mit den wichtigsten Methoden der (meist computergestützten) Datenverarbeitung in der modernen Physik vertraut machen. Sie werden sehen, dass das Messen schnell zur Messkunst avancieren kann. 

Als Aufgabe wählen wir die Bestimmung der Erdbeschleunigung ($g$) mit Hilfe eines Pendels. Wir haben mit Hilfe der kostenfreien *app* [phyphox](https://phyphox.org/de/home-de/) der RWTH Aachen einen Datensatz für Sie vorbereitet den wir mit Ihnen gemeinsam weiterverarbeiten möchten. Sie können das hier vorgestellte Experiment bei sich zu Hause noch einmal von Grund auf neu durchführen. Beachten Sie dabei (hier wie im gesamten P1): "experimentieren" bedeutet "versuchen" – nicht jeder Versuch muss zu einem erfolgreichen Ausgang führen. Wie im gesamten P1, geht es uns mit diesem Vorversuch nicht darum, dass Sie uns die beste Messung von $g$ präsentieren. Uns ist wichtig, dass Sie sich mit den zur Verfügung stehenden Daten vertraut machen, sich mit den vorgestellten Möglichkeiten zur weiteren Datenverarbeitung ernsthaft auseinandersetzen und vielleicht auch neue, eigene Ideen entwickeln.  

## Anmerkungen zum Vorversuch

Wir listen im Folgenden die wichtigsten Lernziele auf, die wir Ihnen mit dem Vorversuch des P1 vermitteln möchten: 

- Sie erhalten einen ersten Einblick darin, welche Stärken und Schwächen eine Messung haben kann?
- Sie lernen, dass Sie mit Hilfe ausgedehnter Messreihen Messunsicherheiten deutlich verringern können?
- Sie gehen mit einem mächtigen Werkzeugkasten aus diesem Versuch hervor, mit dem Sie auch größere Datenmengen mit den Ansprüchen eines Physikers analysieren können. 
- Sie lernen, wie Sie mit Hilfe dieses Werkzeugkastens physikalisch bedeutungsvolle Parameter aus der Anpassung von Modellen an die Daten bestimmen können?
- Sie lernen was der Unterschied zwischen einer Messunsicherheit und einem Messfehler ist?

Machen Sie sich zur Vorbereitung auf das Praktikum den folgenden Umstand bewusst: jeder Messung der modernen Physik liegt ein Modell zugrunde. Die Messung hat i.a. die Bestimmung eines Parameters innerhalb eines solchen Modells zum Ziel.  

## Versuchsaufbau

Wir haben die *app* [phyphox](https://phyphox.org/de/home-de/) auf ein Smartphone geladen und das Smartphone mit Klebestreifen auf eines der [Reversionspendel](https://de.wikipedia.org/wiki/Reversionspendel) aus dem Versuch "P1-20, 21, 22 Pendel" montiert. Für die Messung haben wir die Anwendung "Beschleunigung ohne $g$" verwendet. Der Versuchsaufbau ist im folgenden Bild skizziert:

![Versuchsaufbau](/home/rwolf/Data/Vorlesungen/2022/2022-WS-P1/AnleitungVorversuch/PendelVorversuch.png)

Wir haben das Pendel in Schwingung versetzt, die resultierende Bewegung mit Hilfe der im Smartphone verbauten Beschleunigungssensoren ausgelesen und uns die resultierenden Datensätze im [csv-Format](https://de.wikipedia.org/wiki/CSV_(Dateiformat)) per Mail zugeschickt. Außerdem haben wir alle für unsere Messung relevanten äußeren Parameter festgehalten. Die Datensätze, die wir aufgenommen haben finden Sie in dieser [zip-Datei](http://www-ekp.physik.uni-karlsruhe.de/~simonis/praktikum/p1/p1-versuchsanleitungen/Datenverarbeitung.zip). 

## Anmerkungen zum Versuchsaufbau

- Beim csv-Format handelt es sich um ein einfaches sowohl von Menschen als auch Maschinen lesbares Format, um Daten in Spalten und Zeilen organisiert abzulegen.
- Alle wichtigen Informationen zu Pendel und Smartphone haben wir aus der Anleitung des Versuchs "P1-20, 21, 22 Pendel" und den im Internet verfügbaren Datenblättern des Smartphones bezogen. Zum Teil haben wir die Abmessungen des Smartphones noch einmal mit einfachen Mitteln nachvollzogen. 

## Aufgabe 1: Aufsetzen der Arbeitsumgebung

### Aufgabe 1.1: Wie sehen die Daten aus?

Entpacken Sie die oben verlinkte [zip-Datei](http://www-ekp.physik.uni-karlsruhe.de/~simonis/praktikum/p1/p1-versuchsanleitungen/Datenverarbeitung.zip) in ein Verzeichnis Ihrer Wahl. Untersuchen Sie die Größen der darin befindlichen Dateien mit den Endungen *.csv*. Schauen Sie sich dann die Dateien in einem Texteditor an, um ihre Struktur zu verstehen. Diese Dateien sind die Grundlage für jedes weitere Vorgehen im weiteren Verlauf dieses Vorversuchs.

### Aufgabe 1.2: Legen Sie sich Ihre Werkzeuge zurecht 

Bei so großen Datenmengen ist eine manuelle Weiterverarbeitung der Daten unmöglich. Wir werden dazu die Programmiersprache [python](https://www.python.org/) verwenden. Wir möchten Ihnen weiterhin die Modulsammlung [PhyPraKit](https://readthedocs.org/projects/phyprakit/) vorstellen. Installieren Sie sich beide Softwarepakete und dokumentieren Sie Ihre Installationswege. Beachten Sie hier zu auch Anmerkung 1.1. 

## Anmerkungen zu Aufgabe 1

### Anmerkung 1.1 

Lesen Sie sich zur Verwendung von python und PhyPraKit mit den Betriebssystemen Linux, OS oder Windows die Anleitung zur [Datenauswertung in den Grundpraktika zur Physik](https://etpwww.etp.kit.edu/~quast/Skripte/Datenauswertung.html)  durch, die wir für Sie zusammengestellt haben. Wir unterstützen Sie gerne bei der Einrichtung der für das P1 nützlichen Werkzeuge auf Ihrem bevorzugten Betriebssystem. Falls Sie mit python nicht sehr vertraut sind können Sie sich auf die Verwendung von zwei einfachen Skripten zur weiteren Verarbeitung der Daten beschränken.

Ein Werkzeug soll ein Hilfsmittel sein. Während wir Ihnen bestimmte Hilfsmittel vorstellen können Sie den Versuch auch mit jedem weiteren Ihnen bekannten Hilfsmittel durchführen, dessen Verwendung Ihnen vertrauter ist.  Für uns ist wichtig, dass Sie sich in der Anfangsphase des P1 so einrichten, dass Sie –egal mit welchen Hilfsmitteln– zukünftig in der Lage sein werden Daten wie diese, den Ansprüchen des Studiums gemäß weiter zu verarbeiten.  

### Anmerkung 1.2

Inklusive aller Werkzeuge, die wir Ihnen zur Verwendung vorschlagen, sollten Sie mit $50\,\mathrm{MB}$ Speicher auskommen.

### Anmerkung 1.3

Die *app* phyphox hat die Beschleunigungssensoren des Smartphones mit einer festen [Abtastrate](https://de.wikipedia.org/wiki/Abtastung_(Signalverarbeitung)) (engl. *sampling rate*) von $100\,\mathrm{Hz}$ ausgelesen. Um die Eigenschaften der Schwingung für uns ausreichend gut erfassen zu können haben wir $5\,\mathrm{min}$ lang gemessen. Sie können sich schnell klar machen mit welcher Datenmenge Sie zunächst zu tun haben werden. Die Periode der Schwingung haben wir während des Versuchs zu $\text{1–2}\,\mathrm{s}$ abgeschätzt. Wir haben daher als ersten Schritt der Weiterverarbeitung die Signalrate um den Faktor 10 reduziert, indem wir nur jede 10. Zeile der csv-Datei ausgelesen haben. Man bezeichnet diese Vorgehensweise als *down sampling*.  Diesen nachprozessierten Datensatz finden Sie in der Datei

```shell
RawData_down_sampled_500_2200_10.csv
```

die wir für alle weiteren Versuchsteile nutzen werden.

## Lösung:

*Sie können Ihre Lösung/Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 

## Aufgabe 2: Erste Schritte

### Aufgabe 2.1  Visualisierung der Daten 

Der erste Schritt, um sich mit großen Datensätzen zurechtzufinden ist sie besser sichtbar zu machen. Wählen Sie ein für Sie gut geeignetes Werkzeug aus, um die aufgezeichneten Daten graphisch darzustellen. Wir schlagen das Skript *plotData.py* aus dem tools-Verzeichnis der Modulsammlung PhyPraKit vor. Dieses Skript erlaubt es Ihnen Daten auf der $x$-Achse gegen Daten auf der $y$-Achse graphisch darzustellen. Ein Beispiel für eine mögliche Eingabe für das Skript *plotData.py* finden Sie mit der Datei *data.yaml* aus dem tools-Verzeichnis der Modulsammlung PhyPraKit. Die Verwendung des Skripts mit Ihrer eigenen Eingabedatei könnte z.B. so aussehen: 

```shell
python3 /PhyPraKit/tools/plotData.py my_data.yaml
```

Beachten Sie zur Eingabedatei Anmerkung 1.2.  

### Aufgabe 2.2: Anpassung eines Modells an die Daten 

Der nächste Schritt ist die Anpassung eines einfachen Modells an die beobachteten Daten. Dies können Sie erreichen, indem Sie Ihre Eingabedatei um die Definition einer python-Funktion erweitern, die der mathematischen Abbildung des Modells entspricht. Ein solcher "Funktionsblock" in Ihrer *yaml*-Datei könnte z.B. so aussehen:

```yaml
model_label: "Hamonic oscillation"
model_function: |
  def my_model(x, phi0=0.8, omega=4., delta=0.):
      return A*np.cos(omega*x+phi)
```

Der Funktionsname *my_model* ist frei gewählt. Beachten Sie, dass dieses Modell beim Aufruf des Skripts *plotData.py* mit den Daten zusammen dargestellt wird. Die hierzu verwendeten Funktionsparameter entsprechen den Defaultwerten der Funktionsargumente. 

Wenn Sie das Modell nicht nur mit fest vorgegebenen Parametern, zusammen mit den Daten darstellen, sondern an die Daten anpassen möchten führen Sie das Skript *run_phyFit.py* aus dem tools-Verzeichnis der Modulsammlung PhyPraKit mit der gleichen Eingabedatei aus. Dies könnte für Sie z.B. so aussehen:

```shell
python3 PhyPraKit/tools/run_phyFit.py my_data.yaml 
```

Stellen Sie die Daten geeignet dar und fügen Sie Ihrer Auswertung eine graphische Darstellung zu. Verwenden Sie für diese Aufgabe den Datensatz 

```shell
RawData_down_sampled_500_2200_10.csv
```

## Anmerkungen zu Aufgabe 2

### Anmerkung 2.1

Beachten Sie, dass die Skripte *plotData.py* und *run_phyFit.py* ihre Eingangs- und Konfigurationsdaten nicht im csv-Format sondern in der Struktursprache [yaml](https://de.wikipedia.org/wiki/YAML)  erwarten. Die Notwendigkeit Daten um zu formatieren ist ein häufiges Problem in der Datenverarbeitung. Sie können zur Umformatierung das Skript *cvs2yaml.py* im tools-Verzeichnis der Modulsammlung PhyPraKit verwenden.

### Anmerkung 2.2

Beachten Sie, dass Sie für eine Anpassung mit Hilfe der Funktion *xyFit* des Skripts *run_phyFit.py* Unsicherheiten für die Daten in $x$- und $y$-Richtung angeben müssen. Wir haben Abschätzungen für diese Unsicherheiten für Sie in der Datei

```shell
uncertainties_data.py
```

in der [zip-Datei](http://www-ekp.physik.uni-karlsruhe.de/~simonis/praktikum/p1/p1-versuchsanleitungen/Datenverarbeitung.zip) hinterlegt. 

### Anmerkung 2.3

Wenn Sie Aufgabe 2 zu Ihrer Zufriedenheit abgeschlossen haben sind Sie mit allen Werkzeugen ausgestattet, die Sie benötigen, um die weitere Analyse der Daten fortsetzen zu können. Mehr als die Skripte *plotData.py* und *run_phyFit.py* und ein Grundverständnis, wie man die beiden Skripte mit Hilfe der Struktursprache yaml ansteuert werden Sie für diesen Vorversuch nicht benötigen.  

## Lösung:

*Sie können Ihre Lösung/Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 

## Aufgabe 3: Ein einfaches Modell zur Bestimmung von $g$

Wir legen unserer ersten Messung das einfache Modell eines [mathematischen Pendels](https://de.wikipedia.org/wiki/Mathematisches_Pendel) zugrunde. 
$$
\begin{split}
& m\,l^{2}\,\,\ddot{\phi} + m\,g\,l\,\phi = 0, \\
\end{split}
$$
wobei $m$ einer Punktmasse und $l$ dem Abstand der Punktmasse vom Angelpunkt des Pendels entsprechen. Diese Differentialgleichung wird von harmonischen Schwingungen der Form 
$$
\begin{split}
& \phi(t) = \phi_{0}\cos\left(\omega\,t + \delta\right) \\
\end{split}
$$
gelöst, wobei $\phi_{0}$ die Amplitude, $\omega$ die Kreisfrequenz und $\delta$ eine freie Phase der Schwingung sind. Mit Hilfe dieses Modells können Sie bei gegebenem $l$ die Größe von $g$ mit Hilfe der Gleichung
$$
\begin{equation}
g = \frac{4\,\pi^{2}}{T^{2}}l
\end{equation}
$$
aus der Periode $T$ der Schwingung bestimmen. Zusätzliche Information, die Sie zur Lösung dieser Aufgabe benötigen, finden Sie in der Datei 

```shell
parameters_task_3.py 
```

### Aufgabe 3.1: Die Referenzmessung 

Bestimmen Sie einen einzelnen Wert für $T$ aus der angegebenen *csv*-Datei. Überlegen Sie sich eine sinnvolle Unsicherheit $\Delta T$ und ermitteln Sie einen ersten Wert für $g$ mit entsprechender Unsicherheit $\Delta g$ mit Hilfe linearer Fehlerfortpflanzung. Vergleichen Sie das Ergebnis mit Ihrer Erwartung  und setzen Sie es in Bezug zu $\Delta g$. Beachten Sie hierzu Anmerkung 3.1 

### Aufgabe 3.2: Eine erste Verbesserung 

Erstellen Sie eine *yaml*-Datei für die Anpassung einer harmonischen Schwingung, wie in Gl. (2) angegeben, an die Daten aus der angegebenen *csv*-Datei, so dass Sie $T$ aus einer Anpassung an die Daten bestimmen können. Notieren Sie sich die Qualität dieser Anpassung (quantifiziert durch die Größe $\chi^{2}/n_{\mathrm{dof}}$) und die ermittelten Werte mit entsprechenden Unsicherheiten für alle Parameter. Fügen Sie Ihrer Auswertung eine graphische Darstellung zu. Berechnen Sie aus den bestimmten Werten für $T$ und $\Delta T$ verbesserte Abschätzungen für $g$ und $\Delta g$. Vergleichen Sie das Ergebnis mit Ihrer Erwartung und setzen Sie es in Bezug zu $\Delta g$.    

## Anmerkungen zu Aufgabe 3

### Anmerkung 3.1

Als Referenzwert für Ihre Messungen können Sie den Wert 
$$
\begin{equation*}
g_{\mathrm{exp}} = (9.809599\pm0.000034)\,\mathrm{m/s^{2}}
\end{equation*}
$$
verwenden. Dieser Wert wurde aus der Global Gravtiy Database des Bureau Gravimetrique International (BGI) für die Stadt Mannheim (bei $49,49^{\circ}$ nördlicher Breite und $8,53^{\circ}$ westlicher Länge auf einer Referenzhöhe von $101\,\mathrm{m}$) ausgelesen. 

## Lösung

*Sie können Ihre Lösung/Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 

## Aufgabe 4: Erweiterung des ursprünglichen Modells

Eine offensichtliche Unzulänglichkeit des vorherigen Modells besteht in der Vernachlässigung der physikalischen Ausdehnungen des Pendels. Wir werden unser Modell entsprechend erweitern. Die Formel zur Bestimmung von $g$ nimmt dadurch die folgende Form an: 

$$
g = \frac{4\,\pi^{2}}{T^{2}}\frac{I}{m\,g\,\ell},
$$
wobei $I$ und $m$ dem Trägheitsmoment und der Masse der gesamten Pendelkonstruktion (inklusive aller Montageteile und Smartphone!) und $\ell$ dem Abstand des Schwerpunkts dieser Konstruktion vom Angelpunkt des Pendels entsprechen.  Zusätzliche Information zu den im Folgenden diskutierten Modellen finden Sie in der Datei 

```shell
parameters_task_4.py 
```

### Aufgabe 4.1: Erweiterung des Modells 

Modifizieren Sie Ihr Modell, so dass es dem Modell eines [physikalischen Pendels](https://de.wikipedia.org/wiki/Physikalisches_Pendel) entspricht und berechnen Sie aus den in Aufgabe 3.2 bestimmten Werten für $T$ und $\Delta T$ eine neue Abschätzung von $g$ und $\Delta g$ und diskutieren Sie das Ergebnis. 

### Aufgabe 4.2: Direkte Bestimmung von $g$ 

Sie können $g$ und $\Delta g$ auch direkt aus der Anpassung bestimmen. Formulieren Sie ihre Modellfunktion entsprechend um, führen Sie die Anpassung erneut durch und vergleichen Sie die Ergebnisse mit den Ergebnissen aus Aufgabe 4.1. Beachten Sie zur Bestimmung von $\Delta g$ die Anmerkung 4.1.

### Aufgabe 4.3: Übergang zu einer [gedämpften Schwingung](https://de.wikipedia.org/wiki/Schwingung#Linear_ged%C3%A4mpfte_Schwingung) 

Das Pendel erfährt in seiner Bewegung zusätzlich eine Dämpfung. Legen wir ein Modell linearer Dämpfung zugrunde verändert sich die Formel zur Bestimmung von $g$ wie folgt: 
$$
g = \left(\frac{4\,\pi^{2}}{T^{2}}+\frac{1}{\tau}\right)\frac{I}{m\,g\,\ell},
$$
wobei $1/\tau$ einer Abklingzeit in Sekunden entspricht. Wie Sie sehen handelt es sich um eine Korrektur, die die Abschätzung von $g$ zu größeren Werten hin beeinflusst. Verändern Sie ihr Modell entsprechend und beantworten Sie die folgenden Fragen: ist das zugrundeliegende Modell mit den Daten kompatibel? Wie könnten Sie die Hypothese, dass das zugrundeliegende Modell die Daten beschreiben kann, besser testen? Wie groß ist der Einfluss, den dieser Effekt ggf. auf die Messung von $g$ hat? 

## Anmerkungen zu Aufgabe 4

### Anmerkung 4.1

Beachten Sie, dass das der Wert von $\Delta g$ aus der Anpassung aus Aufgabe 4.2 nur die Unsicherheiten der Datenpunkte widerspiegelt. Wie würden Sie den Einfluss der Variationen in $I$, $m$, und $\ell$ auf $\Delta g$ abschätzen?

## Lösung:

*Sie können Ihre Lösung/Ihr Protokoll direkt in dieses Dokument einfügen. Wenn Sie dieses Dokument als Grundlage für ein [Jupyter notebook](https://jupyter.org/) verwenden wollen können Sie die Auswertung, Skripte und ggf. bildliche Darstellungen mit Hilfe von [python](https://www.python.org/) ebenfalls hier einfügen. Löschen Sie hierzu diesen kursiv gestellten Text aus dem Dokument.* 

## Bonusaufgabe: Vom bloßen Messen zu Kunst

Die Anmerkung zu Aufgabe 4.2 wirft eine Frage auf, die wir im Rahmen dieses Vorversuchs bisher offen gelassen haben: wie sind die Unsicherheiten auf die zusätzlichen Parameter der Messung korreliert? Wenn Sie möchten können Sie dieser Frage mit den folgenden Bonusaufgaben nachgehen. Die Bearbeitung dieser Fragen ist jedoch nicht verpflichtend.

### Bonusaufgabe 1: Korrelierte Unsicherheiten:

Jede Variation eines der drei Parameter $m$, $I$ oder $\ell$ in Aufgabe 4.2 hat einen nicht-trivialen Einfluss auf die jeweils anderen Parameter. Durch quadratische Addition von $\Delta I$, $\Delta m$, und $\Delta \ell$ unterlegen Sie die Annahme, das alle drei Variationen unabhängig sind. Diese Annahme ist auf jeden Fall falsch. Machen Sie einen Vorschlag zur Lösung dieses Problems. 

### Bonusaufgabe 2: Die Kunst des Experimentierens 

Diskutieren Sie, wie dieser Versuch konzeptionell verbessert werden könnte, um die in Bonusaufgabe 1 diskutierten Probleme von vornherein zu vermeiden.  
