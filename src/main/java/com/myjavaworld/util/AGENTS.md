# Utility and event guidance

These utilities are shared by UI, transfer, ZIP, and persistence code. Find callers before changing behavior; preserve exception/null handling, file semantics, event payloads, listener thread/order, timestamps, and text formatting unless the change is intentional and tested.

`FileChangeMonitor` is a Swing-timer poller used to detect edits to temporary downloads and prompt for re-upload. Characterize add/remove/stop/restart behavior, deletion, and timestamp-resolution limitations before replacing it. Listener work can affect responsiveness on the timer's callback thread.

Open `docs/utilities-and-events.md` for the event model and helper behavior. Also open the caller's guide when a shared utility changes FTP, UI, or ZIP behavior. Update those docs when contracts or known limitations change.
