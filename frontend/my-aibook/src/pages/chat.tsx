import React from 'react';
import Layout from '@theme/Layout';
import Chatbot from '../components/Chatbot/Chatbot';
import './chat.css';

function ChatPage(): JSX.Element {
  return (
    <Layout title="AI Chat" description="Ask questions about the Embodied AI Systems Book">
      <div className="container margin-vert--lg">
        <div className="row">
          <div className="col col--8 col--offset-2">
            <h1>AI Assistant for Embodied AI Systems Book</h1>
            <p>
              Ask questions about the book content and get responses based on the material.
              You can also select text on any page and enable "Use selected text only" mode to ask questions specifically about that content.
            </p>

            <div className="chatbot-wrapper">
              <Chatbot />
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default ChatPage;