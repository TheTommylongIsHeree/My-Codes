Set-PSDebug -off #turn off debugging (for better experience)
[console]::WindowWidth=1; [console]::WindowHeight=1; [console]::BufferWidth=[console]::WindowWidth
Test-Administrator
function Test-Administrator {
    $isAdmin = $false
    $windowsIdentity = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $windowsPrincipal = New-Object System.Security.Principal.WindowsPrincipal($windowsIdentity)
    if ($windowsPrincipal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)) {
        $isAdmin = $true
    }
    return $isAdmin
}
