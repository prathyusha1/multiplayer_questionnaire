import React, { Fragment, Component } from "react";
import { render } from "react-dom";
import GameBoard from './game_board';

class App extends Component {
    constructor(props) {
        console.log('**constructor');
        super(props);
        this.state = {
        };
    }

    componentDidMount() {}

    render() {
        return (
            <Fragment>
                <GameBoard/>
            </Fragment>
        );
    }
}

export default App;

const container = document.getElementById("app");
render(<App />, container);
