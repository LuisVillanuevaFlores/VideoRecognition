import json
import boto3
from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

s3 = boto3.resource('s3',
    aws_access_key_id=os.environ['aws_access_key_id'],
    aws_secret_access_key=os.environ['aws_secret_access_key'],
    region_name='us-west-2'
)

array = []
def forSeconds(second_number, output_arrays, count_arrays, average_output_count):
    # print("SECOND : ", second_number)
    # print("Array for the outputs of each frame ", output_arrays)
    # print("Array for output count for unique objects in each frame : ", count_arrays)
    # print("Output average count for unique objects in the last second: ", average_output_count)
    # print("------------END OF A SECOND --------------")
    array.append({second_number:average_output_count})


def procesamiento(video):
    s3.Object('video-processing-s3','videos/'+ video).download_file(video)
    video_detector = VideoObjectDetection()
    video_detector.setModelTypeAsRetinaNet()
    video_detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.1.0.h5"))
    video_detector.loadModel()

    video_detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, video),
            frames_per_second=30, per_second_function=forSeconds,  minimum_percentage_probability=30)

    b = []
    print(array)
    for i in array:
        aux = list(i.keys())
        aux2 = list(i.values())
        final = list(aux2[0].keys())
        b.append({aux[0]:final})
    return b

def lambda_handler(event,context):
    # TODO implement
    body = json.loads(event['body'])
    response = procesamiento(body['video_name'])
    return {
        'statusCode': 200,
        'body':  json.dumps(response)
    }
