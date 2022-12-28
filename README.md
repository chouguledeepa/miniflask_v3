NOTES


## developer notes

### How to setup this project on your machine?

```shell
# INSTALL required libraries

pip install flask
```

### How to run this project?
```shell
# RUN IN DEBUG MODE
flask --app main --debug run

# RUN WITHOUT DEBUG MODE
flask --app main run

# RUN ON NON_DEFAULT PORT
flask --app main --port <port-number> run 
```

## project structure

```
miniflask_v3 (project root)

    - main_v1.py
    - main_v2.py
    - starwars_tasks (sub-application)
        -- __init__.py
        -- tasks.py
    - crud_ops  (sub-application)
        -- __init__.py
        -- starwars.py
    
    - static (directory)
        - flasklogo.png
    - templates (package)
        -- __init__.py
        -- welcome_with_index.html
        -- card.html
    - models (package)
        - __init__.py
        - basemodel.py
        - datamodels 
            - __init__.py
            - films.py
            - planets.py
            - species.py
            - starships.py
            - vehicles.py
        - dal
            - __init__.py
            - db_conn_helper.py
            - dml.py
            - settings (package)
                - __init__.py
                - secrets.yaml
                - secrets.toml
                
        - flashcard_db.json
        - json_db.py
    - requirements.txt
    - utils
        - __init__.py
        - randgen.py
        
    - .gitignore
    
```

## URLS used in project `main_v1`
- http://127.0.0.1:5000/
- http://127.0.0.1:5000/card/0
- http://127.0.0.1:5000/card/1
- http://127.0.0.1:5000/card/2
- http://127.0.0.1:5000/card/3
- http://127.0.0.1:5000/card/4
- http://127.0.0.1:5000/card/5 (NOT FOUND)
- http://127.0.0.1:5000/api/cards
    
    
## Reference material for this project

JINJA templates and it's syntax

```markdown
- JINJA is a package used by flask (as dependency). 
- When we use `render_template()` function from flask, we basically have to
  use JINJA template syntax.
- JINJA syntax can be referred from following link.
```
JINJA template syntax
https://jinja.palletsprojects.com/en/2.11.x/templates/