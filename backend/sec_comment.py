from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
# from backend import serializers
# from backend.serializers import HelloWorldSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

def generate_response(data, status):
    response = JsonResponse(data, safe=False, status = status)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "*"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

@csrf_exempt
@api_view(['GET', 'POST'])
def sec_comment(request):
    with connection.cursor() as cursor:
        if(request.method == "GET"):
            #sec_comment_id = request.GET.get("sec_comment_id")
            parent_id = str(request.GET.get("parentID"))
            # for i in sec_comment_id:
            #     cursor.execute(
            #     """
            #     SELECT * FROM `MultiComments`
            #     WHERE `MultiCommentID`=%s;
            #     """%(str(i))
            #     )
            #     columns = [col[0] for col in cursor.description]
            #     temp = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cursor.execute(
                """
                SELECT * FROM `MultiComments`,`Users`
                WHERE `ParentCommentID` = '%s'
                and Multicomments.UserID = Users.UserID;
                """%parent_id
            )
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            return generate_response(data, status = 200)
        
        #create secondary comment
        elif request.method == "POST":
            data = request.data
            if data is not None: 
                print(data)
                parent_id = str(request.data["ParentCommentID"])
                content = request.data["CONTENT"]
                userid = str(request.data['USERID'])
                cursor.execute(
                    """
                    INSERT INTO `MultiComments` 
                    (`UserID`, `Content`,`ParentCommentID`)
                    VALUES
                    (%s, %s, %s)
                    """,[userid, content, parent_id]
                )
                cursor.execute(
                    """
                    SELECT `MultiCommentID` 
                    FROM `MultiComments`
                    WHERE `UserID` = %s AND `ParentCommentID` = %s;
                    """, [userid, parent_id]
                )
                MultiCommentID = cursor.fetchall()[0][0]
                print(MultiCommentID)
                cursor.execute(
                    """
                    INSERT INTO `MultiCommentsReplyComments` (
                        `CommentID`,`MultiCommentID`) 
                        VALUES (
                        %s,%s)
                    """, [data["ParentCommentID"],MultiCommentID]
                )
                
                return generate_response(None, status = 201)
        else:
            return generate_response(None, status = 400)
