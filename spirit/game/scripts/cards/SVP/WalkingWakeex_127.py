from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="688ecd9a-33d8-5eba-bb4a-46c36ab7d22a",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WalkingWakeex.Name",
    display_name="Walking Wake ex",
    searchable_by=["Walking Wake ex", "Basic", "ex", "Ancient", "WalkingWakeex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=127,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=1009,
    abilities=[
        Ability(
            title="Azure Seas",
            game_text="Damage from attacks used by this Pok\u00e9mon isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Catharsis Roar",
            game_text="If your opponent's Active Pok\u00e9mon is affected by a Special Condition, this attack does 120 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)