[Setup]
AppName=Electric Bass
AppVersion=1.0.0
DefaultDirName={commonpf64}\xAudio
DefaultGroupName=Electric Bass
OutputBaseFilename=Electric Bass
[Files]
Source: "KPSVST\Builds\VisualStudio2019\x64\Release\VST\Electric Bass.dll"; DestDir: "{commonpf64}\Steinberg\VSTPlugins"
Source: "KPSVST\Builds\VisualStudio2019\x64\Release\VST3\Electric Bass.vst3"; DestDir: "{commoncf64}\VST3"
Source: "KPSVST\Builds\VisualStudio2019\x64\Release\Standalone Plugin\Electric Bass.exe"; DestDir: {app}