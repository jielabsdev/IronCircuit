$source = "build/temp.win-amd64-cpython-311/Release/Release/ironcircuit.cp311-win_amd64.pyd"
$dest = "./"

if (Test-Path $source) {
    Copy-Item -Path $source -Destination $dest
    Write-Host "Build successful: .pyd copied to root."
} else {
    Write-Host "Error: Build artifact not found at $source"
}