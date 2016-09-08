import React from 'react';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
import {Drawer,AppBar,Divider,IconButton,IconMenu,MenuItem} from 'material-ui';
import Download from 'material-ui/svg-icons/file/file-download';
import ArrowDropRight from 'material-ui/svg-icons/navigation-arrow-drop-right';
import MoreVertIcon from 'material-ui/svg-icons/navigation/more-vert';
import LeftMenu from './LeftMenu';
import Content from './Content';

var $ = require('jquery');


const RightMenu = (
  <div>
    <IconMenu iconButtonElement={<IconButton><MoreVertIcon /></IconButton>}
      anchorOrigin={{horizontal: 'left', vertical: 'bottom'}}
      targetOrigin={{horizontal: 'left', vertical: 'top'}}>
      <MenuItem primaryText="Copy ^ Paste" />
    </IconMenu>
  </div>
);

class Page extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      open: false,
      data: []
    };
    this.handleToggle = this.handleToggle.bind(this);
  }

  componentDidMount() {
    $.ajax({
      url: 'http://liuhanlong.top/api/v1/crawl/',
      type: 'GET',
      success: function (data) {
        this.setState({data: data});
      }.bind(this)
    });
  }

  handleToggle() {
    this.setState({open: !this.state.open});
  }

  render() {
    return (
      <MuiThemeProvider>
        <div>
          <AppBar onLeftIconButtonTouchTap={this.handleToggle} iconElementRight={RightMenu} />
          <Drawer docked={false} open={this.state.open} onRequestChange={(open) => this.setState({open})}>
            <AppBar title="菜单"/>
            <MenuItem>Menu Item</MenuItem>
            <MenuItem>Menu Item 2</MenuItem>
          </Drawer>
          <div className="main">
            <Content data={this.state.data} />
          </div>
        </div>
      </MuiThemeProvider>
    );
  }
}

export default Page;
