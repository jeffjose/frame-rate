import PIL
import contextlib
from PIL import Image, ImageDraw
import typer
from tailwind_colors import TAILWIND_COLORS_HEX

def create_image_with_ball(width, height, ball_x, ball_y, ball_size):
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.ellipse((ball_x, ball_y, ball_x + ball_size, ball_y + ball_size), fill=TAILWIND_COLORS_HEX.FUCHSIA_700)
    return img

app = typer.Typer()

@app.command()
def hello(name: str) -> int:
    print(f"Hello {name}")
    return 0


@app.command()
def create(input: str = typer.Option(), output:str = typer.Option(), fps: int = typer.Option(), duration: int = typer.Option()) -> int:

    num_frames = fps * duration 
    frame_time = round(1000 / fps, 2)

    print(f"             fps: {fps}")
    print(f"      frame time: {frame_time}ms")
    print(f"  total duration: {duration}s")
    print(f"total num_frames: {num_frames}")


    frames = []
    x, y = 0, 100
    for i in range(num_frames):
        new_frame = create_image_with_ball(800, 600, x, y, 40)
        frames.append(new_frame)
        x += 1
        #y += 40

        filename = f'ball/ball-{str(i).zfill(10)}.jpg'

        new_frame.save(filename)

    # Save into a GIF file that loops forever
    #frames[0].save('moving_ball.gif', format='GIF', optimize=False, append_images=frames[1:], save_all=True, duration=frame_time, loop=0)


    return 0

def main():
    return app()
