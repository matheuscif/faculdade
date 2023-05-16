package Coffee;

/**
 * Methods
 */
public class Methods {
    public static void canal(){
        System.out.println("method");
    }

    public static void msg(String msg, int... n){
        int count = (n.length > 0) ? n[0] : 1;
        for(int i = 0; i < count; i++){
            System.out.println(msg);
        }
    }
    public static int plus(int... numbers){
        int ans = 0;
        for(int n:numbers){
            ans += n; 
        }
        return ans;
    }
}