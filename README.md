# Proyecto3Graficas
Movimiendo con WASD y mouse
Disparo con click izquierdo.
FPS en el borde superior de la pantalla porque 
```
fps = str(int(timer.get_fps()))
    font = pygame.font.SysFont('lucidaconsole', 20)
    fpsScreen = font.render(fps, False, (255, 255, 255))
    fpsText = font.render("FPS: ", False, (255, 255, 255))
    SCREEN.blit(fpsText, (HEIGHT, 0))
    SCREEN.blit(fpsScreen, (HEIGHT, 20))
 ```
no lo presentaba en pantalla a menos que tuviera "fill(0,0,0)".
# REFERENCIAS:
Basado en lo escrito por Coder Space:
https://youtu.be/ECqUrT7IdqQ
Basado en lo escrito por Code Monkey King tambien:
https://youtu.be/Rt5rEW0jQjw
E Ing. Dennis Aldana / Ing. Carlos Alonso
