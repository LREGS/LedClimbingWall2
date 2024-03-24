from nicegui import events, ui





@ui.page("/")
async def index():
    btn = ui.button("Create Climb")
    await btn.clicked()
    ui.navigate.to("/newClimb")


@ui.page("/newClimb")
async def climbPage():
    src = '/home/william/personal/board.jpg'
    ui.interactive_image(src, on_mouse=mouse_handler, events=['mousedown', 'mouseup'], cross=True)

    btn = ui.button("Save Climb")
 

    await btn.clicked()
    ui.navigate.to("/")

def mouse_handler():
    ui.notify("clicked")

    

ui.run()