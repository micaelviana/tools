$Packages = 'google-chrome'

ForEach ($PackageName in $Packages){
    yay -S $PackageName --needed
}
