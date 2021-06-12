# Planning Poker API endpoints

# Auth

| State | Methods | Permissions       | Endpoint                  | Description           |
| ----- | ------- | ----------------- | ------------------------- | --------------------- |
| Done  | `POST`  | `IsAuthenticated` | `/auth/api-token-auth/`   | Obtain Auth Tokens    |
| Done  | `POST`  | `IsAuthenticated` | `/auth/api-token-reresh/` | Token Refresh         |
|       | `GET`   | `IsAuthenticated` | `/api/v1/firebase-token/` | Obtain Firebase Token |
