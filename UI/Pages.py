import requests
from nicegui import events, ui


route = []
def create():
    @ui.page("/")
    async def index():
        btn = ui.button("Create Climb")
        await btn.clicked()
        ui.navigate.to("/addClimb")


    @ui.page("/addClimb")
    async def climbPage():

        
        img = image() 

        btn = ui.button("Save Climb")
    

        await btn.clicked()
        storeRoute()

    def mouse_handler(e: events.MouseEventArguments):
        coords = [e.image_x, e.image_y]

        route.append(coords)

    def image():
        src = 'board.jpg'
        return ui.interactive_image(src, on_mouse=mouse_handler, events=['mouseup'])



    def storeRoute():
        stringData = str(route)
        url = 'http://localhost:8080/addClimb'
        print(stringData)
        response = requests.post(f'{url}/{stringData}')

        if response.status_code == 200:
            print("post was a success")


