import './App.css';

function App() {
  const user = {
    age: 19,
    isLoggedIn: false,
  }

  // if (user.isLoggedIn) {
  //   return <h1>Welcome</h1>
  // } else {
  //   return <h1>Please log in</h1>
  // }

  // if (!user.isLoggedIn) {
  //   return <h1>Log in</h1>
  // }

  return (
    <>
      <h1>
        React Conditionals
      </h1>
      {user.age >= 18 ? <h2>Register to vote</h2> : <h1>Dont vote</h1>}
    </>
  )
}

export default App;