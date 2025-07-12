import java.util.Scanner;
class  FooCorporation {
    public static void get(){
        Scanner scanner=new Scanner(System.in);
        System.out.println("工作时长是");
        int workTime=scanner.nextInt();
        System.out.println("工作时薪是");
        double price=scanner.nextDouble();
        if (price < 8){
            System.out.println("工资低于8元,无法计算");
            return;
        }else{
        getmoney(workTime,price);
        }
    }
    public static void getmoney(int workTime, double price){
        double allmoney = 0;
        if (workTime<=40){
            allmoney = workTime*price;
        }
        else{
            allmoney = 40*price + (workTime-40)*price*1.5;
        }
        System.out.println("总收入是"+allmoney);
    }
    public static void main(String[] arge){
        FooCorporation worker1 = new FooCorporation();
        worker1.get();
        FooCorporation worker2= new FooCorporation();
        worker1.get();
        FooCorporation worker3= new FooCorporation();
        worker1.get();
    }
}