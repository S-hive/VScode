

public class test {
    static int a;
    public test(int a){
        this.a = a;
    }
    public static void main(String[] args) {
        System.out.println(a);
        test test1 = new test(3);
        System.out.println(a);
    }
}