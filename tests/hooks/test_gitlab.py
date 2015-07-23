# -*- coding: utf-8 -*-

from nose2.tools import params

from gewebehaken.hooks.gitlab import gitlab_issue, gitlab_merge_request, \
                                     gitlab_note, gitlab_push, gitlab_tag_push

from ..base import AbstractHooksTestCase


class GitlabHooksTestCase(AbstractHooksTestCase):

    # Examples were taken from GitLab's built-in help on web hooks.

    @params(
        (
            'Push Hook',
            {
                "object_kind": "push",
                "before": "95790bf891e76fee5e1747ab589903a6a1f80f22",
                "after": "da1560886d4f094c3e6c9ef40349f7d38b5d27d7",
                "ref": "refs/heads/master",
                "user_id": 4,
                "user_name": "John Smith",
                "user_email": "john@example.com",
                "project_id": 15,
                "repository": {
                    "name": "Diaspora",
                    "url": "git@example.com:mike/diasporadiaspora.git",
                    "description": "",
                    "homepage": "http://example.com/mike/diaspora",
                    "git_http_url":"http://example.com/mike/diaspora.git",
                    "git_ssh_url":"git@example.com:mike/diaspora.git",
                    "visibility_level": 0
                },
                "commits": [
                    {
                        "id": "b6568db1bc1dcd7f8b4d5a946b0b91f9dacd7327",
                        "message": "Update Catalan translation to e38cb41.",
                        "timestamp": "2011-12-12T14:27:31+02:00",
                        "url": "http://example.com/mike/diaspora/commit/b6568db1bc1dcd7f8b4d5a946b0b91f9dacd7327",
                        "author": {
                            "name": "Jordi Mallach",
                            "email": "jordi@softcatala.org"
                        }
                    },
                    {
                        "id": "da1560886d4f094c3e6c9ef40349f7d38b5d27d7",
                        "message": "fixed readme",
                        "timestamp": "2012-01-03T23:36:29+02:00",
                        "url": "http://example.com/mike/diaspora/commit/da1560886d4f094c3e6c9ef40349f7d38b5d27d7",
                        "author": {
                            "name": "GitLab dev user",
                            "email": "gitlabdev@dv6700.(none)"
                        }
                    }
                ],
                "total_commits_count": 4
            },
            gitlab_push,
        ),
        (
            'Tag Push Hook',
            {
                "object_kind": "tag_push",
                "ref": "refs/tags/v1.0.0",
                "before": "0000000000000000000000000000000000000000",
                "after": "82b3d5ae55f7080f1e6022629cdb57bfae7cccc7",
                "user_id": 1,
                "user_name": "John Smith",
                "project_id": 1,
                "repository": {
                    "name": "jsmith",
                    "url": "ssh://git@example.com/jsmith/example.git",
                    "description": "",
                    "homepage": "http://example.com/jsmith/example",
                    "git_http_url":"http://example.com/jsmith/example.git",
                    "git_ssh_url":"git@example.com:jsmith/example.git",
                    "visibility_level": 0
                },
                "commits": [],
                "total_commits_count": 0
            },
            gitlab_tag_push,
        ),
        (
            'Issue Hook',
            {
                "object_kind": "issue",
                "user": {
                    "name": "Administrator",
                    "username": "root",
                    "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=40\u0026d=identicon"
                },
                "object_attributes": {
                    "id": 301,
                    "title": "New API: create/update/delete file",
                    "assignee_id": 51,
                    "author_id": 51,
                    "project_id": 14,
                    "created_at": "2013-12-03T17:15:43Z",
                    "updated_at": "2013-12-03T17:15:43Z",
                    "position": 0,
                    "branch_name": None,
                    "description": "Create new API for manipulations with repository",
                    "milestone_id": None,
                    "state": "opened",
                    "iid": 23,
                    "url": "http://example.com/diaspora/issues/23",
                    "action": "open"
                }
            },
            gitlab_issue,
        ),
        (
            'Note Hook',
            {
                "object_kind": "note",
                "user": {
                    "name": "Adminstrator",
                    "username": "root",
                    "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=40\u0026d=identicon"
                },
                "project_id": 5,
                "repository": {
                    "name": "Gitlab Test",
                    "url": "http://example.com/gitlab-org/gitlab-test.git",
                    "description": "Aut reprehenderit ut est.",
                    "homepage": "http://example.com/gitlab-org/gitlab-test"
                },
                "object_attributes": {
                    "id": 1241,
                    "note": "Hello world",
                    "noteable_type": "Issue",
                    "author_id": 1,
                    "created_at": "2015-05-17 17:06:40 UTC",
                    "updated_at": "2015-05-17 17:06:40 UTC",
                    "project_id": 5,
                    "attachment": None,
                    "line_code": None,
                    "commit_id": "",
                    "noteable_id": 92,
                    "system": False,
                    "st_diff": None,
                    "url": "http://example.com/gitlab-org/gitlab-test/issues/17#note_1241"
                },
                "issue": {
                    "id": 92,
                    "title": "test",
                    "assignee_id": None,
                    "author_id": 1,
                    "project_id": 5,
                    "created_at": "2015-04-12 14:53:17 UTC",
                    "updated_at": "2015-04-26 08:28:42 UTC",
                    "position": 0,
                    "branch_name": None,
                    "description": "test",
                    "milestone_id": None,
                    "state": "closed",
                    "iid": 17
                }
            },
            gitlab_note,
        ),
        (
            'Merge Request Hook',
            {
                "object_kind": "merge_request",
                "user": {
                    "name": "Administrator",
                    "username": "root",
                    "avatar_url": "http://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=40\u0026d=identicon"
                },
                "object_attributes": {
                    "id": 99,
                    "target_branch": "master",
                    "source_branch": "ms-viewport",
                    "source_project_id": 14,
                    "author_id": 51,
                    "assignee_id": 6,
                    "title": "MS-Viewport",
                    "created_at": "2013-12-03T17:23:34Z",
                    "updated_at": "2013-12-03T17:23:34Z",
                    "st_commits": None,
                    "st_diffs": None,
                    "milestone_id": None,
                    "state": "opened",
                    "merge_status": "unchecked",
                    "target_project_id": 14,
                    "iid": 1,
                    "description": "",
                    "source": {
                        "name": "awesome_project",
                        "ssh_url": "ssh://git@example.com/awesome_space/awesome_project.git",
                        "http_url": "http://example.com/awesome_space/awesome_project.git",
                        "visibility_level": 20,
                        "namespace": "awesome_space"
                    },
                    "target": {
                        "name": "awesome_project",
                        "ssh_url": "ssh://git@example.com/awesome_space/awesome_project.git",
                        "http_url": "http://example.com/awesome_space/awesome_project.git",
                        "visibility_level": 20,
                        "namespace": "awesome_space"
                    },
                    "last_commit": {
                        "id": "da1560886d4f094c3e6c9ef40349f7d38b5d27d7",
                        "message": "fixed readme",
                        "timestamp": "2012-01-03T23:36:29+02:00",
                        "url": "http://example.com/awesome_space/awesome_project/commits/da1560886d4f094c3e6c9ef40349f7d38b5d27d7",
                        "author": {
                            "name": "GitLab dev user",
                            "email": "gitlabdev@dv6700.(none)"
                        }
                    },
                    "url": "http://example.com/diaspora/merge_requests/1",
                    "action": "open"
                }
            },
            gitlab_merge_request,
        ),
    )
    def test_hook_event(self, event_type, request_data, expected_signal):
        @expected_signal.connect
        def receive_signal(sender, **data):
            self.storeReceivedSignalData(data)

        headers = self.build_headers(event_type)

        result = self.post_json('/gitlab', data=request_data, headers=headers)

        self.assert204(result)
        self.assertReceivedSignalDataEqual(request_data)

    def test_unknown_event(self):
        headers = self.build_headers('Some Unknown Hook')

        result = self.post_json('/gitlab', data={}, headers=headers)

        self.assertEqual(result.status_code, 400)

    def build_headers(self, event_type):
        return [
            ('X-Gitlab-Event', event_type),
        ]
