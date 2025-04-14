# 📦 Projet Logistique – Suivi & Prédiction en Temps Réel

## 🔍 Objectif

Ce projet vise à surveiller les livraisons et les stocks en quasi temps réel, et à anticiper les retards ou ruptures grâce à des modèles de machine learning.

---

## 🌐 APIs

Les données sont accessibles via des APIs créées avec **Cube.js** :

- **Livraisons et Stocks**  
  Données sur les commandes, dates, quantités, entrepôts et lieux de livraison.

- **Prédictions de Retard**  
  Score de risque, délai estimé et facteurs de risque pour chaque livraison.

- **Indicateurs Clés (KPI)**  
  Taux de retard, niveaux de stock, performances logistiques.

---

## 🔄 Pipeline de Données

1. **Airflow** collecte les données toutes les heures.
2. Les données sont envoyées dans **Kafka** pour traitement en temps réel.
3. Elles sont stockées dans **Snowflake**.
4. **dbt** transforme et nettoie les données.
5. Les résultats sont disponibles via les APIs et visualisés dans **Streamlit** ou **Grafana**.

---

## 🤖 Modèle Prédictif

- Un modèle ML prédit le risque de retard.
- Entraînement et suivi via **MLflow**.
- Les résultats sont stockés dans Snowflake et intégrés aux APIs.

---

## 📊 Visualisation

- **Cube.js** expose les données sous forme d’API.
- **Streamlit** et **Grafana** permettent de créer des tableaux de bord interactifs.

---

## 🧰 Outils

- Airflow  
- Kafka  
- Snowflake  
- dbt  
- MLflow  
- Cube.js  
- Streamlit / Grafana

---

## 👨‍💻 Auteur

**Ali Rahiqi** 
