using System;

class Program
{
    double sayi1, sayi2, cevap;
    string islem;
    static void Main(string[] args)
    {
        Console.Write("Lütfen ilk tam sayıyı giriniz: ");
        sayi1 = Convert.ToDouble(Console.ReadLine());
        Console.Write("Lütfen yapacağınız işlemi giriniz (+, -, /, *): ");
        islem = Console.ReadLine();
        Console.Write("Lütfen ikinci tam sayıyı giriniz: ");
        sayi2 = Convert.ToDouble(Console.ReadLine());
        switch (islem)
        {
            case "-":
                cevap = sayi1 - sayi2;
                break;
            case "+":
                cevap = sayi1 + sayi2;
                break;
            case "/":
                cevap = sayi1 / sayi2;
                break;
            case "*":
                cevap = sayi1 * sayi2;
                break;
            default:
                cevap = 0;
                break;
        }
        Console.WriteLine(sayi1.ToString() + " " + islem + " " + sayi2.ToString() + " = " + cevap.ToString());
        Console.ReadLine();
    }
}