# Professor
| Request | Type   | Route                    | Request Body                 | Response Body                                                                                                            | Status Code |
|---------|--------|--------------------------|------------------------------|--------------------------------------------------------------------------------------------------------------------------|-------------|
| CREATE  | POST   | /listProfessor           | Professor                    | {message: 'Professor successfully created', id: **prof_id**}                                                             | 201         |
| READ    | GET    | /listProfessor/{prof_id} | --                           | Single database object - {name: **name**, email: **email**, designation: **designation**, interests: **[interest, ..]**} | 200         |
| READ    | GET    | /listProfessors          | designation OR groupName (*) | Multiple database objects - {name: **name**, email: **email**}                                                           | 200         |
| UPDATE  | PUT    | /listProfessor/{prof_id} | Professor                    | {message: 'Professor successfully updated', id: **prof_id**}                                                             | 200         |
| DELETE  | DELETE | /listProfessor/{prof_id} | --                           | {message: 'Professor successfully deleted', if: **prof_id**}                                                             | 200         |


# ResearchGroup
| Request | Type   | Route                 | Request Body  | Response Body                                                                     | Status Code |
|---------|--------|-----------------------|---------------|-----------------------------------------------------------------------------------|-------------|
| CREATE  | POST   | /listGroup            | ResearchGroup | {message: 'Group successfully created', id: **group_id**}                         | 201         |
| READ    | GET    | /listGroup/{group_id} | --            | Single database object - {id: **group_id**, name: **name**, founder: **prof_id**} | 200         |
| UPDATE  | PUT    | /listGroup/{group_id} | ResearchGroup | {message: 'Group successfully updated', id: **group_id**}                         | 200         |
| DELETE  | DELETE | /listGroup/{group_id} | --            | {message: 'Group successfully deleted', if: **group_id**}                         | 200         |


# Student
| Request | Type   | Route                     | Request Body  | Response Body                                                                                                   | Status Code |
|---------|--------|---------------------------|---------------|-----------------------------------------------------------------------------------------------------------------|-------------|
| CREATE  | POST   | /listStudent              | Student       | {message: 'Student successfully created', id: **student_id**}                                                   | 201         |
| READ    | GET    | /listStudent/{student_id} | --            | Single database object - {name: **name**, studentNumber: **studentNumber**, researchGroups: **[group_id, ..]**} | 200         |
| READ    | GET    | /listStudents             | groupName (*) | Multiple database objects - {name: **name**, studentNumber: **studentNumber**}                                  | 200         |
| UPDATE  | PUT    | /listStudent/{student_id} | Student       | {message: 'Student successfully updated', id: **student_id**}                                                   | 200         |
| DELETE  | DELETE | /listStudent/{student_id} | --            | {message: 'Student successfully deleted', if: **student_id**}                                                   | 200         |


**NOTE**: (*) For GET requests, use the query string to pass the parameters.