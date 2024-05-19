import instaloader
import os

# Initialize Instaloader
loader = instaloader.Instaloader()


# Function to download reel
def download_reel(reel_url):
    try:
        # Download the reel using its URL
        loader.download_post(
            instaloader.Post.from_shortcode(loader.context, reel_url.split("/")[-2]),
            target="reels",
        )
        for filename in os.listdir("reels"):
            if not filename.endswith(".mp4"):
                os.remove(os.path.join("reels", filename))
        print("Reel downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example URL of the reel
reel_url = ""
download_reel(reel_url)
