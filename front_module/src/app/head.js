import React from 'react';
import AppBar from 'material-ui/AppBar';
import FlatButton from 'material-ui/FlatButton';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import LeftMenu from './LeftMenu';


class Head extends React.Component {
  render() {
    return (
      <div>
        <MuiThemeProvider>
          <LeftMenu />
        </MuiThemeProvider>
      </div>
    );
  }
}

export default Head;
