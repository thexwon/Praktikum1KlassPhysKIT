# Pendel 

In diesem Verzeichnis finden Sie die Anleitung des P1-Versuchs **"Pendel"**. Wir stellen Ihnen diese Anleitung in drei inhaltsgleichen Formaten zur Verfügung: 

- Markdown (*Pendel.md*);
- PDF (*Pendel.pdf*), dabei handelt es sich um einen *pdf*-Export der Markdown-Datei;
- Jupyter-notebook (*Pendel.ipynb*), dabei handelt es sich um eine Übersetzung der Markdown-Datei.

Sie können die *ipynb*-Version der Anleitung als Ausgangspunkt für Ihre Auswertung verwenden. Die einfachste Art dies zu tun ist die Bearbeitung auf dem [Jupyter-server](https://jupytermachine.etp.kit.edu/hub/spawn) des ETP, auf dem Sie alle notwendigen Software Pakete bereits vorinstallierten vorfinden. Zugang zum Jupyter-server können Sie über [diesen Link](https://comp.physik.kit.edu/Account/) erhalten. 

Beachten Sie, dass die Bilder in den Anleitungen im *md*- und *ipynb*-Format nicht in die Dokumente integriert sondern verlinkt sind. Sie finden die verlinkten Bilder im **Verzeichnis *figures***.   

# Die Verzeichnisstruktur

Dieses Verzeichnis besitzt vier Unterverzeichnisse: 

Im **Verzeichnis *figures*** finden Sie die Bilder, die wir für die Anleitung und für dieses Dokument verwendet haben. 

Im **Verzeichnis *params*** finden Sie einige Meta-Informationen, die Sie bei der Bearbeitung des Versuchs benötigen werden. Es handelt sich um die folgenden Dateien:  

- *parameters_Fadenpendel.py*: Parameter und Unsicherheiten, die Sie für die Messungen mit dem Fadenpendel benötigen;
- *parameters_Reversionspendel.py*: Parameter und Unsicherheiten, die Sie für die Messungen mit dem Reversionspendel benötigen; 
- *parameters_gekoppeltePendel.py*: Parameter und Unsicherheiten, die Sie für die Messungen mit den gekoppelten Pendeln benötigen. 

Im **Verzeichnis *tools*** finden Sie die [PhyPraKit/tools](https://git.scc.kit.edu/yh5078/PhyPraKit/-/tree/master/tools), die für diesen Vorversuch von  Relevanz sein können. Wir haben Ihnen diese tools aus dem [PhyPraKit](https://git.scc.kit.edu/yh5078/PhyPraKit) Repository direkt dorthin kopiert, damit Sie sie während des Versuchs leichter finden und ausführen können. Es handelt sich um die Skripte: 

- [*csv2yml.py*](https://git.scc.kit.edu/yh5078/PhyPraKit/-/blob/master/tools/csv2yml.py): Dieses Skript können Sie verwenden, um Daten vom *csv*- ins *yaml*-Format zu konvertieren. 
- [*plotCSV.py*](https://git.scc.kit.edu/yh5078/PhyPraKit/-/blob/master/tools/plotData.py): Dieses Skript können Sie verwenden, um sich die rohen Daten, wie sie im *csv*-Format vom Smartphone übertragen wurden direkt bildlich darzustellen. 
- [*plotData.py*](https://git.scc.kit.edu/yh5078/PhyPraKit/-/blob/master/tools/plotData.py): Dieses Skript können Sie verwenden, um sich die Daten nach der Konversion in *yaml*-Format anzuschauen. Beachten Sie, dass dieses Skript die Daten in einem speziellen *yaml*-Format erwartet. Eine Beispieldatei, mit der Sie das Skript ausführen können finden Sie im **Verzeichnis *yaml***. Dieses Skript werden Sie vermutlich nicht oft in Verwendung haben.
- [*run_phyFit.py*](https://git.scc.kit.edu/yh5078/PhyPraKit/-/blob/master/tools/run_phyFit.py): Hierbei handelt es sich um jenes Skript, welches Sie in erster Linie zur Anpassung physikalischer Modelle an die Daten verwenden können. Beachten Sie, dass dieses Skript die Daten in einem speziellen *yaml*-Format erwartet. Eine Beispieldatei, mit der Sie das Skript ausführen können finden Sie im **Verzeichnis *yaml***.

Im **Verzeichnis *yaml*** können Sie ihre selbst-erzeugten *yaml*-Dateien ablegen. Sie finden dort auch eine Beispieldatei für die Verwendung mit den Skripten *plotData.py* und *run_phyFit.py*. 

# Wichtige Hinweise zu Protokoll und Auswertung

Beachten Sie zudem die Hinweise zu den folgenden Themen in dieser [README.md](https://git.scc.kit.edu/etp-lehre/p1-for-students/-/blob/main/README.md) Datei: 

- Arbeiten mit dem Jupyter-server;
- Arbeiten mit dem Jupyter-notebook;
- Parameteranpassung mit dem PhyPraKit Skript *run_phyFit.py*;
- Durchführung und Auswertung.
