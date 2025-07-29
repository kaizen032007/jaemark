import java.util.Scanner;
import java.util.Random;

public class BankSystem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        StringBuilder errors = new StringBuilder();

        int year = 2025;

        System.out.print("ENTER YOUR USERNAME: ");
        String name = scanner.nextLine();

        System.out.print("ENTER YOUR AGE: ");
        int age = 0;
        try {
            age = Integer.parseInt(scanner.nextLine());
        } catch (NumberFormatException e) {
            errors.append("Age must be a number.\n");
        }

        System.out.print("ENTER YOUR EMAIL: ");
        String email = scanner.nextLine();

        // Username checks
        if (name.length() < 5) {
            errors.append("You must have more than 5 characters in your username.\n");
        }
        if (name.matches(".*\\d.*")) {
            errors.append("Username must not contain numbers.\n"); 
        }

        // Age checks
        if (age < 18) {
            errors.append("You are not eligible to have a bank account. Must be 18 above.\n");
        }

        // Email checks
        if (!email.contains("@") || !email.contains(".")) {
            errors.append("Invalid email. Email must contain '@' and '.'\n");
        }

        if (errors.length() > 0) {
            System.out.println("REGISTRATION UNSUCCESSFUL. PLEASE FIX THE FOLLOWING:");
            System.out.println(errors.toString());
        } else {
            System.out.println("SUCCESSFUL!");
            System.out.println("WELCOME! " + name);
            System.out.println("You are qualified to have a bank account! You are " + age + " years old.");

            // Generate card number in 9000-XXXX-XXXX-XXXX format
            String firstBlock = "9000";
            String secondBlock = String.format("%04d", random.nextInt(10000));
            String thirdBlock  = String.format("%04d", random.nextInt(10000));
            String fourthBlock = String.format("%04d", random.nextInt(10000));
            String cardNumber = firstBlock + "-" + secondBlock + "-" + thirdBlock + "-" + fourthBlock;

            System.out.println("Here is your card number: " + year + "-" + cardNumber);
        }

        scanner.close();
    }
}