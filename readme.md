# Workshop Duckdb :

1 - Création d'une table : 
**Note : les lignes ui sont précédées par -- sont des commentaires à ne pas exécuter**

``````
duckdb #lancer le moteur duckdb
--création d'une table
CREATE TABLE TEST (id INTEGER, nom VARCHAR)
-- Insertion des valeurs dans la table
INSERT INTO TEST VALUES (1, 'AXEL') ; 
-- Lecture des données depuis la table
SELECT * FROM TEST
-- Fermer duckdb cli
.quit
``````

2. Création d'une base de données persisté (les données sont sauvegardées) :
```````
--lancer le moteur duckdb
duckdb data/myduckdb.db

--création d'une table
CREATE TABLE TEST (id INTEGER, nom VARCHAR)
-- Insertion des valeurs dans la table
INSERT INTO TEST VALUES (1, 'AXEL') ; 
-- Lecture des données depuis la table
SELECT * FROM TEST
-- Fermer duckdb cli
.quit
``````

3. Chargement d'un fichier csv local :
``````
--lancer le moteur duckdb
duckdb data/myduckdb.db

--création d'une table qui chargera le fichier csv
CREATE TABLE titanic AS SELECT * FROM read_csv_auto('data/titanic.csv');

-- Lecture des données depuis la table titanic
SELECT * FROM titanic limit 10;

-- Nombre de passagers
SELECT COUNT (*) as nb_passengers from titanic;

--Nombre de survivants
select sum(Survived) as nb_survivants from titanic;

-- Nombre de survivants groupés par age
select sum(Survived) as nb_survivants, Age from titanic group by Age order by nb_survivants desc limit 10;
``````

4.Chargement d'un fichier csv local :
``````
--lancer le moteur duckdb
duckdb data/myduckdb.db

--création d'une table qui chargera le fichier csv
CREATE TABLE food_allergen AS SELECT * FROM read_csv_auto('data/Allergen_Status_of_Food_Products.csv');

-- Lecture des données depuis la table food_allergen
SELECT * FROM food_allergen limit 10;

-- Nombre de plats
SELECT COUNT (*) as nb_food_products from food_allergen;

--Nombre de produits allergenes
SELECT COUNT (*) as nb_food_allergen from food_allergen where Prediction = 'Contains';

``````

# installation de la librairie python duckdb

``````
pip install duckdb
``````

# installation de streamlit
``````
pip install streamlit
``````
-- tester streamlit
```````
streamlit hello
``````

# ENREGISTREMENT DANS GIT
``````
git clone https://github.com/LindaBDIA/duckdb-streamlit-training.git
cd .\duckdb-streamlit-training\
git status
git add .
git commit -m 'ajout journée du 22mars'
git push