public class Lec03 {
    class Marathon {
    public static void main (String[] arguments) {
        String[] names = {
            "Elena", "Thomas", "Hamilton", "Suzie", "Phil", "Matt", "Alex",
            "Emma", "John", "James", "Jane", "Emily", "Daniel", "Neda",
            "Aaron", "Kate"
        };

        int[] times = {
            341, 273, 278, 329, 445, 402, 388, 275, 243, 334, 412, 393, 299,
            343, 317, 265
        };
        String first;
        String second;
        int firstTime=0;
        int secondTime=0;
        for (int i = 0; i < names.length; i++) {
            System.out.println(names[i] + ": " + times[i]);
            if (times[i]>times[firstTime] || firstTime==0){
                firstTime = i;
            }
            if (secondTime==0 || (times[i]<times[firstTime] && times[i]>times[secondTime] && firstTime!=0)){
                secondTime = i;
            }
        }
        first = names[firstTime];
        second = names[secondTime];
        System.out.println("The first place is " + first);
        System.out.println("The second place is " + second);
    }

    }
} 

