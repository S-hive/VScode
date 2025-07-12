package Lec01.com;

class GravityCalculator {
    public static void main(String[] arguments) {
        double gravity = -9.81;  // Earth's gravity in m/s^2
        double initialVelocity = 0.0;//初始速度
        double fallingTime = 10.0;//下落时间
        double initialPosition = 0.0;//初始位置
        double finalPosition =initialPosition+initialVelocity*fallingTime+0.5*gravity*fallingTime*fallingTime; ;//最终位置
        System.out.println("The object's position after " + fallingTime +
                " seconds is " + finalPosition + " m.");// fallingTime秒之后该物体的位置在finalPosition米     
    }
} 

