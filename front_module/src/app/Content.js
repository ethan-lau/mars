import React from 'react';
import {List, ListItem} from 'material-ui/List';
import Avatar from 'material-ui/Avatar';


let UserInfo = React.createClass({
  render: function() {
    return (<Avatar src='#'/>);
  }
});

export default class Content extends React.Component {
  render() {
    var listItems = [];
    this.props.data.forEach(function(content, index) {
      listItems.push(<ListItem rightAvatar={
        <div>
          <div className='user-info'>
            <Avatar src={content.icon} />
          </div>
          <div className='subject-name'>
            <a href='#'>{content.author}</a>
          </div>
        </div>
      } key={index} primaryText={
        <a target="_blank" href={content.url}>{content.title}</a>
      } secondaryText={content.author} 
        secondaryTextLines={1}></ListItem>);
    });

    return (
      <div className="content-list">
        <List>
          {listItems}
        </List>
      </div>
    );
  }
}