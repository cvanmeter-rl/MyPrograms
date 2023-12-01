import {BrowserRouter as Router,Route,Routes} from 'react-router-dom'
import Header from './Components/Header';
import AddEntryPage from './Components/AddEntryPage';
import ViewList from './Components/ViewList';
import Home from './Components/Home'

function App() {
  return (
    <Router>
      <Header/>
      <div>
        <Routes>
          <Route exact path='/' element={<Home/>}/>
          <Route path='/addEntry' element={<AddEntryPage/>}/>
          <Route path='/listView' element={<ViewList/>}/>
        </Routes>
      </div>
    </Router>
  );
}

export default App;