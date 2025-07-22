import pika, json

def upload(f,fs,channel,access):
    try:
        fid = fs.put(f)
    except Exception as err:
        return "internal server error Could not upload file", 500
    
    message = {
        "video_id": str(fid),
        "mp3_id": None,
        "username": access["username"]
    }

    try:
        channel.basic_publish(
            exchange="",
            routing_key ="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTEN_DELIVERY_MODE
            ),
        )
    except:
        fs.delete(fid)
        return "Upload Faild  Could not add to queue", 500
    
