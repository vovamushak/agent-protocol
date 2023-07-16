# generated by fastapi-codegen:
#   filename:  ../openapi.yml
#   timestamp: 2023-07-16T00:33:45+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class AgentTaskInput(BaseModel):
    pass


class AgentStepDeliverables(BaseModel):
    pass


class AgentStepOutput(BaseModel):
    pass


class AgentTaskRequestBody(BaseModel):
    input: Optional[AgentTaskInput] = None


class AgentTask(BaseModel):
    task_id: Optional[str] = Field(None, description='The ID of the task.')
    input: Optional[AgentTaskInput] = None


class AgentStepRequestBody(BaseModel):
    input: Optional[AgentTaskInput] = None


class AgentStepResult(AgentTask):
    output: Optional[AgentStepOutput] = None
    deliverables: Optional[AgentStepDeliverables] = None
