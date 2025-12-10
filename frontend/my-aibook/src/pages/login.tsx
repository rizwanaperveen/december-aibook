import React, { useState } from 'react';
import Layout from '@theme/Layout';
import './login.css';

function LoginPage(): JSX.Element {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLogin, setIsLogin] = useState(true);
  const [error, setError] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    // Basic validation
    if (!email || !password) {
      setError('Please fill in all fields');
      return;
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      setError('Please enter a valid email address');
      return;
    }

    // In a real application, you would make an API call here
    console.log(`${isLogin ? 'Login' : 'Sign up'} attempted with:`, { email, password });

    // For now, just show a success message
    alert(`${isLogin ? 'Login' : 'Sign up'} successful! (This is a demo)`);
  };

  return (
    <Layout title={isLogin ? "Login" : "Sign Up"} description="User authentication page">
      <div className="container margin-vert--lg">
        <div className="row">
          <div className="col col--4 col--offset-4">
            <div className="auth-container">
              <h2>{isLogin ? "Login to Your Account" : "Create an Account"}</h2>

              {error && <div className="error-message">{error}</div>}

              <form onSubmit={handleSubmit} className="auth-form">
                <div className="form-group">
                  <label htmlFor="email">Email Address</label>
                  <input
                    type="email"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Enter your email"
                    required
                  />
                </div>

                <div className="form-group">
                  <label htmlFor="password">Password</label>
                  <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Enter your password"
                    required
                    minLength={6}
                  />
                </div>

                <button type="submit" className="auth-button">
                  {isLogin ? "Login" : "Sign Up"}
                </button>
              </form>

              <div className="auth-switch">
                <p>
                  {isLogin ? "Don't have an account?" : "Already have an account?"}{' '}
                  <button
                    type="button"
                    className="switch-button"
                    onClick={() => {
                      setIsLogin(!isLogin);
                      setError('');
                    }}
                  >
                    {isLogin ? "Sign Up" : "Login"}
                  </button>
                </p>
              </div>

              <div className="auth-divider">
                <span>OR</span>
              </div>

              <div className="social-login">
                <button type="button" className="social-button google">
                  Continue with Google
                </button>
                <button type="button" className="social-button github">
                  Continue with GitHub
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </Layout>
  );
}

export default LoginPage;