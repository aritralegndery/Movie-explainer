import argparse
import scipy.io.wavfile
from transformers import AutoProcessor, AutoModel

def main(text_file):
    # Load the pre-trained Bark model and processor
    processor = AutoProcessor.from_pretrained("suno/bark-small")
    model = AutoModel.from_pretrained("suno/bark-small")

    # Read the text from the file
    with open(text_file, 'r') as file:
        text = file.read().strip()

    # Process the input text
    inputs = processor(text=[text], return_tensors="pt")

    # Generate speech
    speech_values = model.generate(**inputs, do_sample=True)

    # Save the generated speech to a WAV file
    sampling_rate = model.config.sample_rate
    scipy.io.wavfile.write("bark_out.wav", rate=sampling_rate, data=speech_values.cpu().numpy().squeeze())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text-to-Speech using suno/bark-small model")
    parser.add_argument("tts_txt", type=str, help="Path to the text file to convert to speech")
    args = parser.parse_args()
    main(args.tts_txt)
