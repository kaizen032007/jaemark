import java.util.Scanner;

public class grades {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("ENTER YOUR GRADES: ");
        int score = scanner.nextInt();

        String results = (score >= 60) ? "PASS" : "FAILED";

        String remark = (score >=90) ? "OUTSTANDING"    
                        : (score >=80) ? "EXCELLENT"
                        : (score >=70) ? "GOOD"
                        : (score >=60) ? "FAIR"
                        : (score >= 50) ? "FAILED"
                        : "RESTART AGAIN";
                        
        System.out.println("RESULTS ", results);
        System.out.println("REMARKS " + remark);
                    
        scanner.close();
    }
}