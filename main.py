from faster_whisper import WhisperModel
import time
import whisper

def main():
    # first with faster whisper
    model = WhisperModel("whisper-small-ct2/", device="cpu", compute_type="auto")

    startTime = time.time()
    print('Transcribing with faster_whisper')
    segments, info = model.transcribe('chunk49_16khz.flac', beam_size=1)
    text = " ".join([segment.text for segment in segments])
    intermediateTime = time.time()
    print('Transcribed: %s' % (intermediateTime - startTime))
    print(text)

    # now with regular whisper
    model = whisper.load_model("small.pt", device="cpu")

    startTime = time.time()
    print('Transcribing with whisper')
    audio = whisper.load_audio('chunk49_16khz.flac')
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    options = whisper.DecodingOptions(fp16=False, language='en')
    result = whisper.decode(model, mel, options)
    intermediateTime = time.time()
    print('Transcribed: %s' % (intermediateTime - startTime))
    print(result.text)

    return text

if __name__ == "__main__":
    main()