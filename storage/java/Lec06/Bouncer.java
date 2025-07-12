import java.awt.Graphics;

public class Bouncer {
    private int x;
    private int y;
    private int xDirection;
    private int yDirection;
    private Sprite sprite;

    /** Create a Bouncer that positions sprite at (startX, startY). 创建一个将精灵定位在(startX,startY)位置的弹跳器*/
    public Bouncer(int startX, int startY, Rectangle box) {
        x = startX;
        y = startY;
        this.sprite = box;
    }
    public Bouncer(int startX, int startY, MadeCat box) {
        x = startX;
        y = startY;
        this.sprite = box;
    }
    /** Starts moving the object in the direction (xIncrement, yIncrement).开始沿 (xIncrement, yIncrement) 方向移动该对象 */
    public void setMovementVector(int xIncrement, int yIncrement) {
        xDirection = xIncrement;
        yDirection = yIncrement;
    }

    /** Draws the sprite at its current position on to surface. 将精灵按其当前位置绘制到表面上*/
    public void draw(Graphics surface) {
        // Draw the sprite绘制精灵
        sprite.draw(surface, x, y);

        // Move the object each time we draw it
        x += xDirection;
        y += yDirection;

        // If we have hit the edge and are moving in the wrong direction, reverse direction
        // We check the direction because if a box is placed near the wall, we would get "stuck"
        // rather than moving in the right direction
        // 若碰到边界且移动方向错误，就反转方向
        // 我们检查方向是因为若一个物体放在墙边，它会“卡住”，而不是朝正确方向移动 
        if ((x <= 0 && xDirection < 0) ||
                (x + sprite.getWidth() >= SimpleDraw.WIDTH && xDirection > 0)) {
            xDirection = -xDirection;
        }
        if ((y <= 0 && yDirection < 0) ||
                (y + sprite.getHeight() >= SimpleDraw.HEIGHT && yDirection > 0)) {
            yDirection = -yDirection;
        }
    }
}
