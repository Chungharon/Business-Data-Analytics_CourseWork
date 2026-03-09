// // See https://aka.ms/new-console-template for more information
// public class ExceptionTest
// {
//     static double SafeDivision(double x, double y)
//     {
//         if (y == 0)
//             throw new DivideByZeroException();
//         return x / y;
//     }

//     public static void Main()
//     {
//         // Input for test purposes. Change the values to see
//         // exception handling behavior.
//         double a = 98, b = 0;
//         double result;

//         try
//         {
//             result = SafeDivision(a, b);
//             Console.WriteLine($"{a} divided by {b} = {result}");
//         }
//         catch (DivideByZeroException)
//         {
//             Console.WriteLine("Attempted divide by zero.");
//         }
//     }
// }

// Async Main()

// class Program

// {
//     static async Task<int> Main(string[] args)
//     {
//         return await AsyncConsoleWork();
//     }

//     private static async Task<int> AsyncConsoleWork()
//     {
//         return 0;
//     }
// }

public class Functions
{
    public static long Factorial(int n)
    {
        // Test for invalid input.
        if ((n < 0) || (n > 20))
        {
            return -1;
        }

        // Calculate the factorial iteratively rather than recursively.
        long tempResult = 1;
        for (int i = 1; i <= n; i++)
        {
            tempResult *= i;
        }
        return tempResult;
    }
}

class MainClass
{
    static int Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("Please enter a numeric argument.");
            Console.WriteLine("Usage: Factorial <num>");
            return 1;
        }

        int num;
        bool test = int.TryParse(args[0], out num);
        if (!test)
        {
            Console.WriteLine("Please enter a numeric argument.");
            Console.WriteLine("Usage: Factorial <num>");
            return 1;
        }

        long result = Functions.Factorial(num);

        if (result == -1)
            Console.WriteLine("Input must be >= 0 and <= 20.");
        else
            Console.WriteLine($"The Factorial of {num} is {result}.");

        return 0;
    }
}