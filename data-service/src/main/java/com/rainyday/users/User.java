package com.rainyday.users;

import java.util.HashMap;

public class User {
    String firstName;
    String lastName;


    public User(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public HashMap<String, String> getDetails(){
        HashMap<String, String> user = new HashMap<String, String>();
        user.put("name", this.firstName+" "+this.lastName);
        return user;
    }
    
}
