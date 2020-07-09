# Sugus vs. Chocobons

## Description

Little Streamlabs Script. Catches users preferences from Twitch chat and sends them to a server.

Capture commands `!sugus` and `!chocobons`.

## Configuration

Once installed in Streamlabs Chatbot and logged in as streamer and bot, you must set some settings about server which listen requests from this script, in order to send requests with users preferences:

- **API URL**: Complete URL to send requests.
- **API USER**: Auth user to grant access to the server.
- **API KEY**: Auth token to grant access to the server.

You will need a server which listen requests with following data (in addition to `user` and `key` as mentioned):

- **twitch_id**: Twitch chat user id (numerical).
- **twitch_name**: Twitch chat username (alphanumerical and `_` char).
- **preference**: String with value `sugus` or `chocobons`.

## Usage

Once installed and configured this script will listen all messages from chat of your Twitch channel. If some of this messages starts with `!sugus` or `!chocobons` it sends a request with data needed in order to store users preferences.

This server is already developed but it is private, it also shows some statistics throgh a webpage.

![Status bar](https://raw.githubusercontent.com/bgonp/sugus-vs-chocobons/master/img/statusbar.png)