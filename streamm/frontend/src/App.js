import React, { useEffect } from 'react';
import './App.css';
import {
  User,
  StreamVideoClient,
  StreamVideo,
  StreamCall,
  useCall,
  useCallStateHooks,
  ParticipantView,
} from '@stream-io/video-react-sdk';

const apiKey = 'mmhfdzb5evj2';
const token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiV2VkZ2VfQW50aWxsZXMiLCJpc3MiOiJodHRwczovL3Byb250by5nZXRzdHJlYW0uaW8iLCJzdWIiOiJ1c2VyL1dlZGdlX0FudGlsbGVzIiwiaWF0IjoxNzE0NzQ0MzYwLCJleHAiOjE3MTUzNDkxNjV9.511XXLOP_aV9L2zE3U0nNlmA80jV1PdMA5DoXu9l-Gg';
const userId = 'Wedge_Antilles';
const callId = 'CZfP61S37qML';

const user: User = {
  id: userId,
  name: 'Stefan',
  image: 'https://getstream.io/random_svg/?id=stefan&name=Stefan',
};

const client = new StreamVideoClient({ apiKey, user, token });
const call = client.call('livestream', callId);
call.join({ create: true });

const App = () => {
  return (
    <StreamVideo client={client}>
      <StreamCall call={call}>
        <MyLivestreamUI />
      </StreamCall>
    </StreamVideo>
  );
}

const MyLivestreamUI = () => {
  const call = useCall();
  const { useIsCallLive, useLocalParticipant, useParticipantCount, useCallEgress } = useCallStateHooks();
  const totalParticipants = useParticipantCount();
  const localParticipants = useLocalParticipant();
  const isCallLive = useIsCallLive();
  const egress = useCallEgress();

  useEffect(() => {
    console.log('HLS playlist URL:', egress?.hls?.playlist_url);
  }, [egress?.hls?.playlist_url]);

  useEffect(() => {
    if (!isCallLive) {
      call.camera.disable();
    } else {
      call.camera.enable(); 
    }
  }, [call, isCallLive]);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '5px' }}>
      <div
        style={{
          alignSelf: 'flex-start',
          color: 'white',
          backgroundColor: 'blue',
          borderRadius: '8px',
          padding: "4px 6px",
        }}
      >
        Live: {totalParticipants}
      </div>
      <div style={{ flex: 1 }}>
        {localParticipants && (
          <ParticipantView
            participant={localParticipants}
            ParticipantViewUI={null}
          />
        )}
      </div>
      <div style={{ alignSelf: 'center' }}>
        {isCallLive ? (
          <button onClick={() => call?.stopLive()}>Stop Livestream</button>
        ) : (
          <button onClick={() => call?.goLive({ start_hls: true })}>Start Livestream</button>
        )}
      </div>
    </div>
  );
}

export default App;
