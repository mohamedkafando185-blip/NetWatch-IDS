# 🛡️ Mini Système de Détection d’Intrusion Réseau (IDS)
## Observer, comprendre et détecter les comportements suspects sur un réseau

> 🎓 Projet académique en **Cybersécurité**  
> 🧑‍💻 Réalisé avec **Python**  
> 🖥️ Environnement : Kali Linux  
> ⏱️ Durée : 1 semaine  
> 🎯 Projet pédagogique à forte valeur pratique

---

## 🌍 Contexte et vision du projet

Aujourd’hui, les réseaux informatiques sont exposés en permanence à des tentatives d’intrusion, de reconnaissance ou de perturbation.  
Avant même de bloquer une attaque, **la première étape essentielle est de savoir la détecter**.

Ce projet consiste à concevoir un **mini Système de Détection d’Intrusion Réseau (IDS)** capable de surveiller le trafic réseau d’une machine et d’identifier automatiquement certains comportements anormaux.

👉 L’objectif n’est pas de construire un outil industriel complexe, mais de **comprendre concrètement comment fonctionne un IDS**, depuis l’observation du trafic jusqu’à l’analyse des incidents détectés.

---

## 🧠 Problématique abordée

Ce projet répond à des questions fondamentales en cybersécurité :

- Comment surveiller un réseau en temps réel ?
- Comment reconnaître une activité suspecte sans connaître l’attaque à l’avance ?
- Comment transformer des données réseau brutes en informations exploitables ?
- Comment conserver une trace claire et utile des incidents ?

La réponse apportée repose sur une **approche simple, comportementale et progressive**, accessible même à un non-spécialiste.

---

## 🎯 Objectifs du projet

### Objectifs principaux
- Comprendre les bases de la surveillance réseau  
- Mettre en place une logique de détection simple et efficace  
- Apprendre à structurer un système d’alerte et de journalisation  

### Objectifs atteints
| Objectif | Statut |
|--------|--------|
| Surveillance du trafic réseau | ✅ Réalisé |
| Détection de comportements suspects | ✅ Réalisé |
| Journalisation automatique | ✅ Réalisé |
| Génération de rapport | ✅ Réalisé |
| Documentation claire | ✅ Réalisé |

---

## 🧩 Principe de fonctionnement (explication simple)

Le système fonctionne selon une logique très intuitive :

1. 📡 Il **observe** le trafic réseau
2. 🔍 Il **analyse** le comportement des machines
3. 📊 Il **repère les excès ou répétitions anormales**
4. 🚨 Il **déclenche une alerte**
5. 📝 Il **enregistre l’incident**
6. 📄 Il **génère un rapport clair**

👉 Le système ne bloque rien automatiquement.  
Il se concentre sur **l’observation, la compréhension et la traçabilité**.

---

## 🚨 Types de comportements détectés

### 🟡 Ping Flood (ICMP)
Un ping flood correspond à l’envoi massif de requêtes réseau dans un court laps de temps.

🔎 **Principe** :  
Trop de requêtes provenant d’une même source → comportement suspect.

---

### 🔵 Scan de ports (TCP)
Avant une attaque, un attaquant cherche souvent à identifier les ports ouverts d’une machine.

🔎 **Principe** :  
Multiples tentatives de connexion répétées → tentative de reconnaissance réseau.

---

## 🏗️ Architecture globale du projet
Trafic réseau
↓
Observation des paquets
↓
Analyse du comportement
↓
Détection d’anomalies
↓
Journalisation
↓
Rapport final

Cette architecture volontairement simple permet :
- une compréhension rapide,
- une maintenance facile,
- une évolution future du projet.

---

## 📁 Organisation du projet
Le projet est structuré de manière modulaire pour séparer la logique de détection de la génération de rapports :

```text
Projet_IDS/
├── mini_ids.py         # Programme principal de surveillance (Moteur Scapy)
├── generate_report.py   # Script de parsing et génération du rapport final
├── logs/
│   └── ids.log         # Journal brut des incidents détectés
├── rapport_ids.txt     # Rapport de synthèse généré pour l'utilisateur
└── README.md           # Documentation technique du projet
```

## 📝 Journalisation et rapport

Chaque incident détecté est enregistré avec :
- la date et l’heure,
- le type de comportement suspect,
- la source et la cible,
- des informations complémentaires.

Un script dédié permet ensuite de **transformer ces données en un rapport lisible**, facilitant :
- l’analyse post-incident,
- la compréhension globale des événements,
- la traçabilité.

---

## ✅ Résultats obtenus

| Critère | Résultat |
|------|------|
| Surveillance réseau | ✅ Fonctionnelle |
| Détection ping flood | ✅ Validée |
| Détection scan de ports | ✅ Validée |
| Création des logs | ✅ Fiable |
| Rapport automatique | ✅ Généré |

📈 Le système s’est montré stable, réactif et suffisamment léger pour fonctionner en continu.

---

## 🧠 Ce que ce projet m’a appris

Ce projet a été **très formateur**, bien au-delà de l’aspect purement technique.

### Sur le plan technique
- Comprendre le fonctionnement réel du trafic réseau  
- Mieux appréhender les protocoles IP, ICMP et TCP  
- Découvrir la logique interne d’un IDS  
- Structurer un programme orienté sécurité  

### Sur le plan méthodologique
- Penser en termes de **comportement**, pas seulement de règles fixes  
- Découper un problème complexe en étapes simples  
- Tester, observer, ajuster et valider  

### Sur le plan personnel
- Développer une vraie **rigueur** dans l’analyse  
- Apprendre à documenter clairement un projet technique  
- Gagner en confiance sur des sujets concrets de cybersécurité  

👉 Ce projet m’a permis de passer d’une vision théorique de la sécurité réseau à une **compréhension pratique et opérationnelle**.

---

## ⚠️ Limites actuelles

| Limite | Impact |
|------|--------|
| Détection limitée | Peu de types d’attaques |
| Seuils fixes | Faux positifs possibles |
| Mode passif | Pas de blocage automatique |
| Scope local | Pas de vision réseau globale |

Ces limites sont assumées et font partie de la démarche pédagogique.

---

## 🔮 Perspectives d’amélioration

- Ajout de nouveaux types de détection  
- Adaptation automatique des seuils  
- Blocage automatique des sources suspectes  
- Interface de visualisation des incidents  
- Stockage des données sur le long terme  

---

## 🏁 Conclusion

Ce mini IDS constitue une **excellente introduction pratique à la cybersécurité défensive**.  
Il démontre qu’avec une approche claire et structurée, il est possible de concevoir un système complet de détection, depuis l’observation réseau jusqu’à l’exploitation des incidents.

🎓 Ce projet reflète :
- une forte implication personnelle,
- une volonté de comprendre en profondeur,
- et une base solide pour évoluer vers des projets plus avancés en **Blue Team, SOC ou cybersécurité réseau**.

---

### 🔖 Mots-clés
`Cybersecurity` · `IDS` · `Network Monitoring` · `Python` · `Security Fundamentals`
