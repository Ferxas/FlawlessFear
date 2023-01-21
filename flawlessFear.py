import cv2
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Set up email account details
from_addr = "" # Email to send the data
to_addr = "" # Email that will receive the data
password = "" # Your email password - If you have problems in this part it's important that you read the README

# start camera
cap = cv2.VideoCapture(0)

# Start face detector 
face_cascade = cv2.CascadeClassifier("./haarcascade/haarcascade_frontalface_default.xml") # Directory with the XML for the face detector

while True:
    # Capture frame by frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangle around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # show frame
    cv2.imshow('frame', frame)

    # If a face is detected, take a photo
    if len(faces) > 0:
        img_name = "captura.png"
        cv2.imwrite(img_name, frame)
        print("Imagen guardada!")

        # Create email message
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = "Foto de cara detectada"

        # Attach image to message
        with open(img_name, 'rb') as f:
            img_data = f.read()
        image = MIMEImage(img_data, name="captura.png")
        msg.attach(image)

        # Connect to SMTP server and send email
        server = smtplib.SMTP('smtp.gmail.com', 587) # EXAMPLE: smtp.gmail.com / smtp-mail.outlook.com
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        print("Correo enviado con éxito!")

    # Stop the program if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()