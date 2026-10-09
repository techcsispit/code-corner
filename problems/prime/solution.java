import java.util.Scanner;

public class PrimeCheck {

    public boolean isPrime(long n) {

        // 0 and 1 are not prime 
        if (n <= 1) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        if (n % 2 == 0) {
            return false;
        }
        //checking all odd nos from 3 to square root of n
        for (long i = 3; i <= Math.sqrt(n); i += 2) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;

    }

     public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        if (isPrime(n)) {
            System.out.println("prime");
        } else {
            System.out.println("not prime");
        }
    }
}