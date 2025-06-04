import json

test = []


test.append({
    "threat": {
        "id": 1,
        "actor_risk": {
            "actor_id": 1
        }
    }
})

print(json.dumps(test))