
import java.awt.Graphics;

public class MadeCat implements Sprite{
    private int width;
    private int height;

    public MadeCat(int width,int height){
        this.width = width;//基准50
        this.height = height;
    }

    public void draw(Graphics surface,int x, int y){
            
        surface.drawArc(x + 0, y + 0, this.width + 40, this.height + 20, -30, 360);
        surface.fillArc(x + 20, y + 20, this.width - 45, this.height - 45, 0, 360);
        surface.fillArc(x + 65, y + 20, this.width - 45, this.height - 45, 0, 360);
        surface.drawLine(x + 41, y + 40, x + 47, y + 40);
        surface.drawLine(x + 41, y + 40, x + 44, y + 45);
        surface.drawLine(x + 44, y + 45, x + 47, y + 40);
        surface.drawArc(x - 26, y + 25, this.width + 20, this.height - 15, -5, -45);
        surface.drawArc(x + 45, y + 25, this.width + 20, this.height - 15, 180, 50);
        surface.drawLine(x + 10, y - 10, x + 5, y + 15);
        surface.drawLine(x + 10, y - 10, x + 25, y + 3);
        surface.drawLine(x + 82, y - 10, x + 62, y + 3);
        surface.drawLine(x + 82, y - 10, x + 82, y + 15);
            }
        public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }


}
