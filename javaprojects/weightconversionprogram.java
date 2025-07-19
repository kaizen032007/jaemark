import java.util.Scanner;

public class weightconversionprogram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        double weight;
        double newweight;
        int choice;

        System.out.println("Weight Conversion Program");
        System.out.println("1: Convert lbs to kgs");
        System.out.println("2: Convert kgs to lbs");
        
        System.out.print("CHOOSE AN OPTION: ");
        choice = scanner.nextInt();

        if (choice == 1) {
            System.out.println("Enter your weight in Lbs");
            weight = scanner.nextDouble();
            newweight = weight * 0.45392;
            System.out.printf("Your new weight in kgs is: %.2f", newweight);
        }

        else if(choice == 2) {
            System.out.println("Enter your weight in kgs: ");
            weight = scanner.nextDouble();
            newweight = weight * 2.20462;
            System.out.printf("Your new weight in lbs is: %.2f", newweight);
        }
        else {
            System.out.print("ERROR");
        }

        scanner.close();
    }
}