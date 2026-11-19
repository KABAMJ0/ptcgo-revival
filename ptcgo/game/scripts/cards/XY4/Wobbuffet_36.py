from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aae17f34-9cf4-55bf-8b6a-8581e35d8c1a",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wobbuffet.Name",
    display_name="Wobbuffet",
    searchable_by=["Wobbuffet", "Basic", "Wobbuffet"],
    subtypes=["Basic"],
    collector_number=36,
    set_code="XY4",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=202,
    abilities=[
        Ability(
            title="Bide Barricade",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon, each Pok\u00e9mon in play, in each player's hand, and in each player's discard pile has no Abilities (except for Psychic Pok\u00e9mon).",
            effect=unimplemented,
        ),
        Attack(
            title="Psychic Assault",
            game_text="This attack does 10 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 10, base=10),
        ),
    ],
)