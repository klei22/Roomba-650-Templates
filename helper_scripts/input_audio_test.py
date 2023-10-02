import pyaudio

audio = pyaudio.PyAudio()

for i in range(audio.get_device_count()):
    device_info = audio.get_device_info_by_index(i)
    if device_info["maxInputChannels"] > 0:
        print(f"Index {i} - {device_info['name']}")

audio.terminate()


import sounddevice as sd

samplerates = 32000, 44100, 48000, 96000, 128000
device = 6

supported_samplerates = []
for fs in samplerates:
    try:
        sd.check_output_settings(device=device, samplerate=fs)
    except Exception as e:
        print(fs, e)
    else:
        supported_samplerates.append(fs)
print(supported_samplerates)

