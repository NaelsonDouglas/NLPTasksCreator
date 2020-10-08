import React from 'react';
import axios from 'axios';
import { List, Space, Button } from 'antd';
import Header from './header'
import { MessageOutlined, LikeOutlined, StarOutlined } from '@ant-design/icons';

class TimeList extends React.Component {
        constructor(props) {
          super(props);
          this.state = { timeline: []};
        }

        updateList(props) {
          this.setState({timeline:props.timeline});
        }

        componentDidUpdate() {
          this.render()
        }

        componentDidMount() {
                axios.get(`http://127.0.0.1:8080?text=do%20something%20next%20monday`)
                  .then(res => {
                        console.log(this.state.timeline);
                        //const res = res.data;
                        this.setState({ timeline:res.data });
                  })
              }
        makeRequest(props){
          console.log(props)
          const q = {'params':{'text':props.query}}
          axios.get(`http://127.0.0.1:8080`,q)
            .then(res => {
                  //const res = res.data;
                  this.setState({ timeline:res.data });
            })
        }

        settimeline(props){
          this.setState({timeline:props.timeline})
        }

        render() {
                return <div>
                  <List
                        itemLayout="vertical"
                        size="small"
                        dataSource={this.state.timeline}
                        renderItem={item => (
                          <List.Item
                            key={item.date}
                                          >
                            {item.date}
                          </List.Item>
                        )}
               />
              </div>
        }


      }
export default TimeList