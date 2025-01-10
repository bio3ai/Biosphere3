import asyncio
import websockets
import json
from loguru import logger

characterId = 448450
characterId2 = 240929

requests = {
    "heartbeat": {
        "characterId": characterId,
        "messageCode": 0,
        "messageName": "heartbeat",
        "data": {"msg": "this is a message to keep connection alive"},
    },
    "connectionInit": {
        "characterId": characterId,
        "messageCode": 1,
        "messageName": "connectionInit",
        "data": {"msg": "client request character init"},
    },
    "eventInfo": {
        "characterId": characterId,
        "messageCode": 2,
        "messageName": "eventInfo",
        "data": {"msg": "event string", "gameTime": "time"},
    },
    "actionResult": {
        "characterId": characterId,
        "messageCode": 3,
        "messageName": "actionresult",
        "data": {
            "actionName": "name",
            "actionCode": "code",
            "result": "result",
            "gameTime": "time",
            "msg": "msg",
        },
    },
    "gameTime": {
        "characterId": characterId,
        "messageCode": 5,
        "messageName": "gameTime",
        "data": {"msg": "event string", "gameTime": "time"},
    },
    "conversation": {
        "characterId": characterId,
        "messageCode": 100,
        "messageName": "to_agent",
        "data": {
            "from_id": characterId,
            "to_id": characterId2,
            "latest_message": {
                "playerName": "message_info",
            },
            "Finish": [False, False],
        },
    },
    "cv_submission": {
        "characterId": characterId,
        "messageCode": 13,
        "messageName": "cv_submission",
        "data": {
            "health": 100,
            "studyXp": 100,
            "education": "University",
            "week": 1,
            "date": 1,
        },
    },
    "accommodation_event": {
        "characterId": characterId,
        "messageCode": 14,
        "messageName": "accommodation_event",
        "data": {
            "msg": "House rent will expire tomorrow",
            "gameTime": "time",
        },
    },
}


async def send_request(websocket, request):
    message = json.dumps(request)
    await websocket.send(message)
    if request["messageName"] != "heartbeat":
        logger.info(f"Sent: {message}")


async def receive_response(websocket):
    while True:
        response = await websocket.recv()
        message = json.loads(response)
        if message["messageName"] != "heartbeat":
            logger.info(f"Received: {message}")


async def send_heartbeat(websocket):
    while True:
        await send_request(websocket, requests["heartbeat"])
        await asyncio.sleep(30)


async def send_game_time(websocket):
    while True:
        await send_request(websocket, requests["gameTime"])
        await asyncio.sleep(300)


async def send_event_info(websocket):
    while True:
        await asyncio.sleep(300)
        requests["eventInfo"]["data"]["msg"] = "ActionList Empty"
        await send_request(websocket, requests["eventInfo"])


async def send_cv_submission(websocket):
    while True:
        await asyncio.sleep(1800)
        requests["cv_submission"]["data"]["health"] = 100
        requests["cv_submission"]["data"]["studyXp"] = 100
        requests["cv_submission"]["data"]["education"] = "University"
        requests["cv_submission"]["data"]["week"] = 1
        requests["cv_submission"]["data"]["date"] = 1
        await send_request(websocket, requests["cv_submission"])


async def send_accommodation_event(websocket):
    while True:
        await asyncio.sleep(1800)
        requests["accommodation_event"]["data"][
            "msg"
        ] = "House rent will expire tomorrow"
        await send_request(websocket, requests["accommodation_event"])


async def main():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        await send_request(websocket, requests["connectionInit"])

        receive_task = asyncio.create_task(receive_response(websocket))

        heartbeat_task = asyncio.create_task(send_heartbeat(websocket))
        # game_time_task = asyncio.create_task(send_game_time(websocket))
        event_info_task = asyncio.create_task(send_event_info(websocket))
        cv_submission_task = asyncio.create_task(send_cv_submission(websocket))
        accommodation_event_task = asyncio.create_task(
            send_accommodation_event(websocket)
        )
        await asyncio.gather(
            receive_task,
            heartbeat_task,
            # game_time_task,
            event_info_task,
            cv_submission_task,
            accommodation_event_task,
        )


if __name__ == "__main__":
    asyncio.run(main())
