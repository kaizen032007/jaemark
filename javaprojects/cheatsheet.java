import java.util.Random;
import java.util.Scanner;

public class cheatsheet {
    public static void main(String[] args) {

        // ===== STUDENT REGISTRATION EXAMPLE =====

        import java.util.Scanner;
        import java.util.Random;

        public class workspace {
            public static void main(String[] args) {
                Scanner scanner = new Scanner(System.in);
                Random random = new Random();

                int year = 2025;

                System.out.print("ENTER YOUR NAME: ");
                String name = scanner.nextLine();

                System.out.print("ENTER YOUR AGE: ");
                int age = scanner.nextInt();

                int studentnumber = random.nextInt(10000);

                System.out.println("HELLO AND WELCOME! " + name);
                System.out.print("THIS IS YOUR STUDENT NUMBER: " + year + -studentnumber);
            }
        }

        // ===== DATA TYPES & STRING FORMATTING EXAMPLE =====

        String name = "Mark";
        int age = 25;
        char user = 'm';
        double GPA = 25.6;
        boolean isStudent = true;

        System.out.printf("Hello %s\n", name);
        System.out.printf("Your age is %d\n", age);
        System.out.printf("Your first letter name is %c\n", user);
        System.out.printf("Your GPA is %f\n", GPA);
        System.out.printf("You are a student: %b\n", isStudent);


        // ========COMPOUND INTEREST RATE======== //

        import java.util.Scanner;
        public class  workspace {
            public static void main(String[] args) {
                Scanner scanner = new Scanner(System.in);
            // compount interest calculator
            double principle;
            double rate;
            int timecompounded;
            int years;
            double amount;

        System.out.print("ENTER THE PRINCIPLE AMOUNT: ");
        principle = scanner.nextDouble();

        System.out.print("ENTER THE INTEREST RATE: ");
        rate = scanner.nextDouble() / 100;

        System.out.print("ENTER THE NUMBER OF TIMES COMPOUNDED PER YEAR: ");
        timecompounded = scanner.nextInt();

        System.out.print("ENTER THE NUMBER OF YEARS: ");
        years = scanner.nextInt(); 

        amount = principle * Math.pow(1 + rate / timecompounded, timecompounded * years);

        System.out.printf("The amount after %d years is %.2f", years, amount);
        scanner.close();

    }
}

        // ========== nested if and else statements ============== //
        public class workspace {
            public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.print("ENTER YOUR NAME: ");
        String name = scanner.nextLine();

        System.out.print("Do you have your PSA? ");
        boolean hasPSA = scanner.nextBoolean();

        System.out.print("ENTER YOUR AGE: ");
        int age = scanner.nextInt();

        System.out.print("DO YOU HAVE 2 GOVERNMENT ISSUED ID?: ");
        boolean hasID = scanner.nextBoolean();        

        if (age >=18) {
            if (hasPSA) {
                if (hasID) {
                    System.out.print("Welcome "  + name + " You are eligible for voters ID");
                } else {
                    System.out.print("You are missing document which is PSA");
                }
            } else {
            System.out.print("You have PSA and old enough to register. But do not have any 2 or missing government issued ID");
            }
        } else {
            System.out.print("Pls try again next year and bring 2 valid ID");
        }
        scanner.close();
    }
}

        // 






        */
        // ===== END OF CHEATSHEET =====
    }
}
