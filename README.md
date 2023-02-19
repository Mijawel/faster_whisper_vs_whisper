# faster_whisper_vs_whisper
This is an example comparing faster_whisper vs whisper when running the small model, beam_size=1

## To build and run:
`docker build -t local-faster-whisper .`

Example output from Docker logs:
```
Transcribing with faster_whisper

Transcribed: 7.793492794036865

 One is this Abel Bankew-Summer's Steckhauser paper, and now it's like one or two slides in the lecture today.  We didn't spend a lot of time on it in the lecture, but it's listed there as a supplemental reading along with my own paper.  I'll spend a little more time on my own paper.

Transcribing with whisper

Transcribed: 6.5979859828948975

And one is this Abel, thank you Summers, Stechhauser paper. And now it's like one or two slides in the lecture today. We didn't spend a lot of time on it in the lecture, but it's listed there as a supplemental reading along with my own paper. I'll spend a little more time on my own paper.

```

