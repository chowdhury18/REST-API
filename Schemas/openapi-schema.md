# Course

| Attribute     | Type     | Condition                   | Values                          |
|---------------|----------|-----------------------------|---------------------------------|
| code          | string   | required: true unique: true | any valid string                |
| name          | string   | required: true unique: true | any valid string                |
| description   | string   | --                          | any valid string                |
| course_type   | string   | required: true              | enum: ['compulsory','optional'] |
| semester      | string   | required: true              | enum: ['autumn','spring']       |
| starting_date | datetime | required: true              | datetime                        |
| ending_date   | datetime | required: ture              | datetime                        |