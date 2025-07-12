package Lec05;
import java.awt.Color;
import java.awt.Graphics;
import java.util.ArrayList;
public class DrawGraphics {
    ArrayList<BouncingBox>arr = new ArrayList<>();
    public DrawGraphics() {
        arr.add(new BouncingBox(100,42,Color.BLUE));
        arr.add(new BouncingBox(90,56,Color.green));
        arr.add(new BouncingBox(77,81,Color.red));
        arr.get(0).setMovementVector(5, -2);
        arr.get(1).setMovementVector(3, 4);
        arr.get(2).setMovementVector(3, 6);
    }
    /** Draw the contents of the window on surface. Called 20 times per second. 在表面上绘制窗口内容。每秒调用20次。*/
    /**
    public void draw(Graphics surface) {
        surface.drawArc(50, 100, 90, 70,-30 , 360);
        surface.fillArc(70, 120, 5, 5,0 , 360);
        surface.fillArc(115, 120, 5, 5,0 , 360);
        surface.drawLine(91, 140, 97, 140);
        surface.drawLine(91, 140, 94, 145);
        surface.drawLine(94, 145, 97, 140);
        surface.drawArc(24, 125, 70, 35, -5, -45);
        surface.drawArc(95, 125, 70, 35, 180, 50);
        surface.drawLine(60, 90, 55, 115);
        surface.drawLine(60, 90, 75, 103);
        surface.drawLine(132, 90, 112, 103);
        surface.drawLine(132, 90, 132, 115);
        surface.drawArc(24, 125, 70, 35, -5, -45);
        box.draw(surface);
    }**/
    public void draw(Graphics surface){
        for(BouncingBox box:arr){
            box.draw(surface);
        }
    }
    }

