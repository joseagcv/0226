package com.pontia.demo_spring.controller;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class HelloController {

	@Value("${PYTHON_URL_PORT:python:8000}")
	private String path;

	@GetMapping("/")
	public String index() {
		return "Greetings from Spring Boot!";
	}

	@GetMapping("/messages")
	public String getMessages() {
		RestTemplate restTemplate = new RestTemplate();
		return restTemplate.getForObject("http://"+ path +"/messages", String.class);
	}

	@PostMapping("/messages")
	public String sendMessage(@RequestBody MessageRequest request){
		RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        HttpEntity<MessageRequest> requestEntity = new HttpEntity<>(request, headers);
        ResponseEntity<String> response = restTemplate.postForEntity("http://"+ path +"/messages", requestEntity, String.class);
        return response.getBody();
	}

}