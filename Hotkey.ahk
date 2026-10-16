#Requires AutoHotkey v2.0
#SingleInstance Force

; "=" = ajouter un kill ; ")" = retirer un kill
; Ctrl + "=" = remise à zéro avec confirmation
Hotkey("=", AddKill)
Hotkey(")", UndoKill)
Hotkey("^=", ResetKills)

AddKill(*) => SendCounter("/api/kill")
UndoKill(*) => SendCounter("/api/undo")
ResetKills(*) {
    answer := MsgBox("Remettre le compteur à zéro ?", "ROTK Kill Counter", "YesNo Icon!")
    if answer = "Yes"
        SendCounter("/api/reset")
}
SendCounter(endpoint) {
    try {
        http := ComObject("WinHttp.WinHttpRequest.5.1")
        http.Open("POST", "http://127.0.0.1:8766" endpoint, false)
        http.SetRequestHeader("Content-Type", "application/json")
        http.Send("{}")
    } catch as err {
        MsgBox("Le compteur ne répond pas.`nLancez d'abord start_counter.bat.`n`n" err.Message)
    }
}
