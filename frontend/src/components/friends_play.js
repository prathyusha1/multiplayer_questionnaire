import React, { Component, Fragment } from "react";

class FriendsPlay extends Component {
    constructor(props) {
        super(props);
        this.state = {
            enableCreateRoom: true,
            enableJoinRoom: false
        }
    }

    onCreateRoomClick() {
        this.setState({
            enableCreateRoom: true,
            enableJoinRoom: false
        });
    }

    onJoinRoomClick() {
        this.setState({
            enableCreateRoom: false,
            enableJoinRoom: true
        });
    }

    getCode() {
        return 'abc';
    }

    render() {
        return (
            <Fragment>
                <div className="friends-room-body">
                    <div className="friends-room-selector">
                        <div className="create-room-heading" onClick={()=>this.onCreateRoomClick()}>
                            <span className="create-room-heading__text"> Create Room </span>
                            <div className="right-slash"></div>
                        </div>

                        <div className="join-room-heading" onClick={()=>this.onJoinRoomClick()}>
                            <span className="join-room-heading__text"> Join Room </span>
                            <div className="left-slash"></div>
                        </div>
                    </div>
                    <div className="friends-play-content">
                        {this.state.enableCreateRoom && <div className="create-room-content">
                            <div>
                                <div>
                                    <span> Share the code : {this.getCode()} with your friends </span>
                                </div>
                            </div>
                        </div>}
                        <div className="join-room-content">
                            {this.state.enableJoinRoom && <div>
                                <span> Join Room </span>
                                <div>
                                    <label>
                                        Enter Room Code:
                                        <input type="text" name="name" />
                                    </label>
                                    <button> Join Room </button>
                                </div>
                            </div>}
                        </div>
                    </div>
                </div>
            </Fragment>
        )
    }
}

export default FriendsPlay;
