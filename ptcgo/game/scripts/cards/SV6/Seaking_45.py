from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_defender_tools_then_damage

card = PokemonCardDef(
    guid="63a93af9-9898-50e1-91be-3d19bd851b1d",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seaking.Name",
    display_name="Seaking",
    searchable_by=["Seaking", "Stage 1", "Seaking"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Goldeen.Name",
    family_id=118,
    abilities=[
        Attack(
            title="Peck Off",
            game_text="Before doing damage, discard all Pok\u00e9mon Tools from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=50,
            effect=discard_defender_tools_then_damage(),
        ),
        Attack(
            title="Horn Drill",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
        ),
    ],
)