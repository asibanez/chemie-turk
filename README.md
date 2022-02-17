![tagging](https://user-images.githubusercontent.com/13397560/118203495-33771380-b42a-11eb-8742-edc601a78cd7.gif)


chemie-turk
=========

Chemie-turk builds on top of [localturk](https://github.com/danvk/localturk) including chemistry-specific annotation schemas and functionalities

   1. Annotation review and fine-tuning options
   2. Improved interface with expanded functionalities (e.g. multi-step reaction annotation, paper access, etc.)
   3. Chemistry-specific annotation schemas

It's handy if you want to:

   1. Annotate chemical literature
   2. Review and fine-tune existing annotations from chemical literature

Comprehensive annotation and validations manuals as well as short videos showing the process are available in the annotation and validation tools

Quick Start
-----------

### 1. JavaScript executer
You have to had [node.js](https://nodejs.org/es/download/) installed (or a similar JavaScript executer).


### 2. Clone repository and enter folder:

    git clone https://github.com/asibanez/chemie-turk.git
    cd chemie-turk

### 3. Install required node packages:

    npm install -g localturk

### 4. Run annotation:

    localturk [annotation_template.html] [input.csv] [output.csv]
    
This will open a localhost (e.g., `http://localhost:4321/`) where you can start annotating.
    
    Example:
    localturk forms/annotation.html test_data/annotate.csv test_data/output.csv

### 5. Run review / validation:

    Preprocess annotated dataset:
        python prefill.py [origin_path]
    
    Review / validate annotations
        localturk [validation_template.html] [input.csv] [output.csv]
    Then visit the localhost to start review / validation
        
    Example:
    localturk forms/validation.html test_data/validate_prefilled.csv test_data/output.csv
    
