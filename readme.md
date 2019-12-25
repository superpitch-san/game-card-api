Card Game API frontend application

Requirement:
 - install node, docker, docker-compose on your machine before run this repository.

Installation Project:
 - pull project on your machine.
 - open terminal and cd path of project.
 - run command ' docker-compose up -d ' and waiting about 3 - 5 mins. (you can check docker logs by command 'docker logs [IMAGE ID]' )
 - open https://localhost:8000 on your browser for checking server is running if run normally server will return 400 bad request page.

API Documentation:
 - METHOD GET /api/score/
 - Header:
   - application/json
 - Response:
   - Status: 200
{
  "meta": {
    "limit": 20,
    "next": null,
    "offset": 0,
    "previous": null,
    "total_count": 2
  },
  "objects": [
    {
      "created_at": "2019-12-25T15:38:59.505988",
      "id": 1,
      "resource_uri": "/api/score/1/",
      "top_score": 18
    }
  ]
}
 - METHOD POST /api/score/
 - Header:
   - application/json
 - Body:
{
	"top_score": 18
}
 - Response:
   - Status: 201
   - Status: 400
{
  "error": "Request is not valid JSON."
}
 - METHOD GET /api/score/:id/
 - Header:
   - application/json
 - Response:
   - Status: 200
{
  "created_at": "2019-12-25T15:38:59.505988",
  "id": 1,
  "resource_uri": "/api/score/1/",
  "top_score": 18
}
   if have any problem or questions, Can contact me at supapitch.sangmanee@gmail.com