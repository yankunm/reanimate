package com.yankunm.s3;

import software.amazon.awssdk.core.ResponseInputStream;
import software.amazon.awssdk.core.sync.RequestBody;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.GetObjectRequest;
import software.amazon.awssdk.services.s3.model.GetObjectResponse;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;

import java.io.IOException;

/**
 * Yankun Meng
 */
public class S3Service {

    private final S3Client s3;


    public S3Service(S3Client s3client) {
        this.s3 = s3client;
    }

    // Method for upload
    public void putObject(String bucketName, String key, byte[] file){
        PutObjectRequest objectRequest = PutObjectRequest.builder()
                .bucket(bucketName)
                .key(key)
                .build();
        s3.putObject(objectRequest, RequestBody.fromBytes(file));
    }


    // Method for download
    public byte[] getObject(String bucketName, String key) {
        GetObjectRequest getObjectRequest = GetObjectRequest.builder()
                .bucket(bucketName)
                .key(key)
                .build();

        ResponseInputStream<GetObjectResponse> res = s3.getObject(getObjectRequest);
        try {
            return res.readAllBytes();
        } catch(IOException e){
            throw new RuntimeException(e);
        }
    }
}
