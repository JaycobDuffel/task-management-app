import React from 'react';
import Task from './Task';

const Stage = ({stage}) => {
return (
  <div className='project-stage'>
    <h3>{stage.name}</h3>
    <div className='task-container'>
      <Task />
    </div>
  </div>
)
}

export default Stage