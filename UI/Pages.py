import requests
from nicegui import events, ui


route = []
#
@ui.page("/")
async def index():
    btn = ui.button("Create Climb")
    await btn.clicked()
    ui.navigate.to("/newClimb")


@ui.page("/newClimb")
async def climbPage():

    src = '/home/william/personal/board.jpg'
    ui.interactive_image(src, on_mouse=mouse_handler, events=['mouseup'])

    btn = ui.button("Save Climb")
 

    await btn.clicked()
    storeRoute()

def mouse_handler(e: events.MouseEventArguments):
    coords = [e.image_x, e.image_y]

    route.append(coords)


def storeRoute():
    stringData = str(route)
    url = 'http://localhost:6969/addClimb'
    print(stringData)
    response = requests.post(f'{url}/{stringData}')

    if response.status_code == 200:
        print("post was a success")


ui.run(port=6868)