# Planning Poker API endpoints

A list of all available/planned endpoints for the Planning Poker API.

# Auth

| State        | Methods | Permissions       | Endpoint                  | Description           |
| ------------ | ------- | ----------------- | ------------------------- | --------------------- |
| ✅           | `POST`  | `IsAuthenticated` | `/auth/api-token-auth/`   | Obtain Auth Tokens    |
| ✅           | `POST`  | `IsAuthenticated` | `/auth/api-token-reresh/` | Token Refresh         |
| Not used yet | `GET`   | `IsAuthenticated` | `/api/v1/firebase-token/` | Obtain Firebase Token |

# Users

| State        | Methods                         | Permissions        | Endpoint                                | Description                                    |
| ------------ | ------------------------------- | ------------------ | --------------------------------------- | ---------------------------------------------- |
| ✅           | `POST`                          | `AllowAny`         | `/api/v1/users/`                        | Create New User (Sign Up)                      |
| ✅           | `GET`, `PUT`, `PATCH`, `DELETE` | `IsAuthenticated`, | `/api/v1/users/me/`                     | Read and write `User` object for current user. |
| Not used yet | `POST`                          |                    | `/api/v1/users/activation/`             |                                                |
| Not used yet | `POST`                          |                    | `/api/v1/users/resend_activation/`      |                                                |
| Not used yet | `POST`                          |                    | `/api/v1/users/set_email/`              |                                                |
| Not used yet | `POST`                          |                    | `/api/v1/users/reset_email/`            |                                                |
| Not used yet | `POST`                          |                    | `/api/v1/users/reset_email_confirm/`    |                                                |
| Not used yet | `POST`                          |                    | `/api/v1/users/set_password/`           |                                                |
| Not used yet | `POST`                          |                    | `/api/v1/users/reset_password/`         |                                                |
| Not used yet | `POST`                          |                    | `/api/v1/users/reset_password_confirm/` |                                                |

# Notifications

| State | Methods        | Permissions        | Endpoint                              | Description                                    |
| ----- | -------------- | ------------------ | ------------------------------------- | ---------------------------------------------- |
| ✅    | `PUT`, `PATCH` | `IsAuthenticated`, | `/api/v1/notifications/:id/mark_read` | Indicate that a User has read the notification |

# Projects

| State | Methods                         | Permissions                 | Endpoint                                      | Description                                             |
| ----- | ------------------------------- | --------------------------- | --------------------------------------------- | ------------------------------------------------------- |
| ✅    | `POST`, `GET`                   | `IsAuthenticated`           | `/api/v1/projects/`                           | Create Project or Get List of Projects I'm a member of. |
| ✅    | `GET`, `PUT`, `PATCH`, `DELETE` | `Project Owner` or ReadOnly | `/api/v1/projects/:id/`                       | Get, Update or Delete a specific Project.               |
| ✅    | `POST`                          | `Project Owner`             | `/api/v1/projects/:project_id/members/`       | Add a Project Member to a specific Project.             |
| ✅    | `PUT`, `PATCH`, `DELETE`        | `Project Owner`             | `/api/v1/projects/:project_id/members/:uuid/` | Get, Update or Delete a specific Project Member.        |
| ✅    | `GET`                           | `IsAuthenticated`           | `/api/v1/projects/:project_id/invite_code/`   | Get a UUID invite code to invite users to a Project.    |
| ✅    | `POST`                          | `IsAuthenticated`           | `/api/v1/projects/join/`                      | Join a project by posting invite code in payload.       |

# Stories

| State        | Methods                         | Permissions                  | Endpoint                                                       | Description                                     |
| ------------ | ------------------------------- | ---------------------------- | -------------------------------------------------------------- | ----------------------------------------------- |
| ✅           | `POST`, `GET`                   | `Project Member` or ReadOnly | `/api/v1/projects/:id/stories/`                                | Get or Create Stories for a specific Project.   |
| Not used yet | `PUT`                           | `Project Member` or ReadOnly | `/api/v1/projects/:id/stories/reorder/`                        | Move a specific Story to a specific index.      |
| ✅           | `POST`, `GET`                   | `Project Member` or ReadOnly | `/api/v1/projects/:project_id/stories/:story_id/votes/`        | Get or Create Vote for a specific Story.        |
| ✅           | `GET`, `PUT`, `PATCH`, `DELETE` | `Project Member` or ReadOnly | `/api/v1/projects/:project_id/stories/:id/`                    | Get, Update or Delete a specific Story.         |
| Not used yet | `POST`, `GET`                   | `Project Member` or ReadOnly | `/api/v1/projects/:project_id/stories/:story_id/comments/`     | Get or Create Comments for a specific Story.    |
| Not used yet | `GET`, `PUT`, `PATCH`, `DELETE` | `Comment Author` or ReadOnly | `/api/v1/projects/:project_id/stories/:story_id/comments/:id/` | Get, Update or Delete a specific Story Comment. |

# Planning Sessions

| State    | Methods                         | Permissions                  | Endpoint                                                                          | Description                                                                                                  |
| -------- | ------------------------------- | ---------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| ✅       | `POST`, `GET`                   | `Project Member` or ReadOnly | `/api/v1/projects/:project_id/sessions/`                                          | Get or Create a Planning Session.                                                                            |
| ✅       | `GET`, `PUT`, `PATCH`, `DELETE` | `Project Member` or ReadOnly | `/api/v1/projects/:project_id/sessions/:session_id/`                              | Get, Update or Delete a specific Planning Session.                                                           |
| ✅       | `POST`, `GET`                   | `Project Member` or ReadOnly | `/api/v1/projects/:project_id/sessions/:session_id/participants/`                 | Get or Create Planning Session Participants                                                                  |
| Not used | `GET`, `DELETE`                 | `Project Member` or ReadOnly | `/api/v1/projects/:project_id/sessions/:session_id/participants/:uuid/`           | Get or Create Planning Session Participants                                                                  |
| ✅       | `POST`,                         | `Project Member` or ReadOnly | `/api/v1/projects/:project_id/sessions/:session_id/participants/:uuid/heartbeat/` | Post timestamp when visiting a specific Planning Session, can be done once on enter or in a fixed intervall. |
| ✅       | `POST`,                         | `Project Member` or ReadOnly | `/api/v1/projects/:project_id/sessions/:session_id/participants/:uuid/leave/`     | Post timestamp when explicitly leaving a specific Planning Session.                                          |
| ✅       | `POST`, `GET`                   | `Project Member` or ReadOnly | `/api/v1/projects/:project_id/sessions/:session_id/comments/`                     | Get or Create Planning Session Chat Messages.                                                                |
| ✅       | `GET`, `PUT`, `PATCH`, `DELETE` | `Comment Author` or ReadOnly | `/api/v1/projects/:project_id/sessions/:session_id/comments/:uuid`                | Get, Update or Delete a specific Planning Session Chat Message.                                              |
