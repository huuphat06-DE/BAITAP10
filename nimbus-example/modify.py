import os

jwt_service_path = r"d:\BT10\nimbus-example\src\main\java\vn\iotstar\services\JwtService.java"

content = """package vn.iotstar.services;

import com.nimbusds.jose.*;
import com.nimbusds.jose.crypto.MACSigner;
import com.nimbusds.jose.crypto.MACVerifier;
import com.nimbusds.jwt.JWTClaimsSet;
import com.nimbusds.jwt.SignedJWT;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;

import java.text.ParseException;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;

@Service
public class JwtService {
    @Value("${security.jwt.secret-key}")
    private String secretKey;

    @Value("${security.jwt.expiration-time}")
    private long jwtExpiration;

    public String extractUsername(String token) {
        return extractClaim(token, JWTClaimsSet::getSubject);
    }

    public <T> T extractClaim(String token, Function<JWTClaimsSet, T> claimsResolver) {
        final JWTClaimsSet claims = extractAllClaims(token);
        return claimsResolver.apply(claims);
    }

    public String generateToken(UserDetails userDetails) {
        return generateToken(new HashMap<>(), userDetails);
    }

    public String generateToken(Map<String, Object> extraClaims, UserDetails userDetails) {
        return buildToken(extraClaims, userDetails, jwtExpiration);
    }

    public long getExpirationTime() {
        return jwtExpiration;
    }

    private String buildToken(Map<String, Object> extraClaims, UserDetails userDetails, long expiration) {
        try {
            JWSSigner signer = new MACSigner(secretKey.getBytes());
            JWTClaimsSet.Builder claimsBuilder = new JWTClaimsSet.Builder()
                    .subject(userDetails.getUsername())
                    .issueTime(new Date(System.currentTimeMillis()))
                    .expirationTime(new Date(System.currentTimeMillis() + expiration));

            for (Map.Entry<String, Object> entry : extraClaims.entrySet()) {
                claimsBuilder.claim(entry.getKey(), entry.getValue());
            }

            SignedJWT signedJWT = new SignedJWT(
                    new JWSHeader(JWSAlgorithm.HS256),
                    claimsBuilder.build());

            signedJWT.sign(signer);
            return signedJWT.serialize();
        } catch (JOSEException e) {
            throw new RuntimeException("Error generating JWT token", e);
        }
    }

    public boolean isTokenValid(String token, UserDetails userDetails) {
        try {
            final String username = extractUsername(token);
            SignedJWT signedJWT = SignedJWT.parse(token);
            JWSVerifier verifier = new MACVerifier(secretKey.getBytes());
            
            return username.equals(userDetails.getUsername()) 
                    && signedJWT.verify(verifier) 
                    && !isTokenExpired(token);
        } catch (ParseException | JOSEException e) {
            return false;
        }
    }

    private boolean isTokenExpired(String token) {
        return extractExpiration(token).before(new Date());
    }

    private Date extractExpiration(String token) {
        return extractClaim(token, JWTClaimsSet::getExpirationTime);
    }

    private JWTClaimsSet extractAllClaims(String token) {
        try {
            SignedJWT signedJWT = SignedJWT.parse(token);
            JWSVerifier verifier = new MACVerifier(secretKey.getBytes());
            if (!signedJWT.verify(verifier)) {
                throw new RuntimeException("The JWT signature is invalid");
            }
            return signedJWT.getJWTClaimsSet();
        } catch (ParseException | JOSEException e) {
            throw new RuntimeException("Invalid JWT token", e);
        }
    }
}
"""

with open(jwt_service_path, "w", encoding="utf-8") as f:
    f.write(content)

exception_handler_path = r"d:\BT10\nimbus-example\src\main\java\vn\iotstar\configs\GlobalExceptionHandler.java"

with open(exception_handler_path, "r", encoding="utf-8") as f:
    exception_code = f.read()

# Replace jjwt exceptions with runtime exception catching or specific ones if needed, 
# since we used RuntimeException in extractAllClaims
exception_code = exception_code.replace("import io.jsonwebtoken.ExpiredJwtException;", "")
exception_code = exception_code.replace("import io.jsonwebtoken.security.SignatureException;", "")
exception_code = exception_code.replace("if (exception instanceof SignatureException) {", "if (exception.getMessage() != null && exception.getMessage().contains(\"invalid\")) {")
exception_code = exception_code.replace("if (exception instanceof ExpiredJwtException) {", "if (exception.getMessage() != null && exception.getMessage().contains(\"expired\")) {")

with open(exception_handler_path, "w", encoding="utf-8") as f:
    f.write(exception_code)
