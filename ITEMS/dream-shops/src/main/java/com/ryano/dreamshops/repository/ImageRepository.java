package com.ryano.dreamshops.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.ryano.dreamshops.model.Image;

public interface ImageRepository extends JpaRepository<Image, Long>{
    
}
