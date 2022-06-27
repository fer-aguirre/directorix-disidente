mkdir -p ~/.streamlit/
echo "
[general]n
email = "kay_op@protonmail.com"n
" > ~/.streamlit/credentials.toml
echo "
[server]n
headless = truen
enableCORS=falsen
port = $PORTn
" > ~/.streamlit/config.toml