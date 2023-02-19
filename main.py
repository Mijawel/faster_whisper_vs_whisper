from faster_whisper import WhisperModel
import time
import whisper
import os
os.environ["OMP_NUM_THREADS"] = "4"

def main():
    print('starting main')
    # first with faster whisper
    model = WhisperModel("whisper-small-ct2/", device="cpu", compute_type="auto")

    startTime = time.time()
    print('Transcribing with faster_whisper')
    segments, info = model.transcribe('chunk49_16khz.flac', language="en", beam_size=1)
    text = " ".join([segment.text for segment in segments])
    intermediateTime = time.time()
    print('Transcribed: %s' % (intermediateTime - startTime))
    print(text)

    # now with regular whisper
    model = whisper.load_model("small.pt", device="cpu")

    startTime = time.time()
    print('Transcribing with whisper')
    result = result = model.transcribe('chunk49_16khz.flac', language="en", beam_size=1, fp16=False)
    intermediateTime = time.time()
    print('Transcribed: %s' % (intermediateTime - startTime))
    text = result["text"]
    print(text)

    return text

if __name__ == "__main__":
    main()