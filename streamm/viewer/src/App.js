import React, { useEffect } from 'react';
import './App.css';
import {
  LivestreamLayout,
  StreamCall,
  StreamVideo,
  StreamVideoClient,
  User,
} from '@stream-io/video-react-sdk';

const apiKey = 'mmhfdzb5evj2';
const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiV2VkZ2VfQW50aWxsZXMiLCJpc3MiOiJodHRwczovL3Byb250by5nZXRzdHJlYW0uaW8iLCJzdWIiOiJ1c2VyL1dlZGdlX0FudGlsbGVzIiwiaWF0IjoxNzE0NzQ0MzYwLCJleHAiOjE3MTUzNDkxNjV9.511XXLOP_aV9L2zE3U0nNlmA80jV1PdMA5DoXu9l-Gg';
const userId = 'Wedge_Antilles';
const callId = 'CZfP61S37qML';

const user: User = {
  id: userId,
  name: 'Oliver-Viewer',
  image: 'https://getstream.io/random_svg/?id=oliver&name=Oliver-Viewer',
};

const client = new StreamVideoClient({ apiKey, user, token });
const call = client.call("livestream", callId);

call.camera.disable();
call.microphone.disable();

call.join();

const App = () => {
  return (
    <StreamVideo client={client}>
      <StreamCall call={call}>
        <LivestreamLayout
          showParticipationCount={true}
          showDuration={true}
          showLiveBadge={true}
        />
      </StreamCall>
    </StreamVideo>
  );
}

export default App;
