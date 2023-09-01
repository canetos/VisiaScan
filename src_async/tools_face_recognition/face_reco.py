import cv2
import dlib

# Charger le modèle de reconnaissance faciale
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Charger l'image à analyser
image_path = "path/to/your/image.jpg"
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Détecter les visages dans l'image
faces = detector(gray)

# Parcourir les visages détectés et afficher les rectangles autour des visages
for face in faces:
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Utiliser le prédicteur pour détecter les points de repère du visage
    landmarks = predictor(gray, face)
    for point in landmarks.parts():
        cv2.circle(image, (point.x, point.y), 2, (0, 0, 255), -1)

# Afficher l'image avec les rectangles et les points de repère
cv2.imshow("Facial Landmarks", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
