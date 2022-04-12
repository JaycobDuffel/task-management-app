import React from 'react';

import '../styles/Container.css';
import Stage from './Stage';

const Container = ({project}) => {
return (
  <div className='container'>
    <div className='project-info'>
      <h2>{project.name}</h2>
    </div>
    <div className='project-container'>
      <Stage stage={{name: "To Do"}} />
      <Stage stage={{name: "In Progress"}} />
      <Stage stage={{name: "In Review"}} />
      <Stage stage={{name: "Complete"}} />
    </div>
  </div>
)
}

export default Container