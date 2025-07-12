import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class MagicSquares {
    public static boolean testMagic(String pathName) throws IOException {
        // Open the file 打开文件
        BufferedReader reader = new BufferedReader(new FileReader(pathName));

        boolean isMagic = true;
        int lastSum = -1;
        
        // For each line in the file ... 对于文件中的每一行 ...
        String line;
        while ((line = reader.readLine()) != null) {
            // ... sum each row of numbers 计算每行数字的总和
            String[] parts = line.split("\t");
            int sum = 0;
            for (String part : parts) {
                sum += Integer.parseInt(part);
            }

            if (lastSum == -1) {
                // If this is the first row, remember the sum 如果这是第一行，记住总和
                lastSum = sum;
            } else if (lastSum != sum) {
                // if the sums don't match, it isn't magic, so stop reading 如果总数不匹配，那就不是魔法，所以别再读下去了
                isMagic = false;
                break;
            }
        }
        
        reader.close();
        return isMagic;
    }

    public static void main(String[] args) throws IOException {
        String[] fileNames = { "Mercury.txt", "Luna.txt" };
        for (String fileName : fileNames) {
            System.out.println(fileName + " is magic? " + testMagic("d:\\programming\\MITtxt\\Luna.txt"));
        }
    }
}
