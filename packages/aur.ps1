$Packages = 'google-chrome',
'jre',
'jdk'

ForEach ($PackageName in $Packages){
    yay -S $PackageName --needed
}