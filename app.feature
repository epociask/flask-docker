Feature: API happy path testing
    As a shitty API user, 
    I want to hit the bye endpoint,
    and see my name with bye

Scenario Outline: Ensure that bye works when given request data
  When the API is queried with name: "<string>"
  Then the response has the prefix bye with "<string>" as output
  And the response status code is 200

Examples: Trivia
  | string      |
  | hello world | 
  | golang      | 
  | fuck school |
  | hardworking student | 