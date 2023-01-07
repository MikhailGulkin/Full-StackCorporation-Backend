from rest_framework.test import APITestCase
from rest_framework import status

from django.urls import reverse

from employee.models import Administrator
from employee.tests.utils.administrator import create_administrators
from employee.serializers import AdministratorSerializer

from user.tests.utils import create_profiles
from user.models import CustomUser


class AdministratorTestCase(APITestCase):
    """
    Test Cases for :model:`employee.Administrator`.
    """
    all_admins_url = reverse('all-admins')
    create_admin_url = reverse('create-admin')

    retrieve_admin = 'admin'
    delete_admin = 'delete-admin'
    update_admin = 'update-admin'

    administrator_count = 4

    @classmethod
    def setUpTestData(cls):
        for index, admin in enumerate(
                create_administrators(cls.administrator_count),
                start=1
        ):
            setattr(cls,
                    f'admin_{index}',
                    admin
                    )
        _keyword = 'administrator'

        cls.login_user = CustomUser.objects.create_user(
            username=f'user_{_keyword}',
            email=f'user{_keyword}@example.com',
            password=f'user_{_keyword}',
            first_name=f'first_{_keyword}',
            last_name=f'last_{_keyword}',
        )

    def setUp(self):
        self.client.force_login(self.login_user)

    def test_get_all_admins(self):
        response = self.client.get(self.all_admins_url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            len(response.json()),
            self.administrator_count
        )

    def test_admin_retrieve(self):
        pk = self.admin_1.pk
        response = self.client.get(
            reverse(self.retrieve_admin, kwargs={'pk': pk})
        )
        response_json = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['profile'],
            self.admin_1.profile.pk
        )
        self.assertEqual(
            response_json,
            AdministratorSerializer(self.admin_1).data
        )

    def test_admins_create(self):
        profile_pk = self.administrator_count + abs(hash("create"))
        profile = create_profiles(profile_pk, start=profile_pk)[0]
        json = {
            'profile': profile.pk
        }
        response = self.client.post(
            self.create_admin_url,
            data=json
        )
        response_json = response.json()
        pk = response_json['pk']
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response_json,
            AdministratorSerializer(
                Administrator.objects.get(pk=pk)
            ).data
        )

    def test_delete_admin(self):
        pk = self.admin_1.pk

        response = self.client.delete(
            reverse(
                self.delete_admin,
                kwargs={'pk': pk}
            )
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Administrator.objects.filter(pk=pk).exists(),
            False
        )

    def test_put_admin(self):
        profile_pk = self.administrator_count + abs(hash("put"))
        profile = create_profiles(profile_pk, start=profile_pk)[0]
        pk = self.admin_2.pk
        json = {
            "profile": profile.pk,
        }
        response = self.client.put(
            reverse(
                self.update_admin,
                kwargs={'pk': pk}
            ),
            data=json
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['pk'],
            pk
        )

    def test_patch_admin(self):
        profile_pk = self.administrator_count + abs(hash("patch"))
        profile = create_profiles(profile_pk, start=profile_pk)[0]
        pk = self.admin_2.pk
        json = {
            "profile": profile.pk,
        }
        response = self.client.patch(
            reverse(
                self.update_admin,
                kwargs={'pk': pk}
            ),
            data=json
        )
        response_json = response.json()
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response_json['pk'],
            pk
        )