#Follow The Master
------------------------------------------

##But de l’application

Le but de l’application est de gérer le déplacement d’un drône dit “suiveur”. Ce drône doit “suivre” un drône dit “Maître” piloté manuellement. C’est-à-dire que le drône suiveur devra rester à distance fixe (Cette distance sera paramétrable), à même altitude (Cette altitude sera paramétrable) et se mettre dans le même axe que le drône “Maître”.

##Scénario

Il était une fois deux drônes au sol. 

Les deux drônes sont au sol. Le premier drône “Maître”, piloté manuellement, décolle à une certaine altitude décidée par le pilote. Une fois l’altitude choisie, le mode “AltHold” est activé sur le drône “Maître” afin qu’il reste en vol statique suivant celle-ci.

Une fois le drône “Maître” prêt, notre application est mise en route, ce qui induira les actions suivantes, dans l’ordre correspondant :
- le décollage du drône “Suiveur”
- Ajustement de son altitude avec celle du drône “Maître”
- De même avec la distance
- De même avec l’orientation

A partir de ce moment, tout mouvement du drône “Maître” sera reproduit par le drône “Suiveur” suivant les trois variables suivantes. (Altitude, Distance, Orientation).

Lors de l’arrêt de notre application, le drône “Suiveur” atterrira.

##Composantes techniques
###Logiciel
- Un réseau ROS configuré et dont l’architecture est défini ici : (archi_ros)
		Les commandes de décollage, de contrôle en position et d’atterrissage pour chaque drône pourront être directement publiées sur le réseau ROS.
- Les informations de position des drônes et de leurs différents capteurs pourront être récupérés depuis le réseau ROS.
Python 2.7

###Matériel
- Deux drônes ErleCopter avec GPS
- Une télécommande 
- Un PC superviseur

##Généralités sur le programme

Les consignes en position du drône suiveur (correspondant aux coordonnées actuelles du drône maître seront envoyées sur le réseau ROS toutes les 100ms (10Hz).
Un arrêt du programme (Ctrl+C, appui sur espace) provoquera un atterrissage du drône suiveur


##Liste des fonctions vitales du système

take_off - Décoller 
land - Atterrir
set_position - Donner une consigne de position à un drône
stop_program - arrêt du programme
fix_altitude - corriger l’altitude du drône suiveur
fix_distance - corriger la distance entre les deux drônes
fix_orientation - corriger l‘orientation du drône suiveur
get_ros_flightinfo - Récupérer les données de vol sur le réseau ROS
publish_ros_cmd - Publier les commandes sur le réseau ROS

##Architecture
à venir ...




