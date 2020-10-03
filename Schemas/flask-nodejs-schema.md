# Professor
| Attribute      | Type                        | Condition      | Values                                                            |
|----------------|-----------------------------|----------------|-------------------------------------------------------------------|
| name           | string                      | required: true | any valid string                                                  |
| designation    | string                      | required: true | enum: ['Professor', 'Associate Professor', 'Assistant Professor'] |
| email          | string                      | --             | any valid string                                                  |
| interests      | list/array                  | --             | [any valid string, ..]                                            |
| researchGroups | list/array of ResearchGroup |                | [researchGroupID, ..]                                             |


# ResearchGroup
| Attribute   | Type      | Condition      | Values           |
|-------------|-----------|----------------|------------------|
| name        | string    | required: true | any valid string |
| founder     | Professor | required: true | prof_id          |
| description | string    | --             | any valid string |


# Student
| Attribute      | Type                        | Condition      | Values                |
|----------------|-----------------------------|----------------|-----------------------|
| name           | string                      | required: true | any valid string      |
| studentNumber  | string                      | required: true | any valid string      |
| researchGroups | list/array of ResearchGroup | --             | [researchGroupID, ..] |