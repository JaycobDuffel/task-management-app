import ApiService from "./api/baseAPI";
import './styles/App.css';
import Container from "./components/Container";

function App() {

  const api = new ApiService();
  return (
    <div className="App">
      <Container project={{name: "Tasky"}} />
    </div>
  );
}

export default App;
