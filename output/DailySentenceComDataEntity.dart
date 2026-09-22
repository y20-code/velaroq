class DailySentenceComDataEntity {
  int? id;
  int? userId;
  int? sourceId;
  int? score;
  String? voice;
  int? ctime;

    DailySentenceComDataEntity({
    this.id,
    this.userId,
    this.sourceId,
    this.score,
    this.voice,
    this.ctime,
  });

    factory DailySentenceComDataEntity.fromJson(Map<String, dynamic> json) =>
        DailySentenceComDataEntity(
        id: json['id'] ?? -1,
        userId: json['userId'] ?? -1,
        sourceId: json['sourceId'] ?? -1,
        score: json['score'] ?? 0,
        voice: json['voice'],
        ctime: json['ctime'] ?? 0,
    );
}