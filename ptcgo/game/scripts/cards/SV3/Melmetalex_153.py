from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8d29919f-9611-57a3-b0a6-cca44cea84c7",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Melmetalex.Name",
    display_name="Melmetal ex",
    searchable_by=["Melmetal ex", "Stage 1", "ex", "Melmetalex"],
    subtypes=["Stage 1", "ex"],
    collector_number=153,
    set_code="SV3",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=808,
    abilities=[
        Attack(
            title="Metal-bolize",
            game_text="Search your deck for up to 2 Basic Metal Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.METAL: 1},
            effect=damage_per(count_energy("self", "metal"), 30),
        ),
        Attack(
            title="Full Metal Knuckle",
            game_text="This attack does 30 more damage for each Metal Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=90,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)