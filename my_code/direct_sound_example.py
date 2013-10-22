# http://timgolden.me.uk/pywin32-docs/DirectSound_examples.html

# http://docs.activestate.com/activepython/2.4/pywin32/DirectSound_examples.html

WAV_HEADER_SIZE = struct.calcsize('<4sl4s4slhhllhh4sl')


def wav_header_unpack(data):
    '''Unpack a wav header and stuff it into a WAVEFORMATEX structure'''
    (riff, riffsize, wave, fmt, fmtsize, format, nchannels, samplespersecond, 
    datarate, blockalign, bitspersample, data, datalength) 
    struct.unpack('<4sl4s4slhhllhh4sl', data)
    if riff != 'RIFF' or fmtsize != 16 or fmt != 'fmt ' or data != 'data':
      raise(ValueError, 'illegal wav header')
    
    wfx = pywintypes.WAVEFORMATEX()
    wfx.wFormatTag = format
    wfx.nChannels = nchannels
    wfx.nSamplesPerSec = samplespersecond
    wfx.nAvgBytesPerSec = datarate
    wfx.nBlockAlign = blockalign
    wfx.wBitsPerSample = bitspersample
    return wfx, datalength



# Play a wav file and wait until it's finished

fname = os.path.join(os.path.dirname(__file__), "01-Intro.wav")

f = open(fname, 'rb')



# Read and unpack the wav header

hdr = f.read(WAV_HEADER_SIZE)

wfx, size = wav_header_unpack(hdr)



d = ds.DirectSoundCreate(None, None)

d.SetCooperativeLevel(None, ds.DSSCL_PRIORITY)



sdesc = ds.DSBUFFERDESC()

sdesc.dwFlags = ds.DSBCAPS_STICKYFOCUS | ds.DSBCAPS_CTRLPOSITIONNOTIFY

sdesc.dwBufferBytes = size

sdesc.lpwfxFormat = wfx



buffer = d.CreateSoundBuffer(sdesc, None)



event = win32event.CreateEvent(None, 0, 0, None)
notify = buffer.QueryInterface(ds.IID_IDirectSoundNotify)

notify.SetNotificationPositions((ds.DSBPN_OFFSETSTOP, event))



buffer.Update(0, f.read(size))

buffer.Play(0)

win32event.WaitForSingleObject(event, -1)


#~ #This example shows how to record into a wav file:

import pywintypes

import struct

import win32event

import win32com.directsound.directsound as ds



def wav_header_pack(wfx, datasize):
    return struct.pack('<4sl4s4slhhllhh4sl', 'RIFF', 36 + datasize,
                        'WAVE', 'fmt ', 16,
                        wfx.wFormatTag, wfx.nChannels, wfx.nSamplesPerSec,
                        wfx.nAvgBytesPerSec, wfx.nBlockAlign,
                        wfx.wBitsPerSample, 'data', datasize);


d = ds.DirectSoundCaptureCreate(None, None)



sdesc = ds.DSCBUFFERDESC()

sdesc.dwBufferBytes = 352800 # 2 seconds

sdesc.lpwfxFormat = pywintypes.WAVEFORMATEX()

sdesc.lpwfxFormat.wFormatTag = pywintypes.WAVE_FORMAT_PCM

sdesc.lpwfxFormat.nChannels = 2

sdesc.lpwfxFormat.nSamplesPerSec = 44100

sdesc.lpwfxFormat.nAvgBytesPerSec = 176400

sdesc.lpwfxFormat.nBlockAlign = 4

sdesc.lpwfxFormat.wBitsPerSample = 16



buffer = d.CreateCaptureBuffer(sdesc)



event = win32event.CreateEvent(None, 0, 0, None)

notify = buffer.QueryInterface(ds.IID_IDirectSoundNotify)



notify.SetNotificationPositions((ds.DSBPN_OFFSETSTOP, event))



buffer.Start(0)



win32event.WaitForSingleObject(event, -1)



# in real life, more, smaller buffers should be retrieved

data = buffer.Update(0, 352800)



f = open('recording.wav', 'wb')

f.write(wav_header_pack(sdesc.lpwfxFormat, 352800))

f.write(data)


