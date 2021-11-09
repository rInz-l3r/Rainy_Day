package com.rainyday.users;

import java.util.ArrayList;
import java.util.HashMap;

public class Users {
    ArrayList<HashMap<String, String>> users = new ArrayList<HashMap<String, String>>();

    // Create User List, mocking user DB.
    public Users() {
        users.add(new User("Jacob", "Edmonson").getDetails());
        users.add(new User("Josh", "Dejong").getDetails());
        users.add(new User("Jennifer", "Edmonson").getDetails());
    }
    
    // Return user list
    public ArrayList<HashMap<String, String>> getUsers(){
        return users;
    }

}
