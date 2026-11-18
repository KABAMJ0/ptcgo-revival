from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="932904db-d50f-546b-98f1-d43a1762407a",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thwackey.Name",
    display_name="Thwackey",
    searchable_by=["Thwackey", "Stage 1", "Thwackey"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grookey.Name",
    family_id=810,
    abilities=[
        Ability(
            title="Boom Boom Groove",
            game_text="Once during your turn, if your Active Pok\u00e9mon has the Festival Lead Ability, you may search your deck for a card and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Beat",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
        ),
    ],
)