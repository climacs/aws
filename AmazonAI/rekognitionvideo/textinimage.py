import boto3
from time import sleep

rek = boto3.client('rekognition')

def StartTextDetection(bucket, video):
    response = rek.start_text_detection(Video={'S3Object': {'Bucket': bucket, 'Name': video}})
    print('Start Job Id: ' + response['JobId'])
    return response['JobId']


def GetTextDetectionResults(job_id):
    maxResults = 10
    paginationToken = ''
    finished = False

    while finished == False:
        response = rek.get_text_detection(JobId=job_id,
                                               MaxResults=maxResults,
                                               NextToken=paginationToken)

        print('Codec: ' + response['VideoMetadata']['Codec'])

        print('Duration: ' + str(response['VideoMetadata']['DurationMillis']))
        print('Format: ' + response['VideoMetadata']['Format'])
        print('Frame rate: ' + str(response['VideoMetadata']['FrameRate']))
        print()

        for textDetection in response['TextDetections']:
            text = textDetection['TextDetection']

            print("Timestamp: " + str(textDetection['Timestamp']))
            print("   Text Detected: " + text['DetectedText'])
            print("   Confidence: " + str(text['Confidence']))
            #print("      Bounding box")
            #print("        Top: " + str(text['Geometry']['BoundingBox']['Top']))
            #print("        Left: " + str(text['Geometry']['BoundingBox']['Left']))
            #print("        Width: " + str(text['Geometry']['BoundingBox']['Width']))
            #print("        Height: " + str(text['Geometry']['BoundingBox']['Height']))
            print("   Type: " + str(text['Type']))
            print()

            if 'NextToken' in response:
                paginationToken = response['NextToken']
            else:
                finished = True

if __name__ == '__main__':
    bucket = YOUR_BUCKET
    video = YOUR_VIDEO_FILE

    job_id = StartTextDetection(bucket, video)
    # Wait for a bit, or use an SNS notification
    GetTextDetectionResults(job_id)
