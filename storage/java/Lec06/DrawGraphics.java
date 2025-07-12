import java.awt.Color;
import java.awt.Graphics;
import java.util.ArrayList;

public class DrawGraphics {
    ArrayList<Bouncer>arr = new ArrayList<>();
    
    public Graphics madeCat(Graphics sur) {

        return sur;
    }
    
    /** Initializes this class for drawing. */
    public DrawGraphics() {
        Rectangle box = new Rectangle(15, 20, Color.RED);
        MadeCat secbox = new MadeCat(50, 50);//必须大于45

        arr.add(new Bouncer(100, 170, box));
        arr.add(new Bouncer(50, 10, secbox));
        arr.add(new Bouncer(50, 10, secbox));

        arr.get(0).setMovementVector(3, 1);
        arr.get(1).setMovementVector(2, -6);
    }

    /** Draw the contents of the window on surface. */
    public void draw(Graphics surface) {
        for(Bouncer box:arr){
            box.draw(surface);
        }
    }
}
