import ApiService from "./api/baseAPI";
import './App.css';
import Container from "./components/Container";

function App() {

  const api = new ApiService();
  return (
    <div className="App">
      <Container />
    </div>
  );
}

export default App;
