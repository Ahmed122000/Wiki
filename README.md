# Wiki Encyclopedia - CS50 Web Development Project 1 #

![Wiki Encyclopedia Screenshot](https://github.com/Ahmed122000/Wiki/blob/main/assets/wiki_index.png)

A Wikipedia-like online encyclopedia built with Django as **Project 1** for Harvard's [CS50 Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/) course. This project extends the provided starter code with enhanced functionality.

> **Note**: This project builds upon starter code provided by the CS50 Web course. The core functionality requirements were specified by the course, while specific implementation details and additional features were developed independently.

---

## Features

- 📝 **Markdown Support**: All entries support Markdown formatting
- 🔍 **Enhanced Search**: 
  - Exact matches redirect directly
  - Partial matches show intelligent suggestions
- 🛠️ **Full CRUD Operations**:
  - Create new encyclopedia entries
  - Read existing entries with clean rendering
  - Update any entry through edit interface
  - Implicit delete through edit overwrite
- 🎲 **Random Page**: Discover random articles

---

## Technology Stack

- **Backend**: Django 3.2
- **Frontend**: HTML5, CSS3
- **Markdown Processing**: markdown2
- **Storage**: File-based (Markdown files in `entries/` directory)

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ahmed122000/Wiki.git
   ```
2. **Set up virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate #Linux/Mac
   venv\Scripts\activate    #Windows
   ```
3. **Install dependencies**:
   ```bash
   pip3 install django markdwon2
   ```
5. **Run Server**:
   ```bash
   python manage.py runserver
   ```
6. **Access at `http://127.0.0.1:8000/`

---

## Project Structure

    Wiki/
    ├── encyclopedia/
    │   ├── templates/encyclopedia/
    │   │   ├── layout.html
    │   │   ├── index.html
    │   │   ├── entry_page.html
    │   │   ├── search_result.html
    │   │   ├── new_page.html
    │   │   └── edit_page.html
    │   ├── static/encyclopedia/
    │   │   └── styles.css
    │   ├── urls.py
    │   ├── views.py
    │   └── util.py
    ├── entries/
    └── manage.py

---

## Usage 

### View Entries ### 
  - The homepage(`/`) lists all available entries
  - Click any entry to view its rendered Markdwon content

### Creating New Entries ###
  1. Click "Create New Page" or navigate to `/wiki/new-page`
  2. Enter a title and Markdown content
  3. Click "Save Entry"

### Editing Entries ###
  1. Navigate to any entry page
  2. Click the "Edit" button
  3. Modify the Markdwon content
  4. Click "Save Edit"

### Search ### 
  1. Use the search bar in the sidebar
  2. for exact matches, you'll be redirected to the entry
  3. for partial matches, you'll see a list of similar entries

### Random Page ###  
  - Click "Random Page" in the sidebar to be taken to a random encyclopedia entry
    
---
## Acknowledgements
- Harvard's CS50 Web course for project specification and starter code
- Django documentation for implementation guidance
- markdown2 developers for the Markdown processing library

---

## License ##
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

