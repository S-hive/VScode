import java.awt.Graphics;

public interface Sprite {
    /**
     * Draws this sprite on surface, with the coordinate (leftX, topY) as the
     * top left corner.* 将此精灵绘制在表面上,以坐标(leftX, topY)作为左上角。
     */
    void draw(Graphics surface, int leftX, int topY);

    /** Returns the width of the sprite.返回精灵的宽度 */
    int getWidth();

    /** Returns the height of the sprite. */
    int getHeight();
}
