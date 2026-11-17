from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5c807e1c-adae-5cf3-8c80-35052a378a85",
    key="SV8PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WalkingWakeex.Name",
    display_name="Walking Wake ex",
    searchable_by=["Walking Wake ex", "Basic", "ex", "Ancient", "WalkingWakeex"],
    subtypes=["Basic", "ex", "Ancient"],
    collector_number=178,
    set_code="SV8PT5",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
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