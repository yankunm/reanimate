package com.yankunm.auth;

public record AuthenticationRequest(
        String username,
        String password
) {
}
