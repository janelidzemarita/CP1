import cv2

# Load pre-trained car detection model (Haar cascade)
car_cascade = cv2.CascadeClassifier('Problem_1.4/Car.xml')

# Open video file
cap = cv2.VideoCapture('Problem_1.4/1.mp4')

# Get frames per second (fps) value from the video
fps = cap.get(cv2.CAP_PROP_FPS)

# Get total number of frames in the video
total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

# Calculate time interval between frames
time_interval = 1 / fps

# Initialize variables
previous_frame_time = 0
first_detection_time = None
last_detection_time = None
car_speed = None
car_distance = 300  # Distance in meters
car_last_detection_time = None

while True:
    # Read frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform car detection
    cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Process each detected car
    for (x, y, w, h) in cars:
        # Draw bounding box around the car
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # If it's the first car detection, record the detection time
        if first_detection_time is None:
            first_detection_time = previous_frame_time

        # Record the detection time for each detection
        last_detection_time = previous_frame_time
        if last_detection_time - first_detection_time == 0:
            last_detection_time = None

    # Get current frame time
    current_frame_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000  # Convert milliseconds to seconds

    # Calculate time difference between frames
    time_difference = current_frame_time - previous_frame_time

    # Update previous frame time
    previous_frame_time = current_frame_time

    # Calculate car speed
    if first_detection_time is not None and last_detection_time is not None:
        time_since_first_detection = last_detection_time - first_detection_time
        car_speed = car_distance / time_since_first_detection

        # Display car speed on the frame
        cv2.putText(frame, f"Car Speed: {car_speed:.2f} m/s", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Display the frame
    cv2.imshow('Video with Time Stamp', frame)

    # Exit if 'q' is pressed (quit)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the window
cap.release()
cv2.destroyAllWindows()
