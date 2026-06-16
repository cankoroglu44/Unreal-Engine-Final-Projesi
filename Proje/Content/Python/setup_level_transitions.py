import unreal

# =============================================
#  LEVEL GEÇİŞ SİSTEMİ - OTOMATİK KURULUM
#  Her level'a TriggerBox ekler
#  Blueprints -> Open Level Blueprint'te
#  sadece 2 node bağlaman yeterli!
# =============================================

LEVEL_SEQUENCE = [
    ("/Game/Levels/Level1", "Level2"),
    ("/Game/Levels/Level2", "Level3"),
    ("/Game/Levels/Level3", "Level4"),
    ("/Game/Levels/Level4", "Level5"),
    ("/Game/Levels/Level5", "ENDING"),
]

# Trigger'ın her level'da nereye konulacağı (X, Y, Z)
# Bunu kendi map'ine göre ayarlayabilirsin
TRIGGER_LOCATION = unreal.Vector(0.0, 2000.0, 100.0)
TRIGGER_SCALE    = unreal.Vector(5.0, 5.0, 5.0)

subsystem = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

for current_level, next_level in LEVEL_SEQUENCE:
    unreal.log(f"\n--- {current_level} işleniyor ---")

    # Level'ı aç
    subsystem.load_level(current_level)

    # TriggerBox ekle
    trigger = unreal.EditorLevelLibrary.spawn_actor_from_class(
        unreal.TriggerBox,
        TRIGGER_LOCATION,
        unreal.Rotator(0, 0, 0)
    )

    if trigger:
        trigger.set_actor_label(f"GoTo_{next_level}")
        trigger.set_actor_scale3d(TRIGGER_SCALE)
        unreal.log(f"  ✅ Trigger eklendi -> GoTo_{next_level}")
    else:
        unreal.log_warning(f"  ⚠️ Trigger eklenemedi: {current_level}")

    # Kaydet
    unreal.EditorLoadingAndSavingUtils.save_current_level()
    unreal.log(f"  ✅ Kaydedildi: {current_level}")

unreal.log("\n==============================")
unreal.log("✅ KURULUM TAMAMLANDI!")
unreal.log("==============================")
unreal.log("Şimdi her level için şunu yap:")
unreal.log("1) Blueprints -> Open Level Blueprint")
unreal.log("2) GoTo_LevelX trigger'ını seç")
unreal.log("3) Sağ tık -> Add Event -> OnActorBeginOverlap")
unreal.log("4) Open Level (by Name) node ekle")
unreal.log("5) Level Name'e bir sonraki level adını yaz")
unreal.log("6) Compile et, Kaydet et")
