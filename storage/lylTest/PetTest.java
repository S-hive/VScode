

public class PetTest {
	public static void main(String[] args) {
    Person person = new Person();
    person.feed();
    Cat cat = new Cat();
    Dog dog = new Dog();
    person.use(cat);
    person.use(dog);
    }
}
