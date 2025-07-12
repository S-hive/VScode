
public class Book {

    String title;
    boolean borrowed;

    // Creates a new Book创建一本新书
    public Book(String bookTitle) {
        this.borrowed = false;
        this.title = bookTitle;
        // Implement this method实现这个方法
    }
   
    // Marks the book as rented将这本书标记为已出租
    public void borrowed() {
        // Implement this method实现这个方法
        if (this.borrowed == true){
            System.out.println("该书已被借出");
        }else{
            this.borrowed = true;
        }
    }
   
    // Marks the book as not rented将这本书标记为未借出
    public void returned() {
    }
    public void rented() { //还书
        this.borrowed = true;
    }
    // Returns true if the book is rented, false otherwise如果图书已出租则返回true，否则返回false
    public boolean isBorrowed() {
        // Implement this method
        return this.borrowed;
    }
    
    // Returns the title of the book返回书籍的标题
    public String getTitle() {
        // Implement this method
        return this.title;
    }

    public static void main(String[] arguments) {
        // Small test of the Book class对Book类的小测试
        Book example = new Book("The Da Vinci Code");
        System.out.println("Title (should be The Da Vinci Code): " + example.getTitle());
        System.out.println("Borrowed? (should be false): " + example.isBorrowed());
        example.rented();
        System.out.println("Borrowed? (should be true): " + example.isBorrowed());
        example.returned();
        System.out.println("Borrowed? (should be false): " + example.isBorrowed());
    }
} 