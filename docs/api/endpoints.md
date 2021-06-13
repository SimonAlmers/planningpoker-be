# Planning Poker API endpoints

# Auth

| State | Methods | Permissions       | Endpoint                  | Description           |
| ----- | ------- | ----------------- | ------------------------- | --------------------- |
| Done  | `POST`  | `IsAuthenticated` | `/auth/api-token-auth/`   | Obtain Auth Tokens    |
| Done  | `POST`  | `IsAuthenticated` | `/auth/api-token-reresh/` | Token Refresh         |
|       | `GET`   | `IsAuthenticated` | `/api/v1/firebase-token/` | Obtain Firebase Token |

# Users

| State | Methods                         | Permissions        | Endpoint                                | Description                                    |
| ----- | ------------------------------- | ------------------ | --------------------------------------- | ---------------------------------------------- |
| Done  | `POST`                          | `AllowAny`         | `/api/v1/users/`                        | Create New User (Sign Up)                      |
| Done  | `GET`, `PUT`, `PATCH`, `DELETE` | `IsAuthenticated`, | `/api/v1/users/me/`                     | Read and write `User` object for current user. |
| Done  | `POST`                          |                    | `/api/v1/users/activation/`             |                                                |
| Done  | `POST`                          |                    | `/api/v1/users/resend_activation/`      |                                                |
| Done  | `POST`                          |                    | `/api/v1/users/set_email/`              |                                                |
| Done  | `POST`                          |                    | `/api/v1/users/reset_email/`            |                                                |
| Done  | `POST`                          |                    | `/api/v1/users/reset_email_confirm/`    |                                                |
| Done  | `POST`                          |                    | `/api/v1/users/set_password/`           |                                                |
| Done  | `POST`                          |                    | `/api/v1/users/reset_password/`         |                                                |
| Done  | `POST`                          |                    | `/api/v1/users/reset_password_confirm/` |                                                |
