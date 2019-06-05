[Setup]
AppName=Electric Bass
AppVersion=1.0.0
DefaultDirName={cf}
DefaultGroupName=Electric Bass
OutputBaseFilename=Electric Bass
[Files]
Source: "Electric Bass.dll"; DestDir: "{app}\Steinberg\VST2"
Source: "Electric Bass.vst3"; DestDir: "{app}\Steinberg\VST3"
Source: "Electric Bass.dpm"; DestDir: "{app}\Digidesign\DAE\Plug-Ins"
Source: "Electric Bass.aaxplugin\*"; DestDir: "{app}\Avid\Audio\Plug-Ins\TestPlugin.aaxplugin"; Flags: recursesubdirs