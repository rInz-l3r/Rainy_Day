package com.rainyday.dataservice;

import java.util.ArrayList;

import com.rainyday.users.User;
import com.rainyday.users.Users;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import java.util.HashMap;

@RestController
public class DataServiceController {
    
    @GetMapping("/users")
    ArrayList<HashMap<String,String>> getUsers(){
        return new Users().getUsers();
    }


}
