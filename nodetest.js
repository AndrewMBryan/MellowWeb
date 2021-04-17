

const accountSid = "ACd872f1187267237476504b4c4a629cc3"; //process.env.TWILIO_ACCOUNT_SID;
const authToken = "1b9095c8377850cc32ff106c4285f499";//process.env.TWILIO_AUTH_TOKEN;
const client = require('twilio')(accountSid, authToken);

// client.calls
//       .create({
//          url: 'http://demo.twilio.com/docs/voice.xml',
//          to: '+16179990005',
//          from: '+14049961894'
//        })
//       .then(call => console.log(call.sid));

const http = require('http');
const VoiceResponse = require('twilio').twiml.VoiceResponse;

http
  .createServer((req, res) => {
    // Create TwiML response
    const twiml = new VoiceResponse();

    twiml.say('Hello from your pals at Twilio! Have fun lololo.');

    res.writeHead(200, { 'Content-Type': 'text/xml' });
    res.end(twiml.toString());
  })
  .listen(1337, '127.0.0.1');

console.log('TwiML server running at http://127.0.0.1:1337/');
