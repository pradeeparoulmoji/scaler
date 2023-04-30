class scaler:
    def __init__(self, notes):

        self.note = notes.split(" ")
        self.chord = []


    def test(self):
        return self.note

    def chords(self):
        '''returns a list of two elements: note + chord '''
        for i in range(len(self.note)):
            temp = []

            if len(self.note[i]) == 1: #one note = major
                self.chord.append(self.note[i])
                self.chord.append('Maj')
            elif (self.note[i][1] == "#" and len(self.note[i]) == 2): #one note = note# major
                self.chord.append(self.note[i])
                self.chord.append('Maj')
            else: #other chords
                if self.note[i][1] != "#":
                    temp = self.note[i].split(self.note[i][0]) #separate
                    self.chord.append(self.note[i][0])
                    self.chord.append(temp[1])
                if self.note[i][1] == "#":
                    temp = self.note[i].split(self.note[i][1])
                    self.chord.append(self.note[i][0]+"#")
                    self.chord.append(temp[1])

        return self.chord




    def vector(self):
        '''generate the vector'''

        #deafult vectors for C
        lista = [] #list which contains vectors

        k = 1  # support variable



        #based on the note x will increase

        for i in range(len(self.note)):

            major = [48, 52, 55]
            min = [48, 51, 55]
            dim = [48, 51, 54]
            aug = [48, 52, 56]
            sus2 = [48, 50, 55]
            sus4 = [48, 53, 55]

            maj7 = [48, 52, 55, 59]
            min7 = [48, 51, 55, 58]
            _7 = [48, 52, 55, 58]
            maj7sus2 = [48, 50, 55, 59]
            maj7sus4 = [48, 53, 55, 59]
            majadd13 = [48, 52, 55, 57]

            maj9 = [48, 52, 55, 59, 62]
            min9 = [48, 51, 55, 58, 62]
            min7_11 = [48, 51, 55, 58, 66]
            min11 = [48, 51, 55, 58, 65]
            min13 = [48, 51, 55, 58, 69]

            x = 0

            if self.chord[i+k-1] == "C" :
                x = 0
            elif self.chord[i+k-1] == "C#":
                x = 1
            elif self.chord[i+k-1] == "D":
                x = 2
            elif self.chord[i+k-1] == "D#":
                x = 3
            elif self.chord[i+k-1] == "E":
                x = 4
            elif self.chord[i+k-1] == "F":
                x = 5
            elif self.chord[i+k-1] == "F#":
                x = 6
            elif self.chord[i+k-1] == "G":
                x = 7
            elif self.chord[i+k-1] == "G#":
                x = 8
            elif self.chord[i+k-1] == "A":
                x = 9
            elif self.chord[i+k-1] == "A#":
                x = 10
            elif self.chord[i+k-1] == "B":
                x = 11
            else:
                print("not valid input")
                exit(0)

            #updating required vectors

            if(self.chord[i+k] == 'Maj'):
                for j in range(len(major)): #according to the note shift every element of the vector
                    major[j] = major[j] + x
                k = k + 1
                lista.append(major)


            elif (self.chord[i+k] == 'min'):
                for j in range(len(min)):  # according to the note shift every element of the vector
                    min[j] = min[j] + x
                k = k + 1
                lista.append(min)

            elif (self.chord[i+k] == 'dim'):
                for j in range(len(dim)):  # according to the note shift every element of the vector
                    dim[j] = dim[j] + x
                k = k + 1
                lista.append(dim)

            elif (self.chord[i+k] == 'aug'):
                for j in range(len(aug)):  # according to the note shift every element of the vector
                    aug[j] = aug[j] + x
                k = k + 1
                lista.append(aug)

            elif (self.chord[i+k] == 'sus2'):
                for j in range(len(sus2)):  # according to the note shift every element of the vector
                    sus2[j] = sus2[j] + x
                k = k + 1
                lista.append(sus2)

            elif (self.chord[i+k] == 'sus4'):
                for j in range(len(sus4)):  # according to the note shift every element of the vector
                    sus4[j] = sus4[j] + x
                k = k + 1
                lista.append(sus4)

            elif (self.chord[i + k] == 'maj7'):
                for j in range(len(maj7)):  # according to the note shift every element of the vector
                    maj7[j] = maj7[j] + x
                k = k + 1
                lista.append(maj7)

            elif (self.chord[i + k] == 'min7'):
                for j in range(len(min7)):  # according to the note shift every element of the vector
                    min7[j] = min7[j] + x
                k = k + 1
                lista.append(min7)

            elif (self.chord[i + k] == '_7'):
                for j in range(len(_7)):  # according to the note shift every element of the vector
                    _7[j] = _7[j] + x
                k = k + 1
                lista.append(_7)

            elif (self.chord[i + k] == 'maj7sus2'):
                for j in range(len(maj7sus2)):  # according to the note shift every element of the vector
                    maj7sus2[j] = maj7sus2[j] + x
                k = k + 1
                lista.append(maj7sus2)

            elif (self.chord[i + k] == 'maj7sus4'):
                for j in range(len(maj7sus4)):  # according to the note shift every element of the vector
                    maj7sus4[j] = maj7sus4[j] + x
                k = k + 1
                lista.append(maj7sus4)

            elif (self.chord[i + k] == 'majadd13'):
                for j in range(len(majadd13)):  # according to the note shift every element of the vector
                    majadd13[j] = majadd13[j] + x
                k = k + 1
                lista.append(majadd13)

            elif (self.chord[i + k] == 'maj9'):
                for j in range(len(maj9)):  # according to the note shift every element of the vector
                    maj9[j] = maj9[j] + x
                k = k + 1
                lista.append(maj9)

            elif (self.chord[i + k] == 'min9'):
                for j in range(len(min9)):  # according to the note shift every element of the vector
                    min9[j] = min9[j] + x
                k = k + 1
                lista.append(min9)

            elif (self.chord[i + k] == 'min7_11'):
                for j in range(len(min7_11)):  # according to the note shift every element of the vector
                    min7_11[j] = min7_11[j] + x
                k = k + 1
                lista.append(min7_11)

            elif (self.chord[i + k] == 'min11'):
                for j in range(len(min11)):  # according to the note shift every element of the vector
                    min11[j] = min11[j] + x
                k = k + 1
                lista.append(min11)

            elif (self.chord[i + k] == 'min13'):
                for j in range(len(min13)):  # according to the note shift every element of the vector
                    min13[j] = min13[j] + x
                k = k + 1
                lista.append(min13)


        return lista

    def toXML(self):
        '''conversion to scaler2 xml format'''
        xml_text = '''
<?xml version="1.0" encoding="UTF-8"?>

<Scaler version="2.5.0">
  <ScalerState>
    <InfoState versionNumber="2.5.0"/>
    <DisplayState bassNotation="1" selectedScale="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"/>
    <AnalyserState/>
    <AudioState/>
    <TriggerState/>
    <MappingState/>
    <ArpState/>
    <StrumState/>
    <ExpressionState/>
    <LegatoState/>
    <VoicingState lowestNote="54" highestNote="66"/>
    <HumanizeState/>
    <SuggestionState/>
    <ChordViewerState/>
    <BrowserState selectedBrowserTab="scales"/>
    <FilterState/>
    <ScaleExplorerState diatonicShapes="0-0-0-0-0-0-0" isOpen="1"/>
    <ProgressionState/>
    <ModulationState/>
    <PlaybackState tempo="128.0"/>
    <FretboardState/>
    <ReverbState isOn="1"/>
    <FlutterState/>
    <AnalyseContent/>
    <ProgressionContent selectedTabNum="0" isEditingIndex="-1" isEditingTabNum="-1" isLooping="0">
      <ProgressionPattern tabIdx="0" tabName="Pattern 1">
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,92345c1c9f7049c7b65fbd1f80e30451"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="0" tabIdx="0">
          <PlayableItem>
            {a}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,92345c1c9f7049c7b65fbd1f80e30451"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="1" tabIdx="0">
          <PlayableItem>
            {b}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {c}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {d}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {e}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {f}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {g}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {h}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {i}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {j}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {k}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {l}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {m}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {n}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {o}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {p}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,8cb35132182f4ce493924a17efb99801"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="2" tabIdx="0">
          <PlayableItem>
            {q}
          </PlayableItem>
        </ProgressionSlot>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,92345c1c9f7049c7b65fbd1f80e30451"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="3" tabIdx="0"/>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,92345c1c9f7049c7b65fbd1f80e30451"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="4" tabIdx="0"/>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,92345c1c9f7049c7b65fbd1f80e30451"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="5" tabIdx="0"/>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,92345c1c9f7049c7b65fbd1f80e30451"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="6" tabIdx="0"/>
        <ProgressionSlot octave="3" inversion="0" semitoneDelta="0" durationCoefficient="1.0"
                         repeat="1" expressionSetUuid="ac3b36e617884f14b6238f50be88ad09"
                         expressionResolutionId="100" expressionPhrasePlayStyle="2" expressionPhrasePlayMode="1"
                         expressionStrummedSequencesDirection="1" expressionStrummedSequencesProfile="1"
                         expressionStrummedSequencesFill="1" expressionStrummedSequencesAlternative="1"
                         expressionScaleId="ad72b5cb571e401ba882a686c8bdaec6,92345c1c9f7049c7b65fbd1f80e30451"
                         arpTiming="10" arpPatternId="1" arpNoteLength="100" arpOctaveRange="1"
                         strummingProfileId="1" strummingDirectionId="1" voiceGroupingProfileId="99"
                         playbackPerformanceMode="4" groupId="1" groupPlaybackBehaviour="3"
                         idx="7" tabIdx="0"/>
      </ProgressionPattern>
    </ProgressionContent>
    <CommandManager>
      <CommandMapping>
        <Key type="1" keyPress="shift + A"/>
        <Command id="8"/>
      </CommandMapping>
      <CommandMapping>
        <Key type="1" keyPress="shift + B"/>
        <Command id="9"/>
      </CommandMapping>
      <CommandMapping>
        <Key type="1" keyPress="shift + C"/>
        <Command id="10"/>
      </CommandMapping>
      <CommandMapping>
        <Key type="1" keyPress="alt + S"/>
        <Command id="27"/>
      </CommandMapping>
      <CommandMapping>
        <Key type="1" keyPress="alt + O"/>
        <Command id="28"/>
      </CommandMapping>
    </CommandManager>
  </ScalerState>
</Scaler>

'''

        set = []  # list of chords

        vectors = self.vector()  # set of chords given from the uppper method

        for i in range(len(vectors)):  # optimitation
            set.append(f'<MidiNote number="{vectors[i][0]}" velocity="89"/>')

        for i in range(len(vectors)):  # writing all the required chords
            for j in range(1, len(vectors[i])):
                set[i] += f'\n            <MidiNote number="{vectors[i][j]}" velocity="89"/>'

        print(set[1])

        if len(vectors) < 16:
            for i in range(len(vectors), 17):
                set.append(f'<MidiNote number="48" velocity="89"/>')

        output = xml_text.format(a=set[0], b=set[1], c=set[2], d=set[3], e=set[4], f=set[5], g=set[6], h=set[7],
                                 i=set[8], j=set[9], k=set[10], l=set[11], m=set[12], n=set[13], o=set[14], p=set[15],
                                 q=set[16])

        return output

    def write(self, file):
        '''writing the output in a file'''
        f = open(file,'w')
        f.write(self.toXML())
        f.close()










def main():
    inp = input("input desired chords separated by space: ")

    s = scaler(inp)

    print(s.test())


    print(f"note + chord: {s.chords()}")
    print(f"vector: {s.vector()}")
    print(s.toXML())
    path = input("input the file path (use 2 times \ to separate folders instead of \ once) + name of file with xml extension: ")
    s.write(path)



main() #il codice funziona ora devi solo assegnare le liste agli accordi
