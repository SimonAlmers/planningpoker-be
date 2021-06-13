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

# Projects

| State | Methods                         | Permissions                 | Endpoint                                      | Description |
| ----- | ------------------------------- | --------------------------- | --------------------------------------------- | ----------- |
| Done  | `POST`, `GET`                   | `IsAuthenticated`           | `/api/v1/projects/`                           |             |
| Done  | `GET`, `PUT`, `PATCH`, `DELETE` | `Project Owner` or ReadOnly | `/api/v1/projects/:id/`                       |             |
| Done  | `POST`                          | `Project Owner`             | `/api/v1/projects/:project_id/members/`       |             |
| Done  | `PUT`, `PATCH`, `DELETE`        | `Project Owner`             | `/api/v1/projects/:project_id/members/:uuid/` |             |

# Stories

| State | Methods                         | Permissions                  | Endpoint                                                       | Description |
| ----- | ------------------------------- | ---------------------------- | -------------------------------------------------------------- | ----------- |
| Done  | `POST`, `GET`                   | `Project Member` or ReadOnly | `/api/v1/projects/:id/stories/`                                |             |
|       | `PUT`                           | `Project Member` or ReadOnly | `/api/v1/projects/:id/stories/reorder/`                        |             |
|       | `POST`, `GET`                   | `Project Member` or ReadOnly | `/api/v1/projects/:project_id/stories/:story_id/votes/`        |             |
| Done  | `GET`, `PUT`, `PATCH`, `DELETE` | `Project Member` or ReadOnly | `/api/v1/projects/:project_id/stories/:id/`                    |             |
| Done  | `POST`, `GET`                   | `Project Member` or ReadOnly | `/api/v1/projects/:project_id/stories/:story_id/comments/`     |             |
| Done  | `GET`, `PUT`, `PATCH`, `DELETE` | `Comment Author` or ReadOnly | `/api/v1/projects/:project_id/stories/:story_id/comments/:id/` |             |

# Planning Sessions

| State | Methods | Permissions | Endpoint                                                                      | Description |
| ----- | ------- | ----------- | ----------------------------------------------------------------------------- | ----------- |
|       |         |             | `/api/v1/projects/:uuid/planningsessions/`                                    |             |
|       |         |             | `/api/v1/projects/:uuid/planningsessions/:uuid/`                              |             |
|       |         |             | `/api/v1/projects/:uuid/planningsessions/:uuid/participants/`                 |             |
|       |         |             | `/api/v1/projects/:uuid/planningsessions/:uuid/participants/:uuid/`           |             |
|       |         |             | `/api/v1/projects/:uuid/planningsessions/:uuid/participants/:uuid/heartbeat/` |             |
|       |         |             | `/api/v1/projects/:uuid/planningsessions/:uuid/participants/:uuid/leave/`     |             |
|       |         |             | `/api/v1/projects/:uuid/planningsessions/:uuid/comments/`                     |             |
|       |         |             | `/api/v1/projects/:uuid/planningsessions/:uuid/comments/:uuid`                |             |
