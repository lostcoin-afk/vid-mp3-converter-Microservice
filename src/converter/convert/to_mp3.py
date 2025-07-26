import pika, json, tempfile, os
from bson.objectid import ObjectId
import moviepy

def start(message, fs_videos, fs_mp3s,channel):
    #converts to python object
    message = json.loads(message)
    #empty temp video file
    temp = tempfile.NamedTemporaryFile()
    #video contents
    out= fs_videos.get(ObjectId(message["video_fid"]))
    #add video contents to empty file
    temp.write(out.read())
    #create audeo from temp vid file
    audio = moviepy.editor.VideoFileClip(temp.name).audio
    temp.close()

    #write the audio to the file
    tf_audio_path = tempfile.gettempdir() + f"/{message['video_fid']}.mp3"
    audio.write_audiofile(tf_audio_path)

    #save the file to mongo
    f = open(tf_audio_path,"rb")
    data = f.read()
    fid = fs_mp3s.put(data)
    f.close()
    os.remove(tf_audio_path)

    message["mp3_fid"] = str(fid)

    try:
        channel.basic_publish(
            exchange="",
            routing_key=os.environ.get("MP3_QUEUE"),
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as err:
        fs_mp3s.delete(fid)
        return "fialed to publish message"