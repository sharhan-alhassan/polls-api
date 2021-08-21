import logo from './logo.svg';
import './App.css';

import React, { Component } from 'react'

const list  = [
    {
        "id": 1,
        "title": "laravel development",
        "body": "If you make changes to your local copy and push them to GitHub and need to push them to production, here’s a quick how-to (logged in as our user from earlier)."
    },
    {
        "id": 2,
        "title": "django tutorials",
        "body": "If you make changes to your local copy and push them to GitHub and need to push them to production, here’s a quick how-to (logged in as our user from earlier)."
    },
    {
        "id": 3,
        "title": "Sahih Bukhari",
        "body": "If you make changes to your local copy and push them to GitHub and need to push them to production, here’s a quick how-to (logged in as our user from earlier)."
    }
]

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { list };
  }

  render() {
    return (
       <div>
         {this.state.list.map(item => (
           <div key={item.id}>
             <h1>{item.title}</h1>
             <p>{item.body}</p>
           </div>
         ))}
       </div>
    );
  }
}

export default App;
