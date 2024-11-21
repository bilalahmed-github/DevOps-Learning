# Check if Git is installed
try {
    $gitVersion = git --version
    Write-Output "Git is installed, version: $gitVersion"
} catch {
    Write-Output "Git is not installed"
}

# Display some system information
Write-Output "Fetching system information..."
Write-Output "Hostname: $env:COMPUTERNAME"
Write-Output "System Date and Time: $(Get-Date)"
Write-Output "Uptime: $(Get-Uptime)"

# Optionally, check network connectivity
Write-Output "Checking network connectivity..."
try {
    Test-Connection google.com -Count 3 -ErrorAction Stop | Out-Null
    Write-Output "Network connectivity is fine."
} catch {
    Write-Output "Network issue: Unable to reach google.com"
}
