import ApiService from "./api/baseAPI";
import './App.css';

function App() {

  const api = new ApiService();
  return (
    <div className="App">
      <header className="App-header">
        <button onClick={() => {
          api.createStage({
          title: 'In Progress',
          order: 2,
          project: 1,
        })}}>Add Project</button>
      </header>
    </div>
  );
}

export default App;
