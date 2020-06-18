import React, { Component, Fragment } from "react";
import './game_board.css';
import FriendsPlay from './friends_play';
import BotPlay from './bot_play';

class GameBoard extends Component {
    constructor(props) {
        super(props);
        this.state = {
            mainScreen: true,
            friendsScreen: false,
            botScreen: false
        };
    }

    goToHome() {
        this.setState({
            mainScreen: true,
            friendsScreen: false,
            botScreen: false
        });
    }
    onPlayWithFriends() {
        this.setState({
            mainScreen: false,
            friendsScreen: true,
            botScreen: false
        });
    }

    onPlayWithComputer() {
        this.setState({
            mainScreen: false,
            friendsScreen: false,
            botScreen: true
        });
    }
    render() {
        return (
            <Fragment>
                <h1 className="Title-header"> 20 Questions Game Board </h1> 
                {!this.state.mainScreen && <div> 
                    <span className="home-btn" onClick={() => this.goToHome()}> Home </span>
                    </div>}
                { this.state.mainScreen && <div className="main-screen">
                    {/* <div onClick= {() => this.onPlayWithFriends()} className="main-friends-screen-head">
                        <span>
                            Play With Friends
                        </span>
                    </div> */}
                    <div onClick={() => this.onPlayWithComputer()} className="main-bot-screen-head">
                        <span>
                            Play Vs Computer
                        </span>
                    </div>

                </div> }
                {
                    this.state.friendsScreen && <div className="main-friends-screen">
                        {/* <div>
                        <span>
                        This is Friends screen
                        </span>
                        </div> */}
                        <FriendsPlay />
                    </div>
                }
                {
                    this.state.botScreen && <div className="main-bot-screen">
                        <span className="side-heading">
                        Play Vs Computer
                        </span>
                        <BotPlay />
                    </div>
                }
            </Fragment>
        )

    }
}

export default GameBoard;