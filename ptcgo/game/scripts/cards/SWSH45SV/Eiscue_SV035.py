from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="053828c7-31ad-5e52-bcaf-a2e2d2e7b965",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eiscue.Name",
    display_name="Eiscue",
    searchable_by=["Eiscue", "Basic", "Eiscue"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="SWSH45SV",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=875,
    abilities=[
        Ability(
            title="Ice Face",
            game_text="If this Pok\u00e9mon has full HP, it takes 60 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Blizzard",
            game_text="This attack also does 10 damage to each of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=spread_damage(10, side="opponent", include_active=False),
        ),
    ],
)