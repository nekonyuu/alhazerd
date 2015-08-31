# User document format

## Example

```json
{
  "id": 1,
  "role": "admin",
  "username": "nekonyuu",
  "email": "nk@foo.bar",
  "password": "$5$rounds=80000$zvpXD3gCkrt7tw.1$QqeTSolNHEfgryc5oMgiq1o8qCEAcmye3FoMSuvgToC",
}
```

## Fields

  * ```id```: id of the user ;
  * ```role```: role of the user ;
  * ```username```: username of the user ;
  * ```email```: its email ;
  * ```password```: string of its hashed & salted password.
