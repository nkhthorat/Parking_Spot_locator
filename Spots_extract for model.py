import cv2
import matplotlib.pyplot as plt


def crop_parking_spots(image_path, spot_regions):
    # Load the original image of the parking lot
    parking_lot_image = cv2.imread(image_path)
    parking_lot_image_rgb = cv2.cvtColor(parking_lot_image, cv2.COLOR_BGR2RGB)
    
    # Plot the original image
    plt.imshow(parking_lot_image_rgb)
    plt.axis('off')
    plt.show()
    
    # Iterate over each parking spot region
    for i, spot_region in enumerate(spot_regions, 1):
        # Extract the region from the original image
        x, y, w, h = spot_region
        spot_image = parking_lot_image[y:y+h, x:x+w]

        # Display the cropped image
        plt.imshow(spot_image)
        plt.axis('off')  # Turn off axis
        plt.title(f"Cropped Parking Spot {i}")
        plt.show()


if __name__ == "__main__":
    # Path to the original image of the parking lot
    image_path = "/Users/nikhilthorat/downloads/parking.jpg"
    
    # Define the coordinates and dimensions of each parking spot region
    # Each entry in the list represents a parking spot region as (x, y, width, height)
    spot_regions = [
        (10, 80, 40, 65),(45, 80, 40, 65),(80, 80, 40, 65),(115, 80, 40, 65),(190, 80, 40, 65),(340, 80, 40, 65)  # Example coordinates and dimensions for the first parking spot
        # Add more entries as needed
    ]

    # Crop parking spots and display as separate images
    crop_parking_spots(image_path, spot_regions)
