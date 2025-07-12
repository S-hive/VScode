package Lec05;
import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;

public class BouncingBox {
    int x;
    int y;
    Color color;
    int xDirection = 0;
    int yDirection = 0;
    
    final int SIZE = 20;

    /**
     * Initialize a new box with its center located at (startX, startY), filled 初始化一个新的盒子，其中心位于 (startX, startY) ，且已填充颜色为 startColor。
     * with startColor.
     */
    public BouncingBox(int startX, int startY, Color startColor) { //200,50
        x = startX;
        y = startY;
        color = startColor;
    }

    /** Draws the box at its current position on to surface.  将盒子在其当前位置绘制到表面上。*/
    public void draw(Graphics surface) {
        // Draw the object 绘制该物体
        surface.setColor(color);
        surface.fillRect(x - SIZE/2, y - SIZE/2, SIZE, SIZE);// 190,40,20,20
        surface.setColor(Color.BLACK);
        ((Graphics2D) surface).setStroke(new BasicStroke(3.0f));
        surface.drawRect(x - SIZE/2, y - SIZE/2, SIZE, SIZE);
        
        // Move the center of the object each time we draw it 每次绘制对象时，移动对象的中心位置。
        x += xDirection;
        y += yDirection;

        // If we have hit the edge and are moving in the wrong direction, reverse direction
        // We check the direction because if a box is placed near the wall, we would get "stuck"
        // rather than moving in the right direction
        // 如果我们撞到了边缘并且正朝着错误的方向移动，就反转方向。
        // 我们检查方向是因为如果一个盒子放置在墙边，不检查方向的话，它会 “卡住”，
        // 而不是朝着正确的方向移动。
        if ((x - SIZE/2 <= 0 && xDirection < 0) ||
                (x + SIZE/2 >= SimpleDraw.WIDTH && xDirection > 0)) {
            xDirection = -xDirection;
        }
        if ((y - SIZE/2 <= 0 && yDirection < 0) ||
                (y + SIZE/2 >= SimpleDraw.HEIGHT && yDirection > 0)) {
            yDirection = -yDirection;
        }
    }

    public void setMovementVector(int xIncrement, int yIncrement) {
        xDirection = xIncrement;
        yDirection = yIncrement;
    }
} 