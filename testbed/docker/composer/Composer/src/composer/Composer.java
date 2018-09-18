package composer;

public class Composer {
    public static void main(String[] args) {
        // writer(miners, users)
        Writer writer = new Writer(1, 2); 
        writer.header();
        writer.createMiners();
        writer.createUsers();
        writer.end();
    }    
}
