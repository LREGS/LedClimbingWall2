import home_page
import Pages

from nicegui import app, ui 

@ui.page("/")
def index_page() -> None:
    Pages.create()

()
ui.run(port=8080)