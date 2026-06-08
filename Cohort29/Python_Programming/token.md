# Example: JWT Token Creation Flow

## Step 1: User Sends Login Request

The client sends a POST request to the API with a username and password.

### Request

```bash
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{
        "username": "user1",
        "password": "password"
      }'
```

### Request Body

```json
{
  "username": "user1",
  "password": "password"
}
```

---

## Step 2: Server Validates Credentials

The server checks:

1. Does the user exist?
2. Does the password match?
3. Is the account allowed to log in?

If everything is valid, the server generates a JWT token.

---

## Step 3: Server Returns JWT Token

### Response

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzE3ODUxMjAwLCJleHAiOjE3MTc4NTQ4MDB9.fake-signature-example"
}
```

Status Code:

```http
201 Created
```

or

```http
200 OK
```

depending on the implementation.

---

# Understanding the JWT Structure

A JWT consists of three parts:

```text
HEADER.PAYLOAD.SIGNATURE
```

Example:

```text
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJzdWIiOiJ1c2VyMSIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzE3ODUxMjAwLCJleHAiOjE3MTc4NTQ4MDB9
.
fake-signature-example
```

---

## Header

Contains metadata about the token.

Decoded example:

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

Meaning:

* alg = hashing algorithm
* typ = token type

---

## Payload

Contains information about the user.

Decoded example:

```json
{
  "sub": "user1",
  "role": "user",
  "iat": 1717851200,
  "exp": 1717854800
}
```

Meaning:

| Field | Description        |
| ----- | ------------------ |
| sub   | Username / Subject |
| role  | User role          |
| iat   | Issued At          |
| exp   | Expiration Time    |

---

## Signature

The signature is created by the server using a secret key.

Example:

```text
fake-signature-example
```

The client cannot modify the payload without breaking the signature.

This is what makes JWT secure.

---

# Step 4: Accessing a Protected Route

The client includes the token in future requests.

### Request

```bash
curl http://localhost:5000/jwt-protected \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSIsInJvbGUiOiJ1c2VyIiwiaWF0IjoxNzE3ODUxMjAwLCJleHAiOjE3MTc4NTQ4MDB9.fake-signature-example"
```

---

# Step 5: Server Verifies the Token

The server checks:

* Is the token present?
* Is the signature valid?
* Has the token expired?
* Is the user allowed to access the route?

If valid:

```text
JWT Auth: Access Granted
```

Status Code:

```http
200 OK
```

---

# Invalid Token Example

Request:

```bash
curl http://localhost:5000/jwt-protected
```

Response:

```json
{
  "error": "Missing or invalid token"
}
```

Status Code:

```http
401 Unauthorized
```

---

# JWT Authentication Flow Diagram

```text
+--------+
| Client |
+--------+
     |
     | POST /login
     | username + password
     v
+------------+
| API Server |
+------------+
     |
     | Validate credentials
     |
     | Generate JWT
     v
+--------+
| Client |
+--------+
     |
     | Authorization: Bearer TOKEN
     v
+------------+
| API Server |
+------------+
     |
     | Verify token
     |
     | Grant access
     v
 Protected Route
```

## Key Takeaway

A JWT acts like a temporary digital ID card.

Instead of sending a username and password with every request, the client sends a signed token that proves their identity.
