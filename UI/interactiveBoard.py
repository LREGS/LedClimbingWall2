from nicegui import events, ui
from shapely.geometry import Point, Polygon


class iBoard():
    def __init__(self):
        self.src = 'board.jpg'
        self.holdCoords = [[(660,1305),(811,1311), (811,1346), (660,1344)], [(100, 200), (200, 100), (300, 100), (100,300)]]


    def ReturnCreateClimbBoard(self):
        image = ui.interactive_image(self.src, on_mouse=self.createClimbHandler, events=['mouseup'])
        image = self.drawHolds(image)
        return image

    def createClimbHandler(self, e: events.MouseEventArguments):
        return 
    
    def drawHolds(self, image):
        polygons_svg = ""
        for hold in self.holdCoordst:
            points = ",".join([f"{p[0]},{p[1]}" for p in hold])
            polygons_svg += f'<polygon points="{points}" fill="none" stroke="red" stroke-width="2" />'

        image.content = polygons_svg
        return image

