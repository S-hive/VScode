
abstract class Pet {
    abstract void eat();
}
class Dog extends Pet{
    void eat(){
        System.out.println("小狗吃骨头");
    }
    void guard(){
        System.out.println("小狗会看家护院");
    }
}
class Cat extends Pet{
    void eat(){
        System.out.println("小猫吃罐头");
    }
    void catchMouse(){
        System.out.println("小猫会抓老鼠");
    }
}
class Person{
    void feed(){
        System.out.println("主人喂食");
    }
    void use(Pet pet){
        if(pet instanceof Cat){
            Cat cat = (Cat)pet;
            cat.catchMouse();
        }
        else if(pet instanceof Dog){
            Dog dog = (Dog)pet;
            dog.guard();
        }
    }
}