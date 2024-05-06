// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from tutorial_interfaces:srv/SpinTurtle.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__SRV__DETAIL__SPIN_TURTLE__BUILDER_HPP_
#define TUTORIAL_INTERFACES__SRV__DETAIL__SPIN_TURTLE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "tutorial_interfaces/srv/detail/spin_turtle__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace tutorial_interfaces
{

namespace srv
{

namespace builder
{

class Init_SpinTurtle_Request_dir
{
public:
  Init_SpinTurtle_Request_dir()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::tutorial_interfaces::srv::SpinTurtle_Request dir(::tutorial_interfaces::srv::SpinTurtle_Request::_dir_type arg)
  {
    msg_.dir = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::srv::SpinTurtle_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::srv::SpinTurtle_Request>()
{
  return tutorial_interfaces::srv::builder::Init_SpinTurtle_Request_dir();
}

}  // namespace tutorial_interfaces


namespace tutorial_interfaces
{

namespace srv
{

namespace builder
{

class Init_SpinTurtle_Response_res
{
public:
  Init_SpinTurtle_Response_res()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::tutorial_interfaces::srv::SpinTurtle_Response res(::tutorial_interfaces::srv::SpinTurtle_Response::_res_type arg)
  {
    msg_.res = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::srv::SpinTurtle_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::srv::SpinTurtle_Response>()
{
  return tutorial_interfaces::srv::builder::Init_SpinTurtle_Response_res();
}

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__SRV__DETAIL__SPIN_TURTLE__BUILDER_HPP_
