import json
from imageai.Detection import VideoObjectDetection
import os

execution_path = os.getcwd()

array = []
def forSeconds(second_number, output_arrays, count_arrays, average_output_count):
    # print("SECOND : ", second_number)
    # print("Array for the outputs of each frame ", output_arrays)
    # print("Array for output count for unique objects in each frame : ", count_arrays)
    # print("Output average count for unique objects in the last second: ", average_output_count)
    # print("------------END OF A SECOND --------------")
    array.append({second_number:average_output_count})


video_detector = VideoObjectDetection()
video_detector.setModelTypeAsRetinaNet()
video_detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.1.0.h5"))
video_detector.loadModel()


video_detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "video2.mp4"),
        output_file_path=os.path.join(execution_path, "resultado") ,
        frames_per_second=30, per_second_function=forSeconds,  minimum_percentage_probability=30)

b = []
for i in array:
    aux = list(i.keys())
    aux2 = list(i.values())
    final = list(aux2[0].keys())
    b.append({aux[0]:final})


def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }