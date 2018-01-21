package com.example.jameslu.logintest;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MapsPage extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_maps_page);
    }
    public void sendMessage(View view){
        Intent intent = new Intent(MapsPage.this, Directions.class);
        startActivity(intent);
    }
}
