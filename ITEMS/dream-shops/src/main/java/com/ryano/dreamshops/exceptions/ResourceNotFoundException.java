package com.ryano.dreamshops.exceptions;

public class ResourceNotFoundException extends RuntimeException{

    public ResourceNotFoundException (String message) {
        super(message);
    }

}