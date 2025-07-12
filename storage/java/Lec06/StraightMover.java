import java.awt.Graphics;


public class StraightMover {
    private int x;
    private int y;
    private int xDirection;
    private int yDirection;
    private Sprite sprite;

    /** Create a Bouncer that positions sprite at (startX, startY).创建一个弹跳器,将精灵定位在(startX,startY)位置。 */
    public StraightMover(int startX, int startY, Sprite sprite) {
        x = startX;
        y = startY;
        this.sprite = sprite;
    }

    /** Starts moving the object in the direction (xIncrement, yIncrement).开始沿 (xIncrement, yIncrement) 方向移动对象。 */
    public void setMovementVector(int xIncrement, int yIncrement) {
        xDirection = xIncrement;
        yDirection = yIncrement;
    }

    public void draw(Graphics graphics) {
        sprite.draw(graphics, x, y);

        // Move the center of the object each time we draw it每次绘制对象时，移动对象的中心位置
        x += xDirection;
        y += yDirection;
    }
}
