# AI Service For XMAS 2024 Hack

## Запуск

```Dockerfile
docker build -t python-ai-service .

docker run -e PORT=3000 -p 3000:3000 python-ai-service
```

## API

Swagger

```
localhost:YOUR_PORT/docs
```

```

POST /ai_filtered_data
Req body:
[
  {
    "id": 0,
    "conversion": 0,
    "avg_time": 0,
    "commission": 0,
    "limit_min": 0,
    "limit_max": 0
  }
]

Res:
200 application/json
{
  "filteredData": [
    {
      "id": 0,
      "conversion": 0,
      "avg_time": 0,
      "commission": 0,
      "limit_min": 0,
      "limit_max": 0
    }
  ]
}
```
