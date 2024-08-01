import java.util.Scanner;
class mul{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the number : ");
        int a=sc.nextInt();
        for(int i=1;i<11;i++)
        {
            System.out.println(a+"x"+i+"="+(a*i));
        }
    } 
}
