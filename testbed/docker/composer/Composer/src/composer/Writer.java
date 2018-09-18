/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package composer;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

/**
 *
 * @author john
 */
public class Writer {
    int miners; 
    int users; 
    
    public Writer(int miners, int users) {
        this.miners = miners;
        this.users = users;
    }
    
    public void header() {
        try(  PrintWriter out = new PrintWriter("../docker-compose.yml")){
            int version = 2;  
            out.println("version: " + "'"+version+"'");
            out.println("services:");
        }
        catch(IOException e) {
            
        }    
    }
    
    public void createMiners() {
        try(  FileWriter out = new FileWriter("../docker-compose.yml", true)){
            String tap = "  ";
            String command = "\"mkdir -p code && /bin/bash\"";
            for(int i = 0; i < miners; i++) {
                int ip = 2 + i; 
                out.append(tap+"miner"+i+":\n");
                out.append(tap+tap+"image: test\n");
                out.append(tap+tap+"entrypoint: bash\n");
                out.append(tap+tap+"command: -c " + ""+command+"\n");
                //out.append(tap+tap+"volumes:\n");
                out.append(tap+tap+"tty: true\n");
                out.append(tap+tap+"ports:\n");
                out.append(tap+tap+tap+"- 9000\n");
                out.append(tap+tap+"networks:\n");
                out.append(tap+tap+tap+"app_net:\n");
                out.append(tap+tap+tap+tap+"ipv4_address: 192.168.0."+ip+"\n");
            }
        }
        catch(IOException e) {
            
        }
    }
    
    private static String dirlist(String fname){
        File dir = new File(fname);
        String parentpath = dir.getParent();
        return parentpath;
    }

    public void createUsers() {
        try(  FileWriter out = new FileWriter("../docker-compose.yml", true)){
            String tap = "  ";
            String command = "\"mkdir -p code && /bin/bash\"";
            String fileContainerTemp = dirlist(System.getProperty("user.dir"));
            String fileContainer = "- " + fileContainerTemp + "/filecontainer:/workspace";
            for(int i = 0; i < users; i++) {
                int ip = 2 + miners + i; 
                out.append(tap+"user"+i+":\n");
                out.append(tap+tap+"image: test\n");
                out.append(tap+tap+"entrypoint: bash\n");
                out.append(tap+tap+"command: -c " + ""+command+"\n");
                out.append(tap+tap+"volumes:\n");
                out.append(tap+tap+tap+fileContainer + "\n");
                out.append(tap+tap+"tty: true\n");
                out.append(tap+tap+"ports:\n");
                out.append(tap+tap+tap+"- 9000\n");
                out.append(tap+tap+"networks:\n");
                out.append(tap+tap+tap+"app_net:\n");
                out.append(tap+tap+tap+tap+"ipv4_address: 192.168.0."+ip+"\n");
            }
        }
        catch(IOException e) {
            
        }
    }
    
    public void end() {
        try(  FileWriter out = new FileWriter("../docker-compose.yml", true)){
            //Network
            String tap = "  ";
            out.append("networks:\n");
            out.append(tap + "app_net:\n");
            out.append(tap + tap + "driver: bridge\n");
            out.append(tap + tap + "driver_opts:\n");
            out.append(tap + tap + tap + "com.docker.network.enable_ipv6: \"true\"\n");
            out.append(tap + tap + "ipam:\n"); 
            out.append(tap + tap + tap +"driver: default\n");
            out.append(tap + tap + tap + "config:\n");
            out.append(tap + tap + tap + tap + "- subnet: 192.168.0.0/24\n");
            out.append(tap + tap + tap + tap + tap + "gateway: 192.168.0.1\n");
            out.append(tap + tap + tap + tap + "- subnet: 2001:3984:3989::/64\n");
            out.append(tap + tap + tap + tap + tap + "gateway: 2001:3984:3989::/1\n");       
        } 
        catch (IOException ex) {
            // report
        }
   } 
}
